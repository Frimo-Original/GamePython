import pygame


class GameSpriteGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()

    def draw(self, surface: pygame.Surface) -> None:
        for sprite in self:
            sprite.rect.x = sprite.position.x
            sprite.rect.y = sprite.position.y
        super().draw(surface)
