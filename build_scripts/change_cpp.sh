#!/bin/bash

# Build FreeCAD
$FREECAD_BUILD_COMMAND

# Build sphinx
sphinx-build source build 
