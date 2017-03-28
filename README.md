
nim strings printer
==

A simple pretty printer for some nim values in gdb

The goal is to see how useful can custom pretty printers/commands in gdb be for debugging Nim. 
The current script implements some very simple cases(e.g. handling standard nim strings) which might be useful for easier interpretation of the values in a debug session(print in gdb / hovering over the values in e.g. VSCode show the string value when using the printer instead of a hex pointer)

Another possible experiment is to write a custom gdb command that can help with mangled names (autocompleting the most probable \<name\>_\<hash\> for example)

### Usage

The current version is just a toy, it doesn't handle edge cases etc, to add it, the simplest possible thing you can do is to save the scripts in the folder of your whatever.nim file and `mv` _gdb.py to whatever-gdb.py.

