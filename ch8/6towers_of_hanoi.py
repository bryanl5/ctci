#book outlines OOP. struggling to implement frrom java to python
class HanoiStack:
    def __init__(self, height):
        self.height = height
        self.num_towers = 3
        self.towers = [0] * (height * self.num_towers)
