def sum_of_divisors_upto_n(N):
    # Step 1: Create an array to store sum of divisors for each number
    sum_divisors = [0] * (N + 1)

    # Step 2: Use a modified sieve approach to calculate sum of divisors
    for d in range(1, N + 1):
        for multiple in range(d, N + 1, d):
            sum_divisors[multiple] += d

    # Step 3: Sum up all the divisor sums to get the final result
    result = sum(sum_divisors[1:])  # sum from index 1 to N
    return result

# Example usage
N = 3
print(sum_of_divisors_upto_n(N))


def computeGCD(x, y):
    while(y):
       x, y = y, x % y
    return abs(x)
 
a = 60
b = 48
 
# prints 12
print ("The gcd of 60 and 48 is : ",end="")
print (computeGCD(60, 48))

def sumfun(n,sum):
    if n<1:
        print(sum)
        return
    sumfun(n-1,sum+n)
sumfun(3,1)

import array as arr
a=arr.array('i',[1,3,4,5,6])
print(a)
for i in range(1,7):
    print(i)
    
    
    
a=[1,2,3,4,5,6]
for i in range(0,7):
    print('\r','\n',i)
    
    

# creating a list containing elements
# belonging to different data types
sample_list = [1, "Yash", ['a', 'e']]
print(type(sample_list))
print(sample_list)
print('the third element',sample_list[1])

def revarr(a,start,end):
    if start>=end:
        return
    a[start],a[end]=a[end],a[start]
    revarr(a,start+1,end-1)

a=[8,2,3,4,5,'waleed']
print(a)
revarr(a,0,5)
print(a)


def revsin(a,i):
    n=len[a]
    if n>=n/2:
        return
    rev2=a[i,n-i-1]
    i=i+1
a=[1,2,3,4,5,6]
print(a)
print(revsin(a))


def sumOfSeries(n):
        #code here
    total=0
    a=0
    b=0
    while n>0:
        total=n**3+(n-1)**3
        n=n-1
        b=total+a
        a=total
    return b

sumOfSeries(5)


#creating my own class
class waleed:
    pass
human=waleed()
print(type(human))


class student:
    pass
rollNo=student()
section=student()
city=student()
school=student()
pass
print('\n',type(rollNo),type(human),type(city), end='')




def sumOfSeries(n):
    if n==0:
        return 
    return (n * (n + 1) // 2) ** 2
print(sumOfSeries(5))