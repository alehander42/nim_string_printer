import gdb.printing
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__)))
import nim_pretty

gdb.printing.register_pretty_printer(
	gdb.current_objfile(),
	nim_pretty.nim_printer())

nim_pretty.register_printers(gdb.current_objfile())
