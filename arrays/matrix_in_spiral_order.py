import numpy as np
import math

# # Take one
# def matrix_in_spiral_order(square_matrix):
#     spiral_order = []
#     l = len(square_matrix)
#     for i in range(math.ceil(l / 2)):
#         spiral_order.extend([square_matrix[i][j] for j in range(i, l - i)])
#         spiral_order.extend([square_matrix[j][l - i - 1] for j in range(i + 1, l - i)])
#         spiral_order.extend([square_matrix[l - i - 1][j] for j in reversed(range(i, l - i - 1))])
#         spiral_order.extend([square_matrix[j][i] for j in reversed(range(i + 1, l - i - 1))])
#
#     return spiral_order

# Take two
def matrix_in_spiral_order(square_matrix):
    SHIFT = ((0, 1), (1, 0), (0, -1), (-1, 0))
    x = y = direction = 0
    spiral_order = []
    for _ in range(len(square_matrix) ** 2):
        spiral_order.append(square_matrix[x][y])
        square_matrix[x][y] = 0
        next_x, next_y = x + SHIFT[direction][0], y + SHIFT[direction][1]
        if (next_x not in range(len(square_matrix)) or next_y not in range(len(square_matrix)) or square_matrix[next_x][next_y] == 0):
            direction = (direction + 1) % 4
            next_x, next_y = x + SHIFT[direction][0], y + SHIFT[direction][1]
        x, y = next_x, next_y
    return spiral_order

def main():
    matrix_a = list(map(list, np.array(range(1, 10)).reshape([3, 3])))
    matrix_b = list(map(list, np.array(range(1, 17)).reshape([4, 4])))
    matrix_c = list(map(list, np.array(range(1, 26)).reshape([5, 5])))
    print(matrix_a)
    print(matrix_b)
    print(matrix_c)
    print('Matrices in spiral order:')
    print(matrix_in_spiral_order(matrix_a))
    print(matrix_in_spiral_order(matrix_b))
    print(matrix_in_spiral_order(matrix_c))

if __name__ == '__main__':
    main()
