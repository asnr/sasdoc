
class MacroLib:
    """docstring for MacroLib"""
    def __init__(self):
        self._macros = []
        self._src_path = None

    def add_src_path(self, src_path):
        self._src_path = str(src_path)
        return self

        
    def add_macro(self, macro):
        self._macros.append(macro)
        return self


    def make_reST(self):
        head = ''
        if self._src_path is not None:
            head="""The SAS source file for this library is here:

{src_path}

To include this library in your code, use::

    %include "{src_path}";

""".format(src_path=self._src_path)

        macro_reSTs = [ m.make_reST() for m in self._macros ]
        return head + '\n\n'.join(macro_reSTs)