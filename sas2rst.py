import sys
from pathlib import Path

from builder import Builder


if __name__ == '__main__':
    
    # with open(sys.argv[1]) as fp:
    #     s = fp.read()

    # print(sas_source_2_rst(s))
    # print(simple_sas_2_rst(s))
    # print(Root(Path(sys.argv[1])).make_reST())
    
    builder = Builder(Path(sys.argv[1]))
    builder.write_reST_files()