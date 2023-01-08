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

    def reconstruct_path(self):
        cur_node = self.target
        path = [cur_node]
        while cur_node.parent is not None:
            cur_node = cur_node.parent
            path.append(cur_node)
        # sanity check
        if cur_node.parent is None and not GridNode.is_root(cur_node):
            raise RuntimeError('reconstructed path invalid!')
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
