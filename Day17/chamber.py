from itertools import cycle


class Chamber:
    def __init__(self, width, jets, rocks):
        self.width = width
        self.jet_cycle = cycle(jets)
        self.rocks_cycle = cycle(rocks)

    def place_new_rock(self):
        pass

    def push_rock(self):
        pass

    def let_rock_fall(self):
        pass

    def has_last_rock_landed(self):
        pass

    def get_height(self):
        pass
