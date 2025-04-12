correct = list(map(int, input())) # 請輸入正確答案
times = int(input()) # 次數
for t in range(0, times):
    guess = list(map(int, input()))
    result = [0, 0] # A, B
    guessed_right = {}
    guessed_wrong = {}
    for i in range(0, len(correct)):
        if correct[i] == guess[i]: # 當 猜測答案與正確答案的 i 元皆相同時
            result[0] += 1 # A +1
            guessed_right[guess[i]] = guessed_right.get(guess[i], 0) + 1
        else:
            guessed_wrong[guess[i]] = guessed_wrong.get(guess[i], 0) + 1

    for key, item in guessed_wrong.items():
        if correct.count(key) - guessed_wrong.get(key, 0) >= 0:
            result[1] += 1
    print(f"{result[0]}A{result[1]}B")