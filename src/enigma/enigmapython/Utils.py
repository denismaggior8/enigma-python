from importlib import import_module

class Utils:

    @staticmethod
    def find_all_subclasses(cls):
        return set(cls.__subclasses__()).union(
            [s for c in cls.__subclasses__() for s in Utils.find_all_subclasses(c)])

    @staticmethod
    def instance_class(cls):
        try:
            module_path, class_name = cls.rsplit('.', 1)
            module = import_module(module_path)
            return getattr(module, class_name)
        except (ImportError, AttributeError) as e:
            raise ImportError(cls)