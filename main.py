import sys
from configurations import *
from matrix import *
from getch import *
from os import system
from people import *
from obstacles import *
from generate import *
import time
from gamefunctions import *
from bullets import *

# sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=30, cols=40))
matrix=Matrix()

mando=Mando(matrix)
lives=lives()
bullet=bullets()
dr=Boss()
'''to create magnet'''
mag=Magnet()

'''for creating beams'''
			
horizontal=obstacles()

					
vertical=vertical()

slant=slant()

'''for coins'''
coin=coins()

'''speed boost'''
sb=speedboost()

timeleft=0



''' to go to end '''

# matrix.updateystart(300)
# ystart=matrix.returnystart()
# window=matrix.returnwindow()
# matrix.updateyend(ystart+window-4)

generation(matrix,coin,horizontal,vertical,slant,mag,sb,dr)
system('clear')
temp=''	
for i in range(0,170):
	temp+=' '
print("\033[0;1H")
print(temp)
print("\033[0;1H")	
print(matrix.display(lives,mando,timeleft))

tis=time.time()
tips=time.time()

screenmov=0.3
powertime=10

shstart=-1
flag=0
gamestart=time.time()

q1=5
q2=0
flagnot=0


'''gravity parameters'''
tigs=100
tige=0

'''iceball'''
tics=time.time()
tice=0

while True:

	'''moving dragon'''
	dr.move(matrix,mando)
	tice=time.time()-tics

	ystart=matrix.returnystart()
	if ystart>=310 and tice>0.2:
		dr.throwball(matrix,mando,lives)
		tics=time.time()
	
	'''for getting game time'''
	gamestart1=time.time()
	timeleft=gamestart1-gamestart
	if(timeleft>500):
		system('clear')
		string=colors['Light Green']+"Total Score: "+RESET
		score=matrix.returnscore()
		string+=colors['Light Cyan']+str(score)+RESET
		string+=colors['Red']+"\n\nYou ran out of time"+RESET
		print(string)
		sys.exit()


	'''powerup'''
	tipe=time.time()
	powerup=mando.returnpowerup()
	if(tipe-tips >1 and powerup==1):
		powertime-=1
		tips=tipe
	if powertime<=0:
		mando.updatepowerup(0)

	powerup=mando.returnpowerup()		
	if(powerup==1 and flagnot==0):
		screenmov=0.1
	elif(flagnot==0):
		screenmov=0.3
		powertime=10

	'''lives'''	
	numlives=lives.returnlives()
	if numlives<= 0:
		system('clear')
		string=colors['Light Green']+"Total Score: "+RESET
		score=matrix.returnscore()
		string+=colors['Light Cyan']+str(score)+RESET
		string+=colors['Red']+"\n\nYou got killed :("+RESET
		
		print(string)

		
		sys.exit()

	yend=matrix.returnyend()	
	if 	yend>=490:
		flagnot=1
		screenmov=0

	numvlives=lives.returnvlives()	
	if numvlives<=0:
		system('clear')
		score=matrix.returnscore()
		matrix.updatescore(score+10000)
		string=colors['Light Green']+"Total Score: "+RESET
		score=matrix.returnscore()
		string+=colors['Light Cyan']+str(score)+RESET
		string+=colors['Blue']+"\n\nYou Saved Yoda from Viserion :)"+RESET
		print(string)
		sys.exit()



	'''moving back screen'''	
	tie=time.time()
	if(tie-tis > screenmov and flagnot==0):
		yend=matrix.returnyend()
		matrix.updateyend(yend+1)
		ystart=matrix.returnystart()
		matrix.updateystart(ystart+1)
		tis=tie
	
	'''out of the window'''
	ystart=matrix.returnystart()
	my=mando.returnmy()
	mx=mando.returnmx()
	if my<ystart:
		mando.setpos(matrix,mx,ystart)
	ystart=matrix.returnystart()
	yend=matrix.returnyend()	
	window=matrix.returnwindow()	
	if my>yend:
		mando.setpos(matrix,mx,ystart+window-3)	
	
		
	
	
	input=user_input()



	'''bullets'''
	if input=='s':
		my=mando.returnmy()
		mx=mando.returnmx()
		bullet.setpos(matrix,mando,mx,my)

	powerup=mando.returnpowerup()	
	if(powerup==1):	
		bullet.mov(matrix,lives,dr)
		bullet.mov(matrix,lives,dr)
	else:
		bullet.mov(matrix,lives,dr)


	'''gravity'''
	status=mando.returnstatus()
	if input !='w' and status==1:
		# for k in range(0,num):
		if q1<=q2 and q1>=0:
			checkstatus(mando,matrix,lives)
			q2=0
			q1-=1
		elif q1<0:
			checkstatus(mando,matrix,lives)	

	'''shield'''
	if input==' ' and flag == 0	:
		shstart=time.time()
		mando.updateshield(1)
	
	if shstart!=-1:
		shend=time.time()
		if(shend - shstart > 10):
			shwait=time.time()
			shwaite=time.time()
			mando.updateshieldwait(shwaite-shwait)
			flag=-1
			shstart=-1
			mando.updateshield(0)

	if(flag==-1):
		shwaite=time.time()
		mando.updateshieldwait(shwaite-shwait)
		if(shwaite-shwait > 60):
			flag=0
			mando.updateshieldwait(0)


	shield=mando.returnshield()		
	if	shield == 1:
		shieldgrid=mando.returnshieldgrid()
		mando.updategrid(shieldgrid)
		mx=mando.returnmx()	
		my=mando.returnmy()	
		mando.setpos(matrix,mx,my)
	else:
		grid1=mando.returngrid1()
		mando.updategrid(grid1)
		mx=mando.returnmx()	
		my=mando.returnmy()
		mando.setpos(matrix,mx,my)

	shield=mando.returnshield()
	if(input != 'a' and input!='d' and shield==0):
		mag.attract(matrix,mando,magnets,lives)
		

	
	if input=='w':
		tigs=time.time()
		q1=5		
	if input != '':
		powerup=mando.returnpowerup()
		if(powerup==1):
			mando.movemando(matrix,input,lives)
			mando.movemando(matrix,input,lives)
		else:
			mando.movemando(matrix,input,lives)

	'''printing screen'''			
	temp=''	
	for i in range(0,170):
		temp+=' '
	print("\033[0;1H")
	print(temp)		
	print("\033[0;1H")

	print(matrix.display(lives,mando,timeleft))
	q2+=1
