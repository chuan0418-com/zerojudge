input = input()
output = ""
if int(input) == 0:
    print(0)

for i in range(0, len(input)):
    if str(input[-1-i]) == "0":
        if (not output):
            continue
    output = output+str(input[-1-i])

print(output)