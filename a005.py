times = int(input()) # 令 times 為 輸入次數

for i in range(times): # 執行 「times」 次
    input = list(map(int, input().split())) # 輸入數字，陣列格式
    # 判斷是不是等差數列
    if (input[3] - input[2]) == (input[2] - input[1]): # 如果 第3項減第2項 = 第2項減第1項（等差數列每項差皆相同）
        # 是等差數列
        d = input[3] - input[2] # 取得公差
        input.append(int(input[3] + d)) # 新增答案至最後一項
    else:
        # 題目只有可能是等差或等比，不是等差就是等比了
        r = input[3] / input[2] # 取得公比
        input.append(int(input[3] * r)) # 新增答案至最後一項

    # 輸出答案
    for j in input:
        print(j, end=" ") # 把陣列中的每一項印出來
    
    print("\n") # 因為上面的輸出法會造成每一行最後變成空格（原本應是換行），因此要多印一次換行才不會出錯
    
    # 刪除陣列
    del input