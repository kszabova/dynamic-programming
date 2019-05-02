A = []
while True:
    x = input()
    if x:
        A.append([ int(i) for i in x.split()])
    else:
        break
n = len(A[0])
m = len(A)

aux = [ A[i][n-1] for i in range(m) ]
for col in range(n - 2, -1, -1):
    new_aux = []
    new_aux.append(aux[1] + A[0][col])
    for row in range(1, m - 1):
        new_aux.append(max(aux[row - 1] + A[row][col],
                       aux[row + 1] + A[row][col]))
    new_aux.append(aux[m - 2] + A[m-1][col])
    aux = new_aux

print(max(aux))