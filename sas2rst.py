import sys
from pathlib import Path

from builder import Builder

# buggy - eg. what happens when first asterisk occurs in a literal string,
# eg. myvar = "*"; in a data block?
# def simple_sas_2_rst(sas_src):
#     """Looks for first macro, tries to find any comment above it"""

#     macro_match = _MACRO_RE.search(sas_src)

#     if macro_match is None:
#         return "Didn't find any macros :("
#     else:
#         name, position_params, keyword_params = parse_signature(
#                                                     macro_match.group('signature'))

#         # get the first comment, extract comment body
#         src_before_macro = sas_src[:macro_match.start()]
#         shrt_cmmt_match = _SHORT_CMMT_RE.search(src_before_macro)
#         long_cmmt_match = _LONG_CMMT_RE.search(src_before_macro)
        
#         if shrt_cmmt_match is None and long_cmmt_match is None:
#             comment = None
#         elif shrt_cmmt_match is not None and (long_cmmt_match is None or
#              shrt_cmmt_match.start() < long_cmmt_match.start()):
#             comment = shrt_cmmt_match.group(1)
#         else:
#             comment = long_cmmt_match.group(1)

        
#         macro = SASMacro(name, comment, position_params=position_params,
#                          keyword_params=keyword_params)

#         return MacroLib().add_macro(macro).make_reST()


# def sas_source_2_rst(sas_src):

#     macro_lib = MacroLib()

#     currpos = 0
#     while True:
#         match = _COMMENTED_MACRO_RE.search(sas_src, currpos)
#         if match is None:
#             break
        
#         name, position_params, keyword_params = parse_signature(
#                                                     match.group('signature'))
#         comment = match.group('comment')

#         macro = SASMacro(name, comment, position_params=position_params,
#                          keyword_params=keyword_params)
#         macro_lib.add_macro(macro)
        
#         currpos = match.end()
        

#     return macro_lib.make_reST()



if __name__ == '__main__':
    
    # with open(sys.argv[1]) as fp:
    #     s = fp.read()

    # print(sas_source_2_rst(s))
    # print(simple_sas_2_rst(s))
    # print(Root(Path(sys.argv[1])).make_reST())
    
    builder = Builder(Path(sys.argv[1]))
    builder.write_reST_files()