from sphinxdoc import SphinxDocString
from simpledocstrings import ArbitraryDocString
from simpledocstrings import ReSTDocString
from simpledocstrings import VerbatimDocString

class SASMacro:

    _NUMPYDOC_PREFIX = '*DOC**'
    _reST_PREFIX = '*reST**'

    def __init__(self, name, comment,
                 position_params=None, keyword_params=None):
        self._name = name
        self._position_params = position_params
        self._keyword_params = keyword_params
        if comment is None:
            self._doc_string = None
        elif comment.startswith(self._NUMPYDOC_PREFIX):
            comment = comment[len(self._NUMPYDOC_PREFIX):]
            self._doc_string = SphinxDocString(comment)
        elif comment.startswith(self._reST_PREFIX):
            comment = comment[len(self._reST_PREFIX):]
            self._doc_string = ReSTDocString(comment)
        else:
            self._doc_string = VerbatimDocString(comment)


    def make_reST(self):
        out = []  # put everything in here instead of adding bit by bit?
        out += [self._name] # + 
               # str(self._position_params) + str(self._keyword_params)]
        out += ['-'*len(self._name)]
        out += [str(self._doc_string) if self._doc_string is not None else '']
        return '\n'.join(out)


