#!/usr/bin/env python3
import sys


temp_key=0
path_to_file=(sys.argv[1])
f=open(path_to_file,"w")
cnt=0

for y in sys.stdin:
	separate=y.strip().split()
	value_1, value_2 = separate[0],separate[1]
	if cnt==0:
		print("{0}\t[{1}".format(value_1,value_2),end='')
		cnt+=1
		temp_key=value_1
	elif temp_key==value_1:
		print(", {0}".format(value_2),end='')
	else:
		if temp_key!=0:
			print("]")
		print("{0}\t[{1}".format(value_1,value_2),end='')
		file_rank=temp_key+",1\n"
		f.write(file_rank)
		temp_key=value_1
if temp_key==value_1:
	file_rank=temp_key+",1\n"
	print("]")
	f.write(file_rank)
f.close()
