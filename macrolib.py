
class MacroLib:
    """docstring for MacroLib"""
    def __init__(self):
        self._macros = []
        
    def add_macro(self, macro):
        self._macros.append(macro)

    def make_reST(self):
        macro_reSTs = [ m.make_reST() for m in self._macros ]
        return '\n\n'.join(macro_reSTs)