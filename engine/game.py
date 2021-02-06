import pygame
# import game_sprite
# from game_sprite import *
# import scene
from engine.scene import Scene


def load_image(name, size: (int, int) = None, color_key: pygame.Color = None) -> pygame.image:
    image = pygame.image.load("textures\\" + name)
    if color_key is not None:
        image.set_colorkey(color_key)
    if size is not None:
        image = pygame.transform.scale(image, size)
    return image


class Window:
    time_delay = 1000 // 60

    def __init__(self, scene: Scene, name: str):
        pygame.init()
        pygame.display.set_caption(name)
        self.canvas = pygame.display.set_mode(scene.get_size())
        self.scene = scene

    def set_fps(self, fps: int):
        self.time_delay = 1000 // fps

    def launch(self):
        running = True
        clock = pygame.time.Clock()
        time = 0

        while running:
            events = pygame.event.get()

            for event in events:
                if event.type == pygame.QUIT:
                    running = False

            self.scene.run(time, events)
            self.scene.draw(self.canvas)

            time = clock.tick()
            pygame.time.delay(self.time_delay - time)

            pygame.display.flip()
        pygame.quit()
