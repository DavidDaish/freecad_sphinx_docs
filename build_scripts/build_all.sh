#!/bin/bash

# Build FreeCAD
$FREECAD_BUILD_COMMAND

# Loop through doxygen sections.
for section in $(ls doxygen_and_breathe)
do
    doxygen doxygen_and_breathe/$section/Doxyfile
done

# Build sphinx
sphinx-build -j $(nproc --ignore=2) source build
