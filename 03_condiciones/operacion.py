"""b="7100"
c=int(b)
d=b[c%len(b)]
print(d+d)
"""
m=5
y=""
for i in range(5):
    m=m-1
    if i%4!=0:
        x="o"*m
        y=y+"o"
        print(x+"x"+y)
