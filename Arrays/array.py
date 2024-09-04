# An array is a collection of items stores at contiguous memory location.
# It make it easier to calculate the position of each elementby simply adding an offset to base value
# It store only same types of elements in it.


import array as arr
a=arr.array('i',[1,2,45678,2346] )
print(a)
for i in range(0,2):
    print(a[i],end=" @ ")    






























