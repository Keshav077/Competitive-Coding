def Parenting(time):
    result = [''] * len(time)
    order = []
    for i in range(len(time)):
        order.append([time[i][0], time[i][1], i])
    order.sort(key=lambda x: x[0])
    C = order[0]
    J = order[1]
    result[C[2]], result[J[2]] = 'C', 'J'
    for i in range(2,len(order)):
        if C[1] <= order[i][0]:
            C = order[i]
            result[C[2]] = 'C'
        elif J[1] <= order[i][0]:
            J = order[i]
            result[J[2]] = 'J'
        else:
            return "IMPOSSIBLE"
    return "".join(result)


tc = int(input())
for t in range(tc):
    n = int(input())
    timings = []
    for i in range(n):
        timings.append(list(map(int, input().split())))
    print("Case #{}: {}".format(t+1, Parenting(timings)))

