Primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]


def Sieve(n):
    primeCheck = [True for i in range(n + 1)]
    p = 2
    while p * p <= n:
        if primeCheck[p]:
            for i in range(p * p, n + 1, p):
                primeCheck[i] = False
        p += 1
    arePrimes = []
    for p in range(2, n + 1):
        if primeCheck[p]:
            arePrimes.append(p)
    return arePrimes


Check = set(Sieve(100100))
N1, N2 = list(map(int, input().split()))
require = [str(i) for i in Primes if N1 <= i <= N2]
combination = []
for i in range(len(require)):
    for j in range(len(require)):
        if i != j:
            combination.append(require[i] + require[j])
combination = list(map(int, combination))
required = []
for i in combination:
    if i in Check:
        required.append(i)
required = set(required)
a, b = min(required), max(required)
for i in range(len(required) - 1):
    a, b = b, a + b
print(a)
