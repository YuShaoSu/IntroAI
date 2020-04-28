from itertools import product
from copy import deepcopy

class Node:
    def __init__(self, board, degree):
        super().__init__()
        self.degree = degree
        self.board = board.copy()

# start point
def solve(init_node):
    stack = [init_node]
    while stack:
        now = stack.pop()
        print('degree: ', now.degree, ' ', now.board)
        if check(now):
            print('find')
            break
        else:
            print('cool')
            stack += new_child(now)

# check if reach
def check(node):
    if node.degree == mine_num:
        # check if all hint equals to zero
        for i in range(board_size_x):
            for j in range(board_size_y):
                if node.board[i][j] > 0:
                    return False
        return True
    return False

# create child
def new_child(node):
    child = []
    for j in range(board_size_y):
        for i in range(board_size_x):
            if node.board[i][j] != -1:
                continue
            cor = legal_cor(i, j)
            if applicable(node, cor):
                print('applicable', i, ' ', j)
                new_board = deepcopy(node.board)
                c = Node(new_board, node.degree + 1)
                for x, y in cor:
                    if c.board[x][y] > 0:
                        c.board[x][y] -= 1
                c.board[i][j] = -2
                print(c.board)
                child.append(c)
    return child


def applicable(node, cor):
    for i, j in cor:
        if node.board[i][j] == 0:
            return False
    return True

def legal_cor(x, y):
    x_list = [i for i in [x - 1, x, x + 1] if i >= 0 and i < board_size_x]
    y_list = [i for i in [y - 1, y, y + 1] if i >= 0 and i < board_size_y]
    return [(i, j) for i in x_list for j in y_list if not (i == x and j == y)]



line = input('').split()
board_size_x = int(line[0])
board_size_y = int(line[1])
board_size = board_size_x * board_size_y
mine_num = int(line[2])
board_init = [[int(line[3 + i + (6 * y)]) for i in range(board_size_x)]
              for y in range(board_size_y)]

solve(Node(board_init, 0))
