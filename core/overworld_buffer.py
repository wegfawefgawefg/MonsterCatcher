class OverworldBuffer:
    def __init__(self) -> None:
        self.height = 9
        self.width = 10
        self.buffer = []
        for y in range(self.height):
            row = []
            for x in range(self.width):
                row.append(" ")
            self.buffer.append(row)
        print(f"overworld_dims {len(self.buffer)} {len(self.buffer[0])}")

    def __repr__(self):
        row_strings = []
        for row in self.buffer:
            row_string = "".join(row) + "\n"
            row_strings.append(row_string)
        string_overworld = "".join([row_string for row_string in row_strings])
        return string_overworld
