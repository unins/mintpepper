import time, sys, os
w = ("add","sub","mult","div","divn")

set_LANG = ("Wrong number\n",\
	"Language selected\n",\
	"ธ์ด๊ฐ ค์  ์ต๋n",\
	"่จ่ชใ่จฎใฆใ\n","")
'''
			# ๋ชจ๋  ์๊ฐ 05x5๋ฆฌ์ค์ฑ
			Matrix = [[0]*5 for i in range(5)]

setAsk_KOR = ("\n\tCALCULATOR 1.2.2 ๊ณ์ฐ๊ธฐ์๋ค.",\
	"ค์๋ ฅ์ฃผ์ธ,\
	"์ฒซ๋ฒ์งซ์:",\
	"๋ฒ์งซ์:",\
	"๊ณ์ฐ๋ฒ(ํ๊ธ1,๋นผ๊ธฐ=2,๊ณฑํ๊ธ3,๋๊ธ์)=4,๋๊ธ5):",\
	"ต์",\
	"๋,\
	"๋ชปซ์๋)

'''
def chooLANG():
	global lang; 	lang = 4
	while lang > 3 or lang == 0:
		print("Please select language")
		lang = (int(input("English=1, ๊ตญ2 ฅๆฌ่ช3 : ")))

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
		print (setAsk_KOR[0])			# "\n\tCALCULATOR 1.2.2 ๊ณ์ฐ๊ธฐ์๋ค."
		print ("\n","-"*60)
		print (setAsk_KOR[1])			# "ค์๋ ฅ์ฃผ์ธ

		a = (int(input(setAsk_KOR[2])))	# "์ฒซ๋ฒ์งซ์:",\
		b = (int(input(setAsk_KOR[3])))	# "๋ฒ์งซ์:",\
		c = (int(input(setAsk_KOR[4])))	# ""๊ณ์ฐ๋ฒ(ํ๊ธ1,๋นผ๊ธฐ=2,๊ณฑํ๊ธ3,๋๊ธ์)=4,๋๊ธ5):"\

def run_KOR():
	if c >= 1 and c <=5 :	print(setAsk_KOR[c],add(a,b),setAsk_KOR[c]) # ต์~, ๋
	else:
		print(setAsk_KOR[7])	# ๋ชปซ์๋= setAsk_KOR[7]
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
