from string import ascii_lowercase
from typing import List

from misc.helpers import map_rev


class GridNode:
    ROOT_CHAR = 'S'
    TARGET_CHAR = 'E'
    HM_DICT = dict(map_rev(enumerate(ascii_lowercase, start=1)))
    HM_DICT[ROOT_CHAR] = HM_DICT['a']
    HM_DICT[TARGET_CHAR] = HM_DICT['z']

    def __init__(self, char, neighbor_top=None, neighbor_bottom=None, neighbor_left=None, neighbor_right=None):
        self.char = char
        self.val = self.HM_DICT[char]
        self.neighbors_dict = {
            '^': neighbor_top,
            'v': neighbor_bottom,
            '<': neighbor_left,
            '>': neighbor_right,
        }
        # BFS stuff
        self.was_visited = False
        self.dist = float('inf')

    def __getitem__(self, item):
        return self.neighbors_dict[item]

    def __setitem__(self, key, value):
        self.neighbors_dict[key] = value

    @property
    def neighbors(self):
        return list(filter(None, self.neighbors_dict.values()))

    @classmethod
    def is_root(cls, node):
        return node.char == cls.ROOT_CHAR

    @classmethod
    def is_target(cls, node):
        return node.char == cls.TARGET_CHAR
