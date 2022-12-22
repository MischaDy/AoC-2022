import operator


class Monkey:
    OP_DICT = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.floordiv,
        None: None
    }

    def __init__(self, name, num=None, op_name=None, child_left_name=None, child_right_name=None):
        self.name = name
        self.num = num
        self.op = self.op_name_to_func(op_name)
        self.op_name = op_name
        self.child_left_name = child_left_name
        self.child_right_name = child_right_name

    def yell(self, monkeys):
        if self.num is not None:
            return self.num
        child_left = monkeys[self.child_left_name]
        left_num = child_left.yell(monkeys)
        child_right = monkeys[self.child_right_name]
        right_num = child_right.yell(monkeys)
        return self.op(left_num, right_num)

    @classmethod
    def op_name_to_func(cls, op_name):
        return cls.OP_DICT[op_name]

    def __str__(self):
        if self.num is None:
            job_str = f'{self.child_left_name} {self.op_name} {self.child_right_name}'
        else:
            job_str = str(self.num)
        return f'<name: {self.name}, job: {job_str}>'

    def __repr__(self):
        selfstr = str(self).strip('<>')
        return f'<Monkey {selfstr}>'
