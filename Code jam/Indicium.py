def find_empty_location(arr, l):
    for row in range(len(arr)):
        for col in range(len(arr)):
            if row != col and arr[row][col] == 0:
                l[0] = row
                l[1] = col
                return True
    return False


def used_in_row(arr, row, num):
    for i in range(len(arr)):
        if arr[row][i] == num:
            return True
    return False


def used_in_col(arr, col, num):
    for i in range(len(arr)):
        if arr[i][col] == num:
            return True
    return False


def check_location_is_safe(arr, row, col, num):
    return not used_in_row(arr, row, num) and not used_in_col(arr, col, num)


def Indicium(arr):
    l = [0, 0]

    if not find_empty_location(arr, l):
        return True

    row = l[0]
    col = l[1]

    for num in range(1, len(arr)+1):
        if check_location_is_safe(arr, row, col, num):
            arr[row][col] = num
            if Indicium(arr):
                return True
            arr[row][col] = 0
    return False


def isPossible(n, k):
    if n <= 2:
        return [False, -1]
    for i in range(1, n + 1):
        if i * n == k:
            return [True, i]
    if (n * (n + 1)) // 2:
        return [True, 0]
    return [False, -1]


tc = int(input())
for t in range(tc):
    n, k = list(map(int, input().split()))
    x = isPossible(n, k)
    if x[0]:
        print("Case #{}: POSSIBLE".format(t + 1))
        A = [[0] * n for i in range(n)]
        if x[1] == 0:
            for i in range(n):
                A[i][i] = i + 1
        elif x[1] <= n:
            for i in range(n):
                A[i][i] = x[1]
        Indicium(A)
        for i in range(n):
            for j in range(n):
                print(A[i][j], end=" ")
            print()
    else:
        print("Case #{}: IMPOSSIBLE".format(t + 1))
