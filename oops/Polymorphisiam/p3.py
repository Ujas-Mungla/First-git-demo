# Polymorphism with class methods: 
class India():
    def Capital(self):
        print("New Dilhi is the capital of India")
    def Language(self):
        print("Hindi Is the most widely spoken language language of India.")
    def Type(self):
        print("India is a developing country.")
class Usa():
    def Capital(self):
        print("Washington, D.C. is the capital of USA.")
    def Language(self):
        print("English is the primary language of USA.")
    def Type(self):
        print("USA is a developed country.")

i1=India()
u1=Usa()
for country in(i1,u1):
    country.Capital()
    country.Language()
    country.Type()