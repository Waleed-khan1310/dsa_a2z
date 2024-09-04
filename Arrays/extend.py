# Extend element from Array
# we can do that by using extend method (vaviable_name.extend([1,2,3,4,342,5,32,22]))

import array
ext_arr=array.array('i',[1,2,3,4,5,6])
print('Array without extention: ',end=' ')

for i in range(0,6):
    print(ext_arr[i],end='')
    
ext_arr.extend([7,8,9,10,11,12,13])
print('\nAfter extending: ',end=' ')

for i in range(0,13):
    print(ext_arr[i], end=' ')