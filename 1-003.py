n = int(input())

catalan = [0] * (n + 1)
catalan[0] = 1

for i in range(1, n + 1):
    res = 0
    for j in range(0, i):
        res += catalan[j] * catalan[i - j - 1]
    catalan[i] = res

print(catalan[n])