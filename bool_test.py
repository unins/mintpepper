#
a = bool()      # bool(None=0) = False
b = bool(1)     # bool(1) = True
c = bool(0)     # bool(0) = False

def isCHANGE():
    print("bool(a),default=", a)
    print("bool(b),default=", b)
    print("bool(c),default=", c)
    print()

isCHANGE()

a = bool(1)    # a is changed True
isCHANGE()

a = bool(3)    # Greather than 0 is Frue. (something is INSIDE)
b = bool(4)    # Greather than 0 is Frue. (something is INSIDE)
c = bool(5)    # Greather than 0 is Frue. (something is INSIDE)
isCHANGE()
