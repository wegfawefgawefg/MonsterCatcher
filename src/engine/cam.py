class Rect:
    def __init__(self, center, width, height) -> None:
        self.width = width
        self.height = height
        self.set_center(center)
        # width of 10, height of 9

    def set_center(self, center):
        x, y = center
        self.tl = x - self.width / 2, y - self.height / 2
        self.br = self.tl[0] + self.width, self.tl[1] + self.height

    def contains(self, x, y):
        return self.tl[0] <= x <= self.br[0] and self.tl[1] <= y <= self.br[1]

    def __repr__(self) -> str:
        return f"Rect({self.tl[0]}, {self.tl[1]}, {self.width}, {self.height})"

class Cam:
    def __init__(self, width, height) -> None:
        self.last_x, self.last_y = 0, 0
        self.x, self.y = 0, 0
        self.rect = Rect(center=(self.x, self.y), width=width, height=height)

    @property
    def pos(self):
        return self.x, self.y

    def bound_by_map(self, map):
        if not map.lock_cam_in:
            return
        if self.rect.tl[0] < 0:
            self.set_pos(self.rect.width//2, self.y)
        if self.rect.tl[1] < 0:
            self.set_pos(self.x, self.rect.height//2+1)
        if self.rect.br[0] > map.width-1:
            self.set_pos(map.width - self.rect.width//2-1, self.y)
        if self.rect.br[1] > map.height:
            self.set_pos(self.x, map.height - self.rect.height//2-1)

    def set_pos(self, x: float, y: float):
        if not self.last_x or not self.last_y:
            self.last_x, self.last_y = x, y
        # move an amount towards the target
        #self.x += (x - self.x) * 0.1
        #self.y += (y - self.y) * 0.1
        self.x, self.y = x, y
        self.rect.set_center((self.x, self.y))

    def is_in_view(self, x, y):
        return self.rect.contains(x, y)        

    def to_screen_space(self, pos):
        ''' convert world space  to screen space
        screen space is where 
            for x: 0 is the top and 1 is the bottom, 
            for y: 0 is the left and 1 is the right
        '''
        return (pos[0] - self.rect.tl[0]) / self.rect.width, (pos[1] - self.rect.tl[1]) / self.rect.height

    def to_screen_scale(self, scale):
        ''' convert world space scale to screen space scale
        screen space is where 
            for x: 0 is the top and 1 is the bottom,
            for y: 0 is the left and 1 is the right
        '''
        return scale / self.rect.width, scale / self.rect.height
