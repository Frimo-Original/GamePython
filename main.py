import pygame
from engine.game import *
from engine.scene import Scene
from engine.game_sprite import GameSprite
import random

SCENE_SIZE = (500, 600)

PLATFORM_SIZE = (100, 30)
PLAYER_SIZE = (40, 60)

G = 0.002  # acceleration of gravity

image_cloud = load_image("cloud.png", PLATFORM_SIZE)
image_ground = load_image("ground.png", PLATFORM_SIZE)
image_player = load_image("jumper.png", PLAYER_SIZE)

image_background = load_image("background.png", SCENE_SIZE)

NAME_GROUP_CLOUD = "cloud"
NAME_GROUP_GROUND = "ground"


class Player(GameSprite):
    speed_y = 0
    speed_x = 0.5
    press_left = False
    press_right = False

    def __init__(self, scene):
        super().__init__(scene)
        self.image = image_player
        self.rect = image_player.get_rect()
        self.position.x = SCENE_SIZE[0] // 2 - 20
        self.position.y = SCENE_SIZE[1] // 3

    def run(self, time: int, events: list):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.press_left = True
                if event.key == pygame.K_RIGHT:
                    self.press_right = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.press_left = False
                if event.key == pygame.K_RIGHT:
                    self.press_right = False

        self.speed_y += G * time
        self.position.y += self.speed_y * time

        self.check_jump_platform()

        # if self.position.y >= SCENE_SIZE[1] - self.rect.height:
        #     self.speed_y = -1.4

        if self.press_right:
            self.position.x += time * self.speed_x
        elif self.press_left:
            self.position.x -= time * self.speed_x

        if self.position.x < 0:
            self.position.x = SCENE_SIZE[0] - self.rect.width
        elif self.position.x > SCENE_SIZE[0] - self.rect.width:
            self.position.x = 0

    def check_jump_platform(self):
        clouds_groups = self.scene.get_groups()[NAME_GROUP_CLOUD]
        grounds_groups = self.scene.get_groups()[NAME_GROUP_GROUND]

        if clouds_groups is not None:
            cloud_sprite = pygame.sprite.spritecollideany(self, clouds_groups)
            if cloud_sprite is not None:
                cloud_sprite.jumped()
                self.speed_y = -1.4
        if grounds_groups is not None:
            ground_sprite = pygame.sprite.spritecollideany(self, grounds_groups)
            if ground_sprite is not None:
                self.speed_y = -1.4


class PlatformSprite(GameSprite):
    def __init__(self, image: pygame.image, x: int, y: int, scene):
        super().__init__(scene)
        self.image = image
        self.rect = image.get_rect()
        self.position.x = x
        self.position.y = y

    def run(self, time: int, events: list):
        raise NotImplementedError()


class CloudSprite(PlatformSprite):
    def __init__(self, x: int, y: int, scene):
        super().__init__(image_cloud, x, y, scene)

    def jumped(self):
        pass

    def run(self, time: int, events: list):
        pass


class GroundSprite(PlatformSprite):
    def __init__(self, x: int, y: int, scene):
        super().__init__(image_ground, x, y, scene)

    def run(self, time: int, events: list):
        pass


# class Camera:
#     def __init__(self):
#         self.dx = 0
#         self.dy = 0
#
#     # сдвинуть объект obj на смещение камеры
#     def apply(self, obj):
#         obj.position.x += self.dx
#         obj.position.y += self.dy
#
#     # позиционировать камеру на объекте target
#     def update(self, target):
#         self.dx = -(target.position.x + target.position.w // 2 - width // 2)
#         self.dy = -(target.position.y + target.position.h // 2 - height // 2)


class JumpScene(Scene):
    def __init__(self):
        super().__init__((500, 600), image_background)
        self.time = 0

        position_x = random.randint(0, self.get_size()[0] - 100)
        if random.randint(0, 1):
            self.get_groups().add(NAME_GROUP_CLOUD, CloudSprite(position_x, 500, self))
        else:
            self.get_groups().add(NAME_GROUP_GROUND, GroundSprite(position_x, 500, self))

    def run(self, time: int, events: list()):
        super().run(time, events)
        # self.time += time
        #
        # if self.time > 2000:
        #     position_x = random.randint(0, self.get_size()[0] - 100)
        #     if random.randint(0, 1):
        #         self.get_groups().add(NAME_GROUP_CLOUD, CloudSprite(position_x, 400, self))
        #     else:
        #         self.get_groups().add(NAME_GROUP_GROUND, GroundSprite(position_x, 400, self))
        #
        #     self.time = 0


jump_scene = JumpScene()
jump_scene.get_groups().add("player", Player(jump_scene))


if __name__ == '__main__':
    window = Window(jump_scene, "Jump")
    window.set_fps(165)
    window.launch()
