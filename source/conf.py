# -- FreeCAD setup -----------------------------------------------------------

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
    "breathe",
    "sphinx.ext.napoleon"
]

templates_path = ['_templates']

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
