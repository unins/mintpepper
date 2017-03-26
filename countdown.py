#!/usr/bin/env python = Py 2.x command, No need.
# -*- coding: utf-8 -*- = Py3.6's Basic encoding is utf-8, so.. No need.

from time import *				# module for using sleep()
n=1
def countdown(n):
	if n < 0:
		sleep(1)				# wait 1 sec.
		print ("fire~!!!")
	else:
		sleep(.5)
		print (n,"~!\n")
		countdown(n-1)			# self call function with modified arguments.
def main():						#	..... it is said as recurssive use.
	countdown(10)

if True: main()					# Run main() ... count 10
