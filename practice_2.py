excer=('WaleedzKhanbpipi')
for i in excer:
    if i=='z' or i=='b' or i=='p' or i=='i':
        continue
    print(i,end=' ')
    
for day in range(1, 8):
    distance = 3 + (day - 1) * 0.5
    print(f"Day {day}: Run {distance:.1f} miles")

    
    
    for day in range(3,7):
        distance= 3 +(day - 4)*0.76
        print(f'in {day} days you will cover this {distance:.4f} distance.')
        
        
        
import array
arr = array.array('i', [1, 2, 3, 1, 2, 5])
print("The new created array is : ", end="")
for i in range(0, 6):
    print(arr[i], end=" ")

print("\r")
print("The index of 1st occurrence of 2 is : ", end="")
print(arr.index(2))
print("The index of 1st occurrence of 1 is : ", end="")
print(arr.index(1))





import array as arr 
u=arr.array('i',[5,4,3,2,1])
print('array is: ')
for i in range(0,5):
    print(u[i],end=' ')

print('\n')    
print(u.index(3))
slicarr=u[1:3]
print(slicarr)




import array
y=array.array('i',[9,8,7,6,5,4,3,2,1])
for i in range(0,9):
    print(y[i],end=' ')
print('\n',y.index(4))
    
y[4]=10
print(y)

t=y.count(8)
print(t)

y.reverse()
print(y)

y.extend([11,12,13,14,15])
print(y)


''' 

AB MASLA YE HA K DIFFENCE KIA HA IN DONO MEI SIMPLE 'Y' K SATH OUTPUT LYNY KA OR RANGE DY OUTPUT LYNY KA

'''


a=0
b='waleedkhan'
while a<len(b):
    
    pass
print('the length is: ', a)





d=int(input('the any number to continue and -1 to exist: '))
while d!=-1:
    d=int(input('the any number to continue and -1 to exist: '))
    print(d)
    
    
    
    
    
i=int(input('enter the num less than 70 to run the code: '))
while(i<70):
    j=i
    print(j)
print('Doen with the code')