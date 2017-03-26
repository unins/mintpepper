#hello
import time, sys, os

w = ("add","sub","mult","div","divn")

set_LANG = ("Wrong number\n",\
	"Language selected\n",\
	"언어가 설정 되었습니다\n",\
	"言語が設定されてい\n","")

setAsk_KOR = ("\n\tCALCULATOR 1.2.2 계산기입니다.",\
	"다음을 입력해 주세요",\
	"첫번째 숫자:",\
	"두번째 숫자:",\
	"계산법 (더하기=1,빼기=2,곱하기=3,나누기(소수)=4,나누기=5):",\
	"답은",\
	"입니다",\
	"잘못된 숫자입니다")

def chooLANG():
	global lang; 	lang = 4

	while lang > 3 or lang == 0:
		print("Please select language")
		lang = (int(input("English=1, 한국어=2 日本語=3 : ")))

		if lang >= 1 and lang <=3 :		print(set_LANG[lang])
		else:
			print(set_LANG[0])		# wrong message = 0
			time.sleep(2)
			os.system('cls')

			chooLANG()

def add(a,b):
	re = a + b
	print(a,"+",b,"=",re)
	return re

def sub(a,b):
	re = a - b
	print(a,"-",b,"=",re)
	return re
def mult(a,b):
	re = a * b
	print(a,"*",b,"=",re)
	return re
def div(a,b):
	re = a / b
	print(a,"/",b,"=",re)
	return re
def divn(a,b):
	re = a // b
	print(a,"//",b,"=",re)
	return re

def ask_KOR():
	global a,b,c
	if lang is 2:
		print (setAsk_KOR[0])			# "\n\tCALCULATOR 1.2.2 계산기입니다."
		print ("\n","-"*60)
		print (setAsk_KOR[1])

		a = (int(input(setAsk_KOR[2])))
		b = (int(input(setAsk_KOR[3])))
		c = (int(input(setAsk_KOR[4])))

def run_KOR():
	if c >= 1 and c <=5 :	print(setAsk_KOR[5],add(a,b),setAsk_KOR[6]) # 답은~, 입니다.
	else:
		print(setAsk_KOR[7])	# 잘못된 숫자입니다 = setAsk_KOR[7]
		ask_KOR()


def main():
	chooLANG()
	if lang == 1:
		ask_ENG()
		run_ENG()

	elif lang == 2:
		ask_KOR()
		run_KOR()

	elif lang == 3:
		ask_JAP()
		run_JAP()

main()

'''
def ask_ENG():
	c = (int(input("Calculation (add=1,sub=2,mult=3,div(float)=4,div=5):")))
	if c is 1:
		w = add
		print("Answer is",w(a,b))
	elif c is 2:
		w = sub
		print("Answer is",w(a,b))
	elif c is 3:
		w = mult
		print("Answer is",w(a,b))
	elif c is 4:
		w = div
		print("Answer is",w(a,b))
	elif c is 5:
		w = divn
		print("Answer is",w(a,b))
	else:
		print("Wrong number")
		askENG()
def run_ENG():
	if lang is 1:
		print ("\n\tThis is CALCULATOR 1.1.2")
		print ("\n","-"*60)
		print ("Enter Number")

		a = (int(input("First number:")))
		b = (int(input("Second number:")))

		askENG()

def run_JAP():
	elif lang is 3:
		print ("\n\tCALCULATOR 1.2.2 計算機です.")
		print ("\n","-"*60)
		print ("数字を入力してください")


		a = (int(input("最初の数字:")))
		b = (int(input("第二の数字:")))

		ask_JAP()
def ask_JAP():
	c = (int(input("計算 (プラス=1,マイナス=2,乗算=3,除算(小数)=4,除算=5):")))


	if c is 1:
		w = add
		print("答えは",w(a,b),"です")
	elif c is 2:
		w = sub
		print("答えは",w(a,b),"です")
	elif c is 3:
		w = mult
		print("答えは",w(a,b),"です")
	elif c is 4:
		w = div
		print("答えは",w(a,b),"です")
	elif c is 5:
		w = divn
		print("答えは",w(a,b),"です")
	else:
		print("誤った数字です")
		ask_JAP()
'''
