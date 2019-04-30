n = int(input())

f1 = 1
f2 = 1

for i in range(3, n + 1):
    new = f1 + f2
    f1 = f2
    f2 = new

print(f2)