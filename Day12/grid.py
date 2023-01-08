from collections import deque
from typing import List

from Day12.gridnode import GridNode
from misc.helpers import flatten_once


class Grid:
    def __init__(self, root: GridNode, target: GridNode, nodes: List[List[GridNode]]):
        if nodes is None:
            nodes = []
        self.root = root
        self.target = target
        self.nodes = nodes

    def __len__(self):
        return len(self.nodes)

    def __getitem__(self, item):
        if isinstance(item, tuple):
            row, col = item
            return self.nodes[row][col]
        return self.nodes[item]

    def run_bfs_sssp(self):
        # based on https://en.wikipedia.org/wiki/Breadth-first_search#Pseudocode
        self.root.visited = True
        self.root.dist = 0
        queue = deque([self.root])
        while queue:
            cur_node = queue.popleft()
            if GridNode.is_target(cur_node):
                return cur_node.dist
            for neighbor in cur_node.neighbors:
                if neighbor.was_visited or neighbor.val - cur_node.val > 1:
                    # we've been there or don't want to climb
                    continue
                neighbor.was_visited = True
                neighbor.dist = min(neighbor.dist, cur_node.dist + 1)
                queue.append(neighbor)

    @classmethod
    def from_heightmap(cls, hm: List[str]):
        nodes = [list(map(GridNode, row))
                 for row in hm]
        shift_dict = {
            '^': (-1, 0),
            'v': (+1, 0),
            '<': (0, -1),
            '>': (0, +1),
        }
        for r, row in enumerate(nodes):
            for c, col in enumerate(row):
                node = nodes[r][c]
                for dir_, (delta_r, delta_c) in shift_dict.items():
                    try:
                        neighbor = nodes[r + delta_r][c + delta_c]
                    except IndexError:
                        neighbor = None
                    node[dir_] = neighbor
        nodes_flat = flatten_once(nodes)
        root = next(filter(GridNode.is_root, nodes_flat))
        target = next(filter(GridNode.is_target, nodes_flat))
        return cls(root, target, nodes)
