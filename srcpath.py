from pathlib import Path

class SrcPath:

    REST_EXT = '.rst'
    SAS_EXT  = '.sas'  # also used by traversedir, sort this shit out

    def __init__(self, sas_src_path):
        self._src_parent = sas_src_path.parent
        self._src_stem = sas_src_path.stem

    def sas_path(self):
        return self._src_parent / (self._src_stem + self.SAS_EXT)

    def reST_path(self):
        return self._src_parent / (self._src_stem + self.REST_EXT)

    def docname(self, root_dir):
        return str(self._src_parent.relative_to(root_dir) / self._src_stem)