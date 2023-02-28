n, a, b = map(int, input().split())
result = 0
for i in range(1, n+1):
    digit_sum = 0
    digit_num = i
    while digit_num > 0:
        digit_sum += digit_num % 10
        digit_num = digit_num // 10
    if digit_sum >= a and digit_sum <= b:
        result += i
print(result)