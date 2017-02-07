# print node: node, depth, value, alpha, beta
def print_node(i, j, d, value, a, b):
    global traverse_log
    traverse_log += (
        position_str(i, j) + ',' + str(d) + ',' + infinity_str(value) + ',' + infinity_str(a) + ',' + infinity_str(
            b) + '\n')
    print position_str(i, j) + ',' + str(d) + ',' + infinity_str(value) + ',' + infinity_str(a) + ',' + infinity_str(
        b)


# return node str
# pass=-2 root=-1
def position_str(i, j):
    if j == -2:
        return 'pass'
    elif j == -1:
        return 'root'
    elif j == 0:
        return 'a' + str(i + 1)
    elif j == 1:
        return 'b' + str(i + 1)
    elif j == 2:
        return 'c' + str(i + 1)
    elif j == 3:
        return 'd' + str(i + 1)
    elif j == 4:
        return 'e' + str(i + 1)
    elif j == 5:
        return 'f' + str(i + 1)
    elif j == 6:
        return 'g' + str(i + 1)
    elif j == 7:
        return 'h' + str(i + 1)
    else:
        return


# -1000=-Infinity 1000=Infinity
def infinity_str(v):
    if v == 1000:
        value_str = 'Infinity'
    elif v == -1000:
        value_str = '-Infinity'
    else:
        value_str = str(v)
    return value_str


def check_north_west(board, i, j, player):
    count = 0
    temp_i = i - 1
    temp_j = j - 1
    if board[temp_i][temp_j] == 1 - player:
        while temp_i >= 0 and temp_j >= 0 and board[temp_i][temp_j] == 1 - player:
            temp_i -= 1
            temp_j -= 1
            count += 1
        if temp_i >= 0 and temp_j >= 0 and board[temp_i][temp_j] == player:
            return count
    return 0


def check_north(board, i, j, player):
    count = 0
    temp_i = i - 1
    if board[temp_i][j] == 1 - player:
        while temp_i >= 0 and board[temp_i][j] == 1 - player:
            temp_i -= 1
            count += 1
        if temp_i >= 0 and board[temp_i][j] == player:
            return count
    return 0


def check_north_east(board, i, j, player):
    count = 0
    temp_i = i - 1
    temp_j = j + 1
    if board[temp_i][temp_j] == 1 - player:
        while temp_i >= 0 and temp_j <= 7 and board[temp_i][temp_j] == 1 - player:
            temp_i -= 1
            temp_j += 1
            count += 1
        if temp_i >= 0 and temp_j <= 7 and board[temp_i][temp_j] == player:
            return count
    return 0


def check_west(board, i, j, player):
    count = 0
    temp_j = j - 1
    if board[i][temp_j] == 1 - player:
        while temp_j >= 0 and board[i][temp_j] == 1 - player:
            temp_j -= 1
            count += 1
        if temp_j >= 0 and board[i][temp_j] == player:
            return count
    return 0


def check_east(board, i, j, player):
    count = 0
    temp_j = j + 1
    if board[i][temp_j] == 1 - player:
        while temp_j <= 7 and board[i][temp_j] == 1 - player:
            temp_j += 1
            count += 1
        if temp_j <= 7 and board[i][temp_j] == player:
            return count
    return 0


def check_south_west(board, i, j, player):
    count = 0
    temp_i = i + 1
    temp_j = j - 1
    if board[temp_i][temp_j] == 1 - player:
        while temp_i <= 7 and temp_j >= 0 and board[temp_i][temp_j] == 1 - player:
            temp_i += 1
            temp_j -= 1
            count += 1
        if temp_i <= 7 and temp_j >= 0 and board[temp_i][temp_j] == player:
            return count
    return 0


def check_south(board, i, j, player):
    count = 0
    temp_i = i + 1
    if board[temp_i][j] == 1 - player:
        while temp_i <= 7 and board[temp_i][j] == 1 - player:
            temp_i += 1
            count += 1
        if temp_i <= 7 and board[temp_i][j] == player:
            return count
    return 0


def check_south_east(board, i, j, player):
    count = 0
    temp_i = i + 1
    temp_j = j + 1
    if board[temp_i][temp_j] == 1 - player:
        while temp_i <= 7 and temp_j <= 7 and board[temp_i][temp_j] == 1 - player:
            temp_i += 1
            temp_j += 1
            count += 1
        if temp_i <= 7 and temp_j <= 7 and board[temp_i][temp_j] == player:
            return count
    return 0


