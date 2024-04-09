num1=0
num2=1
print("Fibonacci Series :")
for sq in range(10):
    print(num1 ,end=" ")
    num3=num1+num2
    num1=num2
    num2=num3

# fib=lambda n:n if n<=1 else fib(n-1 )+fib(n-2) 