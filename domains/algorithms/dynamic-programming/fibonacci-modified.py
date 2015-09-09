nums = map(int, raw_input().split(' '))

a = nums[0]
b = nums[1]
n = nums[2]

result = 0
for i in range(n-2):
    result = b**2 + a
    a = b
    b = result
print b
