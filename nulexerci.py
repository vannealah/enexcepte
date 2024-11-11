class Object:
    def __init__(self):
        self._dirty = False

    def is_dirty(self):
        return self._dirty

    def mark_dirty(self):
        self._dirty = True

    def clean(self):
        self._dirty = False
