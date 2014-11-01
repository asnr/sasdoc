from traversedir import search_dir_for_sas
from sas_parsers import simple_sas_2_rst
from toc import Root

class Builder:

    __reST_EXT = '.rst'
    __ROOT_STEM = 'index'

    def __init__(self, dir_path):
        self._child_paths = search_dir_for_sas(dir_path)
        self._root_path = dir_path

    def build_reST_files(self):

        # This is to keep track of the names to put into the index TOC
        child_docs = []        

        for child_path in self._child_paths:
            # check if we actually have a SAS file? Eh..
            
            with open(str(child_path)) as fp:
                src_str = fp.read()

            reST_str = simple_sas_2_rst(src_str).make_reST()
            child_out_doc = child_path.parent / child_path.stem

            with open(str(child_out_doc) + self.__reST_EXT, 'w') as out_fp:
                print('Writing to ' + str(child_out_doc) + self.__reST_EXT)
                out_fp.write(reST_str)

            child_docs.append(str(child_out_doc))

        # Build then write the root reST file
        root_str = Root(child_docs).make_reST()
        root_reST_path = self._root_path / (self.__ROOT_STEM+self.__reST_EXT)
        with open(str(root_reST_path), 'w') as root_fp:
            print('Writing to ' + str(root_reST_path))
            root_fp.write(root_str)


    # def 
