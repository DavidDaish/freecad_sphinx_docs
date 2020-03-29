# Sphinx FreeCAD documentation

## Setup

1) Successfully build FreeCAD
2) Install sphinx: www.sphinx-doc.org/en/stable/usage/installation.html
3) Install breathe: https://github.com/michaeljones/breathe
4) Install doxygen: http://www.doxygen.nl/manual/install.html
5) Install entr, if you'd like to build the documentation automatically on changes: http://eradman.com/entrproject/

## Building the documentation automatically on change

To auto-generate sphinx documentation when you make a source code change, edit
the `variables_file` and set the variables to their appropriate values,
suitable for your personal development environment.

They are, respectively:

- The command or script that builds FreeCAD from source;
- The absolute path to the root directory of the build location of FreeCAD;
- The absolute path to the root directory of the source code location of FreeCAD.

Now run the following three sets of commands in three separate terminals. Feel
free to exclude any if you don't intend to edit the relevant file types.

To regenerate when sphinx code is changed:

```bash
source variables_file
find ./source | entr ./build_scripts/change_sphinx.sh
```

To regenerate when python code is changed:

```bash
source variables_file
find $FREECAD_SOURCE_LOCATION -iname *.py | entr ./build_scripts/change_python.sh
```

To regenerate when c++ code is changed:

```bash
source variables_file
export section=Draft
find $FREECAD_SOURCE_LOCATION -name *$section*.cpp -o -name *$section*.h -o -name *$section*.dox | entr ./build_scripts/change_cpp.sh $section
```

You can now find the built html documentation in `build/index.html`.

## Building the documentation manually

To generate documentation manually, first, build FreeCAD. Then, export the
following environment variables.

They are, respectively:

- The absolute path to the root directory of the build location of FreeCAD;
- The absolute path to the root directory of the source code location of FreeCAD.

```
export FREECAD_BUILD_LOCATION=/home/me/freecad_build
export FREECAD_SOURCE_LOCATION=/home/me/freecad_source
```

Run doxygen over the source code

```
doxygen doxygen_and_breathe/Doxyfile
```

Now run sphinx-build.

```
sphinx-build source build
```
