for _ in range(int(input())):
    X, Y, L, R = map(int, input().split())
    Z = X | Y
    print(X, Y)
    X = (X << 1) & X
    Y = Y >> 1
    print(X, Y)
    """while not L < Z < R:
        X >>= 1
        Z >>= 1
        Z = X | Y
        print(Z)"""