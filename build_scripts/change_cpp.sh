#!/bin/bash

# Section to run doxygen on
section = $1

# Run doxygen on section
doxygen doxygen_and_breathe/$section/Doxyfile

# Build sphinx
sphinx-build -j $(nproc --ignore=2) source build 
