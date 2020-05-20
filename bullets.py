from configurations import *
from matrix import *
from obstacles import *
from people import *
import sys
from gamefunctions import *


class bullets:
	def __init__(self):
		p=colors['Gray']+'-'+RESET
		self.__grid=[p]
		self.__bullets=0
	def setpos(self,matrix,mando,x,y):
		rx=x
		ry=y+2
		a=[rx,ry]
		bulletpos.append(a)
		p=colors['Gray']+'-'+RESET
		gridtoin=matrix.returnmatrix()
		gridtoin[bulletpos[len(bulletpos)-1][0]][bulletpos[len(bulletpos)-1][1]] = p
		matrix.updatematrix(gridtoin)
	def mov(self,matrix,lives,dr):
		gridtoin=matrix.returnmatrix()
		for i in range(0,len(bulletpos)):
			if bulletpos[i][0] < 1:
				gridtoin[bulletpos[i][0]][bulletpos[i][1]]=' '
				bulletpos[i][0]=100
			
			yend=matrix.returnyend()	
			if bulletpos[i][1]>=yend and bulletpos[i][0]<50:
				gridtoin[bulletpos[i][0]][bulletpos[i][1]]=' '
				bulletpos[i][0]=100	
			if(bulletpos[i][0]<50):
				'''  write'''
				ret=self.checkfiring(matrix,bulletpos[i][0],bulletpos[i][1]+1,dr)
				if(ret==6):
					numvlives=lives.returnvlives()
					numvlives-=1
					lives.updatevlives(numvlives)
					gridtoin[bulletpos[i][0]][bulletpos[i][1]] =' '
					bulletpos[i][0]=100


				elif(ret!=1 and ret!=2 and ret!=3 and ret!=4 and ret!=5 and ret!=6 and ret!=7):
					bulletpos[i][1]+=1
					
					gridtoin[bulletpos[i][0]][bulletpos[i][1]-1] =' '
					
				elif(ret ==1 or ret ==2 or ret ==3 or ret==4 or ret ==5 ):
					gridtoin[bulletpos[i][0]][bulletpos[i][1]] =' '
					gridtoin[bulletpos[i][0]][bulletpos[i][1]+1] =' '
					bulletpos[i][0]=100
				elif(ret == 7):
					gridtoin[bulletpos[i][0]][bulletpos[i][1]] =' '
					bulletpos[i][0]=100

						

		for i in range(0,len(bulletpos)):
			if(bulletpos[i][0]<50):
				p=colors['Gray']+'-'+RESET
				gridtoin[bulletpos[i][0]][bulletpos[i][1]] = p
		
		matrix.updatematrix(gridtoin)
		

	def checkfiring(self,matrix,x,y,dr):
		self.__grid=matrix.returnmatrix()
		flagh=-1
		flagv=-1
		flags=-1
		flagmag=-1
		flagcoin=-1
		a=[x,y]

		yend=matrix.returnyend()
		if(self.__grid[x][y]==iceballcolor or y>yend-1):
			return 7

		dy=dr.returndy()
		dx=dr.returndx()

		if(dy<=y):
			if(x>=dx and x<=dx+18):
				return 6	

		if(self.__grid[x][y]==beam1 or self.__grid[x][y]==beam2):
			
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
					
		elif(self.__grid[x][y]== magnet):
			for i1 in range(0,len(magnets)):
					'''generate all co-ordinates'''
					if flagmag==1:
							break

					axm=magnets[i1][0]
					aym=magnets[i1][1]
					for k1 in range(0,4):
						if flagmag==1:
							break
						for j1 in range(0,5):
							if(axm+k1==a[0] and aym+j1 == a[1]):
								flagmag=1
								magnets[i1][0]=1000
								magnets[i1][1]=2000
								break
		elif(self.__grid[x][y]==coin):
			flagcoin=1		
								
		if flagh==1:
			flagh=0
			removeobs(matrix,axh,ayh,2,5)
			return 1
		if flagv==1:
			flagv=0
			removeobs(matrix,axv,ayv,5,2)
			return 2
		if flags==1:
			flags=0
			removeobs(matrix,axs,ays,4,4)
			return 3
		if flagmag==1:
			flagmag=0
			removeobs(matrix,axm,aym,4,5)	
			return 4
		if flagcoin==1:
			flagcoin=0
			return 5




		

