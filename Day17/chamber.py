from itertools import cycle

from Day17.rock import Rock

START_DIST_LEFT = 2  # left edge starts out two units away from left wall
START_DIST_DOWN = 3  # bottom edge starts out three units above the highest rock/floor


class Chamber:
    def __init__(self, width, jets, rock_patterns):
        self.width = width
        self.occupied_spaces = set((0, col)  # floor
                                   for col in range(width))
        self.jet_cycle = cycle(jets)
        self.patterns_cycle = cycle(rock_patterns)
        self.cur_rock = None

    def place_new_rock(self):
        new_pattern = next(self.patterns_cycle)
        self.cur_rock = Rock(new_pattern)
        pass

    def push_rock(self):
        jet = next(self.jet_cycle)
        pass

    def let_rock_fall(self):
        pass

    def has_last_rock_landed(self):
        pass

    def get_height(self):
        pass