# check for valid moves for particular position
# board: current board status
# player: X=1 O=0
def valid_moves_single(board, i, j, player):
    # north
    if i >= 2:
        # north west
        if j >= 2 and check_north_west(board, i, j, player) > 0:
            return True
        # north
        if check_north(board, i, j, player):
            return True
        # north east
        if j <= 5 and check_north_east(board, i, j, player):
            return True
    # west
    if j >= 2 and check_west(board, i, j, player):
        return True
    # east
    if j <= 5 and check_east(board, i, j, player):
        return True
    # south
    if i <= 5:
        # south west
        if j >= 2 and check_south_west(board, i, j, player):
            return True
        # south
        if check_south(board, i, j, player):
            return True
        # south east
        if j <= 5 and check_south_east(board, i, j, player):
            return True
    return False


# check for valid moves for whole board for particular player
def valid_moves_whole(board, player):
    moves = ''
    for i in range(8):
        for j in range(8):
            if board[i][j] == -1 and valid_moves_single(board, i, j, player):
                moves += (str(i) + str(j))
    return moves


# copy 2-dimensional array
def copy_board(board):
    new_board = [[]] * 8
    for i in range(8):
        new_board[i] = [-1] * 8
        for j in range(8):
            new_board[i][j] = board[i][j]
    return new_board


# calculate the new board after player put a disc at (i, j)
def get_new_board(board, i, j, player):
    new_board = copy_board(board)
    new_board[i][j] = player
    # change opponent's disc
    # north
    if i >= 2:
        # north west
        if j >= 2:
            count = check_north_west(board, i, j, player)
            if count > 0:
                for k in range(count):
                    new_board[i - (k + 1)][j - (k + 1)] = player
        # north
        count = check_north(board, i, j, player)
        if count > 0:
            for k in range(count):
                new_board[i - (k + 1)][j] = player
        # north east
        if j <= 5:
            count = check_north_east(board, i, j, player)
            if count > 0:
                for k in range(count):
                    new_board[i - (k + 1)][j + (k + 1)] = player
    # west
    if j >= 2:
        count = check_west(board, i, j, player)
        if count > 0:
            for k in range(count):
                new_board[i][j - (k + 1)] = player
    # east
    if j <= 5:
        count = check_east(board, i, j, player)
        if count > 0:
            for k in range(count):
                new_board[i][j + (k + 1)] = player
    # south
    if i <= 5:
        # south west
        if j >= 2:
            count = check_south_west(board, i, j, player)
            if count > 0:
                for k in range(count):
                    new_board[i + (k + 1)][j - (k + 1)] = player
        # south
        count = check_south(board, i, j, player)
        if count > 0:
            for k in range(count):
                new_board[i + (k + 1)][j] = player
        # south east
        if j <= 5:
            count = check_south_east(board, i, j, player)
            if count > 0:
                for k in range(count):
                    new_board[i + (k + 1)][j + (k + 1)] = player
    return new_board


# calculate utility
def get_utility(board):
    x_sum = 0
    o_sum = 0
    for i in range(8):
        for j in range(8):
            if board[i][j] == 1:
                x_sum += weight[i][j]
            elif board[i][j] == 0:
                o_sum += weight[i][j]
    return x_sum - o_sum


# check whether current status is an endgame node
def is_endgame(board, player):
    if valid_moves_whole(board, player) == '' and valid_moves_whole(board, 1 - player) == '':
        return True
    else:
        return False


# alpha-beta pruning
def ab_pruning(board, player, depth):
    # X turn MAX
    a = -1000
    b = 1000
    if player == 1:
        value = max_value(board, a, b, depth, -1, -1)
    else:
        value = min_value(board, a, b, depth, -1, -1)
    return value


