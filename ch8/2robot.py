def robot(maze):
    path = []
    if get_path(maze, len(maze) - 1, len(maze[0]) - 1, path):
        return path
    return "no path"
def get_path(maze, r, c, path):
    if (r, c) == (0, 0):
        path.append((r,c))
        return True
    if r < 0 or c < 0 or maze[r][c] == False:
        return False

    if get_path(maze, r - 1, c, path) or get_path(maze, r, c - 1, path):
        path.append((r,c))
        return True
    return False
    
print(robot([[True, False, False],[False, True, False], [False, False, True]])) #no path
print(robot([[True, False, False],[True, True, False], [False, True, True]])) #0,0   1,0  1,1  2,1  2,2

#15 minutes thinking
#25 minutes coding (got sstuck onn recursion and whenn to append to path)