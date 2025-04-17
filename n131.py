# 尋找質數 START
# primes = [2, 3, 5, 7]
# for input in range(2, 1000):
#     is_com = False
#     for i in primes:
#         if input % i == 0:
#             is_com = True
#             break
#     if not is_com:
#         primes.append(input)
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]
# 尋找質數 END

caled = {}

def cal(input): # 分割成本
    if not isPrimes(input): # 若不是質數
        return 0
    else: # 質數
        if input == 2 or input == 3:
            return 0
        else:
            if caled.get(input):
                return caled[input]
            else:
                if isPrimes(input-2):
                    caled[input] = input+cal(input-2)
                    return caled[input]
                else:
                    return 0

def isPrimes(input):
    return primes.count(input) == 1 

long = int(input())

cut = []

for i in range(2, int(long/2)+1):
    if isPrimes(i) & isPrimes(long-i):
        cut.append(cal(i)+cal(long-i))

cut.sort()
l = len(cut)
if len(cut) == 0:
    print(0)
else:
    print(long+cut[0])



# cut = [int(input())]
# # def 判斷分割合法？
# for i in primes: # 第一塊的大小
#     for curr_num in cut:
#         if curr_num<i:
#             break

#         if primes.count(curr_num-i) == 1:
#             cut.append(primes, curr_num-i)