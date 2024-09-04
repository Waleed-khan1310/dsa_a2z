# UPDATING IN AN ARRAY
# In this we simply reasign a new value to the desired index ( valiable_name[desired_index] = new value )
import array
update_arr=array.array('i',[1,2,3,8,5,6,5,9,2])
print('Array of updating: ',end=' ')
for i in update_arr:
    print(i, end=' ')
 
print('\nNew updated array: ',end=' ')
update_arr[3]=4
print(update_arr)

print('2nd updated array: ',end=' ')
update_arr[6]=7
print(update_arr)

print('3rd array: ',end=' ')
update_arr[8]=10
print(update_arr)

''' We dont have 8 in the array thats why i insert it '''
print('After insertion: ',end=' ')
update_arr.insert(7,8)
print(update_arr)