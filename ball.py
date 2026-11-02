from pico2d import get_canvas_width, load_image

import game_world


class Ball:
    image = None

    def __init__(self, x, y, direction):
        if Ball.image is None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y = x, y
        self.dir = direction

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        self.x += self.dir * 10
        if self.x < -10 or self.x > get_canvas_width() + 10:
            game_world.remove_object(self)
