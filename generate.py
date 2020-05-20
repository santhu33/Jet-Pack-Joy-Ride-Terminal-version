from configurations import *
import sys
from matrix import *
from people import *
import random
from gamefunctions import *




def generation(matrix,coin,horizontal,vertical,slant,mag,sb,dragon):
	coinm=coin.returngrid()
	horizontalm=horizontal.alignment()
	verticalm=vertical.alignment()
	slantm=slant.alignment()


	i=0
	j=0
	prevy=0
	while i<3:
		j=0
		while j<3:
			ry=random.randint(20,50)
			ry+=prevy
			prevy=ry
			if(ry>450):
				i=20
				break
			rx=random.randint(8,35)
			coin.SetPos(coinm,matrix,rx,ry,3,3)
			a=[rx,ry]
			coinpos.append(a)
			j+=1	 
		i+=1

	i=0
	j=0

	'''beams'''
	prevy=0
	while i<8:
		j=0
		while j<2:
			decide=random.randint(0,100)%3
			if decide == 0:
				
				ry=random.randint(15,50)
				rx=random.randint(14,38)
				ry+=prevy
				if ry>310:
					i=20
					break
				a=[rx,ry]
				prevy=ry
				temp=[]
				horizontal.SetPos(horizontalm,matrix,rx,ry,2,5)
				beamsh.append(a)
			elif decide == 1:
				ry=random.randint(15,50)
				rx=random.randint(9,30)
				ry+=prevy
				if ry>310:
					i=20
					break
				a=[rx,ry]
				prevy=ry
				vertical.SetPos(verticalm,matrix,rx,ry,5,2)
				beamsv.append(a)
			elif decide ==2:
				ry=random.randint(15,50)
				ry+=prevy
				if ry>310:
					i=20
					break
				rx=random.randint(16,31)
				prevy=ry
				a=[rx,ry]
				slant.SetPos(slantm,matrix,rx,ry,4,4)
				beamss.append(a)	

			j+=1	 
		i+=1


	rx=random.randint(3,4)
	ry=random.randint(50,100)
	a=[rx,ry]
	mag.y=ry
	mag.x=rx
	mag.SetPos(mag.grid,matrix,rx,ry,4,5)
	magnets.append(a)

	i=1
	while i < 3:
		rx=random.randint(3,4)
		ry=random.randint(i*100+30+i*50,i*200+(1-i)*60)
		if ry>400:
			ry=random.randint(350,400)
		i+=1
		a=[rx,ry]
		mag.x=rx
		mag.y=ry
		mag.SetPos(mag.grid,matrix,rx,ry,4,5)
		magnets.append(a)

	i=0
	j=0

	rx=random.randint(4,25)
	ry=random.randint(10,150)
	prevy=150
	a=[rx,ry]
	sb.y=ry
	sb.x=rx
	sb.setpos(matrix,rx,ry)
	for i in range(0,2):
			boost.append(a)
	i=0		

	while i< 4:
		rx=random.randint(11,38)

		ry=random.randint(40,80)
		ry+=prevy
		if(ry>340):
			i=20
			break
		a=[rx,ry]
		prevy=ry
		sb.y=ry
		sb.x=rx
		sb.setpos(matrix,rx,ry)

		for j in range(0,2):
			boost.append(a)
		i+=1


	dragon.SetPos(matrix,23,460)	








