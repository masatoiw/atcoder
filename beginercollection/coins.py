a = int(input())
b = int(input())
c = int(input())
x = int(input())
counter = 0
for i in range(a + 1):
    for j in range(b + 1):
        for k in range(c+1):
            sum = i*500 + j*100 + k * 50
            if sum == x:
                counter += 1
print(counter)