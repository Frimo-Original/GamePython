import pygame


class DrawInterface:
    def draw(self, canvas: pygame.surface):
        raise NotImplementedError()


class RunInterface:
    def run(self, time: int, events: list):
        raise NotImplementedError()