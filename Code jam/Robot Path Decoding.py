tc = int(input())
for t in range(tc):
    s = input()
    i, j = 1, 1
    stack = []
    depth = 1
    for k in s:
        if k.isnumeric():
            stack.append(int(k))
            depth *= int(k)
        elif k.isalpha():
            if k == 'N':
                i -= depth
            elif k == 'S':
                i += depth
            elif k == 'E':
                j += depth
            elif k == 'W':
                j -= depth
        elif k == ')':
            depth //= stack.pop()
    i, j = i % 10 ** 9, j % 10 ** 9
    if i == 0:  i = 10 ** 9
    if j == 0:  j = 10 ** 9
    print("Case #{}: {} {}".format(t + 1, j, i))
