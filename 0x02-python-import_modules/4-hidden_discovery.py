import importlib.util

def list_module_names(module_file):
    # Create a spec for the module
    module_spec = importlib.util.spec_from_file_location("hidden_module", module_file)

    # Load the module from the spec
    module = importlib.util.module_from_spec(module_spec)
    module_spec.loader.exec_module(module)

    # Get the names defined in the module
    module_names = [name for name in dir(module) if not name.startswith("__")]

    return sorted(module_names)

if __name__ == "__main__":
    module_file = "hidden_4.pyc"

    module_names = list_module_names(module_file)

    for name in module_names:
        print(name)
