print("Printing Current and Previous number sum in a range (10)")
previous=0
for i in range(0,10):
    sum=previous+i
    print("Current Number ", i ,"Previous Number ", previous , "Sum :" ,sum)
    previous=i
