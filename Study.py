li = [int(input()) for i in range(28)]
box = [0 for i in range(30)]
for i in li:
    box[i-1] = 1
result = list(filter(lambda x: box[x] == 0, range(len(box))))
for i in result:
    print(i+1)