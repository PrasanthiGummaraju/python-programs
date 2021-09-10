n=int(input())
l=len(str(n))
t=n
s=0
while(n!=0):
    r=n%10
    s=s+r**l
    n=n//10
if (t==s):
    print("armstrong")
else:
    print("not armstrong")
    
