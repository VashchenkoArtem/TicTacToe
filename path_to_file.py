import os

def path_file(name_file):
    path = __file__.split('\\')
    del path[-1]
    del path[-1]
    path = '\\'.join(path)
    path = os.path.join(path, "images/",name_file)
    return path
