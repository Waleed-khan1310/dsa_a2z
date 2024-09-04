# POP method only remove the word by getting index of the word we want to remove

import array as arr
a=arr.array('i',[1,2,3,4,5,6])
print('Array list: ',end=' ')
for i in range(0,6):
    print(a[i],end=' ') 
print('\nHere the pop word: ',end='')
print(a.pop(3))
print("Here is the new array:",end=' ')
for i in range(0,5):
    print(a[i],end=' ')