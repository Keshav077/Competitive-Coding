n, p = map(int, input().split())
s = input()
index = []
for i in range(n - 1):
    if i == n - 2:
        if s[i] == s[i+1]:
            index.append([i+1, int(s[i])])
        else:
            index.append([i, int(s[i])])
            index.append([i+1, int(s[i+1])])
    elif s[i] != s[i+1]:
        index.append([i, int(s[i])])

print(index)
while p > 0:
    p -= 1
    if index[1][0] - index[0][1] > index[-2][1] - index[-3][1]:
        index.pop(0)
        index.pop(0)
    else:
        index.pop(-2)
        index.pop(-2)
print(index)
