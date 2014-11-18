from traversedir import search_dir_for_sas

class Root:

# child_docs is already destemmed
    def __init__(self, child_docs):
        self._child_docs = child_docs


    def make_reST(self):

        head = """.. tmp_test documentation master file, created by
   sphinx-quickstart on Sun Nov  2 11:57:47 2014, modified by Andres later.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to auto-generated docs
==============================

Contents:

.. toctree::
   :maxdepth: 1

"""

        children = ''.join([ '   ' + p + '\n' for p in self._child_docs ])

        foot = """
Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""
        return head + children + foot





