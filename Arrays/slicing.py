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
