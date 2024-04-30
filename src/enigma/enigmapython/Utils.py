from importlib import import_module

class Utils:

    @staticmethod
    def find_all_subclasses(cls):
        return set(cls.__subclasses__()).union(
            [s for c in cls.__subclasses__() for s in Utils.find_all_subclasses(c)])

    @staticmethod
    def get_class_instance(cls):
        try:
            module_path, class_name = cls.rsplit('.', 1)
            module = import_module(module_path)
            return getattr(module, class_name)
        except (ImportError, AttributeError) as e:
            raise ImportError(cls)

    @staticmethod    
    def swap_chars(string, ch1, ch2):
        if ch1 == ch2: return string
        str_list = []
        for char in string:
            if char == ch1:
                str_list.append(ch2)
            elif char == ch2:
                str_list.append(ch1)
            else:
                str_list.append(char)
        return ''.join(str_list)
    