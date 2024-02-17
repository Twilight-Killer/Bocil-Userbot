from glob import glob
from os.path import basename, dirname, isfile


def loadP():
    mod_paths = glob(f"{dirname(file)}/*.py")
    return sorted(
        [
            basename(f)[:-3]
            for f in mod_paths
            if isfile(f) and f.endswith(".py") and not f.endswith("init.py")
        ]
    )
