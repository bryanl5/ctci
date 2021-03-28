class Tower():
    def __init__(self, num_disks):
        self.num_disks = num_disks 
        self.stack = []
        for i in range(num_disks, 0, -1):
            self.stack.append(i)

    def add_disk(self, num):
        self.stack.append(num)

    def remove_disk(self):
        if len(self.stack) == 0:
            raise Exception("cannot remove anymore disks")
        return self.stack.pop()

class HanoiGame():
    def __init__(self, num_disks):
        self.towers = [] * 3
        self.towers[0] = Tower(num_disks)
        self.towers[1] = Tower(0)
        self.towers[2] = Tower(0)

    def solve_puzzle(self):
        self.solve_puzzle_helper(self.towers[0], self.towers[2], self.towers[1])
        
    def solve_puzzle_helper(self, start, end, unused):
        n = len(start.stack)
        if n > 0:
            self.solve_puzzle_helper(start, unused, end)
            move_disk(start, end)
            self.solve_puzzle_helper(unused, end, start)

    def move_disk(self, start, end):
        end.add_disk(start.remove_disk())

hanoi = HanoiGame(3)
hanoi.solve_puzzle()
print(hanoi.towers[2])

# 4321 0 0 
# 432 1 0
# 43 1 2
# 43 0 21
# 4 3 21
# 41 3 2
# 41 32 0
# 4 321 0
# 0 321 4
# 0 32 41
# 2 3 41
# 21 3 4
# 21 0 43
# 2 1 43
# 0 1 432
# 0 0 4321

# r1
# s   u e
# 321 0 0  
# s  e u  
# 32 0 1 
# u e s
# 3 2 1
# 3 21 0
# 0 21 3
# 1 2 3 
# 1 0 32
# 0 0 321

# 21 0 0 
# 2 1 0
# 0 1 2
# 0 0 21

# 1 0 0
# 0 0 1

# ctci solution

# r2_1
# t  b d
# 21 0 0

# r1_1
# t d b
# 1 0 0

# r0_1
# t b d
# 1 0 0

# r1_1
# t d b
# 0 1 0

# r0_2
# t(b) d b(t) 
# 0 1 0

# r2_1
# t b d
# 2 1 0
# 0 1 2

# r2_2
# t(b) b(t) d
# 0    0    21

    