def add(a,b):
	re = a + b
	print(a,"+",b,"=",re)
	return re

def sub(a,b):
	re = a - b
	print(a,"-",b,"=",re)
	return re

def mul(a,b):
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

def main():
    add(12,12)
    sub(12,12)
    mul(12,12)
    div(12,12)
    divn(12,12)
    print()
