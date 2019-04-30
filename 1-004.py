n = int(input())

### computing the Bell number using the Stirling number
stirling = []
for i in range(n):
    stirling.append([0] * n)
stirling[0][0] = 1

for i in range(1, n):
    stirling[i][0] = 1
    for j in range(1, i + 1):
        stirling[i][j] = stirling[i-1][j-1] + (j + 1)*stirling[i-1][j]

bell_n = 0
for j in range(n):
    bell_n += stirling[n-1][j]

print(bell_n)

### computing the Bell number using the Bell triangle
bell = []
for i in range(n):
    bell.append([0] * n)
bell[0][0] = 1
for i in range(1, n):
    bell[i][0] = bell[i-1][i-1]
    for j in range(1, i+1):
        bell[i][j] = bell[i][j-1] + bell[i-1][j-1]

print(bell[n-1][n-1])