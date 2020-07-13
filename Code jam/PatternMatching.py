def check(a, b):
    b = b[::-1]
    a = a[::-1]
    for i in range(len(a)):
        if b[i] != a[i]:
            return False
    return True


tc = int(input())
for t in range(tc):
    n = int(input())
    pattern = []
    X = None
    for i in range(n):
        pattern.append(input())
        if X is None:
            X = pattern[-1]
        else:
            if len(pattern[-1]) > len(X):
                X = pattern[-1]
    for i in pattern:
        if not check(i[1:], X):
            print("Case #{}: {}".format(t+1, "*"))
            exit()
    print("Case #{}: {}".format(t+1, X[1:]))

