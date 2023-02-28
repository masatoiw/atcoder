n = int(input())
t = 0
x = 0
y = 0
for i in range(n):
    tn, xn, yn = map(int, input().split())
    td = abs(tn - t)
    xd = abs(xn - x)
    yd = abs(yn - y)
    if td < xd + yd:
        print('No')
        exit()
    if td % 2 != (xd + yd) % 2:
        print('No')
        exit()
    t = tn
    x = xn
    y = yn
print('Yes')