class Book:
    def subjectName(self):
        print("This is a generic Book")
    def aboutMe(self):
        print("Hi I'm From book")
class Physics(Book):
    def subjectName(self):
        print("This is a physics Book")
class Chemistry(Book):
    def subjectName(self):
        print("This is a chemistry book")
class Science(Physics,Chemistry):
    def subjectName(self):
        print("This is a science Book")

sc=Science()
sc.subjectName()
sc.aboutMe()
