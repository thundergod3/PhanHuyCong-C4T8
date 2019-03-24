#Part 5
figure = {
    'Name' : 'Light',
    'Age': 17,
    'Strength' : 8,
    'Defense' : 10,
    'HP' : 100, 
    'Backpack' : 'Shield, Bread Loaf',
    'Gold': 100,
    'Level': 2,
}

figure['Gold'] +=50
figure['Backpack'] = 'FlinStone'
figure['Pocket'] = ['MonsterDex', 'Flashlight']

for x,y in figure.items():
    print(x, ':', y)
skill = [
    {
        'Skill1' : {
        'Name' : 'Tackle',
        'Minimum level' : 1,
        'Damage': 5,
        'Hit rate': 0.3,
        },
    },
    {
        'Skill2' : {
            'Name' : 'Quick attack',
            'Minimum level' : 2,
            'Damage' : 3,
            'Hit rate' : 0.5,
        },
    },
    {
        'Skill3' : {
            'Name' : 'Strong Kick',
            'Minimum level' : 4,
            'Damage' : 7,
            'Hit rate' : 0.2,
        }
    }
]

for i in skill:
    for j,l in i.items():
        print(j, ':')
        for m,n in l.items():
            print(m, ':', n)
        # for index,item in enumerate(l):
        #     print(index + 1, '-', item)

import random 

output = input('what skill do you want to use?').lower()
hit_rate_random = random.random()

if output in 'Skill1':
    if hit_rate_random < skill[0]['Skill1']['Hit rate']:
        print('Your damage is ', skill[0]['Skill1']['Damage'])
    else :
        print('Your skill slip over the target')
elif output in 'Skill2':
    if hit_rate_random < skill[1]['Skill2']['Hit rate']:
        print('Your damage is ', skill[1]['Skill2']['Damage'])
    else :
        print('Your skill slip over the target')    
elif output in 'Skill3':
    print('Your lv is not enough =)')
else : 
    print('Not exist this skill')

        

