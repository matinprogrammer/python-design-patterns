"""
    Prototype pattern
"""
import copy


class Prototype:
    def __init__(self):
        self._objects = {}

    def register(self, name, obj):
        self._objects[name] = obj

    def unregister(self, name):
        del self._objects[name]

    def clone(self, name, **kwargs):
        cloned_obj = copy.deepcopy(self._objects.get(name))
        cloned_obj.__dict__.update(kwargs)
        return cloned_obj


def client_prototype(name, obj, **kwargs):
    prototype = Prototype()
    prototype.register(name, obj)
    return prototype.clone(name, **kwargs)
