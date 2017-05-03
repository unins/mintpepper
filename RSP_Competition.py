import random, sys

RSP = ['Rock','Scissors','Paper']

resultMssg = [
"You Draw ---> Try it again!!!\n",
"Yeah, You Win~!!",
"Oh no, You Loss;;;;;;;"
]

def RSP_random():       # Pick random and Show
    global mine, yours
    mine = RSP[random.randint(0,2)]
    yours = RSP[random.randint(0,2)]
    print ("mine=",mine,"   <--- vs. --->  yours=",yours)
def RSP_draw():         # Decision for Draw and Run Again.
    if mine == yours:
        print(resultMssg[0])        # draw message
        return True
    else:   return False
def RSP_WorL():
    global judge
    if mine == RSP[0]:              # Rock=0, Scissors=1, Paper=2
        if yours == RSP[1]:
            print(resultMssg[1])     # Win=1 / Loss=2
            judge = 1
        else:
            print(resultMssg[2])
            judge = 0

    elif mine == RSP[1]:
        if yours == RSP[2]:
            print(resultMssg[1])
            judge = 1
        else:
            print(resultMssg[2])
            judge = 0

    elif mine == RSP[2]:
        if yours == RSP[0]:
            print(resultMssg[1])
            judge = 1
        else:
            print(resultMssg[2])
            judge = 0
def RSP_main():
    RSP_random()
    if RSP_draw() == True:
        RSP_main()
    else:
        RSP_WorL()
        #sys.exit("\nProgram's terminated.")

RSP_main()
