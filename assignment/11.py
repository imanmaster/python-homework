b=[]
for i in range(101,1000):
    c=0
    for x in range(1,int(i//2)):
        if i%x==0:
            c+=1
    if c==1:        
        b.append(i)
print(b)