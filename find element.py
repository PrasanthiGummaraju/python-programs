r,c=[int(v) for v in input().split()]
m=[]
for row in range(r):
    curr=[int(v) for v in input().split()]
    m.append(curr)
x=int(input())
for r in m:
    if x in r:
        print("Yes")
        break
else:
    print("No")
