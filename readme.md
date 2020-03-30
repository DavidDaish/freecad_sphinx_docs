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
- The absolute path to the root directory of the source code location of
  FreeCAD.

Now run these commands to build the entire documentation.

```bash
source variables_file
./build_scripts/build_all.sh
```

Now run the following commands in *separate terminals* to regenerate the
documentation whenever specific sections change. Feel free to exclude any if
you don't intend to edit the relevant file types.

### To regenerate when sphinx code is changed

```bash
source variables_file
find ./source | entr ./build_scripts/change_sphinx.sh
```

### To regenerate when python code is changed

```bash
source variables_file
find $FREECAD_SOURCE_LOCATION -name *.py | entr ./build_scripts/change_python.sh
```

### To regenerate when c++ code is changed

This is more complicated. To bring compile times down to usable levels, each of
the major parts of the FreeCAD code, such as Arch, Draft, Main, or Gui are
processed seperately. You can see the different sections in the
`doxygen_and_breathe` directory.

To process changes to the c++ code in each of these sections, export an
enviroment variable named `section`, with the value being one of the
directories in the `doxygen_and_breathe` directory. EG:

```bash
export section=Draft
```

Then run the following commands.

```bash
source variables_file
find $FREECAD_SOURCE_LOCATION -name *$section*.cpp -o -name *$section*.h -o -name *$section*.dox | entr ./build_scripts/change_cpp.sh $section
```
