from pixies import *

class Character:
    def __init__(self, x, y, motion, pixie) -> None:
        self.x = x
        self.y = y
        self.pixie = pixie
        self.render_state = "default"

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
        self.render_state = "facing_down"
        self.move(self.x, self.y + 1, map, npcs)

    def move_left(self, map, npcs):
        self.render_state = "facing_left"
        self.move(self.x - 1, self.y, map, npcs)

    def move_right(self, map, npcs):
        self.render_state = "facing_right"
        self.move(self.x + 1, self.y, map, npcs)

    def move_up(self, map, npcs):
        self.render_state = "facing_up"
        self.move(self.x, self.y - 1, map, npcs)

    def render(self, player, overworld_buffer):
        ''' assumes you already checked the character is on screen  '''
        if self.render_state in self.pixie.chars:
            char = self.pixie.chars[self.render_state]
        else:
            char = self.pixie.chars["default"]
        x = 4 + self.x - player.x
        y = 4 + self.y - player.y
        overworld_buffer.buffer[y][x] = char

class Player(Character):
    def __init__(self) -> None:
        pixie = PlayerPixie()
        super().__init__(x=4, y=4, motion="static", pixie=pixie)

    #def render(self, overworld_buffer):
    #    write_x = 4
    #    write_y = 4
    #    if self.x < 4:
    #        write_x = self.x
    #    if self.y < 4:
    #        write_y = self.y
    #    super().render(overworld_buffer)
        
        #overworld_buffer.buffer[write_y][write_x] = self.char
