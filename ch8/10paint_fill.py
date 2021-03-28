def paint_fill(matrix, color, r, c):
    if matrix[r][c] == color or r < 0 or r > len(matrix) or c < 0 or c > len(matrix[0]):
        return
    
    matrix[r][c] = color

    paint_fill(matrix, color, r + 1, c)
    paint_fill(matrix, color, r - 1, c)
    paint_fill(matrix, color, r, c + 1)
    paint_fill(matrix, color, r, c - 1)