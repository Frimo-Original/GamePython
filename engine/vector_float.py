
class VectorFloat:
    def __init__(self, x: float = 0, y: float = 0):
        self.x = x
        self.y = y

    def get_int(self) -> (int, int):
        return int(self.x), int(self.y)
