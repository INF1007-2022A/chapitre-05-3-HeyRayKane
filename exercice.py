#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

def get_num_letters(text):
	count = 0
	for i in text:
		if i.isalnum():
			count+=1
	return count

def get_word_length_histogram(text):
	a = ""
	for i in text:
		if i.isalnum() or i.isspace() or i == "-":
			a+=i
		else:
			a+= " "
	list=a.split()
	histogram=[0]*(get_num_letters(text))
	b=0
	for j in range(len(list)):
		if "-" not in list[j]:
			histogram[len(list[j])] +=1
			if len(list[j]) > b:
				b = len(list[j])
		elif "-" in list[j]:
			histogram[len(list[j])-1] += 1
			if len(list[j])-1 > b:
				b = len(list[j])-1
	histogramf =histogram[:b+1]
	return histogramf
"""
def format_histogram(histogram):
	ROW_CHAR = "*"

	return ""

def format_horizontal_histogram(histogram):
	BLOCK_CHAR = "|"
	LINE_CHAR = "¯"

	return ""
"""

if __name__ == "__main__":
	spam = "Stop right there criminal scum! shouted the guard confidently."
	eggs = get_word_length_histogram(spam)
	print(eggs, "\n")
	#print(format_histogram(eggs), "\n")
	#print(format_horizontal_histogram(eggs))
