def solve():
    X = input().split()
    X, Y, M = int(X[0]), int(X[1]), X[2]
    found = False
    for i in range(len(M)):
        if M[i] == "S":
            Y -= 1
        elif M[i] == "N":
            Y += 1
        elif M[i] == "E":
            X += 1
        else:
            X -= 1
        if abs(X) + abs(Y) <= i + 1:
            print(i + 1)
            found = True
            break
    if not found:
        print("IMPOSSIBLE")


tc = int(input())
for t in range(tc):
    print("Case #{}:".format(t+1),end=" ")
    solve()

