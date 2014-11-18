import re
from sasmacro import SASMacro
from macrolib import MacroLib
from toc import Root



# NOTE this is buggy if semicolons ';' can feature in keyword
# arguments, eg. p=%str(;)
#_COMMENTED_MACRO_RE = re.compile(r'/\*\*(?P<comment>.+?)\*/\s*%' +
#                                 r'macro(?P<signature>.+?);',
#                                 re.MULTILINE|re.DOTALL)
_MACRO_RE = re.compile(r'%macro(?P<signature>.+?);', re.MULTILINE|re.DOTALL)

# This regex relies on the greediness of the .* for the parameters
# to avoid stuffing up parameters like '(param=%str( ))'.
_SIGNATURE_RE = re.compile(r'\s*(?P<name>\w+)\s*(\((?P<params>.*)\))*',
                           re.MULTILINE|re.DOTALL)

_SHORT_CMMT_RE = re.compile(r'\*(.*?);', re.MULTILINE|re.DOTALL)
_LONG_CMMT_RE = re.compile(r'/\*(.*?)\*/', re.MULTILINE|re.DOTALL)


class MacroSignature:

    # this holds the parameters as well as the name
    def __init__(self, sign_str):
        pass


    def __str__(self):
        pass




def parse_signature(s):
    
    signature_match = _SIGNATURE_RE.search(s)
    
    if signature_match is None:
        return ("ERROR COULDN'T PARSE SIGNATURE :(", None, None)
    elif signature_match.group('params') is None:
        return (signature_match.group('name').strip(), None, None)
    else:
        params = signature_match.group('params').split(',')
        pos_params = [ p.strip() for p in params if p.find('=') < 0 ]
        key_params = [ p.strip() for p in params if p.find('=') >= 0 ]
        return (signature_match.group('name').strip(), pos_params, key_params)


def simple_sas_2_rst(sas_src):
    """Looks for first macro, tries to find any comment above it"""

    macro_match = _MACRO_RE.search(sas_src)

    if macro_match is None:
        return "Didn't find any macros :("
    else:
        name, position_params, keyword_params = parse_signature(
                                                    macro_match.group('signature'))

        # get the first comment, extract comment body
        src_before_macro = sas_src[:macro_match.start()]
        shrt_cmmt_match = _SHORT_CMMT_RE.search(src_before_macro)
        long_cmmt_match = _LONG_CMMT_RE.search(src_before_macro)
        
        if shrt_cmmt_match is None and long_cmmt_match is None:
            comment = None
        elif shrt_cmmt_match is not None and (long_cmmt_match is None or
             shrt_cmmt_match.start() < long_cmmt_match.start()):
            comment = shrt_cmmt_match.group(1)
        else:
            comment = long_cmmt_match.group(1)

        
        macro = SASMacro(name, comment, position_params=position_params,
                         keyword_params=keyword_params)

        return MacroLib().add_macro(macro)


def sas_source_2_rst(sas_src):

    macro_lib = MacroLib()

    currpos = 0
    while True:
        match = _COMMENTED_MACRO_RE.search(sas_src, currpos)
        if match is None:
            break
        
        name, position_params, keyword_params = parse_signature(
                                                    match.group('signature'))
        comment = match.group('comment')

        macro = SASMacro(name, comment, position_params=position_params,
                         keyword_params=keyword_params)
        macro_lib.add_macro(macro)
        
        currpos = match.end()
        

    return macro_lib