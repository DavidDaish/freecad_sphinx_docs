#!/bin/bash

# Build FreeCAD
$FREECAD_BUILD_COMMAND

# Build sphinx
sphinx-build -j $(nproc --ignore=2) source build
