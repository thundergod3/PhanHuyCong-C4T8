#Part 3

county = ['ST', 'BĐ', 'BTL', 'CG', 'ĐĐ', 'HBT']
population = ['150.300', '247.100', '333.300', '266.800', '420.900', '318.000']
for i in range(len(population)):
    print(county[i] + '-' + population[i])


print(max(population), '-', county[4])
print(min(population), '-', county[0])

sq = ['117.43', '9.224', '43.35', '12.04', '9.96', '10.09']
DS = []
b = []
new_population = []
for k in sq:
    DS.append(float(k))
for j in population:
    new_population.append(float(j))

for z in range(len(DS)):
    a = (new_population[z])/(DS[z])
    b.append(a)

for g in range(len(county)):
    print(county[g], '-', b[g])

print('Mat do dan cu tb =', sum(b)/6)

