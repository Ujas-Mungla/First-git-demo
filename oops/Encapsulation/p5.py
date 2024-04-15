# protected
class company:
    def __init__(self):
        self._project="NLP"
class emplpoyee(company):
    def __init__(self,name):
        self.name=name
        company.__init__(self)
    def show(self):
        print("Employee Name :",self.name)
        print("Workingg on Project :",self._project)
c=emplpoyee("Jessa")
c.show()
print("Project :",c._project)