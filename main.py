import pprint

board = [
    [1, 9, 5, 0, 0, 0, 6, 3, 0],
    [0, 0, 7, 6, 0, 9, 0, 0, 0],
    [0, 0, 0, 0, 0, 3, 8, 9, 7],
    [0, 7, 0, 0, 8, 0, 1, 5, 9],
    [5, 0, 9, 0, 0, 1, 7, 0, 8],
    [2, 8, 0, 5, 0, 0, 0, 0, 0],
    [7, 0, 0, 0, 4, 0, 0, 0, 5],
    [3, 0, 0, 0, 1, 8, 9, 7, 0],
    [0, 1, 4, 7, 3, 0, 0, 8, 0]
]

def solveSudoku(board):
  solvePartialSudoku(0, 0, board)
  return board

def solvePartialSudoku(row, col, board):
	currentRow = row
	currentCol = col
	
	if currentCol == len(board[currentRow]):
		currentRow += 1
		currentCol = 0
		if currentRow == len(board):
			return True #board complete
		
	if board[currentRow][currentCol] == 0:
		return tryDigitsAtPosition(currentRow, currentCol, board)
	
	return solvePartialSudoku(currentRow, currentCol + 1, board)

def tryDigitsAtPosition(row, col, board):
	for digit in range(1, 10):
		if isValidAtPosition(digit, row, col, board):
			board[row][col] = digit
			if solvePartialSudoku(row, col + 1, board):
				return True
			
	board[row][col] = 0
	return False

def isValidAtPosition(value, row, col, board):
	rowIsValid = value not in board[row]
	columnIsValid = value not in map(lambda r: r[col], board)
	
	if not rowIsValid or not columnIsValid:
		return False
	
	#Check subgrid constraint
	subgridRowStart = (row // 3) * 3
	subgridColStart = (col // 3) * 3
	for rowIdx in range(3):
		for colIdx in range(3):
			rowToCheck = subgridRowStart + rowIdx
			colToCheck = subgridColStart + colIdx
			existingValue = board[rowToCheck][colToCheck]
			
			if existingValue == value:
				return False
			
	return True

pp = pprint.PrettyPrinter(depth=6)

pp.pprint(solveSudoku(board))
