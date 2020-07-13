n = int(input())
S = input().lower()
Max = [[None, 0] for i in range(n)]
MaxSFA, MaxSFC = "", 0
for i in range(n):
    if S[i] > MaxSFA:
        MaxSFA = S[i]
        MaxSFC = 1
    elif S[i] == MaxSFA:
        MaxSFC += 1
    Max[i][0] = MaxSFA
    Max[i][1] = MaxSFC
print(Max)
Q = int(input())
for i in range(Q):
    x, y = map(int, input().split())
    if Max[x][0] == Max[y][0] and Max[x][1] != Max[y][1]:
        if Max[x][0] == S[x]:
            print(Max[y][1] - Max[x][1] + 1)
        else:
            print(Max[y][1] - Max[x][1])
    elif Max[x][0] != Max[y][0]:
        print(Max[y][1])
    else:
        if Max[y][0] == S[x]:
            print(1)
        else:
            print(S[x: y + 1].count(max(S[x: y + 1])))