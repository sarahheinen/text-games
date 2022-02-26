import random

# Pool of ducks - numbers are hidden
row1 = ["0", "0", "0", "0", "0"]
row2 = ["0", "0", "0", "0", "0"]
row3 = ["0", "0", "0", "0", "0"]
row4 = ["0", "0", "0", "0", "0"]
row5 = ["0", "0", "0", "0", "0"]

duckPool = [row1, row2, row3, row4, row5]

# List of Duck numbers that will be shuffled - higher numbers are more rare
numList = [1,1,1,1,2,2,2,2,3,3,3,4,4,4,5,5,5,6,6,7,7,8,8,9,9]

# List of prizes that corresponds to the number on the bottom of the duck - higher number prizes are better
prizeList = [
    "mini eraser shaped like a dinosaur!",
    "star shaped sticker!",
    "purple slinky!",
    "shiny blue pinwheel!",
    "plastic pink maraca with a smiley face on it!",
    "pink paddle ball game!",
    "yellow pair of star-shaped sunglasses!",
    "red pull-back toy car!",
    "multi-colored fuzzy slap bracelet!"
]

round = 0

def ducks():
    # Shuffles numbers at the beginning of each game
    random.shuffle(numList)
    numRow1 = numList[:5]
    numRow2 = numList[5:10]
    numRow3 = numList[10:15]
    numRow4 = numList[15:20]
    numRow5 = numList[20:25]

    numPool = [numRow1, numRow2, numRow3, numRow4, numRow5]

    # Game begins with the following statement
    print("Step right up to our Duck Matching Game!  Choose any two ducks.  If they have the same number, you win a prize!  You have 3 attempts.")

    # Each game has 3 rounds/attempts
    for round in range(3):

        # Prints duck pool
        for row in duckPool:
            for duck in range(5):
                if duck == 4:
                    print(row[duck])
                else:
                    print(row[duck], end=" ")

        # Prompts the user to select their duck by choosing a row and column
        duck1row = input("Row of first duck: ")
        duck1col = input("Column of first duck: ")

        # If the row or number columns are out of the range, the user is prompted to re-input a number
        while duck1row not in ["1","2","3","4","5"] or duck1col not in ["1","2","3","4","5"]:
            print("The rows and columns are numbered 1-5!  Pick a row and column in this range.")
            duck1row = input("Row of first duck: ")
            duck1col = input("Column of first duck: ")

        # Changes row and column type to int
        duck1row = int(duck1row)
        duck1col = int(duck1col)

        # Allows the user to see the number on the duck they chose
        duckPool[duck1row - 1][duck1col - 1] = numPool[duck1row - 1][duck1col - 1]

        # Prints the pool, showing the number on the bottom of their duck
        for row in duckPool:
            for duck in range(5):
                if duck == 4:
                    print(row[duck])
                else:
                    print(row[duck], end=" ")

        # Prompts the user to select their duck by choosing a row and column
        duck2row = input("Row of second duck: ")
        duck2col = input("Column of second duck: ")

        # If the row or number columns are out of the range, the user is prompted to re-input a number
        while duck2row not in ["1","2","3","4","5"] or duck2col not in ["1","2","3","4","5"]:
            print("The rows and columns are numbered 1-5!  Pick a row or column in this range.")
            duck2row = input("Row of second duck: ")
            duck2col = input("Column of second duck: ")

        # Changes row and column type to int
        duck2row = int(duck2row)
        duck2col = int(duck2col)

        # Allows the user to see the number on the duck they chose
        duckPool[duck2row - 1][duck2col - 1] = numPool[duck2row - 1][duck2col - 1]

        # Prints the pool, showing the number on the bottom of their duck
        for row in duckPool:
            for duck in range(5):
                if duck == 4:
                    print(row[duck])
                else:
                    print(row[duck], end=" ")

        # User wins when the numbers on the bottom of their ducks match
        if numPool[duck1row - 1][duck1col - 1] == numPool[duck2row - 1][duck2col - 1]:
            # The prizes correspond to the number on the bottom of the matching ducks
            print("Your ducks match!  Congratulations!  You won a", prizeList[numPool[duck1row - 1][duck1col - 1] - 1])
            break

        # Print statements for each round/attempt
        elif round == 0:
            print("Not a match!  Try again!  You have 2 attempts remaining.")

        elif round == 1:
            print("Those don't match either!  You have 1 more shot!")

        elif round == 2:
            print("Those don't match either.  Better luck next time!")
            break

        # Hides number locations before asking for the next two ducks
        duckPool[duck1row - 1][duck1col - 1] = "0"
        duckPool[duck2row - 1][duck2col - 1] = "0"

ducks()