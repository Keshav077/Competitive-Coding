n, m = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
j, res = 1, 0
for i in range(n):
    res += A[i] * j
    if (i + 1) % m == 0 and n - i - 1 > m:
        j += 1
print(res % (10 ** 9 + 7))
