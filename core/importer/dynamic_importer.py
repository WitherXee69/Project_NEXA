import importlib.util
from pathlib import Path
import inspect
from core.error_handler import ImportFilesNotFoundError

class DynamicImporter:
    def dynamic_import(self, directory, imported_modules, extension='.py'):
        import_path = Path(directory).resolve()
        if not import_path.is_dir():
            raise ImportFilesNotFoundError(directory)
        
        for file in import_path.iterdir():
            if file.is_file() and file.suffix == extension and file.stem != '__init__':
                module_name = file.stem
                file_path = Path(file).resolve()

                spec = importlib.util.spec_from_file_location(module_name, file_path)
                if spec and spec.loader:
                    module = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(module)
                    imported_modules[module_name] = module
                else:
                    print(f"Failed to load module from {file_path}")
        return imported_modules
    
    def get_classes_from_module(self, modules):
        classes = {}
        for module_name, module in modules.items():
            for name, obj in inspect.getmembers(module, inspect.isclass):
                if obj.__module__ == module.__name__:
                    classes[name] = obj
        return classes