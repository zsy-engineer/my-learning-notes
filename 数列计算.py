a1=1
a2=1
n=int(input())
if n==1:
    total=1
    print(a1)
    print(total)
elif n==2:
    total=2
    print(a1)
    print(a2)
    print(total)
else:
    print(a1)
    print(a2)
    total=2
    for i in range(3,n+1):
        a3=a1+a2
        print(a3)
        a1=a2
        a2=a3
        total+=a3
    print(total)
    

