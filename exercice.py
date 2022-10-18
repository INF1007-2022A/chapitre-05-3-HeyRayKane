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
			a=list[j].count("-")
			histogram[len(list[j])-a] += 1
			if len(list[j])-a > b:
				b = len(list[j])-a
	histogramf =histogram[:b+1]
	return histogramf

def format_histogram(histogram):
	ROW_CHAR = "*"
	vertical = ""
	for i in range(1,len(histogram)):
		vertical+= f"\n{i:>2} {ROW_CHAR * histogram[i]}"
	return vertical

def format_horizontal_histogram(histogram):
	BLOCK_CHAR = "|"
	LINE_CHAR = "¯"
	horizontal = LINE_CHAR*(len(histogram))
	for i in range(1,max(histogram)+1):
		liste = [""] * (len(histogram))
		b=0
		a = ""
		for j in histogram[1:]:
			if j>=i:
				liste[b] = BLOCK_CHAR
			else:
				liste[b] = " "
			b += 1
		for k in liste:
			a+=k
		horizontal = a+chr(10)+horizontal
	return horizontal


if __name__ == "__main__":
	spam = "Stop right there criminal scum! shouted the guard confidently."
	eggs = get_word_length_histogram(spam)
	print(eggs, "\n")
	print(format_histogram(eggs), "\n")
	print(format_horizontal_histogram(eggs))
