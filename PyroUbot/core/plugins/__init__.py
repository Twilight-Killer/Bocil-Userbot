import importlib.util
import os

plugin_dir = os.path.join(os.path.dirname(__file__), "core", "plugins")

for file_name in os.listdir(plugin_dir):
    if file_name.endswith(".py") and not file_name.startswith("__"):
        module_name = file_name[:-3]
        spec = importlib.util.spec_from_file_location(module_name, os.path.join(plugin_dir, file_name))
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
