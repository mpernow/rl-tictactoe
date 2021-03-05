# Short script to examine the q-table

import pickle

f1 = open('q.pkl', 'rb')
q1 = pickle.load(f1)
f1.close()

[print(key,q1[key]) for key in q1 if key != 'n']
print('n: ',q1['n'])


print('Number of states:', len(q1)-1)
