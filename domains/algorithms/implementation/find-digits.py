t = input()
for i in range(t):
    n = input()
    numStr = str(n)
    count = 0
    for j in numStr:
        if int(j) != 0 and n % int(j) == 0:
            count += 1
    print count
