# Continure in Python for_loop
''' It print all the letters except the give letter (l,5,e) '''

eg=(1,3,5,2,'waleed')
for i in eg:
    if i=='l'or i==5 or i=='e':
        continue
    print('current letter is: ',i)    
    
''' Another example '''

eg=('waleed')
for i in eg:
    if i=='l' or i=='e':
        continue
    print('current letter is: ',i)    