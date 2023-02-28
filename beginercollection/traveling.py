n = int(input())
x = 0
y = 0
t = 0

for _ in range(n):
    t1, x1, y1 = map(int, input().split())
    td = t1 - t
    xd = abs(x1 - x)
    yd = abs(y1 - y)
    if td < xd + yd:
        print('No')
        exit()
    if td % 2 != (xd + yd) % 2:
        print('No')
        exit()
    x = x1
    y = y1
    t = t1
print('Yes')