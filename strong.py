n=int(input())
t=n
s=0
while(n):
    i=1
    f=1
    r=n%10
    while(i<=r):
        f=f*i
        i=i+1
    s=s+f
    n=n//10
if(s==t):
    print("strong")
else:
    print("no")
