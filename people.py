import sys
from configurations import *
from matrix import *
from getch import *
from os import system
from obstacles import *
import time
from gamefunctions import *


class Person:
	def __init__(self):
		self._x=None
		self._y=None
		self._grid=[]
		self._length=4
		self._width=3
	
	def setpos(self,matrix,x,y):
		gridtoin=matrix.returnmatrix()
		gridtoput=self.returnmatrix()
		for i in range(self.__x,self.__x+4):
			for j in range(self.__y,self.__y +3):
				gridtoin[i][j] = ' '
		
		for i in range(x, x + 4):
			for j in range(y, y +3 ):
				gridtoin[i][j] = gridtoput[i-x][j-y]
		matrix.updatematrix(gridtoin)
		self.__x=x
		self.__y=y
		if self.__x<36:
			self.__status=1
		else:
			self.__status=0		
	
class Mando(Person):
	def __init__(self,matrix):
		self.__length=4
		self.__width=3
		self.__x=36
		self.__y=4
		self.__shield=0
		self.__shieldwait=0
		self.__shieldstat=0
		self.__powerup=0

		#status=0 if mando is on ground else 1 
		self.__status=0

		head = colors['Yellow'] + chr(213) + RESET
		mid = colors['Red'] + '|' + RESET
		left = colors['Purple'] + '/' + RESET
		right = colors['Purple'] + '\\' + RESET
		self.__grid= [[' ', head, ' '], [left, mid, right], [' ', mid, ' '], [left, ' ', right]]
		self.__grid1= [[' ', head, ' '], [left, mid, right], [' ', mid, ' '], [left, ' ', right]]

		'''when shield is active'''
		head = colors['Green'] + chr(213) + RESET
		mid = colors['Green'] + '|' + RESET
		left = colors['Green'] + '/' + RESET
		right = colors['Green'] + '\\' + RESET
		self.__shieldgrid= [[' ', head, ' '], [left, mid, right], [' ', mid, ' '], [left, ' ', right]]
		self.setpos(matrix,36,3)

	def setpos(self,matrix,x,y):
		gridtoin=matrix.returnmatrix()
		gridtoput=self.returnmatrix()
		for i in range(self.__x,self.__x+4):
			for j in range(self.__y,self.__y +3):
				gridtoin[i][j] = ' '
		
		for i in range(x, x + 4):
			for j in range(y, y +3 ):
				gridtoin[i][j] = gridtoput[i-x][j-y]
		matrix.updatematrix(gridtoin)
		self.__x=x
		self.__y=y
		if self.__x<36:
			self.__status=1
		else:
			self.__status=0

	'''getter functions'''

	def returnmx(self):
		return self.__x 
	def returnmy(self):
		return self.__y 
	def returnshield(self):
		return self.__shield
	def returnshieldwait(self):
		return self.__shieldwait
	def returnshieldstat(self):
		return self.__shieldstat
	def returnstatus(self):
		return self.__status 
	def returnpowerup(self):
		return self.__powerup
	
	def returnmatrix(self):
		return self.__grid		
	def returngrid1(self):
		return self.__grid1
	def returnshieldgrid(self):
		return self.__shieldgrid
	
	'''setter functions'''
	def updatemx(self,x):
		self.__x=x 
	def updatemy(self,x):
		self.__y==x 
	def updateshield(self,x):
		self.__shield=x
	def updateshieldwait(self,x):
		self.__shieldwait=x
	def updateshieldstat(self,x):
		self.__shieldstat=x
	def updatestatus(self,x):
		self.__status=x 
	def updatepowerup(self,x):
		self.__powerup=x 	
	def updategrid(self,x):
		self.__grid=x 			
		 			 	 		

	def movemando(self,matrix,input,lives):
		'''check clashes'''
		ystart=matrix.returnystart()
		if self.__y<ystart:
			self.setpos(matrix,self.__x,ystart)
		yend=matrix.returnyend()	
		window=matrix.returnwindow()	
		if self.__y>yend:
			self.setpos(matrix,self.__x,ystart+window-3)	
		if self.__y>458:
			numlives=lives.returnlives()
			numlives-=1
			lives.updatelives(numlives)
			ystart=matrix.returnystart()
			self.setpos(matrix,6,ystart+2)

		if self.__x==36:
			self.__status=0
		

		if self.__shield == 1:
			self.__grid=self.__shieldgrid

		else:
			self.__grid=self.__grid1

		if input == 'Q':
			system('clear')
			string=colors['Red']+"Game Stopped!"+RESET
			print(string)
			sys.exit()
		elif input == 'w':
			self.__status=1
			ret=clashcheck(matrix,self,self.__x-1,self.__y)
			if(ret==1):
				num=numcoins(matrix,self.__x-1,self.__y)
				score=matrix.returnscore()
				matrix.updatescore(score+num*50)
			elif(ret==2):
				numlives=lives.returnlives()
				numlives-=1
				lives.updatelives(numlives)
				ystart=matrix.returnystart()
				self.setpos(matrix,6,ystart+2)
			if self.__x>1 and ret!=3:
				self.setpos(matrix,self.__x-1,self.__y)
		elif input== 'a':
			ret=clashcheck(matrix,self,self.__x,self.__y-1)
			if(ret==1):
				num=numcoins(matrix,self.__x,self.__y-1)
				score=matrix.returnscore()
				matrix.updatescore(score+num*50)
			elif(ret==2):
				numlives=lives.returnlives()
				numlives-=1
				lives.updatelives(numlives)
				ystart=matrix.returnystart()
				self.setpos(matrix,6,ystart+2)

			ystart=matrix.returnystart()	
			if self.__y> ystart and ret!=3:
				self.setpos(matrix,self.__x,self.__y-1)
		elif input=='d':
			ret=clashcheck(matrix,self,self.__x,self.__y+1)
			if(ret==1):
				num=numcoins(matrix,self.__x,self.__y+1)
				score=matrix.returnscore()
				matrix.updatescore(score+num*50)

			elif(ret==2):
				numlives=lives.returnlives()
				numlives-=1
				lives.updatelives(numlives)
				ystart=matrix.returnystart()
				self.setpos(matrix,6,ystart+2)
			
			yend=matrix.returnyend()
			if self.__y < yend and ret!=3:
				self.setpos(matrix,self.__x,self.__y+1)


