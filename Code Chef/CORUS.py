from collections import Counter
for _ in range(int(input())):
    N, Q = map(int, input().split())
    S = input()
    C = Counter(S)
    for q in range(Q):
        D = int(input())
        for i in C.keys():
            C[i] -= D
        X = [i for i in C.values() if i > 0]
        print(sum(X))
        for i in C.keys():
            C[i] += D
        #print(C)
