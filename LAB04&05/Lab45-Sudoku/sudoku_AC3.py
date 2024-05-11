
import time
from csp import csp
from AC3 import *
import argparse


# THE MAIN FUNCTION GOES HERE
if __name__ == "__main__":
    argument_parser = argparse.ArgumentParser(description="Sudoku Solving Problem")
    argument_parser.add_argument("--inputFile", type=str, help="Sudoku Input File")
    args = argument_parser.parse_args()

    filename = args.inputFile
    array = []
    with open(filename, "r") as ins:
        for line in ins:
            array.append(line)

    ins.close()
    i = 0
    boardno = 0
    start = time.time()

    for grid in array:
        prev = time.time()
        sudoku = csp(grid=grid)
        solved = AC3(sudoku)
        boardno = boardno + 1
        if isComplete(sudoku) and solved:
            print(boardno)
            print("Before solving: ", grid)
            print("After solving: ", write(sudoku.values))
            print("Running time: ", time.time() - prev, "\n")
            i = i + 1

    print("Number of problems solved is: ", i)
    print("The complete run time is: ", time.time() - start)