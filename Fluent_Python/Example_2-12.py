#We can use the * operator to concatenate lists, 
#Example [1,2,3] * 3 = [1,2,3,1,2,3,1,2,3]
#but it does not work with lists of lists. See example 2_13 to see why.

board = [["_"] * 3 for _ in range(3)]
print(board)
board[1][1] = "X"
print(board)