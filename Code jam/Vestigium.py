def Trace(a):
    trace = 0
    rowCount = 0
    for i in range(len(a)):
        row = set()
        found = False
        for j in range(len(a)):
            if i == j:
                trace += a[i][j]
            if not found and a[i][j] in row:
                rowCount += 1
                found = True
            else:
                row.add(a[i][j])
    colCount = 0
    for j in range(len(a)):
        col = set()
        for i in range(len(a)):
            if a[i][j] in col:
                colCount += 1
                break
            else:
                col.add(a[i][j])
    return trace, rowCount, colCount


tc = int(input())
for t in range(tc):
    n = int(input())
    A = []
    for i in range(n):
        A.append(list(map(int, input().split())))
    k, r, c = Trace(A)
    print("Case #{}: {} {} {}".format(t + 1, k, r, c))
