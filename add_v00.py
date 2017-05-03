lang = 4
while lang > 3 or lang == 0:
	print("Please select language")
	lang = (int(input("English=1, 한국어=2 日本語=3 : ")))
	
	if lang is 1:
		print("Language selected")
	elif lang is 2:
		print("언어가 설정 되었습니다")
	elif lang is 3:
		print("言語が設定されてい")
	else:
		print("Wrong number")
		
	
	
	

	
	

if lang is 2:
	print ("\n\tCALCULATOR 1.2.2 계산기입니다.")
	print ("\n","-"*60)
	print ("다음을 입력해 주세요")

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
		
	a = (int(input("첫번째 숫자:")))
	b = (int(input("두번째 숫자:")))
	def ask():
		c = (int(input("계산법 (더하기=1,빼기=2,곱하기=3,나누기(소수)=4,나누기=5):")))


		if c is 1:
			w = add
			print("답은",w(a,b),"입니다")
		elif c is 2:
			w = sub
			print("답은",w(a,b),"입니다")
		elif c is 3: 
			w = mult
			print("답은",w(a,b),"입니다")
		elif c is 4:
			w = div
			print("답은",w(a,b),"입니다")
		elif c is 5:
			w = divn
			print("답은",w(a,b),"입니다")
		else:
			print("잘못된 숫자입니다")
			ask()


	ask()
elif lang is 1:
	print ("\n\tThis is CALCULATOR 1.1.2")
	print ("\n","-"*60)
	print ("Enter Number")

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
		
	a = (int(input("First number:")))
	b = (int(input("Second number:")))
	def ask():
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
			ask()


	ask()

if lang is 3:
	print ("\n\tCALCULATOR 1.2.2 計算機です.")
	print ("\n","-"*60)
	print ("数字を入力してください")

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
		
	a = (int(input("最初の数字:")))
	b = (int(input("第二の数字:")))
	def ask():
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
			ask()


	ask()
	


