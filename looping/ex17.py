n=5
sum=0
start=2
for i in range(0,n):
    print(start,end="+")
    sum+=start
    start=start*10+2
print("Sum of ",sum)    