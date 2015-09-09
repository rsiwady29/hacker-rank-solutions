# Still needs love -> 6.5/20
for i in range(100):
    r = ''
    if (i+1)%3==0:
        r+='Fizz'
    if (i+1)%5==0:
        r+='Buzz'
    print r if r!=''else i+1
