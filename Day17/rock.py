PATTERNS = [
    ['####'],

    ['.#.',
     '###',
     '.#.'],

    ['..#',
     '..#',
     '###'],

    ['#',
     '#',
     '#',
     '#'],

    ['##',
     '##'],
]


class Rock:
    def __init__(self, pattern):
        self.pattern = pattern
        self.height = len(pattern)
        self.width = len(pattern[0])
        self.empty_spaces = self._find_empty_spaces()

    def _find_empty_spaces(self):
        empty_spaces = set(
            (row_ind, col_ind)
            for row_ind, row in enumerate(self.pattern)
            for col_ind, col in enumerate(row)
            if col == '.'
        )
        return empty_spaces
