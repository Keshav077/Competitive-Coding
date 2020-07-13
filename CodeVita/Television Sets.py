N = int(input())
R1, R2 = list(map(int, input().split()))
revenue = int(input())
patients = [[] for i in range(12)]
roomsAllotted = [0] * (N+1)
for m in range(1, 12+1):
    if m > 7:
        if m % 2 == 0:
            for d in range(1, 31 + 1):
                noPat = (6 - m) ** 2 + abs(d - 15)
                noPat = noPat if N >= noPat else N
                roomsAllotted[noPat] += 1
                patients[m - 1].append(noPat)
        else:
            for d in range(1, 30+1):
                noPat = (6 - m) ** 2 + abs(d - 15)
                noPat = noPat if N >= noPat else N
                roomsAllotted[noPat] += 1
                patients[m - 1].append(noPat)
    elif m % 2 == 1:
        for d in range(1, 31+1):
            noPat = (6 - m) ** 2 + abs(d - 15)
            noPat = noPat if N >= noPat else N
            roomsAllotted[noPat] += 1
            patients[m-1].append(noPat)
    else:
        if m == 2:
            for d in range(1, 28+1):
                noPat = (6 - m) ** 2 + abs(d - 15)
                noPat = noPat if N >= noPat else N
                roomsAllotted[noPat] += 1
                patients[m - 1].append(noPat)
        else:
            for d in range(1, 30+1):
                noPat = (6 - m) ** 2 + abs(d - 15)
                noPat = noPat if N >= noPat else N
                roomsAllotted[noPat] += 1
                patients[m - 1].append(noPat)
totalPat = 0
for i in range(12):
    totalPat += sum(patients[i])
SoFarRevenue = totalPat * R2
diff = R1 - R2
for i in range(1, N+1):
    additionalCharges = 0
    dup = 1
    for j in range(N-i+1, N+1):
        additionalCharges += roomsAllotted[j] * diff * dup
        dup += 1
    if SoFarRevenue + additionalCharges >= revenue:
        print(i)
        exit()
print(N)
