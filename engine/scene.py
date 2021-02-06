from engine.interfaces import *
from engine.groups import GameSpriteGroups
import pygame


class Scene(DrawInterface, RunInterface):
    groups_sprites: GameSpriteGroups

    def __init__(self, size: (int, int), background: pygame.image):
        self.groups_sprites = GameSpriteGroups()
        self.size = size
        self.background = background

    def draw(self, canvas: pygame.surface):
        canvas.blit(self.background, (0, 0))
        for group in self.groups_sprites:
            group.draw(canvas)

    def run(self, time: int, events: list):
        for group in self.groups_sprites:
            for sprite in group:
                sprite.run(time, events)

    def get_size(self) -> (int, int):
        return self.size

    def get_groups(self) -> GameSpriteGroups:
        return self.groups_sprites
