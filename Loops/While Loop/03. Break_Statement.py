# Break statement in While_loop

fnum=0
snum=5

while(fnum<=20):
    if fnum==14 or fnum==16:
        print('The statement is break it is equal to', fnum)
        break
    multiple=snum*fnum
    print(snum, "X" , fnum, '=', multiple)
    fnum+=1