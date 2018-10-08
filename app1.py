a = (1,2,3,1,1)
d = {}
count = len(a)/3
for i in a:
    d[i]=d.get(i,0)+1
    if(d[i]>count):
        print(i)

print('-1')
