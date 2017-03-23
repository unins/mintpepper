#coffee.py

coffee = 10
while True:
    money = int(input("put money: "))
    if money == 300:
        print("give you a cup of coffee.")
        coffee = coffee -1
    elif money > 300:
        print("giving you a cup of coffe with change %d amount." % (money -300))
        coffee = coffee -1
    else:
        print("give money back and refuse to give a cup of coffee.")
        print("remain cup of coffee are %d cup(s)" % coffee)
    if not coffee:
        print("run out of coffee today. sold out.")
        break
