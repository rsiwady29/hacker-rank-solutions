def validHotels(hotels, price, facilities):
    valid = [];
    for i in range(len (hotels)):
        if  hotels[i][1] <= price:
            contained = True
            for j in range( len(facilities) ):
                if facilities[j] not in hotels[i]:
                    contained = False
            if contained:
                valid += [ (len(hotels[i][2:]), hotels[i][1] , hotels[i][0] ) ]
    return sorted(valid, key=lambda tup:  tup[0], reverse = True)

n = input()
hotels = []
for i in range(n):
    hotels += [ raw_input().split(' ') ]
    hotels[i][0] = int(hotels[i][0])
    hotels[i][1] = int(hotels[i][1])

m = input()
testcases = []
for i in range(m):
    testcases += [ raw_input().split(' ') ]
    testcases[i][0] = int(testcases[i][0])
    passing = validHotels(hotels, testcases[i][0], testcases[i][1:])
    print ' '.join( str(x[2]) for x in passing)
