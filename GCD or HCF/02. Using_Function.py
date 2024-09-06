# Now let's create a GCD code by using function
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