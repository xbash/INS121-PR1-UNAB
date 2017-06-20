a=[1,2,3,4,5]
l=len(a)
for i in range(l):
    n=(i+1)%l
    print(a[i]+a[n], end=" ")
print()
