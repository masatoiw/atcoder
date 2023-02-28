n, y = map(int, input().split())
is_possible = False
for i in range(0, n+1):
    for j in range(0, n + 1 - i):
        k = n - i - j
        sum = i * 10000 + j * 5000 + k * 1000
        if sum == y:
            print(f'{i} {j} {k}')
            is_possible = True
            break
    if is_possible:
        break
if not is_possible:
    print('-1 -1 -1')