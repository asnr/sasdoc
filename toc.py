from traversedir import search_dir_for_sas

class Root:

# child_docs is already destemmed
    def __init__(self, child_docs):
        self._child_docs = child_docs


    def make_reST(self):
        head = '.. toctree::\n\n'
        children = ''.join([ '   ' + p + '\n' for p in self._child_docs ])
        return head + children





