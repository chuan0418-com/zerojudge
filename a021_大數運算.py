input = list(map(str, input().split()))
input[0] = int(input[0])
input[2] = int(input[2])
if input[1] == "+":
    print(input[0]+input[2])
elif input[1] == "-":
    print(input[0]-input[2])
elif input[1] == "*":
    print(input[0]*input[2])
elif input[1] == "/":
    print(input[0]//input[2])
