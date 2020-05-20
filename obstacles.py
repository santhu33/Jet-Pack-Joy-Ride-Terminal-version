import sys
from configurations import *
from matrix import *
from getch import *
from os import system
from people import *
from gamefunctions import *


class obstacles:
	'''Base definition for any obstacle'''
	
	def __init__(self):
		self._x=None
		self._y=None
		self._ball='O'
		self._grid=[]
		self._stick='' #depends on alignment
		self._length=2
		self._width=5
		
		

	def alignment(self):
		'''default is horizontal'''
		p=colors['Blue']+'%' + RESET
		q=colors['Red'] +'*' +RESET
		self._grid=[[p,q,q,q,p],[p,q,q,q,p]]
		return self._grid

	def SetPos(self,gridtoput,matrix,x,y,leng,wid):
		gridtoin=matrix.returnmatrix()
		for i in range(x, x + leng):
			for j in range(y, y +wid):
				gridtoin[i][j] = gridtoput[i-x][j-y]
		matrix.updatematrix(gridtoin)		

class vertical(obstacles):
	def SetPos(self,gridtoput,matrix,x,y,leng,wid):
		gridtoin=matrix.returnmatrix()
		for i in range(x, x + leng):
			for j in range(y, y +wid):
				gridtoin[i][j] = gridtoput[i-x][j-y]
		matrix.updatematrix(gridtoin)	

	def alignment(self):
		p=colors['Blue']+'%' + RESET
		q=colors['Red'] +'*' +RESET
		self._length=5
		self._width=2
		self._grid=[[p,p],[q,q],[q,q],[q,q],[p,p]]
		return self._grid

class slant(obstacles):
	def SetPos(self,gridtoput,matrix,x,y,leng,wid):
		gridtoin=matrix.returnmatrix()
		for i in range(x, x + leng):
			for j in range(y, y +wid):
				gridtoin[i][j] = gridtoput[i-x][j-y]
		matrix.updatematrix(gridtoin)	

	def alignment(self):
		p=colors['Blue']+'%' + RESET
		q=colors['Red'] +'*' +RESET
		self._length=4
		self._width=4
		self._grid=[[p,' ',' ',' '],[' ',q,' ',' '],[' ',' ',q,' '],[' ',' ',' ',p]]
		return self._grid


class coins:
	def __init__(self):
		self.grid=[]
		self.length=3
		self.width=3
		p=colors['Yellow']+'$'+RESET
		q=' '
		self.grid=[[q,p,q],[p,p,p],[q,p,q]]
	def SetPos(self,gridtoput,matrix,x,y,leng,wid):
		gridtoin=matrix.returnmatrix()
		for i in range(x, x + leng):
			for j in range(y, y +wid):
				gridtoin[i][j] = gridtoput[i-x][j-y]
		matrix.updatematrix(gridtoin)	

	def returngrid(self):
		return self.grid

class speedboost:
	def __init__(self):
		p=colors['Light Cyan']+'>'+RESET
		self.grid=[p,p]

		self.x=None
		self.y=None
		self.length=1
		self.width=1
		self.boost=0
	def setpos(self,matrix,rx,ry):
		gridtoin=matrix.returnmatrix()
		gridtoput=self.grid
		gridtoin[rx][ry] = gridtoput[0]
		gridtoin[rx][ry+1] = gridtoput[1]
		matrix.updatematrix(gridtoin)	
			



class Magnet:
	def __init__(self):
		self.grid=[]
		self.length=4
		self.width=5
		p=colors['Red']+'%'+RESET
		q=' '
		self.x=None
		self.y=None
		self.grid=[[p,p,p,p,p],[p,q,q,q,p],[p,q,q,q,p],[p,q,q,q,p]]

	def SetPos(self,gridtoput,matrix,x,y,leng,wid):
		gridtoin=matrix.returnmatrix()
		for i in range(x, x + leng):
			for j in range(y, y +wid):
				gridtoin[i][j] = gridtoput[i-x][j-y]
		matrix.updatematrix(gridtoin)	
			
	def returngrid(self):
		return self.grid
	def attract(self,matrix,mando,magnets,lives):
		my=mando.returnmy()
		if my < 130:
			num_magnet=0
		elif my <230:
			num_magnet=1
		else:
			num_magnet=2		
		my=mando.returnmy()
		if my+3 >= magnets[num_magnet][1]-20 and my<= magnets[num_magnet][1]+25:
			mx=mando.returnmx()
			my=mando.returnmy()
			
			if my+1 < magnets[num_magnet][1]+2:
				mx=mando.returnmx()
				my=mando.returnmy()
				ret=clashcheck(matrix,mando,mx,my+1)
				if(ret==1):
					mx=mando.returnmx()
					my=mando.returnmy()
					num=numcoins(matrix,mx,my+1)
					score=matrix.returnscore()
					matrix.updatescore(score+num*50)
				elif(ret==2):
					numlives=lives.returnlives()
					numlives-=1
					lives.updatelives(numlives)
					ystart=matrix.returnystart()
					mando.setpos(matrix,6,ystart+2)
				elif ret!=3:
					mx=mando.returnmx()
					my=mando.returnmy()
					mando.setpos(matrix,mx,my+1)	
			elif my>=magnets[num_magnet][1]+2:
				mx=mando.returnmx()
				my=mando.returnmy()
				ret=clashcheck(matrix,mando,mx,my-1)
				if(ret==1):
					mx=mando.returnmx()
					my=mando.returnmy()
					num=numcoins(matrix,mx,my-1)
					score=matrix.returnscore()
					matrix.updatescore(score+num*50)
				elif(ret==2):
					numlives=lives.returnlives()
					numlives-=1
					lives.updatelives(numlives)
					ystart=matrix.returnystart()
					mando.setpos(matrix,6,ystart+2)
				elif ret!=3:
					mx=mando.returnmx()
					my=mando.returnmy()
					mando.setpos(matrix,mx,my-1)	

				



			

		


