n = int(raw_input())
matrix = []
for i in range(n):
    matrix += [ [ int(x) for x in raw_input().split() ] ]

sum1, sum2 = 0,0
for i in range(n):
    sum1 += matrix[i][i]
    sum2 += matrix[(n-1)-i][i]

print abs(sum1 - sum2)
