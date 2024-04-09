
def multip_sum(num1, num2):
    product = num1 * num2
    if product <= 1000:
        return product
    else:
        return num1 + num2
result=multip_sum(5,9)
print("Multiplication is :",result)
sum=multip_sum(8,10)
print("Sum  is :",sum)

