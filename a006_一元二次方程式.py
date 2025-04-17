a, b, c = map(int, input().split())

delta = b**2 - 4*a*c
if delta < 0:
    print("No real root")
elif delta == 0:
    print(f"Two same roots x={int((-b)/(2*a))}")
else:
    x1 = int((-b+delta**0.5)/(2*a))
    x2 = int((-b-delta**0.5)/(2*a))
    if x2 > x1:
        x1, x2 = x2, x1
    print(f"Two different roots x1={x1} , x2={x2}")