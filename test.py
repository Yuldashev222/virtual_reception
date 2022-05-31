n = 10

j = 0
k = n
for i in range(n):
    if k >= 0:
        print(" " * j, "\\\\", " " * k, "//")
        k -= 2
        j += 1
    else:
        print(" " * j, "//", " " * k, "\\\\")
        j -= 1
        k += 2
