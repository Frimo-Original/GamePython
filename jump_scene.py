# from engine.scene import Scene
#
#
# class JumpScene(Scene):
#     def __init__(self):
#         super().__init__((500, 600), image_background)
#         self.time = 0
#
#     def run(self, time: int, events: list()):
#         super().run(time, events)
#         self.time += time
#
#         if self.time > 2000:
#             position_x = random.randint(0, self.get_size()[0] - 100)
#             if random.randint(0, 1):
#                 self.get_groups().add("clouds", CloudSprite(position_x, 400))
#             else:
#                 self.get_groups().add("grounds", GroundSprite(position_x, 400))
#
#             self.time = 0
