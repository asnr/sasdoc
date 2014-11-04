
def search_dir_for_extension(dir_path, ext=''):

    if ext and ext[0] != '.':
        ext = '.' + ext

    # Warning! In "large directory trees may consume 
    # an inordinate amount of time", in which case use
    # return [ f for f in dir_path.iterdir() if f.suffix() == ext ]
    paths = dir_path.glob('**/*' + ext)

    return paths


def search_dir_for_sas(dir_path):

    return search_dir_for_extension(dir_path, ext='.sas')