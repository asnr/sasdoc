from sasmacro import SASMacro
from macrolib import MacroLib
from sas_parsers import simple_sas_2_rst

s = open('sas_source/Production/CharAnal_CT_Tom.sas').read()
macro_lib = simple_sas_2_rst(s)
print(macro_lib._macros[0].make_reST())
# print(macro_lib.make_reST())

# sas = SASMacro('yep', s)
# print(sas.make_reST())