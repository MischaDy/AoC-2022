from typing import Set, Dict

from Day7.file import File
from Day7.filesystem_object import FileSystemObj


class Directory(FileSystemObj):
    def __init__(self, name, children: Dict[str, "Directory"] = None, parent: "Directory" = None):
        if children is None:
            children = dict()
        self.name = name
        self.children = children
        self.child_names = set(map(lambda c: c.name, children))
        self.parent = parent

    def add_child(self, name, size=0):
        """
        Add child. If child already exists, fail *silently*.
        :param name:
        :param size:
        :return:
        """
        if name in self.child_names:
            raise ValueError(f'child {name} already exists')
            # return

        if size:
            child = File(name, size, parent=self)
        else:
            child = Directory(name, parent=self)
        self.children[name] = child
        self.child_names.add(name)

    def get_child(self, name):
        return self.children[name]

    # def get_descendant(self, desc_name):
    #     if desc_name == self.name:
    #         return self
    #
    #     for child in self.children.values():
    #         child_res = child.get_descendant(desc_name)
    #         if child_res is not None:
    #             return child_res

    def get_all_subdirs(self) -> Set["Directory"]:
        subdirs = {self}
        for child in self.children.values():
            if not child.is_dir():
                continue

            subdirs.add(child)
            subdirs.update(child.get_all_subdirs())
        return subdirs

    @staticmethod
    def is_dir():
        return True

    def prettyprint(self):
        print(self.prettify())

    def prettify(self, level=0):
        string = f'- {self.name} (dir)'
        for child in self.children.values():
            string += '\n' + (level + 1) * '  '
            if child.is_dir():
                string += child.prettify(level + 1)
            else:
                string += str(child)

        if level:
            return string
        print(string)  # only print at level 0

    def get_size(self):
        return sum(c.get_size() for c in self.children.values())

    def __str__(self):
        return self.name

