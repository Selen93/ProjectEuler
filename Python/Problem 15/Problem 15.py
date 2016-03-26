# how many routes are in a 20x20 lattice grid?

field = []
sum = 0

for i in range(21):
    field.append([1])

for n in range(0,21):
    for i in range(1,21):
        sum = field[n][i-1]
        if n>0: sum += field[n-1][i]
        field[n].append(sum)

print(field)