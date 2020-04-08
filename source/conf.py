import os
import sys
import pathlib
import git
import re

# -- FreeCAD setup -----------------------------------------------------------


# Adding FreeCAD and FreeCADGui so it can be accessed by autodoc
try:
    freecad_build_path = os.environ['FREECAD_BUILD_LOCATION']
except:
    raise Exception("Please enter the base directory of FreeCAD's build location.")

lib_from_base = "lib/"
freecad_lib_path = os.path.join(freecad_build_path, lib_from_base)
sys.path.append(freecad_lib_path)

import FreeCAD, FreeCADGui
FreeCADGui.showMainWindow() # this is needed for complete import of GUI modules
doc = FreeCAD.newDocument("doc")

# -- Getting links to sourcecode ---------------------------------------------

try:
    freecad_source_path = os.environ['FREECAD_SOURCE_LOCATION']
except:
    raise Exception("Please enter the base directory of FreeCAD's source location.")


gitrepo = git.Repo(freecad_source_path)

# Get name of current branch.
branch_name = gitrepo.active_branch.name

# Get references between branches and remotes.
references = gitrepo.refs
branch_to_remote_refs = [r.name.split("/") for r in references if len(r.name.split("/")) > 1]

# Get the url for the remote of the active branch.
active_remote_name = [r[0] for r in branch_to_remote_refs if r[1] == branch_name][0]
active_remote_url = gitrepo.remote(active_remote_name).url

source_url = False

# Parse ssh remote urls
if active_remote_url[:4] == "git@":
    source_url_template = "https://{domain}/{repo}/blob/{branch}"

    remote_url_sans_git = active_remote_url[4:-4]
    split = remote_url_sans_git.split(":")
    domain_name = split[0]
    repo = split[1]
    source_url = source_url_template.format(domain=domain_name,
                                            repo=repo,
                                            branch=branch_name)

# Parse http remote urls
elif active_remote_url[:4] == "http":
    url_sans_git = active_remote_url[:-4]
    source_url = url_sans_git + "/blob/" + branch_name
    pass

# Could not understand the url type
else:
    source_url = False


# Defining the function that will fetch links to the source code.
def linkcode_resolve(domain, info):
    """Defines the url for links from the docs to the source.

    Currently only implemented for python code.

    See sphinx docs for more information:
    https://www.sphinx-doc.org/en/master/usage/extensions/linkcode.html#confval-linkcode_resolve

    Returns
    -------
    str:
        Url to sourcecode if successful.
    None:
        Returns none if no url could or should be generated.
    """

    if source_url == False:
        return None

    if domain == "py":
        # Get the path to the source file of the module in string form.
        code_path = pathlib.Path(os.path.join(freecad_source_path, "src"))
        matching_files = [f for f in code_path.glob("**/{}.py".format(info["module"]))]

        # If there's more than one file, don't bother, too hard.
        if len(matching_files) > 1:
            return None

        # Get the line number the thing appears on.
        name = info["fullname"]

        if len(name.split(".")) == 1:
            method = False
        else:
            method = True


        define_line = None

        # If it's a class or a function, just straightformwardly get the line
        # it's defined on.
        if not method:
            with open(matching_files[0], "r") as file:
                lines = file.readlines()
                
                relevant_lines = [(i,l) for i,l in enumerate(lines) if name in l]

                for linenum, line in relevant_lines:
                    pattern = "(def|class)\s+{}.*:".format(name)
                    if re.search(pattern, line):
                        define_line = (linenum, line)
                        break

        # If its a method, it may be defined multiple times. So find the lines
        # it's defined on, then find the method's class, and use that class's
        # definition specifically.
        elif method:

            class_name = name.split(".")[0]
            method_name = name.split(".")[1]

            # Find the times the method is defined anywhere in the file.
            with open(matching_files[0], "r") as file:
                lines = file.readlines()
                
                relevant_lines = [(i,l) for i,l in enumerate(lines) if method_name in l]

                define_lines = []

                for linenum, line in relevant_lines:
                    pattern = "def\s+{}.*:".format(method_name)
                    if re.search(pattern, line):
                        define_lines.append((linenum, line))

                # If it's only defined once, just use that one.
                if len(define_lines) == 1:
                    define_line = define_lines[0]
                
                # Find where the method's class is defined.
                else:
                    class_relevant_lines = [(i,l) for i,l in enumerate(lines) if class_name in l]
                    
                    class_define_line = None

                    for linenum, line in class_relevant_lines:
                        pattern = "class\s+{}.*:".format(class_name)
                        if re.search(pattern, line):
                            class_define_line = (linenum,line)
                            break

                    # Find the first definition of the method after the class
                    # is defined.
                    for linenum, line in define_lines:
                        if linenum > class_define_line[0]:
                            define_line = (linenum, line)
                            break


        define_line_anchor = "#L{line_num}".format(line_num = define_line[0] + 1)

        str_path_to_file = [str(f)[len(freecad_source_path) :] for f in matching_files][0]

        url_to_file = source_url + str_path_to_file + define_line_anchor

        return url_to_file

    return None


# -- Project information -----------------------------------------------------

project = 'FreeCAD'
copyright = '2020, FreeCAD community'
author = 'FreeCAD community'

# -- General configuration ---------------------------------------------------

extensions = [
    "sphinx.ext.autodoc",
    "breathe",
    "sphinx.ext.napoleon",
    "sphinx.ext.linkcode"
]

templates_path = ['_templates']

# Autodoc config
autodoc_default_options = {
    "member-order": "bysource"
        }


# -- Breathe configuration ---------------------------------------------------

# For each section of FreeCAD that contains cpp code, a seperate breathe
# project must be made to limit the amount of code doxygen and breath needs to
# scrape each time the documentation gets generated.

breathe_path = "../doxygen_and_breathe/{}/dox_output/xml"

breathe_projects = {
    "App": breathe_path.format("App"),
    "Base": breathe_path.format("Base"),
    "Gui": breathe_path.format("Gui"),
    "Main": breathe_path.format("Main"),
    "Assembly": breathe_path.format("Assembly"),
    "Drawing": breathe_path.format("Drawing"),
    "Draft": breathe_path.format("Draft"),
    "Fem": breathe_path.format("Fem"),
    "Part": breathe_path.format("Part"),
    "Sketcher": breathe_path.format("Sketcher")
    }

# -- Options for HTML output -------------------------------------------------

html_theme = 'alabaster'
html_static_path = ['static']
