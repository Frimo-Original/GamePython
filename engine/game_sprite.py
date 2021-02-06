from engine.vector_float import *
from engine.interfaces import *


class GameSprite(pygame.sprite.Sprite, RunInterface):
    position: VectorFloat

    def __init__(self, scene):
        super().__init__()
        self.scene = scene
        self.position = VectorFloat()

    def run(self, time: int, events: list):
        raise NotImplementedError()

    def convert(self):
        self.rect.x = self.position.x
        self.rect.y = self.position.y
