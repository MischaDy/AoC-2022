from typing import List, Callable


class Monkey:
    def __init__(self, items: List[int], op: Callable[[int], int], divisor: int, next_monkeys: List["Monkey"] = None):
        if next_monkeys is None:
            next_monkeys = []
        self.items = items
        self.op = op
        self.divisor = divisor
        self.next_monkeys = next_monkeys
        self.num_items_checked = 0

    def give(self, item: int):
        self.items.append(item)

    def make_turn(self):
        for item in self.items:
            self.num_items_checked += 1
            new_item = self.op(item) // 3
            next_monkey_ind = 0 if new_item % self.divisor == 0 else 1
            self.next_monkeys[next_monkey_ind].give(new_item)
        self.items = []
