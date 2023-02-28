n, a, b = map(int, input().split())
result = 0

for i in range(n+1):
    i_sum = 0
    j = i
    while j >0:
        i_sum += j % 10
        j //= 10
    if i_sum >= a and i_sum <= b:
        result += i
print(result)