n, k = [int(x) for x in input().split()]

pascal = [ [0] * (n+1) for i in range(n + 1)]
pascal[0][0] = 1
for i in range(1, n + 1):
    pascal[i][0] = 1
    for j in range(1, i + 1):
        pascal[i][j] = pascal[i-1][j] + pascal[i-1][j-1]

print(pascal[n][k])
