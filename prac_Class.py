# Practice classification

class Thing:
    prop_01 = "existing on Earth."
    pass

# class InAnimate(Thing):
#    pass

class Animate(Thing):          # Lives = plants / anmails
    prop_02 = "evolute on to next generation"
    def alive(self):
        print("breath..........")
    pass

class Animals(Animate):
    def move(self):
        print("I'm moving now!")
    pass

class Mamals(Animals):
    def breathFEED(self):
        print("Choop...choop..")
    pass
# class Ampibious(Animals):
#    pass

# class Humans(Mamals):
#    pass
class Giraffe(Mamals):
    prop_03 = "I have long- long neck about 5 meters"
    def longLEGS(self):
        print("I have way too long legs, so it is inconveninet when I have water")
    pass
# class Flogs(Ampibious):
#    pass

Kevin = Giraffe()   # Kevin = Object
print()
print(Kevin.prop_01)
print(Kevin.prop_02)
print(Kevin.prop_03)
print()

Kevin.alive()   # Animage Class
kevin.move()    # Animals Class
Kevin.longLEGS()

Kay = Giraffe()
print()
print(Kay.prop_01)
print(Kay.prop_02)
print(Kay.prop_03)
print()
