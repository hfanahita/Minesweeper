import random

global size, board, mines, printable_board


# Creates a random board of given size with given number of mines
def create_board(board_size, num_mines):
    global size, board, mines, printable_board
    mines = []
    board = []
    printable_board = []
    size = board_size
    '''To pick a random number in range of 0 to size*size 
    it takes the list of numbers from 0 to size*size and shuffles it,
    so that it can choose random cells for mines'''
    cell_numbers = list(range(0, size * size))
    random.shuffle(cell_numbers)
    index_of_mines = cell_numbers[:num_mines]
    index_of_mines.sort()
    row = []
    cell_number = 0
    for i in range(size):
        for j in range(size):
            # If one is in a mine's cell then it adds its position to the list of mines
            if cell_number in index_of_mines:
                mines.append([i, j])
            row.append(0)
            cell_number += 1
        # Making board with its initializing values
        board.append(row)
        # Cloning board into printable_board
        printable_board.append(row[:])
        row = []


# Prints game board; also shows mines if show_mines is True
def print_board(show_mines):
    for (index_of_row, row) in enumerate(board):
        for (index_of_cell, cell) in enumerate(row):
            # if it's a mine, and it's not already revealed and show_mines is true, then it changes the value of this
            # cell to '@'
            if [index_of_row, index_of_cell] in mines and show_mines and not (
                    printable_board[index_of_row][index_of_cell] == 'T' or printable_board[index_of_row][
                index_of_cell] == 'F'):
                printable_board[index_of_row][index_of_cell] = '@'
            # if the cell has no flag and has not been revealed yet, then it changes the value of this cell to #
            elif board[index_of_row][index_of_cell] == 0:
                printable_board[index_of_row][index_of_cell] = '#'
            # if the cell has been revealed, then it counts the mines around it and changes its value to that number
            elif board[index_of_row][index_of_cell] == 1:
                printable_board[index_of_row][index_of_cell] = count_mines(index_of_row + 1, index_of_cell + 1)
            # if the cell has flags and the game isn't over, then it changes the value of this cell to p
            if board[index_of_row][index_of_cell] == 2 and not (
                    printable_board[index_of_row][index_of_cell] == 'T' or printable_board[index_of_row][
                index_of_cell] == 'F'):
                printable_board[index_of_row][index_of_cell] = 'p'
            print(printable_board[index_of_row][index_of_cell], end=' ')
        print()


# Puts flag in the given cell
def put_flag(row, column):
    if board[row - 1][column - 1] != 1:
        board[row - 1][column - 1] = 2
    else:
        print('')


# Removes flag in the given cell
def remove_flag(row, column):
    board[row - 1][column - 1] = 0


""" Counts mines adjacent to the given cell by creating a list of neighbours around that cell 
and checking whether there is a mine in them or not """


def count_mines(row, column):
    row -= 1
    column -= 1
    number_of_mines = 0
    cell_coordinates = [[row, column + 1], [row, column - 1], [row - 1, column], [row + 1, column],
                        [row - 1, column - 1], [row + 1, column - 1], [row - 1, column + 1], [row + 1, column + 1]]
    for cell_coordinate in cell_coordinates:
        if 0 <= cell_coordinate[0] < size and 0 <= cell_coordinate[1] < size:
            if cell_coordinate in mines:
                number_of_mines += 1
    return number_of_mines


""" Reveals the given cell and returns number of mines around that cell 
and if there is a mine in the given cell, it returns -1 """


