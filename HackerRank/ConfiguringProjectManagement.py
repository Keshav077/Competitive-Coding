for _ in range(int(input())):
    n, m = map(int, input().split())
    A = []
    for i in range(m):
        edge = list(map(int, input().split()))
        A.append(edge)
    res = [set() for i in range(n)]
    for i in A:
        res[i[0] - 1].add(i[1])
        res[i[1] - 1].add(i[0])
    res[0] -= {1, 2}
    # print(res)
    X = []
    for i in res[0]:
        if 2 in res[i - 1]:
            continue
        else:
            found = False
            for j in res[i - 1]:
                if 2 in res[j - 1]:
                    found = True
            if not found:
                X.append(i)
    if len(X) > 0:
        print(" ".join(map(str, sorted(X))))
    else:
        print(-1)
