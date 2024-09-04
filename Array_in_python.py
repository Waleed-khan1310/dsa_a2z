# An array is a collection of items stores at contiguous memory location.
# It make it easier to calculate the position of each elementby simply adding an offset to base value
# It store only same types of elements in it.




import array as arr
a=arr.array('i',[1,2,45678,2346] )
print(a)
for i in range(0,2):
    print(a[i],end=" @ ")    
    
    
    
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
    
    
 
    
# Now accessing elements from th array

import array as arr 
accarr=arr.array('i',[6,8,9,0,5,76])
print('\n''Here your array: ', accarr)   
print('Accessing the fourth number: ', accarr[3])




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




# REMOVE method only remove the give word from the array which we gave him
import array as arr 
remarr=arr.array('d',[1.1,2.1,3.1,4.1,5.1,6.1,7.1])
print('\nRemove array list: ',end=' ')
for i in range(0,6):
    print(remarr[i],end=' ')

remarr.remove(3.1)
print('\nHere after removing: ',end=' ')
for i in range(0,5):
    print(remarr[i],end=' ')
    
    
    

# Slicing of an array
# This can slice an array form anywhere we want by slice operation (sliced_array= array_name[from where:to where])    
import array as arr 
ex_slice=arr.array('i',[1,2,3,4,5,6,7,8,9,10])
print('\nSlicing example:', end=' ')
for i in ex_slice:
    print(i,end=' ')
sliced_array=ex_slice[4:7]
print('\nHere the sliced array: ',end=' ')
print(sliced_array)


''' It see the index from the beginning. It print all the num after 3RD index '''
sliced_array=ex_slice[3:]
print('\nHere the Second sliced array: ',end=' ')
print(sliced_array)


''' It see the index from the end '''
sliced_array=ex_slice[:-3]
print('\nHere the Third sliced array: ',end=' ')
print(sliced_array)


''' It prints all the element in the array '''
sliced_array=ex_slice[:]
print('\nHere the 4th sliced array: ',end=' ')
print(sliced_array)




# Searching elements in array
# We can search element in array by a built in function (index())
import array
newmethod=[1,3,5,7,3,5,9,1]
sea_arr=array.array('i',newmethod)
print(type(sea_arr))


print('Search array ex: ', end=' ')
for i in sea_arr:
    print(i,end=' ')
    

print('\nThe index of first number 5: ',end=' ')
print(sea_arr.index(5))


''' Now we take input form the user '''
print('index of second number:',end=' ')
print(sea_arr.index(9))

index = int(input("Enter index to be searched: "))
print(sea_arr[index])




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




# Counting elements in array
# To count element in python we use count method (variable_name.count(element we want to count))

import array
count_array=array.array('i',[1,2,3,2,1,2,3,1,2,4,5,7,3,2,1])
count=int(input('Enter num of the array: '))
print('Total num is: ', count_array.count(count))




# Reverse element in array
# To reverse element in python we use reverse method (variable_name.reverse())

import array
exrev=array.array('i',[1,2,3,4,5])
print('Orignal Array: ', *exrev)
exrev.reverse()
print('Reversed Array: ', *exrev)




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











































