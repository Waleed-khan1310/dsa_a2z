'''
GCD means greatest common factor
'''

x=16
y=12
if x>y:
    small=y
else:
    small=x
for i in range(1,small+1):
    if x%i==0 and y%i==0:
        GCD=i
print(GCD)



# Now let's create GCD function
def gcdfun(a,b):
    if a>b:
        small=b
        print('small number is:',small)
    else:
        small=a
        print('small number is:',small)
    for i in range(1,small+1):
        if a%i==0 and b%i==0:
            GCD=i
    return GCD

print(gcdfun(40,22))