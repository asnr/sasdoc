
class MacroLib:
    """docstring for MacroLib"""
    def __init__(self):
        self._macros = []
        self._lib_title = None
        self._src_path = None

    def add_src_path(self, src_path):
        self._src_path = str(src_path)
        if self._lib_title is None:
            self._lib_title = src_path.stem
        return self

        
    def add_macro(self, macro):
        self._macros.append(macro)
        return self


    def make_reST(self):

        head = ''
        if self._lib_title is not None:
            head = self._lib_title + '\n' + \
                   ('='*len(self._lib_title)) + '\n\n'

        intro = ''
        if self._src_path is not None:
            intro="""The SAS source file for this library is here:

``{src_path}``

To include this library in your code, use::

    %include "{src_path}";

""".format(src_path=self._src_path)

        macro_reSTs = '\n\n'.join([ m.make_reST() for m in self._macros ])
        return ''.join([head, intro, macro_reSTs])