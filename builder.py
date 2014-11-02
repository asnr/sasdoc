from traversedir import search_dir_for_sas
from sas_parsers import simple_sas_2_rst
from toc import Root
from srcpath import SrcPath
from srcpath import ReSTPath

class Builder:


    __ROOT_STEM = 'index'


    def __init__(self, dir_path):
        self._srcs = [ SrcPath(p) for p in search_dir_for_sas(dir_path) ]
        self._root_path = dir_path


    def write_reST_files(self):

        for src in self._srcs:
            # check if we actually have a SAS file? Eh..
            
            with open(str(src.sas_path())) as fp:
                sas_src_str = fp.read()

            reST_str = simple_sas_2_rst(sas_src_str).make_reST()
            
            with open(str(src.reST_path()), 'w') as out_fp:
                print('Writing to ' + str(src.reST_path()))
                out_fp.write(reST_str)
            
        # Build the root reST file
        docnames_for_toc = [ s.docname(self._root_path) for s in self._srcs]
        root_str = Root(docnames_for_toc).make_reST()

        # Write root reST file
        raw_root_path = self._root_path / (self.__ROOT_STEM+ReSTPath.REST_EXT)
        root_path = ReSTPath(raw_root_path)
        with open(str(root_path.reST_path()), 'w') as root_fp:
            print('Writing to ' + str(root_path.reST_path()))
            root_fp.write(root_str)

