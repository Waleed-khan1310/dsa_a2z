#Here we reversing an arrat using recursion
def revarr(a,start,end):
    if start>=end:
        return
    a[start],a[end]=a[end],a[start]
    revarr(a,start+1,end-1)

a=[1,2,3,4,5,6]
print(a)
revarr(a,0,5)
print(a)