#Par 4
high_scores = ['40', '46', '54', '73', '84', '96']

# high_scores.sort(reverse = True)
print('High scores :')

# for i,j in enumerate(high_scores):
#     if (i + 1) < 6 :
#         print(i + 1, '.', j)
a = input('new score :')

temp = 0
for i in range(len(high_scores)-1):
    if high_scores[i] < high_scores[i+1]:
        temp = high_scores[i]
        high_scores[i] = high_scores[i+1]
        high_scores[i+1] = temp
                
print(high_scores)
# for i,j in enumerate(high_scores):
#     if (i + 1) < 7:
#         print(i + 1, '.', j)