class Boss(Person):
	def __init__(self):
		self.__grid=[]
		self.__x=None
		self.__y=None
		with open ("./dragon.txt") as obj:
			for line in  obj:
				self.__grid.append(line.strip('\n'))

	'''getter functions'''
	def returndx(self):
		return self.__x

	def returndy(self):
		return self.__y

		

	def SetPos(self,matrix,x,y):
		self.__x=x
		self.__y=y
		gridtoin=matrix.returnmatrix()
		for k in range(x, x +len(self.__grid)):
			for p in range(y, y +len(self.__grid[k-x])):
				gridtoin[k][p] = colors['Red']+self.__grid[k-x][p-y]+RESET
		matrix.updatematrix(gridtoin)

	def move(self,matrix,mando):
		mx=mando.returnmx()
		ax=mx-13
		ay=self.__y
		if ax<=1:
			ax=1
		gridtoin=matrix.returnmatrix()
		for k in range(self.__x, self.__x +len(self.__grid)):
			for p in range(self.__y, self.__y +len(self.__grid[k-self.__x])):
				gridtoin[k][p] =' '

		for k in range(ax, ax +len(self.__grid)):
			for p in range(ay, ay +len(self.__grid[k-ax])):
				gridtoin[k][p] = colors['Red']+self.__grid[k-ax][p-ay]+RESET		
		matrix.updatematrix(gridtoin)
		self.__x=ax

	def collision(self,matrix,x,y):
		grid=matrix.returnmatrix()
		if grid[x][y-1]==' ' or grid[x][y-1]=='' or grid[x][y-1]==bullet :
			return 0
		elif grid[x][y-1]==head or  grid[x][y-1]==mid or grid[x][y-1]==left or grid[x][y-1]==right:
			return 2
		elif grid[x][y-1]==magnet:
			return 3
		else:
			return 1	

	def throwball(self,matrix,mando,lives):
		x1=self.__x+5
		x2=self.__x+13
		y=self.__y
		a=[x1,y]
		b=[x2,y]
		iceball.append(a)
		iceball.append(b)
		for i in range(0,2):
			gridtoin=matrix.returnmatrix()
			if(iceball[len(iceball)-1-i][0]<50):
				gridtoin[iceball[len(iceball)-1-i][0]][iceball[len(iceball)-1-i][1]] = iceballcolor
			matrix.updatematrix(gridtoin)	

		gridtoin=matrix.returnmatrix()


		for i in range(0,len(iceball)):

			if iceball[i][0] < 1:
				gridtoin[iceball[i][0]][iceball[i][1]]=' '
				iceball[i][0]=100

			ystart=matrix.returnystart()
			if iceball[i][1]<=ystart and iceball[i][0]<50:
				gridtoin[iceball[i][0]][iceball[i][1]]=' '
				iceball[i][0]=100

			if(iceball[i][0]<50):
				ret=self.collision(matrix,iceball[i][0],iceball[i][1])
				
				if(ret!=1 and ret!=2 and ret!=3):
					iceball[i][1]-=1
					gridtoin[iceball[i][0]][iceball[i][1]+1] =' '
					matrix.updatematrix(gridtoin)
				elif(ret ==1 ):
					gridtoin[iceball[i][0]][iceball[i][1]] =' '
					gridtoin[iceball[i][0]][iceball[i][1]-1] =' '
					iceball[i][0]=100
				elif(ret==2):
					gridtoin[iceball[i][0]][iceball[i][1]] =' '
					gridtoin[iceball[i][0]][iceball[i][1]-1] =' '
					numlives=lives.returnlives()
					numlives-=1
					lives.updatelives(numlives)
					ystart=matrix.returnystart()
					mando.setpos(matrix,6,ystart+2)

					iceball[i][0]=100
				elif(ret==3):
					iceball[i][1]-=1
					ax=magnets[len(magnets)-1][0]
					ay=magnets[len(magnets)-1][1]
					
					removeobs(matrix,ax,ay,4,5)
					gridtoin[iceball[i][0]][iceball[i][1]+1] =' '
					matrix.updatematrix(gridtoin)
				matrix.updatematrix(gridtoin)


					

		matrix.updatematrix(gridtoin)
		for i in range(0,len(iceball)):
			if(iceball[i][0]<50):
				gridtoin[iceball[i][0]][iceball[i][1]] = iceballcolor
				matrix.updatematrix(gridtoin)	
