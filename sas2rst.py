import sys
from pathlib import Path

from builder import Builder


if __name__ == '__main__':
    
    src_dir = Path(sys.argv[1])
    
    builder = Builder(src_dir)
    builder.write_reST_files(Path(sys.argv[2]))
    # builder.copy_reST_files(Path(sys.argv[2]))