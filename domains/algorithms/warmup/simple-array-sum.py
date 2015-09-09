def add(x,y):
    return x+y

n = input()
array = map(int, raw_input().split(' '))
print reduce(add, array)
