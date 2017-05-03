#coffee.py

coffee = 5

HEADER  = "\n---------------------------------------------"
FOOTER  = "\n----------------- THANK YOU~! ---------------"
FOOTER1 = "\n-------------------- SORRY ------------------"

while True:
    money = int(input("\nStaff: \tMay I have your order, Please?\nI put money: "))

    if money == None:
        break

    elif money == 300:
        print(HEADER, "\nStaff gives you a cup of coffee.",FOOTER)
        coffee = coffee -1

    elif money > 300:
        print(HEADER, "\ngiving you a cup of coffe with change %d amount." % (money -300),FOOTER)
        coffee = coffee -1

    else:
        print(HEADER, "\ngive you money back and refuse to serve coffee.",FOOTER1)
        print("remain cup of coffee are %d cup(s)" % coffee)

    if not coffee:
        print("\nrun out of coffee today. sold out.")
        break
