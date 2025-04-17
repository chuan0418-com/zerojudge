code = {"A": 1, "B": 10, "C": 19, "D": 28, "E": 37, "F": 46, "G": 55, "H": 64, "I": 39, "J": 73, "K": 82, "L": 2, "M": 11, "N": 20, "O": 48, "P": 29, "Q": 38, "R": 47, "S": 56, "T": 65, "U": 74, "V": 83, "W": 21, "X": 3, "Y": 12, "Z": 30}
input = input()
ans = code[input[0]] + int(input[1])*8 + int(input[2])*7 + int(input[3])*6 + int(input[4])*5 + int(input[5])*4 + int(input[6])*3 + int(input[7])*2 + int(input[8])*1 + int(input[9])
if ans % 10 == 0:
    print("real")
else:
    print("fake")