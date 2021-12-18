# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 21:38:01 2021

@author: T. Katemann
@description: AoC 2021 12 with Pydroid 3
"""

import numpy as np


def fp(r0,pth0,cnt0):
	cnt0+=1
	if bVerb:
		print("lvl:",cnt0,pth0,r0)
		
	if np.mod(len(pth),1000) == 0:
		print("ActLen",len(pth))
		
	for i in r0:
		if i == "end":
			# end reached
			pth1 = pth0[:]
			pth1.append(i)
			if bVerb:
				print("End:",pth0, pth1)
			
			if pth0 in pth:
				pth.remove(pth0)
				
			# append global
			pth.append(pth1)
				
		if i in p.keys():
			# remove ncomplete 
			if pth0 in pth:
				pth.remove(pth0)
				
			pth1=[]
			r1 = p[i]
			if bVerb:
				print(i,r1)
			
			pth1 = pth0[:]
			
			if (i in pth1) and i.islower():
				cntlow = 0
				for it1 in pth1:
					if it1 != "start":
						if it1.islower():
							cntlow=max([cntlow,
								pth1.count(it1)])
				if cntlow <= 1:
					if pth1.count(i) >= numfrst:
						if bVerb:
							print("skip",i,pth1.count(i))
						continue
				else:
					if pth1.count(i) >= 1:
						if bVerb:
							print("skip",i,pth1.count(i))
						continue
				
			pth1.append(i)
			if bVerb:
				print(pth0, pth1)
				
			# append global
			pth.append(pth1)
		
			if cnt0 <= 5000:
				fp(r1,pth1,cnt0)
		
f = open("aoc_2112_data.dat", "r")
data=(f.read().splitlines())
print(data)
db = {}
for it in data:
	a1,a2 = it.split("-")
	if a1 != "end" and a2 != "start":
		if a1 not in db.keys():
			db[a1] = [a2]
		else:
			da = db[a1]
			da.append(a2)
			
	if a2 != "end" and a1 != "start":
		if a2 not in db.keys():
			db[a2] = [a1]
		else:
			da = db[a2]
			da.append(a1)
			
		
print(db)
		
p= db
bVerb=0
numfrst = 2

if 1:
	# main
	cnt1=0
	ks="start"
	pth =[[ks]]
	
	if ks in p.keys():
		r=p[ks]
		print(ks,r)
		fp(r,pth[0],cnt1)
	else:
		print("wrongkey")
	
	print()

	for pth2 in pth:
		print(pth2)
	print("num path:",len(pth))
 