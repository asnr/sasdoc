
class SASMacro:

    def __init__(self, name, comment, position_params=None, keyword_params=None):
        self._name = name
        self._position_params = position_params
        self._keyword_params = keyword_params
        self._comment = comment

    def make_reST(self):
        return self._comment
