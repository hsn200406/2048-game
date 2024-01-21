# student name: Hassan ElGhayaty
# student number: 56002538

# A command-line 2048 game

import random

board: list[list] = []  # a 2-D list to keep the current status of the game board

def init() -> None:  # Use as is
    """ 
        initializes the board variable
        and prints a welcome message
    """
    # initialize the board cells with ''
    for _ in range(4):     
        rowList = []
        for _ in range(4):
            rowList.append('')
        board.append(rowList)
    # add two starting 2's at random cells
    twoRandomNumbers = random.sample(range(16), 2)   # randomly choose two numbers between 0 and 15   
    # correspond each of the two random numbers to the corresponding cell
    twoRandomCells = ((twoRandomNumbers[0]//4,twoRandomNumbers[0]%4),
                      (twoRandomNumbers[1]//4,twoRandomNumbers[1]%4))
    for cell in twoRandomCells:  # put a 2 on each of the two chosen random cells
        board[cell[0]][cell[1]] = 2

    print(); print("Welcome! Let's play the 2048 game."); print()


def displayGame() -> None:  # Use as is
    """ displays the current board on the console """
    print("+-----+-----+-----+-----+")
    for row in range(4): 
        for column in range(4):
            cell = board[row][column] 
            print(f"|{str(cell).center(5)}", end="")
        print("|")
        print("+-----+-----+-----+-----+")


def promptGamerForTheNextMove() -> str: # Use as is
    """
        prompts the gamer until a valid next move or Q (to quit) is selected
        (valid move direction: one of 'W', 'A', 'S' or 'D')
        returns the user input
    """
    print("Enter one of WASD (move direction) or Q (to quit)")
    while True:  # prompt until a valid input is entered
        move = input('> ').upper()
        if move in ('W', 'A', 'S', 'D', 'Q'): # a valid move direction or 'Q'
            break
        print('Enter one of "W", "A", "S", "D", or "Q"') # otherwise inform the user about valid input
    return move


def addANewTwoToBoard() -> None:
    # If the board is empty (not full) enter
    if not isFull():
        # Creates an infinite loop, so that it keeps looping until an empty cell is obtained and it places a 2 in that empty cell
        while True:
            cell = random_cell() # Calls the random cell generator
            if board[cell[0]][cell[1]] == '': # If the cell is empty enter 
                board[cell[0]][cell[1]] = 2 # Place the integer 2 in the empty cell
                break # breaks out of the loop 
            
    else: # Otherwhise the board is empty
        pass    
    """ 
        adds a new 2 at an available randomly-selected cell of the board
    """
     


def isFull() -> bool:
    # Loop that goes through every single element in the board
    for cell in board:
        for i in range(4):
            if cell[i] == '': # If an empty cell is found return false
                return False
          
    return True # Otherwhise it returns true if not empty cell is found
    """ 
        returns True if no empty cell is left, False otherwise 
    """


def getCurrentScore() -> int:
    
    score = 0 # Initialized value of score as 0
    # Loop through every cell in the board
    for cell in board:
        for i in range(4):
            if cell[i] != '': # If the cell contains an integer add it to the current score
                score += cell[i]
    
    return score # Returns the total accumulated score
    """ 
        calculates and returns the current score
        the score is the sum of all the numbers currently on the board
    """


def updateTheBoardBasedOnTheUserMove(move: str) -> None:
    # If the letter W is pressed by user enter
    if move == 'W':
        # Loops starting from row 1 as row 0 is stationary because it is at the top and cannot go a step upwards
        for row in range(1, 4):
            for col in range(4): 
                if board[row][col] == '': # If current cell is empty then check next cell
                    pass  
                else:
                    if row == 1: # If current cell is at row 1, we check every single possible movement

                        if board[row][col] == board[row - 1][col]: # If the current cell is equal to the cell above, added them up and replace with top cell with the addition
                            cell = board[row][col] 
                            board[row - 1][col] += cell # Adds both cells and replaces top cell
                            board[row][col] = '' # Current cell becomes empty

                        elif board[row - 1][col] == '': # If the top cell is empty, move the current cell upwards to the top cell
                            cell = board[row][col] 
                            board[row - 1][col] = cell # Replaces top cell with current cell
                            board[row][col] = '' # Current cell becomes empty

                        else: # Otherwhise the cell just remains at its position
                            pass

                    elif row == 2: # If current cell is at row 2, we check every single possible movement   

                        if board[row - 1][col] == '' and board[row - 2][col] == '': # If the top two cells are empty, replaces the highest cell position with current cell
                            cell = board[row][col] 
                            board[row - 2][col] = cell # Replaces the top cell with the current cell
                            board[row][col] = '' # Current cell becomes empty

                        elif board[row - 1][col] == '' and board[row - 2][col] == board[row][col]: # If the first cell on top is empty, but the other cell on top of that is equal to current cell, replace that top cell with the addition of it and current cell
                            cell = board[row][col] 
                            board[row - 2][col] += cell # Adds both cells and replaces top cell
                            board[row][col] = '' # Current cell becomes empty

                        elif board[row - 1][col] == '' and board[row - 2][col] != board[row][col]: # If the first cell on top is empty but the other cell on top is not equal to current cell, replace the first cell on top with current cell
                            cell = board[row][col]
                            board[row - 1][col] = cell # Replaces the top cell
                            board[row][col] = '' # Current cell becomes empty

                        elif board[row][col] == board[row - 1][col]: # If the current cell is equal to the cell on top, then add both cells and replace the top cell with the addition
                            cell = board[row][col]
                            board[row - 1][col] += cell # Replaces the top cell with the addition
                            board[row][col] = '' # Current cell becomes empty

                        else: # Otherwhise the cell does not move at all
                            pass
                    else:
                        # Here row is 3
                        if board[row - 1][col] == '' and board[row - 2][col] == '' and board[row - 3][col] == '': # If all 3 top cells are empty, move the current cell to the highest cell
                            cell = board[row][col]
                            board[row - 3][col] = cell # Replaces the top cell
                            board[row][col] = '' # Current cell becomes empty

                        elif board[row - 1][col] == '' and board[row - 2][col] == '' and board[row - 3][col] == board[row][col]: # If the top 2 cells are empty but the third cell on top is equal to current cell, replace it with the addition with the current cell
                            cell = board[row][col]
                            board[row - 3][col] += cell # Adds both cells and replaces top cell
                            board[row][col] = '' # Current cell becomes empty

                        elif board[row - 1][col] == '' and board[row - 2][col] == '' and board[row - 3][col] != board[row][col]: # If the top 2 cells are empty and third top cell is not equal to current cell, move the current cell to the position of the second top cell
                            cell = board[row][col]
                            board[row - 2][col] = cell # Replaces the top cell
                            board[row][col] = '' # Current cell becomes empty

                        elif board[row - 1][col] == '' and board[row - 2][col] == board[row][col]: # If the top cell is empty, but the second top cell is equal, replace it with its addition with current cell
                            cell = board[row][col]
                            board[row - 2][col] += cell # Adds both cells and replaces top cell
                            board[row][col] = '' # Current cell becomes empty

                        elif board[row - 1][col] == '' and board[row - 2][col] != board[row][col]: # If the top cell is empty, but the second top cell is not equal to current cell, replace the empty cell with the current cell
                            cell = board[row][col]
                            board[row - 1][col] = cell # Replaces the top cell
                            board[row][col] = '' # Current cell becomes empty

                        elif board[row][col] == board[row - 1][col]: # If the current cell is equal to the top cell, replace the top cell with its addition with the current cell
                            cell = board[row][col]
                            board[row - 1][col] += cell # Adds both cells and replaces top cell
                            board[row][col] = '' # Current cell becomes empty

                        else: # Otherwhise the current cell does not move
                            pass
   
    # If the letter A is pressed by user enter
    elif move == 'A':
        # Loops through the whole board from row 0-3 and column 1-3 
        for row in range(4):
            for col in range(1, 4): 
                if board[row][col] == '': # If current cell is empty then check next cell
                    pass  
                else:
                    if col == 1: # If we are at column 1
                        if board[row][col] == board[row][col - 1]: # If the current cell is equal to the Left cell, replace the Left cell with addition of both cells
                            cell = board[row][col]
                            board[row][col - 1] += cell # Replacement of Left cell with their addition
                            board[row][col] = '' # Current cell becomes empty

                        elif board[row][col - 1] == '': # If left cell is empty, replace that cell with the current cell
                            cell = board[row][col]
                            board[row][col - 1] = cell # Replacement of the left cell with current cell
                            board[row][col] = '' # Current cell becomes empty

                        else: # Otherwhise current cell does not move
                            pass

                    # If the column is 2
                    elif col == 2:
                        if board[row][col - 1] == '' and board[row][col - 2] == '': # If both left cells are empty, replace the leftmost cell with current cell
                            cell = board[row][col]
                            board[row][col - 2] = cell # Replacement of the left cell with current cell
                            board[row][col] = '' # Current cell becomes empty

                        elif board[row][col - 1] == '' and board[row][col - 2] == board[row][col]: # If the first left cell is empty, but the second left cell is equal to current cell, replace the second left cell with its addition with current cell
                            cell = board[row][col]
                            board[row][col - 2] += cell # Replacement of the leftmost cell with the addition
                            board[row][col] = '' # Current cell becomes empty

                        elif board[row][col - 1] == '' and board[row][col - 2] != board[row][col]: # If the first left cell is empty, but the second left cell is not equal to current cell, replace the first cell with current cell
                            cell = board[row][col]
                            board[row][col - 1] = cell # Replacement of empty cell with current cell
                            board[row][col] = '' # Current cell becomes empty

                        elif board[row][col] == board[row][col - 1]: # If current cell equals left cell, replace the left cell with its addition to current cell
                            cell = board[row][col]
                            board[row][col - 1] += cell # Replacement of left cell with the addition
                            board[row][col] = '' # Current cell becomes empty

                        else: # Otherwhise current cell does not move
                            pass

                    # If column is 3
                    else:
                        if board[row][col - 1] == '' and board[row][col - 2] == '' and board[row][col - 3] == '': # If all the left cells are empty, replace the leftmost cell with current cell
                            cell = board[row][col]
                            board[row][col - 3] = cell # Replacement of leftmost cell with current cell
                            board[row][col] = '' # Current cell becomes empty

                        elif board[row][col - 1] == '' and board[row][col - 2] == '' and board[row][col - 3] == board[row][col]: # If the first 2 left cells are empty, but leftmost cell is equal to current cell, replace the leftmost cell with its addition with current cell
                            cell = board[row][col]
                            board[row][col - 3] += cell # Replacement of leftmost cell with the addition
                            board[row][col] = '' # Current cell becomes empty

                        elif board[row][col - 1] == '' and board[row][col - 2] == '' and board[row][col - 3] != board[row][col]: # If the first two left cells are empty, but the leftmost cell is not equal to current cell, replace the second left cell with current cell
                            cell = board[row][col]
                            board[row][col - 2] = cell # Replacement of second left cell with current cell
                            board[row][col] = '' # Current cell becomes empty

                        elif board[row][col - 1] == '' and board[row][col - 2] == board[row][col]: # If the first cell is empty, and the second cell is equal to current cell, replace the second left cell witg its addition to current cell
                            cell = board[row][col]
                            board[row][col - 2] += cell # Replacement of leftmost cell with addition
                            board[row][col] = '' # Current cell becomes empty

                        elif board[row][col - 1] == '' and board[row][col - 2] != board[row][col]: # If the first cell is empty, and the second cell is not equal to current cell, replace the first cell with current cell
                            cell = board[row][col]
                            board[row][col - 1] = cell # Replacement of first left cell with current cell
                            board[row][col] = '' # Current cell becomes empty

                        elif board[row][col] == board[row][col - 1]: # If the left cell is equal to the current cell, replace the left cell with its addition with the current cell
                            cell = board[row][col]
                            board[row][col - 1] += cell # Replacement of the left cell with the addition
                            board[row][col] = '' # Current cell becomes empty

                        else: # Otherwhise the current cell does not move
                            pass
    
    # If the letter S is pressed by the user
    elif move == 'S':
        # Loops through the board from row 2-0 and from col 0-3
        for row in reversed(range(3)):
            for col in range(4): 
                if board[row][col] == '': # If current cell is empty then check next cell
                    pass  
                else:
                    if row == 2: # If row is 2
                        if board[row + 1][col] == '': # If bottom cell is empty, replace the bottom cell with current cell
                            cell = board[row][col]
                            board[row + 1][col] = cell # Replacement of lower cell with current cell
                            board[row][col] = '' # Current cell becomes empty

                        elif board[row + 1][col] == board[row][col]: # If bottom cell is equal to current cell, replace the bottom cell with its addition with current cell
                            cell = board[row][col]
                            board[row + 1][col] += cell # Replacement of bottom row with the addition
                            board[row][col] = '' # Current cell becomes empty

                        else: # Otherwhise the current cell does not move
                            pass

                    elif row == 1: # If row is 1
                        if board[row + 1][col] == '' and board[row + 2][col] == '': # If both bottom cells are empty, replace the lowest cell with current cell
                            cell = board[row][col]
                            board[row + 2][col] = cell # Replacement of the lowest cell with current cell
                            board[row][col] = '' # Current cell becomes empty

                        elif board[row + 1][col] == '' and board[row + 2][col] == board[row][col]: # If first bottom cell is empty and the second bottom cell is equal to current cell, replace the lowest cell with its addition with current cell
                            cell = board[row][col]
                            board[row + 2][col] += cell # Replacement of lowest cell with the addition
                            board[row][col] = '' # Current cell becomes empty

                        elif board[row + 1][col] == '' and board[row + 2][col] != board[row][col]: # If first bottom cell is empty and second bottom cell is not equal to current cell, replace the empty cell with current cell
                            cell = board[row][col]
                            board[row + 1][col] = cell # Replacement of empty cell with current cell
                            board[row][col] = '' # Current cell becomes empty

                        elif board[row + 1][col] == board[row][col]: # If bottom cell is equal to current cell, replace the bottom cell with its addition with current cell
                            cell = board[row][col]
                            board[row + 1][col] += cell # Replacement of bottom cell with the addition
                            board[row][col] = '' # Current cell becomes empty

                        else: # Otherwhise the current cell does not move
                            pass

                    # If row is 0
                    else:
                        if board[row + 1][col] == '' and board[row + 2][col] == '' and board[row + 3][col] == '': # If all bottom cells are empty, replace the lowest cell with current cell
                            cell = board[row][col]
                            board[row + 3][col] = cell # Replacement of lowest cell with current cell
                            board[row][col] = '' # Current cell becomes empty

                        elif board[row + 1][col] == '' and board[row + 2][col] == '' and board[row + 3][col] == board[row][col]: # If the first 2 bottom cells are empty, and the third bottom cell is equal to current cell, replace the lowest cell with its addition with current cell
                            cell = board[row][col]
                            board[row + 3][col] += cell # Replacement of the lowest cell with the addition
                            board[row][col] = '' # Current cell becomes empty

                        elif board[row + 1][col] == '' and board[row + 2][col] == '' and board[row + 3][col] != board[row][col]: # If the first 2 bottom cells are empty, but the third bottom cell is not equal to current cell, replace the second bottom cell with current cell
                            cell = board[row][col]
                            board[row + 2][col] = cell # Replacement of second bottom cell with current cell
                            board[row][col] = '' # Current cell becomes empty

                        elif board[row + 1][col] == '' and board[row + 2][col] == board[row][col]: # If the first bottom cell is empty, and the lowest cell is equal to current cell, replace the lowest cell with its addition with the current cell
                            cell = board[row][col]
                            board[row + 2][col] += cell # Replacement of the lowest cell with the addition
                            board[row][col] = '' # Current cell becomes empty

                        elif board[row + 1][col] == '' and board[row + 2][col] != board[row][col]: # If the first bottom cell is empty, but the second bottom cell is not equal to the current cell, replace the empty cell with the current cell
                            cell = board[row][col]
                            board[row + 1][col] = cell # Replacement of empty cell with current cell
                            board[row][col] = '' # Current cell becomes empty

                        elif board[row][col] == board[row + 1][col]: # If the bottom cell is equal to current cell, replace the bottom cell with itts addition with the current cell
                            cell = board[row][col]
                            board[row + 1][col] += cell # Repalcement of the bottom cell with the addition
                            board[row][col] = '' # Current cell becomes empty       

                        else: # Otherwhise the current cell does not move
                            pass

    # If the letter pressed by the user is D
    elif move == 'D':
        # Loops through the board from row 0-3 and from col 2-0
        for row in range(4):
            for col in reversed(range(3)): 
                if board[row][col] == '': # If current cell is empty then check next cell
                    pass  
                else:
                    if col == 2: # If we are at column 2
                        if board[row][col] == board[row][col + 1]: # If the right cell is equal to current cell, replace the right cell with its addition with current cell
                            cell = board[row][col]
                            board[row][col + 1] += cell # Replacement of right cell with the addition
                            board[row][col] = '' # Current cell becomes empty

                        elif board[row][col + 1] == '': # If right cell is empty replace it with current cell
                            cell = board[row][col]
                            board[row][col + 1] = cell # Replacement of empty cell with current cell
                            board[row][col] = '' # Current cell becomes empty

                        else: # Otherwhise the current cell does not move
                            pass

                    elif col == 1: # If we are at column 1
                        if board[row][col + 1] == '' and board[row][col + 2] == '': # If both right cells are empty, replace the rightmost cell with current cell
                            cell = board[row][col]
                            board[row][col + 2] = cell # Replacement of the rightmost cell with current cell
                            board[row][col] = '' # Current cell becomes empty

                        elif board[row][col + 1] == '' and board[row][col + 2] == board[row][col]: # If first right cell is empty and second right cell is equal to the current cell, replace the second right cell with its addition with current cell
                            cell = board[row][col]
                            board[row][col + 2] += cell # Replacement of rightmost cell with the addition
                            board[row][col] = '' # Current cell becomes empty

                        elif board[row][col + 1] == '' and board[row][col + 2] != board[row][col]: # If first right cell is empty and second right cell is not equal to the current cell, replace the empty cell with the current cell
                            cell = board[row][col]
                            board[row][col + 1] = cell # Replacement of empty cell with current cell
                            board[row][col] = '' # Current cell becomes empty

                        elif board[row][col] == board[row][col + 1]: # If the right cell is equal to the current cell, replace the right cell with its addition with current cell 
                            cell = board[row][col]
                            board[row][col + 1] += cell # Replacement of right cell with the addition
                            board[row][col] = '' # Current cell becomes empty

                        else: # Otherwhise the current cell does not move
                            pass

                    # If at column 0
                    else:
                        if board[row][col + 1] == '' and board[row][col + 2] == '' and board[row][col + 3] == '': # If all 3 right cells are empty, replace the rightmost cell with current cell
                            cell = board[row][col]
                            board[row][col + 3] = cell # Replacement of rightmost cell with current cell
                            board[row][col] = '' # Current cell becomes empty

                        elif board[row][col + 1] == '' and board[row][col + 2] == '' and board[row][col + 3] == board[row][col]: # If the first 2 right cells are empty and the third right cell is equal to the current cell, replace the third right cell with its addiition with current cell
                            cell = board[row][col]
                            board[row][col + 3] += cell # Replacement of rightmost cell with the addition
                            board[row][col] = '' # Current cell becomes empty

                        elif board[row][col + 1] == '' and board[row][col + 2] == '' and board[row][col + 3] != board[row][col]: # If the first 2 right cells are empty, and the third right cell is not equal to current cell, replace the second right cell with the current cell
                            cell = board[row][col]
                            board[row][col + 2] = cell #Replacement of the second right cell with current cell
                            board[row][col] = '' # Current cell becomes empty

                        elif board[row][col + 1] == '' and board[row][col + 2] == board[row][col]: # If first right cell si empty and second right cell is equal, replace the rightmost cell with its addition with the current cell
                            cell = board[row][col]
                            board[row][col + 2] += cell # Replacement of rightmost cell with addition
                            board[row][col] = '' # Current cell becomes empty

                        elif board[row][col + 1] == '' and board[row][col + 2] != board[row][col]: # If the first right cell is empty and second right cell is not equal, move the current cell to the first right cell
                            cell = board[row][col]
                            board[row][col + 1] = cell # Replacement of the empty cell with current cell
                            board[row][col] = '' # Current cell becomes empty

                        elif board[row][col] == board[row][col + 1]: # If the right cell is equal to the current cell, replace the right cell with its addition to the current cell
                            cell = board[row][col]
                            board[row][col + 1] += cell # Replacmemnt of right cell with the addition
                            board[row][col] = '' # Current cell becomes empty

                        else: # Otherwhise the current cell does not move
                            pass                       
                    
    """
        updates the board variable based on the move argument by sliding and merging
        the move argument is either 'W', 'A', 'S', or 'D'
        directions: W for up; A for left; S for down, and D for right
    """

#up to two new functions allowed to be added (if needed)
#as usual, they must be documented well
#they have to be placed below this line


def random_cell():

    twoRandomNumbers = random.sample(range(16), 2)
    oneRandomCell = ((twoRandomNumbers[0]//4,twoRandomNumbers[0]%4))

    return oneRandomCell

    """This is a random cell generator"""



if __name__ == "__main__":  # Use as is  
    init()
    displayGame()
    while True:  # Super-loop for the game
        print(f"Score: {getCurrentScore()}")
        userInput = promptGamerForTheNextMove()
        if(userInput == 'Q'):
            print("Exiting the game. Thanks for playing!")
            break
        updateTheBoardBasedOnTheUserMove(userInput)
        addANewTwoToBoard()
        displayGame()

        if isFull(): #game is over once all cells are taken
            print("Game is Over. Check out your score.")
            print("Thanks for playing!")
            break