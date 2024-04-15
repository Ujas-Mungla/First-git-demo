# Multiple Inheritance
class Akhilesh:
    Back="Oracle DB & Java"
    def Backend(self):
        print("Backend Task Impliment Using :",self.Back)
class Ankush:
    front="Html,Css,JS"
    def Frontend(self):
        print("Frontend Task Impliment Using :",self.front)    

class TeamLEad(Akhilesh,Ankush):
    def Show(self):
        print("DYnamic WEbsite Created......")

t1=TeamLEad()
t1.Backend()
t1.Frontend()
t1.Show()