# X turn MAX
# i, j is the current disc got placed
def max_value(board, a, b, depth, i, j):
    value = -1000
    moves = valid_moves_whole(board, 1)
    global pass_limit_count
    # leaf cutoff
    if depth == 0:
        value = get_utility(board)
        print_node(i, j, cutoff_depth - depth, value, a, b)
        return value
    # leaf endgame
    if moves == '' and pass_limit_count == 2:
        value = get_utility(board)
        print_node(i, j, cutoff_depth - depth, value, a, b)
        return value
    # non leaf
    print_node(i, j, cutoff_depth - depth, value, a, b)
    # no legal move, then pass
    if moves == '':
        pass_limit_count += 1
        temp = min_value(board, a, b, depth - 1, -2, -2)
        if temp > value:
            value = temp
        if value >= b:
            print_node(i, j, cutoff_depth - depth, value, a, b)
            return value
        if value > a:
            a = value
        print_node(i, j, cutoff_depth - depth, value, a, b)
    # exist legal move, do DFS
    else:
        pass_limit_count = 0
        while moves != '':
            next_i = int(moves[0])
            next_j = int(moves[1])
            new_board = get_new_board(board, next_i, next_j, 1)
            temp = min_value(new_board, a, b, depth - 1, next_i, next_j)
            if temp > value:
                value = temp
                if i == -1:
                    global best
                    best = str(next_i) + str(next_j)
            if value >= b:
                print_node(i, j, cutoff_depth - depth, value, a, b)
                return value
            if value > a:
                a = value
            print_node(i, j, cutoff_depth - depth, value, a, b)
            moves = moves[2:len(moves)]
    return value


# O turn MIN
# i, j is the current disc got placed
def min_value(board, a, b, depth, i, j):
    value = 1000
    moves = valid_moves_whole(board, 0)
    global pass_limit_count
    # leaf cutoff
    if depth == 0:
        value = get_utility(board)
        print_node(i, j, cutoff_depth - depth, value, a, b)
        return value
    # leaf endgame
    if moves == '' and pass_limit_count == 2:
        value = get_utility(board)
        print_node(i, j, cutoff_depth - depth, value, a, b)
        return value
    # non leaf
    print_node(i, j, cutoff_depth - depth, value, a, b)
    # no legal move, then pass
    if moves == '':
        pass_limit_count += 1
        temp = max_value(board, a, b, depth - 1, -2, -2)
        if temp < value:
            value = temp
        if value <= a:
            print_node(i, j, cutoff_depth - depth, value, a, b)
            return value
        if value < b:
            b = value
        print_node(i, j, cutoff_depth - depth, value, a, b)
    # exist legal move, do DFS
    else:
        pass_limit_count = 0
        while moves != '':
            next_i = int(moves[0])
            next_j = int(moves[1])
            new_board = get_new_board(board, next_i, next_j, 0)
            temp = max_value(new_board, a, b, depth - 1, next_i, next_j)
            if temp < value:
                value = temp
                if i == -1:
                    global best
                    best = str(next_i) + str(next_j)
            if value <= a:
                print_node(i, j, cutoff_depth - depth, value, a, b)
                return value
            if value < b:
                b = value
            print_node(i, j, cutoff_depth - depth, value, a, b)
            moves = moves[2:len(moves)]
    return value


# place the best choice of disc
def place_best(board, player):
    global best
    if best == '':
        return board
    else:
        i = int(best[0])
        j = int(best[1])
        new_board = get_new_board(board, i, j, player)
    return new_board


# initialize weight table
weight = [[99, -8, 8, 6, 6, 8, -8, 99],
          [-8, -24, -4, -3, -3, -4, -24, -8],
          [8, -4, 7, 4, 4, 7, -4, 8],
          [6, -3, 4, 0, 0, 4, -3, 6],
          [6, -3, 4, 0, 0, 4, -3, 6],
          [8, -4, 7, 4, 4, 7, -4, 8],
          [-8, -24, -4, -3, -3, -4, -24, -8],
          [99, -8, 8, 6, 6, 8, -8, 99]]

# store board status in 2-dimensional array
initial_board = [[]] * 8
# read file
input_file = open("input.txt")
# X=1 0=0 *=no disc=-1
if input_file.readline()[0] == 'X':
    first_player = 1
else:
    first_player = 0
cutoff_depth = int(input_file.readline())
# initialize board & disc list
for i in range(8):
    initial_board[i] = [-1] * 8
    line = input_file.readline()
    for j in range(8):
        if line[j] == 'X':
            initial_board[i][j] = 1
        elif line[j] == 'O':
            initial_board[i][j] = 0
# best moves
best = ''
traverse_log = ''
pass_limit_count = 0
# alpha-beta pruning
ab_pruning(initial_board, first_player, cutoff_depth)
new_board = place_best(initial_board, first_player)

# format the ouput string
output = ''
for i in range(8):
    for j in range(8):
        if new_board[i][j] == -1:
            output += '*'
        elif new_board[i][j] == 0:
            output += 'O'
        elif new_board[i][j] == 1:
            output += 'X'
    output += '\n'
output += 'Node,Depth,Value,Alpha,Beta\n'
output += traverse_log
output = output[0:len(output) - 1]
# write in file
output_file = open('output.txt', 'w')
output_file.write(output)
