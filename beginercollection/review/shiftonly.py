n = int(input())
data = list(map(int, input().split()))
result = []
for d in data:
    counter = 0
    while d > 0:
       if d % 2 == 0:
           counter += 1
           d = int(d/2)
       else:
           break
    result.append(counter)
print(min(result))