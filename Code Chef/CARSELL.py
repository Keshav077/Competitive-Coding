for _ in range(int(input())):
    n = int(input())
    A = list(map(int,input().split()))
    A.sort(reverse=True)
    result = 0
    for i in range(n):
        X = A.pop(0)
        result += X - i if X - i > 0 else 0
    print(result%1000000007)