# Counting elements in array
# To count element in python we use count method (variable_name.count(element we want to count))

import array
count_array=array.array('i',[1,2,3,2,1,2,3,1,2,4,5,7,3,2,1])
count=int(input('Enter num of the array: '))
print('Total num is: ', count_array.count(count))