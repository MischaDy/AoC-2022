from collections import deque
from typing import Tuple, List, Dict


class Cave:
    def __init__(self, valves):
        self._valves_dict = self.build_valves_dict(valves)
        self.root_name = 'AA'
        self.root = self._valves_dict[self.root_name]

    @property
    def valves(self):
        return self._valves_dict.values()

    @staticmethod
    def build_valves_dict(valves) -> Dict[str, "Valve"]:
        valves_dict = dict()
        for valve in valves:
            valves_dict[valve.name] = valve
        return valves_dict

    @classmethod
    def from_input_lines(cls, lines: List[Tuple[str, int, List]]):
        valves = []
        for name, flow_rate, neighbor_names in lines:
            valves.append(Valve(name, flow_rate, neighbor_names))
        return cls(valves)

    def release_pressure(self, time_lim):
        paths = []
        cur_path = Path(time_lim)
        for neighbor in cur_path[-1].neighbors:
            pass


class Valve:
    def __init__(self, name, flow_rate, neighbors=None):
        if neighbors is None:
            neighbors = []
        self.name = name
        self.flow_rate = flow_rate
        self.neighbors = neighbors
        self.closed = True


class Path:
    def __init__(self, time_left, valves=None, pressure_released=0):
        if valves is None:
            valves = []
        self.time_left = time_left
        self.valves = valves
        self.pressure_released = pressure_released

    def __getitem__(self, item):
        return self.valves[item]

    def add(self, valve, open_valve):
        self.valves.append(valve)
        self.time_left -= 1
        if valve.closed and open_valve:
            self.pressure_released += self.time_left * valve.flow_rate
            valve.closed = False
            self.time_left -= 1
