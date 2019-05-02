n = int(input())

array = [ 0 for i in range(n + 1) ]
array[0] = 1
array[1] = 1

for i in range(2, n + 1):
    array[i] = array[i-2] + array[i - 1]

print(array[n])