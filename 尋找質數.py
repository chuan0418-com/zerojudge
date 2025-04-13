out = [2, 3, 5, 7]
for input in range(2, 1000):
    is_com = False
    for i in out:
        if input % i == 0:
            is_com = True
            break
    if not is_com:
        out.append(input)
print(out)