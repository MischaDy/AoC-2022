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
        self.root.was_visited = True
        queue = deque([self.root])
        while queue:
            cur_node = queue.popleft()
            if GridNode.is_target(cur_node):
                break
            for neighbor in cur_node.neighbors:
                if neighbor.was_visited or neighbor.val - cur_node.val > 1:
                    # we've been there or don't want to climb
                    continue
                neighbor.was_visited = True
                neighbor.parent = cur_node
                queue.append(neighbor)
        path = self.reconstruct_path()
        return len(path) - 1

    def run_bfs_mssp(self):
        # based on https://en.wikipedia.org/wiki/Breadth-first_search#Pseudocode
        a_node_chars = 'Sa'
        self.target.was_visited = True
        queue = deque([self.target])
        cur_node = None  # for the linter...
        while queue:
            cur_node = queue.popleft()
            if cur_node.char in a_node_chars:
                break
            for neighbor in cur_node.neighbors:
                if neighbor.was_visited or cur_node.val - neighbor.val > 1:
                    # we've been there or don't want to climb
                    continue
                neighbor.was_visited = True
                neighbor.parent = cur_node
                queue.append(neighbor)
        path = self.reconstruct_path(cur_node, GridNode.is_target)
        return len(path) - 1

    def reconstruct_path(self, start=None, finish_check=GridNode.is_root):
        if start is None:
            start = self.target
        cur_node = start
        path = [cur_node]
        while not finish_check(cur_node):
            cur_node = cur_node.parent
            path.append(cur_node)
        return path

    @staticmethod
    def reconstruct_path2(start):
        cur_node = start
        path = [cur_node]
        while not GridNode.is_target(cur_node):
            cur_node = cur_node.parent
            path.append(cur_node)
        return path

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
                    shifted_r, shifted_c = r + delta_r, c + delta_c
                    if shifted_r not in range(len(nodes)):
                        neighbor = None
                    elif shifted_c not in range(len(row)):
                        neighbor = None
                    else:
                        neighbor = nodes[r + delta_r][c + delta_c]
                    node[dir_] = neighbor
        nodes_flat = flatten_once(nodes)
        root = next(filter(GridNode.is_root, nodes_flat))
        target = next(filter(GridNode.is_target, nodes_flat))
        return cls(root, target, nodes)
