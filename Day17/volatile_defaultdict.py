from collections import defaultdict


class VolatileDefaultDict(defaultdict):
    """
    Provides a defaultdict-like functionality, but key is *not* added when __getitem__ is called.
    """
    def __init__(self, default_factory, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.default_factory = default_factory

    def __getitem__(self, item):
        if item in self:
            return super().__getitem__(item)
        return self.default_factory()
