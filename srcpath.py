from pathlib import Path

# Should probably inherit from Path...

class ReSTPath:

    REST_EXT = '.rst'

    def __init__(self, reST_path):
        self._src_parent = reST_path.parent
        self._src_stem = reST_path.stem

    def reST_path(self):
        return self._src_parent / (self._src_stem + self.REST_EXT)

    # for placement in toc_tree
    def docname(self, root_dir):
        return str(self._src_parent.relative_to(root_dir) / self._src_stem)

    # two args are paths
    def reST_root_change(self, src_dir, dst_dir):
        dst_path = dst_dir / self.reST_path().relative_to(src_dir)        
        return dst_path


class SrcPath(ReSTPath):

    SAS_EXT  = '.sas'  # also used by traversedir, sort this shit out

    def __init__(self, sas_src_path):
        self._src_parent = sas_src_path.parent
        self._src_stem = sas_src_path.stem

    def sas_path(self):
        return self._src_parent / (self._src_stem + self.SAS_EXT)