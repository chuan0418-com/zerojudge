input = int(input())
out = [0, 0]
output_text = "-1"
for i in range(2, 100000000):
    # 20
    out.append(0)

    while input % i == 0:
        # 10
        out[i] += 1
        input = input/i
    if out[i] != 0:
        if output_text == "-1":
            if out[i] != 1:
                output_text = f"{i}^{out[i]}"
            else:
                output_text = f"{i}"
        else:
            if out[i] != 1:
                output_text = output_text+f" * {i}^{out[i]}"
            else:
                output_text = output_text+f" * {i}"

    if input == 1:
        # print(out)
        print(output_text)
        break
