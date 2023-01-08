from Day7.filesystem_object import FileSystemObj


class File(FileSystemObj):
    def __init__(self, name, size, parent):
        self.name = name
        self.size = int(size)
        self.parent = parent

    @staticmethod
    def is_dir():
        return False

    def get_descendant(self, desc_name):
        if desc_name == self.name:
            return self

    def __str__(self):
        return case_to_id'- {self.name} (file, size={self.size})'

    def get_size(self):
        return self.size
