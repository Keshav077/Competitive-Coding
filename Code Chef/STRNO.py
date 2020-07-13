def isPrime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


observed = []
for i in range(1, 10**4):
    X = []
    for j in range(1, int(i ** 0.5) + 1):
        if i % j == 0:
            if j == i // j:
                X.append(j)
            else:
                X.extend([j, i // j])

    cnt = 0
    for i in X:
        if isPrime(i):
            cnt += 1

    observed.append(str(len(X)) + " " + str(cnt))
observed = list(set(observed))
Z = []
for i in observed:
    Z.append(list(map(int, i.split())))
Z.sort()
for i in Z:
    print(i)
