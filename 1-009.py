n = int(input())
coins = [ int(x) for x in input().split() ]
k = len(coins)

cache = [ 0 for i in range(n + 1) ]
cache[0] = 1

for i in range(k):
    for j in range(coins[i], n + 1):
        cache[j] += cache[j - coins[i]]

print(cache[n])