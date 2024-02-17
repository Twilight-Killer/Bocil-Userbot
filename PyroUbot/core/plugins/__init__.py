from glob import glob
from os.path import basename, dirname, isfile


def loadP():
    mod_paths = glob(f"{dirname(__file__)}/*.py")
    return sorted(
        [
            basename(f)[:-3]
            for f in mod_paths
            if isfile(f) and f.endswith(".py") and not f.endswith("__init__.py")
        ]
    )


for module_name in loadP():
    import_statement = f"from PyroUbot.core.plugins.{module_name} import *"
    exec(import_statement)
