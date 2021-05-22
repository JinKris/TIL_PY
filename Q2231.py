n=str(input())
m=int(n)
k=len(n)
a=m-k*9
if(a<0) :
    a+=9

for i in range(k*9) :
    b=a
    for j in str(a) :
        b+=int(j)
    if(b==m) :
        break
    a+=1

if(m<10) :
    print(m//2 if m%2==0 else 0)
else :
    print(a if a!=m else 0)


