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

extensions = [
    "sphinx.ext.autodoc",
    "breathe"
]

templates_path = ['_templates']

# -- Breathe configuration ---------------------------------------------------

breathe_projects = {"FreeCAD": "../doxygen_and_breathe/dox_output/xml"}
breathe_default_project = "FreeCAD"

# -- Options for HTML output -------------------------------------------------

html_theme = 'alabaster'
html_static_path = ['_static']
