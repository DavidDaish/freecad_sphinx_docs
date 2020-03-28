# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys

# Adding FreeCAD and FreeCADGui
try:
    freecad_build_path = os.environ['FREECAD_BUILD_LOCATION']
except:
    raise Exception("Please enter the base directory of FreeCAD's build location.")

print("Specified Freecad build path: {}".format(freecad_build_path))

lib_from_base = "lib/"
freecad_lib_path = os.path.join(freecad_build_path, lib_from_base)
sys.path.append(freecad_lib_path)

import FreeCAD, FreeCADGui
# FreeCADGui.showMainWindow() # this is needed for complete import of GUI modules
doc = FreeCAD.newDocument("doc")

# -- Project information -----------------------------------------------------

project = 'FreeCAD'
copyright = '2020, FreeCAD community'
author = 'FreeCAD community'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc"
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
