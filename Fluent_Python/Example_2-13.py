board = [["_"] * 3] * 3
print(board)
board[1][1] = "X"
print(board)
# This will show that all rows are the same reference, so changing one changes all.
# This is because the * creates a list of references to the same inner list.