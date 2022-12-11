from typing import List, Callable


class Monkey:
    def __init__(self, items: List[int], op: Callable[[int], int], test_div: int, next_monkeys: List["Monkey"] = None):
        if next_monkeys is None:
            next_monkeys = []
        self.items = items
        self.op = op
        self.test_div = test_div
        self.next_monkeys = next_monkeys
        self.num_items_checked = 0

    def give(self, item: int):
        self.items.append(item)

    def make_turn(self):
        for item in self.items:
            self.num_items_checked += 1
            new_item = self.op(item) // 3
            next_monkey_ind = 0 if new_item % self.test_div == 0 else 1
            self.next_monkeys[next_monkey_ind].give(new_item)
        self.items = []

    def make_turn2(self, worry_reducer):
        for item in self.items:
            self.num_items_checked += 1
            new_item = self.op(item)
            next_monkey_ind = 0 if new_item % self.test_div == 0 else 1
            new_item %= worry_reducer
            self.next_monkeys[next_monkey_ind].give(new_item)
        self.items = []
