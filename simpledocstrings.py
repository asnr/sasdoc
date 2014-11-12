import re

class ArbitraryDocString:

    # Note that regexes that are truncations of other regexes need to appear
    # later in the alternatives list, eg.
    #   re.search(r'a|ab', 'ab').group() -> 'a'
    #   re.search(r'ab|a', 'ab').group() -> 'ab'
    _COMMENT_NOISE_RE = re.compile(r'^\s*\*\*\s*--+\s*|^\s*--+$|^\s*/\*-*|^\s*\*+[ \t]*|^\s+', #|^\s*-+\s*$|
                                   re.MULTILINE)

    def __init__(self, comment_str):
        self._comment_str = comment_str


    def _sanitise_comment(self):
        return self._COMMENT_NOISE_RE.sub('', self._comment_str)


    def __str__(self):
        return self._sanitise_comment()


class ReSTDocString:


    def __init__(self, comment_str):
        self._comment_str = comment_str


    def __str__(self):
        return self._comment_str