#!/usr/bin/env python3
import sys

for hi in sys.stdin:
	
	if hi[0]=="#":
		continue
	temp=hi.split("\t")
	hi=" ".join(temp)
	print(hi, end="")
