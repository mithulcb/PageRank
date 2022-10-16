#!/usr/bin/env python3
import sys
temp=-1
sum1=0

for y in sys.stdin:
	
	separate=y.strip().split()
	value_1, value_2 = int(separate[0]),float(separate[1])
	#print(value_1,value_2)
	if temp==-1:
		sum1+=value_2
		temp=value_1
	elif temp==value_1:
		sum1+=value_2
	else:
		if temp!=-1:
			new_rank=0.34 + 0.57*(sum1)
			print("{0},{1}".format(temp,round(new_rank,2)),end='\n')
			#print(temp,round(new_rank,2),sep=",")
		sum1=0
		temp=value_1
		sum1+=value_2
if temp==value_1:
	#sum1+=value_2
	new_rank=0.34 + 0.57*(sum1)
	print("{0},{1}".format(temp,round(new_rank,2)),end='\n')
	#print(temp,round(new_rank,2),sep=",")
