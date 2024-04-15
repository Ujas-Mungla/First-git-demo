class Student:
    def __init__(self,name,marks) :
        self.name=name
        self.marks=marks   
    def get_average(self):
        sum=0
        for value in self.marks:
            sum=sum+value
        print(f"Hi",self.name,"Your Average Score Is :" ,sum/3)  
s1=Student("Rohan",[99,98,97])
s1.get_average()