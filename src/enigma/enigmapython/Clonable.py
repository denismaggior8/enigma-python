import copy

class Clonable:
    def clone(self):
        """
        Creates a deep copy of the current instance.
        Override this method in subclasses if custom logic is needed.
        """
        return copy.deepcopy(self)