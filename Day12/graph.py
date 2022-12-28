from collections import deque
from itertools import product
from typing import List

from helpers import flatten


class Graph:
    class Node:
        def __init__(self, value: int, neighbors: List["Graph.Node"] = None):
            if neighbors is None:
                neighbors = []
            self.value = value
            self.neighbors = neighbors
            self.dist = 0

    def __init__(self, nodes: List[Node], start: Node, end: Node):
        self.nodes = nodes
        self.start = start
        self.end = end

    def run_bfs(self):
        queue = deque([self.start])
        while queue:
            node = queue.popleft()

    @classmethod
    def from_heightmap(cls, heightmap):
        nodes = [[Graph.Node(cls.to_elevation(char)) for char in row]
                 for row in heightmap]
        start, end = None, None
        for row, col in product(range(len(heightmap)), repeat=2):
            node = nodes[row][col]
            node.neighbors = cls.get_neighbors(row, col, heightmap)
            if node.value == 'S':
                start = node
            elif node.value == 'E':
                end = node

        if start is None or end is None:
            raise ValueError("heightmap must contain start ('S') and end ('E')")
        return cls(flatten(nodes), start, end)

    @classmethod
    def get_neighbors(cls, row, col, heightmap):
        neighbor_inds = ...
        return neighbors

    @classmethod
    def to_elevation(cls, char):
        if char == 'S':
            char = 'a'
        elif char == 'E':
            char = 'z'
        ord_a = 97  # ord('a')
        return ord(char) - ord_a + 1
