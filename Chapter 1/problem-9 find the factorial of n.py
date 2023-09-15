n = 10

if n < 0:
    print("Negetive number not allow")

elif n == 0:
    print(1)

else:
    r = 1
    for x in range(1, n + 1):
        r *= x
        print(r)
