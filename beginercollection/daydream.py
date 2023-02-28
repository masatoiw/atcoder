s = input()
sentences =['eraser', 'erase', 'dreamer', 'dream']
for sen in sentences:
    s = s.replace(sen, '')
    # print(s)
if len(s) == 0:
    print('YES')
else:
    print('NO')
