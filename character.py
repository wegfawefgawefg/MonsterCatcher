class Character:
    def __init__(self, x, y, chars) -> None:
        self.x = x
        self.y = y
        self.char = chars["default"]

        if chars["directional"]:
            self.down_char = "v"
            self.right_char = ">"
            self.left_char = "<"
            self.up_char = "^"

    def move(self, x, y, map, npcs):
        #   is new spot on map?
        if not (0 <= x < map.width) or not (0 <= y < map.width):
                return

        #   tile collisions
        if not map.tiles[y][x].allows:
            return

        #   npc collisions
        npc_already_there = False
        for npc in npcs:
            if npc.x == x and npc.y == y:
                npc_already_there = True
                break
        if not npc_already_there:
            self.x = x
            self.y = y
    
    def move_down(self, map, npcs):
        self.char = self.down_char
        self.move(self.x, self.y + 1, map, npcs)

    def move_left(self, map, npcs):
        self.char = self.left_char
        self.move(self.x - 1, self.y, map, npcs)

    def move_right(self, map, npcs):
        self.char = self.right_char
        self.move(self.x + 1, self.y, map, npcs)

    def move_up(self, map, npcs):
        self.char = self.up_char
        self.move(self.x, self.y - 1, map, npcs)

    def render(self, overworld_buffer):
        ''' assumes you already checked the character is on screen  '''
        overworld_buffer.buffer[self.y][self.x] = self.char

class Player(Character):
    def __init__(self) -> None:
        super().__init__(x=4, y=4, char="v")

    def render(self, overworld_buffer):
        write_x = 4
        write_y = 4
        if self.x < 4:
            write_x = self.x
        if self.y < 4:
            write_y = self.y
        overworld_buffer.buffer[write_y][write_x] = self.char
