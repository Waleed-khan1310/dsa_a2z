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