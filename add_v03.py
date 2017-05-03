import time, sys, os                    # import module
from add_calc import *                  # add all def from add_calc.py

goStop = True
again = False

def waitAndClear(sec):
	time.sleep(sec)
	os.system('cls')

def variableSet():
    global set_LANG, setAsk_LANG        # if use outside, declair global

    # set_LANG = [3] : Kor, Eng, Jap
    set_LANG = (
        "한국어로 언어가 설정 되었습니다\n",
    	"English is set as default Language\n",
    	"日本語での言語が設定されました\n",
        "تم تعيين اللغة اليابانية.\n",
        )

    # setAsk_KOR[9][3] = metrix for Kor, Eng, Jap
    setAsk_LANG = [
    	["\n\tCALCULATOR 1.2.2 계산기입니다.",\
    		"\n\tThis is CALCULATOR 1.1.2",\
    		"\n\tCALCULATOR 1.2.2 計算機です."],\
    	["다음을 입력해 주세요",	"Enter Number",	"数字を入力してください"],\
    	["첫번째 숫자:",		"First number:", 	"最初の数字:"],\
    	["두번째 숫자:", 	"Second number",	"第二の数字:"],\
    	["계산법 (더하기=1,빼기=2,곱하기=3,나누기(소수)=4,나누기=5):",\
    		"Calculation (add=1,sub=2,mult=3,div(float)=4,div=5):",\
    		"計算 (プラス=1,マイナス=2,乗算=3,除算(小数)=4,除算=5):"],\
    	["답은",	"Answer is", "答えは"],\
    	["입니다", " ...", "です"],\
    	["잘못된 숫자를 입력하셨습니다. 다시 입력해 주십시요~!",\
            "INVAILID NUMBER WAS PUNCHED IN, PLEASE TRY IT AGAIN~!",\
             "誤った数字を入力しました。再度入力してください〜！"],\
    	["다시 한번, 더 실행 하시겠습니까?(예=1/아니오=2)",\
            "Do you want to calculate something again?(yes=1/no=2)",\
             "もう一度、より実行しますか？ (はい=1/いいえ=2)"],\
    	["종료합니다. 안녕히가십시요..",\
            "BYE BYE, SEE YOU SOON..",\
             "終了します。さようならはなさい.."],\
    ]

def selectLanguage():
    global lang

    print("Please select language")
    lang = (int(input("1=한국어, 2=English, 3=日本語 : ")))

    if lang >= 1 and lang <=3 :
        waitAndClear(0.5)            # wait seconds and clear screen
        print(set_LANG[lang-1])

    else:
        print("\n\n","*"*70,"\n\t",setAsk_LANG[7][1],"\n","*"*70)
        waitAndClear(4)
        return selectLanguage()

def inputNumbers():
    global a,b,c

    print (setAsk_LANG[0][lang-1])			# \n\tCALCULATOR 1.2.2 계산기입니다.
    print ("\n"+"-"*60)
    print (setAsk_LANG[1][lang-1])			# 다음을 입력해 주세요

    a = (int(input(setAsk_LANG[2][lang-1])))	# 첫번째 숫자:
    b = (int(input(setAsk_LANG[3][lang-1])))	# 두번째 숫자:
    c = (int(input(setAsk_LANG[4][lang-1])))	# 계산법 (더하기=1,빼기=2,곱하기=3,나누기(소수)=4,나누기=5)

    if c >= 6 or c <= 0:
        print("\n\n","*"*70,"\n\t",setAsk_LANG[7][lang-1],"\n","*"*70)
        waitAndClear(4)
        return inputNumbers()

def calculate():
    global results

    print("\n")
    if c == 1:
        results = add(a,b)
        return results
    elif c == 2:
        results = sub(a,b)
        return results
    elif c == 3:
        results = mul(a,b)
        return results
    elif c == 4:
        results = div(a,b)
        return results
    elif c == 5:
        results = divn(a,b)
        return results

def displayResult():
    print(setAsk_LANG[5][lang-1],end=" ")   # "답은"
    print(results,end=" ")
    print(setAsk_LANG[6][lang-1])           # "입니다"
    print("\n\n")

def askOnceAgain():
    global goStop, again

    d = int(input(setAsk_LANG[8][lang-1]))  # "다시 한번, 더 실행 하시겠습니까?"

    if d == 1:              # GO!
        goStop = True
        again = True
        waitAndClear(0.5)
        return goStop
    elif d == 2:              # STOP!
        waitAndClear(1)
        print("*"*50,"\n\t",setAsk_LANG[9][lang-1],"\n"+"*"*50)
        waitAndClear(4)
        sys.exit()
    else:
        print("\n\n","*"*70,"\n\t",setAsk_LANG[7][lang-1],"\n","*"*70)
        waitAndClear(4)
        return askOnceAgain()

def main():
    if again == False:
        variableSet()
        selectLanguage()

    inputNumbers()
    calculate()
    displayResult()
    askOnceAgain()

while goStop == True:
    main()
