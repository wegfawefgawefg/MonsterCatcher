class Engine:
    def render_map(self, cam, map, overworld_buffer):
        for y in range(overworld_buffer.height):
            for x in range(overworld_buffer.width):
                tile_x = cam.rect.x + x
                tile_y = cam.rect.y + y
                if 0 <= tile_x < map.width and 0 <= tile_y < map.height:
                    tile = map.tiles[tile_y][tile_x]
                    overworld_buffer.buffer[y][x] = tile.char
                else:
                    overworld_buffer.buffer[y][x] = " "

    def render_character(self, character, buffer_x, buffer_y, overworld_buffer):
        if character.render_state in character.pixie.chars:
            char = character.pixie.chars[character.render_state]
        else:
            char = character.pixie.chars["facing_down"]
        overworld_buffer.buffer[buffer_y][buffer_x] = char

    def render_player(self, cam, player, overworld_buffer):
        cam_x, cam_y = cam.to_cam_space(player.x, player.y)
        self.render_character(player, cam_x, cam_y, overworld_buffer)

    def render_npcs(self, cam, npcs, overworld_buffer):
        for npc in npcs:
            cam_x, cam_y = cam.to_cam_space(npc.x, npc.y)
            if cam.contains_cam_space(cam_x, cam_y):
                self.render_character(npc, cam_x, cam_y, overworld_buffer)

    def render(self, game, cam, overworld_buffer):
        if game.mode == "overworld":
            self.render_map(cam, game.map, overworld_buffer)
            self.render_player(cam, game.player, overworld_buffer)
            self.render_npcs(cam, game.npcs, overworld_buffer)

            print("OVERWORLD\n")
            print("__________")
            print(overworld_buffer)