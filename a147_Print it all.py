while True:
    input = int(input())
    if input == 0:
        break
    for i in range(1, input):
        if i % 7 == 0:
            continue
        print(i, end=" ")
    print("\n")
    del input