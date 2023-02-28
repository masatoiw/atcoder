n = int(input())
a = list(map(int, input().split()))

result = []
for num in a:
    counter = 0
    while num > 0:
        if num % 2 == 1:
            result.append(counter)
        counter += 1
        num = num / 2
print(min(result))
