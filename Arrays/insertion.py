# Inserting in Array, we can add in array everywhere like START,MIDDLE,LAST by using  insert() and append() function    

import array as arr
exarr=arr.array('i',[1,2,3,5,6])
print('\n'"Array before insertion: ",end=" ")
for i in range(0,5):
    print(exarr[i],end=" ")
exarr.insert(3,4)
print('\n'"Array after insertion: ",end=" ")
for i in exarr:
    print(i,end=' ')
    
    
exarr2=arr.array('d',[1.4,5.5,7687.33,2.876,78.74534,46])
print('\n'"Here another example before insertion: ",end=' ')
for i in range(0,6):
    print(exarr2[i],end=' ')
exarr2.insert(4,77.73)
print('\n''Here is after insertion: ',end=' ')
for i in exarr2:
    print(i, end=' ')