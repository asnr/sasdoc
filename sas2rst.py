import sys
import re
from pathlib import Path

from sasmacro import SASMacro
from macrolib import MacroLib


def parse_signature(s):
    params_start = s.find('(')
    if params_start < 0:
        return (s.strip, None, None)
    else:
        return (s[:params_start], None, None)


# NOTE this is buggy if semicolons ';' can feature in keyword
# arguments, eg. p=%str(;)
_COMMENTED_MACRO_RE = re.compile(r'/\*\*(?P<comment>.+?)\*/\s*%' +
                                 r'macro(?P<signature>.+?);',
                                 re.MULTILINE | re.DOTALL)
# _PARANTHESES_RE = re.compile(r'\(|\)', re.MULTILINE)

def sas_source_2_rst(sas_src):

    macro_lib = MacroLib()

    currpos = 0
    while True:
        match = _COMMENTED_MACRO_RE.search(sas_src, currpos)
        if match is None:
            break
        
        name, position_params, keyword_params = parse_signature(match.group('signature'))
        comment = match.group('comment')

        macro = SASMacro(name, comment, position_params=position_params,
                         keyword_params=keyword_params)
        macro_lib.add_macro(macro)
        
        currpos = match.end()
        

    return macro_lib.make_reST()


# def find_brackets():
#     # search for the bracket ending the parameters
#     num_open_parens = 1
#     currpos = m.end()

#     while True:
        
#         paren_m = _PARANTHESES_RE.search(sas_src, currpos)

#         if paren_m is None:
#             break

#         if paren_m.group() == '(':
#             num_open_parens += 1
#         elif paren_m.group() == ')':
#             num_open_parens += -1
        
#         currpos = paren_m.end()

#         if num_open_parens == 0:
#             break

#     if num_open_parens == 0:
#         print('Start: {}, End: {}'.format(m.start(), currpos))
#         print(sas_src[m.start():currpos])



if __name__ == '__main__':
    with open(sys.argv[1]) as fp:
        s = fp.read()

    print(sas_source_2_rst(s))
