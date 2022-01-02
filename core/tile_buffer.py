class TileBuffer:
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
        self.buffer = []
        for _ in range(self.height):
            row = []
            for _ in range(self.width):
                row.append(" ")
            self.buffer.append(row)

    def as_lines(self):
        return ["".join(row) for row in self.buffer]

    def __repr__(self):
        row_strings = []
        for row in self.buffer:
            row_string = "".join(row) + "\n"
            row_strings.append(row_string)
        string_overworld = "".join([row_string for row_string in row_strings])
        return string_overworld
