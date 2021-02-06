from engine.group import GameSpriteGroup
from engine.game_sprite import GameSprite


class GameSpriteGroups:
    groups = dict()

    def add(self, name_group: str, sprite: GameSprite):
        if self[name_group] is None:
            group = GameSpriteGroup()
            group.add(sprite)
            self.groups[name_group] = group
        else:
            self.groups[name_group].add(sprite)

    def __getitem__(self, item) -> GameSpriteGroup:
        return self.get_group(item)

    def __iter__(self):
        return self.groups.values().__iter__()

    def get_group(self, name_group: str) -> GameSpriteGroup:
        return self.groups.get(name_group)
