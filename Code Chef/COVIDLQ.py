def following(A):
    step = 1
    for i in A:
        if i == 1:
            if step < 6:
                return False
            step = 1
        else:
            step += 1
    return True


for _ in range(int(input())):
    n = int(input())
    A = list(map(int,input().split()))
    if following(A[A.index(1)+1:]):
        print("YES")
    else:
        print("NO")