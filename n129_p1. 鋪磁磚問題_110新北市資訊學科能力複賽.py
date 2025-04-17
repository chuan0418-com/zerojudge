# 1, 2, 4
k = [1, 2, 4]
space = int(input())
if space < 3:
    print(k[space-1])
else:
    for i in range(2, space-1):
        k.append(k[i]+k[i-1]+k[i-2])
    print(k[-1])