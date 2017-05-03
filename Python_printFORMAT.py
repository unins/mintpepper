# Python TEST Script = 2017.3/1(Wed)
a = bool()      # bool(None=0) = False
b = bool(1)     # bool(1) = True
c = bool(0)     # bool(0) = False

print ("a = ", a, end=" \n" )
favorite =["Apple","Pizza","PASTA","P-P-A-P","Freak","Undertale"]

def listUP_favorites():
    print ("Hello Python World!! \n-----------------------\n\
    - THESE ARE My Favorites!!-\n\
    - You can Enjoy it~!! ^__^\n")
    for i in range(0,6):
        print(end=" \t")
        print(i,end=". ")
        print(favorite[i])
def tailMAKEup():
    print ("\n-----------------------\n\"Hello\" Python World!! ")
    return True
def main():
    listUP_favorites()
    tailMAKEup()
    return False

while True:
    if main() == True:
        a = main()
        print("return=", a )
    else:
        print ("\na = ", a )
        break
