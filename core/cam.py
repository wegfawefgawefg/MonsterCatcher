class Rect:
    def __init__(self, x, y, width, height) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def contains(self, x, y):
        br_x = self.x + self.width
        br_y = self.y + self.height
        if self.x <= x < br_x and\
                self.y <= y < br_y:
            return True
        else:
            return False

class Cam:
    def __init__(self, width, height) -> None:
        self.rect = Rect(x=0, y=0, width=width, height=height)

    def set_pos(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def contains_cam_space(self, camx, camy):
        if 0 <= camx < self.rect.width and\
                0 <= camy < self.rect.height:
            return True
        else:
            return False
        
    def contains_world_space(self, x, y):
        return self.rect.contains(x, y)        

    def to_cam_space(self, x, y):
        cam_space_x = x - self.rect.x
        cam_space_y = y - self.rect.y
        return cam_space_x, cam_space_y
