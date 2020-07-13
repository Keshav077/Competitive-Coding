def sieve(n):
    prime = [True] * n
    multiples = {}
    mi = 0
    for i in range(2, int(n**0.5) + 1):
        if prime[i-1]:
            for j in range(i,n+1,i):
                if prime[j-1]:
                    if i not in multiples:
                        multiples[i] = [j]#set()
                        #multiples[i].add(j)
                    else:
                        multiples[i].append(j)
                prime[j-1] = False
            mi += 1
    #print(multiples)
    for i in multiples:
        print(i,multiples[i])
    #primeNos = [i+1 for i in range(n) if prime[i]]
    #print(primeNos)



for _ in range(int(input())):
    N = int(input())
    sieve(N)
