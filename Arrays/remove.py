# REMOVE method only remove the give word from the array which we 
# gave him
import array as arr 
remarr=arr.array('d',[1.1,2.1,3.1,4.1,5.1,6.1,7.1])
print('\nRemove array list: ',end=' ')
for i in range(0,6):
    print(remarr[i],end=' ')

remarr.remove(3.1)
print('\nHere after removing: ',end=' ')
for i in range(0,5):
    print(remarr[i],end=' ')
    