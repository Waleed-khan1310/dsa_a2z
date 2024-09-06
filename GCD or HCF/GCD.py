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