import time

class Human:
    secret = "concsciouss has gone, already...."
    def walk(self,where):
        print("I'm walking along the %s"%where)
        pass
    pass

class Programmer(Human):
    secret = "I have No money, No time, No Energy, No reasons to live, full all-nighter\n"
    def __init__(self,name,age):
        self.Name = name
        self.Age = age

    def myNAME(self):
        print("\nMy name is \"%s\", I'm \"%s\" years old, Now... Nice to meet you~!!"%(self.Name,self.Age))
    pass

a = Human()
a.walk("street")
print(a.secret)
print("-"*40)

id_K = Programmer("Kevin",18)
id_K.myNAME()

time.sleep(5)
print("I'm telling you the truth....")

time.sleep(3)
print(id_K.secret)
