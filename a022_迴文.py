flag = "yes"

input = input()

for i in range(0, len(input)):
    if input[i] != input[-1-i]:
        flag = "no"
        break

print(flag)