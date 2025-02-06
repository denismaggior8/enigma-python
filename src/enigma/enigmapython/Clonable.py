import copy

class Clonable:

    def __init__(self):
        super().__init__()

    def clone(self):
        """
        Creates a deep copy of the current instance.
        Override this method in subclasses if custom logic is needed.
        """
        return copy.deepcopy(self)