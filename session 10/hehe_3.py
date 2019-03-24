salar_week = [
    {
        'Name' : 'Huy',
        'Role' : 'Waiter',
        'Hours' : 12,
        'Salary' : 0.8,
    },
    {
        'Name' : 'Tung',
        'Role' : 'Cook',
        'Hours' : 24,
        'Salary' : 1.5,
    },
    {
        'Name' : 'M.Duc',
        'Role' : 'Manager',
        'Hours' : 20,
        'Salary' : 2,
    }
]   

p1 = {
    'Name' : 'Don',
    'Role' : 'Waiter',
    'Hours' : 12,
    'Salary' : 0.9,
}

p2 = {
    'Name' : 'H.Duc',
    'Role' : 'Waiter',
    'Hours' : 14,
    'Salary' : 0.7,
}

salar_week.append(p1)
salar_week.append(p2)
print(salar_week)

for i in salar_week:
    print(i['Hours'])

new_person = {
    'Name' : 'Huyen',
    'Role' : 'Waitress',
    'Hours' : 14,
    'Salary' : 1,
}
salar_week[0] = new_person
print(salar_week)

# for j in salar_week:
#     del j['Salary']
# print(salar_week)

for k,l in enumerate(salar_week):
    print(k+1, ':', l)

a = 0
for f in salar_week:
    Money = f['Hours']*f['Salary']
    a = Money + a
    print(Money, '$')
print(a, '$')



