import sys
from configurations import *
from os import system
import time





def checkstatus(mando,matrix,lives):
	'''to implement gravity'''
	status=mando.returnstatus()
	mx=mando.returnmx()
	
	if status ==1 and mx<36: 
		'''mando is in air!!,let's drag him down.'''
		dist=3
		mx=mando.returnmx()
		my=mando.returnmy()
		ret=clashcheck(matrix,mando,mx+dist,my)
		if(ret ==1):
			num=numcoins(matrix,mx+dist,my)
			score=matrix.returnscore()
			matrix.updatescore(score+num*50)

		elif ret==2:
			numlives=lives.returnlives()
			numlives-=1
			lives.updatelives(numlives)
			ystart=matrix.returnystart()
			mando.setpos(matrix,6,ystart+2)
		if ret !=2 and ret!=3 and ret!=6:
			mx=mando.returnmx()
			my=mando.returnmy()
			mando.setpos(matrix,mx+dist,my)
		if ret==6:
			my=mando.returnmy()
			mando.setpos(matrix,36,my)	


	else:
		mando.updatestatus(0)

'''to check collisions with obstacles'''
def clashcheck(matrix,mando,x,y):
	flagcoin=-1
	flagbeam=-1
	flagmag=-1
	flagh=0
	flagv=0
	flags=0
	flagpower=0
	flagg=0
	flagice=0

	gridtoin=matrix.returnmatrix()

	for i in range(x,x+4):
		if(flagice==1 or flagcoin==1 or flagbeam ==1 or flagcoin==1 or flagh==1 or flagv==1 or flags==1):
			break
		for j in range(y,y+3):
			if(flagh==1 or flagv==1 or flags==1 or flagice==1):
				break
				

			if(gridtoin[i][j] == coin):
				flagcoin=1
				break
			elif gridtoin[i][j]==iceballcolor:
				shield=mando.returnshield()
				if shield==0:
					flagice=1
					break
						
			elif(gridtoin[i][j]==beam1 or gridtoin[i][j]==beam2):
				shield=mando.returnshield()
				if shield==0:
					flagbeam=1
					break
				else:
					# pass
					'''check horizontal beam'''
					a=[i,j]
					if(flagv!=1 and flags!=1):
						for i1 in range(0,len(beamsh)):
							'''generate all co-ordinates'''
							if flagh==1:
									break

							axh=beamsh[i1][0]
							ayh=beamsh[i1][1]
							for k1 in range(0,2):
								if flagh==1:
									break
								for j1 in range(0,5):
									if(axh+k1==a[0] and ayh+j1 == a[1]):
										flagh=1
										beamsh[i1][0]=1000
										beamsh[i1][1]=2000
										break
						

					'''vertical beam'''				
					if(flagh!=1 and flags!=1):
						for i1 in range(0,len(beamsv)):
							'''generate all co-ordinates'''
							if flagv==1:
									break

							axv=beamsv[i1][0]
							ayv=beamsv[i1][1]
							for k1 in range(0,5):
								if flagv==1:
									break
								for j1 in range(0,2):
									if(axv+k1==a[0] and ayv+j1 == a[1]):
										flagv=1
										beamsv[i1][0]=1000
										beamsv[i1][1]=2000
										break
					

					'''slant beam'''
					if(flagh!=1 and flagv!=1):				
						for i1 in range(0,len(beamss)):
							'''generate all co-ordinates'''
							if flags==1:
									break

							axs=beamss[i1][0]
							ays=beamss[i1][1]
							for k1 in range(0,4):
								if flags==1:
									break
								for j1 in range(0,4):
									if(axs+k1==a[0] and ays+j1 == a[1]):
										flags=1
										beamss[i1][0]=1000
										beamss[i1][1]=2000
										break						
					
			elif(gridtoin[i][j]== magnet):
				flagmag=1
				break		
			elif gridtoin[i][j]==powerup:
				flagpower=1
				axp=i
				ayp=j
				break				
			elif gridtoin[i][j]==ground:
				flagg=1	
	if flagh==1:
		flagh=0
		removeobs(matrix,axh,ayh,2,5)	
		mx=mando.returnmx()
		my=mando.returnmy()
		mando.setpos(matrix,mx,my)
	if flagv==1:
		flagv=0
		mx=mando.returnmx()
		my=mando.returnmy()
		removeobs(matrix,axv,ayv,5,2)
		mx=mando.returnmx()
		my=mando.returnmy()
		mando.setpos(matrix,mx,my)
	if flags==1:
		flags=0
		removeobs(matrix,axs,ays,4,4)
		mx=mando.returnmx()
		my=mando.returnmy()
		mando.setpos(matrix,mx,my)
	if flagpower==1:
		flagpower==0
		mando.updatepowerup(1)
		if(gridtoin[axp][ayp-1]==powerup):
			gridtoin[axp][ayp-1]=' '
		elif(gridtoin[axp][ayp+1]==powerup):
			gridtoin[axp][ayp+1]=' '

	matrix.updatematrix(gridtoin)			

				
	if(flagbeam==1 or flagice==1):
		return 2
	elif(flagcoin==1):
		return 1
	elif(flagmag==1):
		return 3		
	elif(flagpower==1):
		return 5
	elif flagg==1:
		flagg=0
		return 6

	else:
		return 4				

'''to count number of coins collected'''
def numcoins(matrix,x,y):
	flagcoin=0
	gridtoin=matrix.returnmatrix()
	for i in range(x,x+4):
		for j in range(y,y+3):
			if(gridtoin[i][j] == coin):
				flagcoin+=1
	return flagcoin	

'''to remove a specified obstacle'''
def removeobs(matrix,x,y,leng,wid):
	gridtoin=matrix.returnmatrix()
	for i in range(x, x + leng):
		for j in range(y, y +wid):
			gridtoin[i][j] =' '
	matrix.updatematrix(gridtoin)
	