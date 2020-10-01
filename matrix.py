from configurations import *
from getch import *
import sys
from gamefunctions import *

class lives:
	'''contains lives left of dragon and mando'''
	def __init__(self):
		self.__lives=3
		self.__vlives=30
	def returnlives(self):
		return self.__lives 
	def returnvlives(self):
		return self.__vlives
	def updatelives(self,x):
		self.__lives=x 
	def updatevlives(self,x):
		self.__vlives=x	

class Matrix:
	def __init__(self):
		self.__rows=40
		self.__cols=500
		self.__window=150	
		self.__matrix=[]  #contains all elements to display
		self.__x=None
		self.__y=None
		self.__ystart=0
		self.__yend=self.__window-4
		self.__score=0

		for i in range(0,1):
			self.__matrix.append([])
			for j in range(0,self.__cols):
				self.__matrix[i].append('-')

		for i in range(1,self.__rows):
			self.__matrix.append([])
			for j in range(0,self.__cols):
				self.__matrix[i].append(' ')

		for i in range(40,42):
			self.__matrix.append([])
			for j in range(0,self.__cols):
				self.__matrix[i].append(ground)

	'''getterfunctions'''
	def returnrows(self):
		return self.__rows

	def returncols(self):
		return self.__cols

	def returnwindow(self):
		return self.__window

	def returnx(self):
		return self.__x

	def returny(self):
		return self.__y

	def returnystart(self):
		return self.__ystart

	def returnyend(self):
		return self.__yend	

	def returnscore(self):
		return self.__score

	def returnmatrix(self):
		return self.__matrix	
	
	'''setter functions'''
	def updatex(self,x):
		self.__x =x

	def updatey(self,y):
		self.__y=y

	def updateystart(self,x):
		self.__ystart=x

	def updateyend(self,x):
		self.__yend=x	

	def updatescore(self,x):
		self.__score=x

	def updatematrix(self,grid):
		self.__matrix=grid			

	def display(self,lives,mando,timeleft):
		temp=''
		temp+=colors['Light Green']+"Score:"+RESET
		temp+=colors['Cyan']+str(self.__score)+RESET
		temp+='\t\t'
		temp+=colors['Light Green']+"Lives:"+RESET

		numlives=lives.returnlives()

		temp+=colors['Cyan']+str(numlives)+RESET
		temp+='\t\t'

		temp+=colors['Light Green']+"Shield Status: "+RESET
		shield=mando.returnshield()
		shieldwait=mando.returnshieldwait()
		if(shield==1):
			temp+=colors['Cyan']+"Active"+RESET
		elif(shieldwait==0):
			temp+=colors['Cyan']+"Ready"+RESET
		else:
			temp+=colors['Light Green']+"Back in "+RESET		
			temp+=colors['Cyan']+str(int(60-shieldwait))+str("s")+RESET
		temp+='\t\t'

		temp+=colors['Light Green']+"Time left: "+RESET
		temp+=colors['Cyan']+str(int(500-timeleft))+"s" +RESET

		temp+='\t\t'
		temp+=colors['Light Green']+"Speed up Status: "+RESET
		powerup=mando.returnpowerup()
		if(powerup==1):
			temp+=colors['Cyan']+"Active"+RESET
		elif(powerup==0):
			temp+=colors['Cyan']+"Not Active"+RESET
		temp+='\t\t'

		if(self.__ystart>=310):
			temp+=colors['Light Green']+"Viseron Lives:"+RESET
			numvlives=lives.returnvlives()
			temp+=colors['Cyan']+str(numvlives)+RESET
		temp+='\n'	

		for i in range(0,42):
			for j in range(self.__ystart,self.__ystart+self.__window):
				if(j>self.__cols-2):
					break
				temp+=self.__matrix[i][j]
			temp+='\n'
		temp+= colors['Red'] + "Press Q to exit\n" + RESET

		return temp
