t = raw_input()
for index in range(int(t)):
    s = raw_input()
    r = s[::-1]
    isFunny = True
    for i in range(len(s) - 1):
        if (abs(ord(s[i+1]) - ord(s[i]))) != ( abs(ord(r[i+1]) - ord(r[i])) ) :
            isFunny = False
    print 'Funny' if isFunny else 'Not Funny'
