question = [
    {
        'question' : '2*3',
        
        'answer' : {
            'a' : '1',
            'b' : '3',
            'c' : '4',
            'd' : '6',
        },
        'answerRight': 'd'
    },
    {
        'question' : 'How many leg an octopus has ?',

        'answer' : {
            'a' : 'One leg',
            'b' : 'Two legs',
            'c' : 'Four legs',
            'd' : 'Eight legs',
        },
         'answerRight': 'b'
    },
    {
        'question' : '1+2 = ?',

        'answer' : {
            'a' : '1',
            'b' : '2',
            'c' : '3',
            'd' : '4',
        },
         'answerRight': 'c'
    }
]

right_score = 0

for i in question:
    print(i['question'])
    for k,v in i['answer'].items():
        print(k, ':', v)

    answer_output = input('Your answer ?').lower()
    if answer_output == i['answerRight'] :
        print('Love you =)')
        right_score += 1

    else:
        print('Hate you !')

percent_right_score = ((right_score)/len(question)) * 100

print('your correct answer', '=', right_score)
print(percent_right_score, '%')