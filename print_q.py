import pickle

f1 = open('q1.pkl', 'rb')
q1 = pickle.load(f1)
f1.close()

f2 = open('q2.pkl', 'rb')
q2 = pickle.load(f2)
f2.close()

print('Player 1')
print('n: ',q1['n'])
[print(key,q1[key]) for key in q1 if key != 'n']



print('\nPlayer 2')
print('n: ',q2['n'])
[print(key,q2[key]) for key in q2 if key != 'n']
