t= [0]*30
a=0
b=1
c=a+b
for i in range(1,30):
    if i == 1:
        t[i]=0
    if i == 2:
        t[i]=1
    else:
        t[i]=c
        a=b
        b=c
        c=a+b
print(t)
    