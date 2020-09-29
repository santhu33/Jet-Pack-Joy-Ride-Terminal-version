# Guide

## Requirements:
    python3

## Controls:
    
    a - Move Left
    d - Move Right
    w - Move Up
    s - Shoot Bullets

## Instructions:

    Run python3 main.py to start the game

# OOPS

## Inheritance:

* Different types of obstacles are inherited from base obstacle class.
* Mandalorian and Boss enemy are inherited from person class.

## Polymorphism:

* The alignment function is overrided in obstacle classes.

## Encapsulation:
* Used class and object based approach for all the functionality  implemented.

## Abstraction:

* Some functional details are abstracted(hidden) using methods like to move mandalorian you need not know the implementation,you can just use as mando.mov where mando is instance of mandalorian class.     

## Features:

* Press Space to get enable shield. It lasts for 10s and takes 60s more to re-enable it. 

* Collect '>>' while playing to increase the fastness of game.

* Randomly a Magnet appears and attracts towards it in X-Direction.

* Gravity like effect will be present in the game i.e if you are in air then due to the acceleration towards ground,your downward velocity keeps on increasing untill you hit the ground or try to move up.

* Colors are added to objects to make it colorful.

* Viserion will adjust according to mandalorian position in y-axis direction.

* Mandalorian loses live when he touches fire beams provided that his shield is not active.


## More Information Regarding Game:

* All attributes of objects are Only Private
and Protected variables. 
* Game is implemented following OOPS following all properties of oops like inheritance,abstarction,encapsulation and polymorphism.

* Mandalorian cannnot go out of the window and screen keeps moving till Viserion enters.

* Mandalorian cannot go out of the window but he shows slight deviation towards out of the window indicating your in magnetic range of some magnet and after he becomes normal.

* Collect coins to increase your score and kill Viseron to get more score and also to save Yoda

* If a bullet is fired at beam or magnet whole object gets disappeared.

* If a bullet touches coin then that coin disappeares,reason to implement is that you should not misuse bullets if you want high score though you have infinite bullets.

* You have three lives and Viseron have 50 lives.

* Viserion iceballs are much stronger than mandalorian bullets,So if they strike each other mandalorian bullets disappear i.e bullets cannot penetrate through Viserion iceballs.

* It may seem that if you continuosly shoot bullets at a place you are able to stop the iceballs but u cannot stop those comming towards you,they will forward towards you suddenly.You should just try to find gaps between ice balls.  

* If Mandalorian touches Viserion his life decreases though he has shield.

* When Mandalorian touches beams when he has shield,beams disappear and also magnetic effect won't be there when he has shield.       And also when bullet touches obstacles such as fire beam or magnet they disappear completely. 

* Press Q to exit from game.

# Tip to defeat Viserion:
    Don't shoot randomly somewhere at the iceballs while you are in battle with Viserion,Concentrate and find gaps between iceballs.


### Good Luck! May the Force be with you! :')


