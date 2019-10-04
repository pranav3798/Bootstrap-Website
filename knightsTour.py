
# Check if the move is valid and has not been made before
def isSafe(x, y, sol):
	if(x >=0 and x <len(sol) and y >=0 and y<len(sol) and sol[x][y] == -1):
		return True
	return False


def printSolution(sol):
	for x in sol:
		for y in x:
			print(y, end=" ")
		print()


def solveKT(n):
	sol = [[-1 for i in range(n)] for i in range(n)]

	xMoves = [2, 1, -1, -2, -2, -1, 1, 2]
	yMoves = [1, 2, 2, 1, -1, -2, -2, -1]

	sol[0][0] = 0

	if(solveKTUtil(0,0,1,sol, xMoves, yMoves) == False):
		print("Solution does not exist")
		for i in sol:
			print(i)
		return False
	else:
		printSolution(sol)
	return True

def solveKTUtil(x,y,movei,sol,xMoves, yMoves):

	if(movei == len(sol)**2):
		return True

	for k in range(8):
		next_x = x+xMoves[k]
		next_y = y+yMoves[k]

		if(isSafe(next_x, next_y, sol)):
			sol[next_x][next_y] = movei
			if(solveKTUtil(next_x, next_y,movei+1, sol, xMoves, yMoves) == True):
				return True
			else:
				sol[next_x][next_y] = -1

	return False

solveKT(3)

