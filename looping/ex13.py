num=int(input("Enter The Number :"))
fact=1
i=1
while(i<=num):
    fact=fact*i
    i+=1
print("Factorial Number is :",fact)

# fact=lambda n:[1,0] [n > 1] or fact(n-1*n)