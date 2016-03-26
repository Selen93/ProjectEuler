# how many routes are in a 20x20 lattice grid?
# incomplete

row = []
field = []
count = 0
for i in range(20):
    row.append(0)
for i in range(20):
    field.append(row)
field[0][0] = 1


