import re

class SASMacro:

    # Note that regexes that are truncations of other regexes need to appear
    # later in the alternatives list, eg.
    #   re.search(r'a|ab', 'ab').group() -> 'a'
    #   re.search(r'ab|a', 'ab').group() -> 'ab'
    _COMMENT_NOISE_RE = re.compile(r'^\s*\*\*\s*--+\s*|^\s*--+$|^\s*/\*-*|^\s*\*+[ \t]*|^\s+', #|^\s*-+\s*$|
                                   re.MULTILINE)

    def __init__(self, name, comment,
                 position_params=None, keyword_params=None):
        self._name = name
        self._position_params = position_params
        self._keyword_params = keyword_params
        self._comment = comment

    def make_reST(self):
        return self._name + '\n' + \
               ('-'*len(self._name)) + '\n' + \
               self._sanitise_comment() if self._comment is not None else ''


    def _sanitise_comment(self):
        return self._COMMENT_NOISE_RE.sub('', self._comment)

