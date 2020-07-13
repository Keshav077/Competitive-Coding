fSeries = [0, 1]
while fSeries[-1] <= 10 ** 10:
    fSeries.append(fSeries[-1] + fSeries[-2])
fSeries = set(fSeries)
for _ in range(int(input())):
    if int(input()) in fSeries:
        print("IsFibo")
    else:
        print("IsNotFibo")