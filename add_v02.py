import time, sys, os
w = ("add","sub","mult","div","divn")

set_LANG = ("Wrong number\n",\
	"Language selected\n",\
	"¸ì–´ê°€ ¤ì • ˜ì—ˆµë‹ˆn",\
	"è¨€èªãŒè¨®š•ã‚Œ¦ã„\n","")
'''
			# ëª¨ë“  ì†Œê°€ 05x5ë¦¬ìŠ¤ì„±
			Matrix = [[0]*5 for i in range(5)]

setAsk_KOR = ("\n\tCALCULATOR 1.2.2 ê³„ì‚°ê¸°ì…ˆë‹¤.",\
	"¤ìŒ…ë ¥ì£¼ì„¸,\
	"ì²«ë²ˆì§«ì:",\
	"ë²ˆì§«ì:",\
	"ê³„ì‚°ë²(”í•˜ê¸1,ë¹¼ê¸°=2,ê³±í•˜ê¸3,˜ëˆ„ê¸Œìˆ˜)=4,˜ëˆ„ê¸5):",\
	"µì",\
	"…ë‹ˆ,\
	"˜ëª»«ì…ë‹ˆ)

'''
def chooLANG():
	global lang; 	lang = 4
	while lang > 3 or lang == 0:
		print("Please select language")
		lang = (int(input("English=1, œêµ­2 ¥æœ¬èª3 : ")))

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
		print (setAsk_KOR[0])			# "\n\tCALCULATOR 1.2.2 ê³„ì‚°ê¸°ì…ˆë‹¤."
		print ("\n","-"*60)
		print (setAsk_KOR[1])			# "¤ìŒ…ë ¥ì£¼ì„¸

		a = (int(input(setAsk_KOR[2])))	# "ì²«ë²ˆì§«ì:",\
		b = (int(input(setAsk_KOR[3])))	# "ë²ˆì§«ì:",\
		c = (int(input(setAsk_KOR[4])))	# ""ê³„ì‚°ë²(”í•˜ê¸1,ë¹¼ê¸°=2,ê³±í•˜ê¸3,˜ëˆ„ê¸Œìˆ˜)=4,˜ëˆ„ê¸5):"\

def run_KOR():
	if c >= 1 and c <=5 :	print(setAsk_KOR[c],add(a,b),setAsk_KOR[c]) # µì~, …ë‹ˆ
	else:
		print(setAsk_KOR[7])	# ˜ëª»«ì…ë‹ˆ= setAsk_KOR[7]
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
