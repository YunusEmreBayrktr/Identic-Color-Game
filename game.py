import sys

data = open(sys.argv[1], "r").read().splitlines()
board = [i.split(" ") for i in data]

pop_list = []
x_pop_list = []
score = 0

def board_print():                       # Prints the board
    print()
    for i in board:
        for j in i:
            print(j,end=" ")
        print()
    print()


def end_game():                         # Calculates all possible moves and appends in the 'possible_moves' list
    possible_moves = []                 # Returns 'True' if there is still possible moves
                                        # Returns 'False' if there is no more possible moves
    for row in range(len(board)):
        for column in range(len(board[row])):

            if board[row][column] == "X":
                possible_moves.append([row, column])

            if board[row][column] != " ":

                try:
                    if board[row][column] == board[row - 1][column]:
                        if [row, column] not in possible_moves and row != 0:
                            possible_moves.append([row, column])
                        if [row - 1, column] not in pop_list and row != 0:
                            possible_moves.append([row - 1, column])
                except:
                    pass
                try:
                    if board[row][column] == board[row + 1][column]:
                        if [row, column] not in possible_moves:
                            possible_moves.append([row, column])
                        if [row + 1, column] not in pop_list:
                            possible_moves.append([row + 1, column])
                except:
                    pass
                try:
                    if board[row][column] == board[row][column - 1]:
                        if [row, column] not in possible_moves and column != 0:
                            possible_moves.append([row, column])
                        if [row, column - 1] not in pop_list and column != 0:
                            possible_moves.append([row, column - 1])
                except:
                    pass
                try:
                    if board[row][column] == board[row][column + 1]:
                        if [row, column] not in possible_moves:
                            possible_moves.append([row, column])
                        if [row, column + 1] not in pop_list:
                            possible_moves.append([row, column + 1])
                except:
                    pass

                index = 0
                while index < len(possible_moves):
                    if possible_moves[index][0] < 0 or possible_moves[index][1] < 0:
                        possible_moves.pop(index)
                    index += 1

    if len(possible_moves) != 0:
        possible_moves.clear()
        return True
    else:
        possible_moves.clear()
        return False


def check(y,x):                         # Checks all adjoining balls with the selected ball
    global pop_list                     # Appends their coordinates to the 'pop_list' if they have the same colour
    global board

    try:
        if board[y][x] == board[y - 1][x]:
            if [y,x] not in pop_list:
                pop_list.append([y, x])
            if [y - 1,x] not in pop_list:
                pop_list.append([y - 1, x])
    except:
        pass
    try:
        if board[y][x] == board[y + 1][x]:
            if [y, x] not in pop_list:
                pop_list.append([y, x])
            if [y + 1, x] not in pop_list:
                pop_list.append([y + 1, x])
    except:
        pass
    try:
        if board[y][x] == board[y][x - 1]:
            if [y, x] not in pop_list:
                pop_list.append([y, x])
            if [y, x - 1] not in pop_list:
                pop_list.append([y, x - 1])
    except:
        pass
    try:
        if board[y][x] == board[y][x + 1]:
            if [y, x] not in pop_list:
                pop_list.append([y, x])
            if [y, x + 1] not in pop_list:
                pop_list.append([y, x + 1])
    except:
        pass

    i = 0
    while i < len(pop_list):
        if pop_list[i][0] < 0 or pop_list[i][1] < 0:
            pop_list.pop(i)
        i += 1


def total():                               # Calculates the recent score when a non 'X' cell is choosen
    global score
    global pop_list

    if   board[numbers[0]][numbers[1]] == "B":
        score += len(pop_list) * 9
    elif board[numbers[0]][numbers[1]] == "G":
        score += len(pop_list) * 8
    elif board[numbers[0]][numbers[1]] == "W":
        score += len(pop_list) * 7
    elif board[numbers[0]][numbers[1]] == "Y":
        score += len(pop_list) * 6
    elif board[numbers[0]][numbers[1]] == "R":
        score += len(pop_list) * 5
    elif board[numbers[0]][numbers[1]] == "P":
        score += len(pop_list) * 4
    elif board[numbers[0]][numbers[1]] == "O":
        score += len(pop_list) * 3
    elif board[numbers[0]][numbers[1]] == "D":
        score += len(pop_list) * 2
    elif board[numbers[0]][numbers[1]] == "F":
        score += len(pop_list) * 1
    else :
        pass


def delete():                           # Deletes all cells in the 'pop_list'
    global pop_list

    for i in pop_list:
        board[i[0]][i[1]] = " "
    pop_list.clear()


def drop():
    global board
                                # First part drops the balls to fill the blanks and removes the empty rows
    for k in range(len(board)):
        for l in range(len(board) - 1, -1, -1):
            for m in range(len(board[0])):
                if board[l][m] == " " and l - 1 != -1:
                    board[l][m] = board[l - 1][m]
                    board[l - 1][m] = " "

    i = 0
    while i <len(board):
        if board[i] == [" " for j in range(len(board[i]))]:
            board.pop(i)
        i += 1

                                # Second part removes the empty columns
    try:
        transpose = [[board[y][x] for y in range(len(board))] for x in range(len(board[0]))]

        index = 0
        while index < len(transpose):
            if transpose[index] == [" " for i in range(len(transpose[index]))]:
               transpose.pop(index)
            index += 1

        board = [[transpose[y][x] for y in range(len(transpose))] for x in range(len(transpose[0]))]

    except:
        pass


def pop(y,x):                       # Creates a 'pop_list'
    global pop_list
    check(y, x)

    while True:
        a = len(pop_list)
        for i in pop_list:
            check(i[0], i[1])
        if a == len(pop_list):
            break

    index = 0
    while index < len(pop_list):
        if pop_list[index][0] < 0 or pop_list[index][1] < 0:
            pop_list.pop(index)
        index += 1


def x_pop(y,x):                     # Blasts the bomb while considering the possibility of chaining bombs
    global score                    # and adds the values of the popped balls to the score
    global x_pop_list
    board[y][x] = " "

    for row in range(len(board)):
        for column in range(len(board[row])):

            if y == row:
                if board[row][column] == "X":
                    x_pop(row,column)
                else:
                    x_pop_list.append(board[row][column])
                    board[row][column] = " "


            elif x == column:
                if board[row][column] == "X":
                    x_pop(row,column)
                else:
                    x_pop_list.append(board[row][column])
                    board[row][column] = " "

    for ball in x_pop_list:

        if ball == "B":
            score += 9
        elif ball == "G":
            score += 8
        elif ball == "W":
            score += 7
        elif ball == "Y":
            score += 6
        elif ball == "R":
            score += 5
        elif ball == "P":
            score += 4
        elif ball == "O":
            score += 3
        elif ball == "D":
            score += 2
        elif ball == "F":
            score += 1
        else:
            pass

    x_pop_list.clear()




while end_game():                   # Calling the functions in the right order

    board_print()
    print(f"Your score is: {score}\n")

    while True :

        try:
            numbers = [int(i) for i in input("Please enter a row and column number: ").split(" ")]

            if board[numbers[0]][numbers[1]] == "X":
                x_pop(numbers[0],numbers[1])
                drop()
                break
            elif board[numbers[0]][numbers[1]] != " ":
                pop(numbers[0],numbers[1])
                total()
                delete()
                drop()
                break
            else:
                raise Exception

        except Exception:
            print("Please enter a valid size!")

board_print()
print(f"Your score is: {score}\n")
print("Game over!")