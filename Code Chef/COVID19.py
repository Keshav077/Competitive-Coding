for _ in range(int(input())):
    n = int(input())
    A = list(map(int, input().split()))
    res = []
    cnt = 1
    for i in range(n - 1):
        if A[i+1] - A[i] > 2:
            res.append(cnt)
            cnt = 1
        else:
            cnt += 1
    if A[-2] - A[-1] > 2:
        res.append(1)
    else:
        res.append(cnt)
    print(min(res), max(res))
