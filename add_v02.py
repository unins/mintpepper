import time, sys, os
w = ("add","sub","mult","div","divn")

set_LANG = ("Wrong number\n",\
	"Language selected\n",\
	"�어가 �정 �었�니n",\
	"言語が訮��れ�い\n","")
'''
			# 모든 �소가 05x5리스�성
			Matrix = [[0]*5 for i in range(5)]

setAsk_KOR = ("\n\tCALCULATOR 1.2.2 계산기입�다.",\
	"�음�력주세,\
	"첫번짫자:",\
	"�번짫자:",\
	"계산�(�하�1,빼기=2,곱하�3,�누긌수)=4,�누�5):",\
	"��",\
	"�니,\
	"�못�자�니)

'''
def chooLANG():
	global lang; 	lang = 4
	while lang > 3 or lang == 0:
		print("Please select language")
		lang = (int(input("English=1, �국2 �本�3 : ")))

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
		print (setAsk_KOR[0])			# "\n\tCALCULATOR 1.2.2 계산기입�다."
		print ("\n","-"*60)
		print (setAsk_KOR[1])			# "�음�력주세

		a = (int(input(setAsk_KOR[2])))	# "첫번짫자:",\
		b = (int(input(setAsk_KOR[3])))	# "�번짫자:",\
		c = (int(input(setAsk_KOR[4])))	# ""계산�(�하�1,빼기=2,곱하�3,�누긌수)=4,�누�5):"\

def run_KOR():
	if c >= 1 and c <=5 :	print(setAsk_KOR[c],add(a,b),setAsk_KOR[c]) # ��~, �니
	else:
		print(setAsk_KOR[7])	# �못�자�니= setAsk_KOR[7]
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
