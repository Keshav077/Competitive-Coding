def assign():
    for i in range(len(B)):
        for j in range(len(B[i])):
            A[i][j] = B[i][j]
    return


def solve():
    Sum = 0
    for i in range(1, r + 1):
        for j in range(1, c + 1):
            Sum += A[i][j]
            compNg = []
            row, col = i, j + 1
            # right
            while col < len(A[i]) and A[row][col] == 0:
                col += 1
            if col < len(A[i]):
                compNg.append(A[row][col])
            # down
            row, col = i + 1, j
            while row < len(A) and A[row][col] == 0:
                row += 1
            if row < len(A):
                compNg.append(A[row][col])
            # left
            row, col = i, j - 1
            while col > 0 and A[row][col] == 0:
                col -= 1
            if col > 0:
                compNg.append(A[row][col])
            # top
            row, col = i - 1, j
            while row > 0 and A[row][col] == 0:
                row -= 1
            if row > 0:
                compNg.append(A[row][col])
            if len(compNg) > 0:
                if sum(compNg)/len(compNg) > A[i][j]:
                    B[i][j] = 0
    return Sum


tc = int(input())
for t in range(tc):
    r, c = [int(x) for x in input().split()]
    A = [[0] * (c + 2) for i in range(r + 2)]
    B = [[0] * (c + 2) for i in range(r + 2)]
    for i in range(1,r+1):
        X = list(map(int,input().split()))
        for j in range(1,c+1):
            A[i][j] = X[j - 1]
            B[i][j] = X[j - 1]
    res = []
    while True:
        X = solve()
        if len(res) > 0:
            if res[-1] == X:
                break
            else:
                res.append(X)
        else:
            res.append(X)
        assign()
    print("Case #{}: {}".format(t+1, sum(res)))

