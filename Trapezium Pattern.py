n = int(input())
a = 1
b = n * n + 1
for i in range(n, 0,-1):
    for h in range(n-i):
        print("--", end="")
    for j in range(i):
        print(a, end="*")
        a += 1
    for k in range(i-1):
        print(b, end="*")
        b += 1
    print(b)
    b = b-2 * (i-1)
