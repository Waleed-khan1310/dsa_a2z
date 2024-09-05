# Continue While_loop
# It print all the letter except the one we are giving it

a=0
b= 'ArtificialoIntelligenceq'
while a<len(b):
    if b[a]=='o' or b[a]=='q':
        a+=1
        continue
    print(b[a],end='')
    a+=1
    
    
    
# Continue statement in while_loop

a=0
b=4

while(a<=15):
    if a==11 or a==14:
        print('We skip this iteration.')
        a+=1
        continue
    c=b*a
    print(b, 'X', a, '=',c)
    a+=1