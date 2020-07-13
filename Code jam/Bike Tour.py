tc = int(input())
for t in range(tc):
    n = int(input())
    A = list(map(int,input().split()))
    res = 0
    for i in range(1,n-1):
        if A[i] > A[i+1] and A[i] > A[i-1]:
            res += 1
    print("Case #{}: {}".format(t+1,res))