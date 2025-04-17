n = int(input()) # 輸入幾列

triangle = []
triangle.append([1]) # n = 1, 0
triangle.append([1, 1]) # n = 2, 1
# triangle.append([1, triangle[1][0]+triangle[1][1], 1]) # n = 3, 2
# triangle.append([1, triangle[2][0]+triangle[2][1], triangle[2][1]+triangle[2][2], 1]) # n = 4

for i in range(2, n):
    row = [1]
    for j in range(0, i-1):
        row.append(triangle[i-1][j]+triangle[i-1][j+1])
    row.append(1)
    triangle.append(row)

for row in range(0, n):
    for col in triangle[row]:
        print(col, end=" ")
    print("\n")
