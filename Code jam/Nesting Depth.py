def Depth(st):
    curDepth = 0
    result = ""
    for i in st:
        if int(i) > curDepth:
            result += '(' * (int(i) - curDepth ) + i
            curDepth = int(i)
        elif int(i) < curDepth:
            result += ')' * (curDepth - int(i)) + i
            curDepth = int(i)
        else:
            result += i
            curDepth = int(i)
    result += ')' * curDepth
    return result


tc = int(input())
for t in range(tc):
    s = input()
    print("Case #{}: {}".format(t+1, Depth(s)))