def reveal_cell(row, column):
    row -= 1
    column -= 1
    cells_coordinates = [[row, column + 1], [row, column - 1], [row - 1, column], [row + 1, column],
                         [row - 1, column - 1], [row + 1, column - 1], [row - 1, column + 1], [row + 1, column + 1]]
    if [row, column] in mines:
        return -1
    board[row][column] = 1
    if count_mines(row + 1, column + 1) == 0:
        for cell_coordinate in cells_coordinates:
            """ If the cell has a valid coordinate and
             the number of mines around it is 0 then it recursively reveals the cell
             and if it's not 0 then it only reveals this cell """
            if 0 <= cell_coordinate[0] < size and 0 <= cell_coordinate[1] < size:
                if count_mines(cell_coordinate[0] + 1, cell_coordinate[1] + 1) == 0:
                    if board[cell_coordinate[0]][cell_coordinate[1]] != 1:
                        reveal_cell(cell_coordinate[0] + 1, cell_coordinate[1] + 1)
                else:
                    board[cell_coordinate[0]][cell_coordinate[1]] = 1
    return count_mines(row + 1, column + 1)


# Checks whether the player has won or not
def won():
    # If there is any cell containing a mine without a flag on it, then it means that the player hasn't won
    for mine in mines:
        if board[mine[0]][mine[1]] != 2:
            return False
    # If there is a cell that hasn't been revealed and has no flags, then it means that the player hasn't won
    for row in board:
        for cell in row:
            if cell == 0:
                return False
    return True


# The main loop of the game
def main():
    global printable_board
    row = int(input("Please enter the number of rows:"))
    number_of_mines = int(input("Please enter the number of mines:"))
    create_board(row, number_of_mines)
    print_board(False)
    print("Now enter a command to start the game.")
    # If the player hasn't won yet, then the game goes on until either the player wins or loses
    while not won():
        command = input().split()
        # Stops the game
        if command[0] == 'x':
            print_board(False)
            break
        # Validating the command
        if (len(command) <= 1 and command[0] != 'x') or len(command) > 3 or len(command) == 2:
            print('Invalid Command!')
            continue
        if command[0] != 'r' and command[0] != 'f' and command[0] != 'u' and command[0] != 'x':
            print('Invalid Command!')
            continue
        command[1] = int(command[1])
        command[2] = int(command[2])
        if not (0 < command[1] <= size and 0 < command[2] <= size):
            print('Invalid Command!')
            continue
        # Executing command
        # Reveals cell
        if command[0] == 'r':
            """if there is a flag in the given cell then it must be removed first 
            and the cell cannot be revealed, so it asks the player to give another command"""
            if board[command[1] - 1][command[2] - 1] == 2:
                print('First remove the flag!')
                continue
            """if the cell is already revealed then it cannot be revealed again,
             so it asks the player to give another command"""
            if board[command[1] - 1][command[2] - 1] == 1:
                print('This cell is already revealed!')
                continue
            # If there is a mine in the given cell then the game is over, and it prints the board
            if reveal_cell(command[1], command[2]) == -1:
                for (index_of_row, row) in enumerate(printable_board):
                    for (index_of_cell, cell) in enumerate(row):
                        if cell == 'p':
                            """ If the cell has a flag, then it checks whether the flag was in a right place 
                            and there was a mine in that cell or not, if yes, then the cell will be revealed by T 
                            and if no it'll be revealed by F """
                            if [index_of_row, index_of_cell] in mines:
                                printable_board[index_of_row][index_of_cell] = 'T'
                            else:
                                printable_board[index_of_row][index_of_cell] = 'F'
                print_board(True)
                print('You Lost!')
                break
            print_board(False)
        elif command[0] == 'f':
            """ If the cell is already revealed then it cannot have a flag,
             so it asks the player to give another command """
            if board[command[1] - 1][command[2] - 1] == 1:
                print('This cell is already revealed!')
                continue
            # If the cell has a flag already then the player must give another command!
            elif board[command[1] - 1][command[2] - 1] == 2:
                print('This cell already has a flag!')
                continue
            put_flag(command[1], command[2])
            print_board(False)
        elif command[0] == 'u':
            # If there isn't a flag on the given cell then the player must give another command!
            if board[command[1] - 1][command[2] - 1] != 2:
                print('There is no flag to remove!')
                continue
            remove_flag(command[1], command[2])
            print_board(False)
    if won():
        print('You Won!')


main()
