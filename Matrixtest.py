from numpy import full

levensteinTable = full([10, 20],0)

print(levensteinTable)
n = 10
udo = [[i*3, i**2] for i, i in zip(range(0,n), range(0, 1))]
print(udo)