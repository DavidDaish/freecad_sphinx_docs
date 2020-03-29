#!/bin/bash

sphinx-build -j $(nproc --ignore=2) source build
