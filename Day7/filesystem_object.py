from abc import ABC


class FileSystemObj(ABC):
    def get_descendant(self, desc_name):
        pass

    @staticmethod
    def is_dir():
        pass

    def get_size(self):
        pass
