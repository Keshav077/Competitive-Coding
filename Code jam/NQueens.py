def diaCheck(a, row, col):
    i, j = row, col
    while i >= 0 and j >= 0:
        if a[i][j] == 1:
            return False
        i -= 1
        j -= 1
    i, j = row, col
    while i >= 0 and j < len(a):
        if a[i][j] == 1:
            return False
        i -= 1
        j += 1
    return True


def colCheck(a, row, col):
    for i in range(row):
        if a[i][col] == 1:
            return False
    return True


def isSafe(a, row, col):
    return colCheck(a, row, col) and diaCheck(a, row, col)


def solveNQueens(a, row):
    if row == len(a):
        return True
    for i in range(len(a)):
        if isSafe(a, row, i):
            a[row][i] = 1
            if solveNQueens(a, row+1):
                return True
            a[row][i] = 0
    return False


N = int(input())
A = [[0] * N for i in range(N)]
if solveNQueens(A, 0):
    for i in A:
        print(" ".join(map(str, i)))
else:
    print("Impossible")
