N = 7 # Глубина треугольника
collections = []

for i in range(N):
    row = [1] * (i+1)
    for j in range (i+1):
        if j != 0 and j != i:
            row[j] = collections[i-1][j-1] + collections[i-1][j]

    collections.append(row)

for r in collections:
    print(r)