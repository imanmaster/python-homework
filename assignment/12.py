a=0
b=1
box=[0,1]
for i in range(5):
    c=a+b
    box.append(c)
    a=b
    b=c
print(box)