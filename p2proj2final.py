
from tkinter import *
import random
from tkinter import messagebox

#-----------------------------------    

class Vector:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

#-----------------------------------    

class GameObject:
    
    def __init__(self, pos):
        self.position = Vector(pos[0], pos[1])
    
    def isCollidingWith(self, otherGameObject):
        
        if ((self.position.x+self.width//2) > (otherGameObject.position.x - otherGameObject.width//2) and (self.position.x -self.width//2) < (otherGameObject.position.x + otherGameObject.width//2) and (self.position.y + self.height//2) > (otherGameObject.position.y - otherGameObject.height//2) and (self.position.y - self.height//2) < (otherGameObject.position.y + otherGameObject.height//2)):
        
            return True
        else:
            return False
        
    def Ddraw(self):
        Game.canvas.create_image(self.position.x,self.position.y, image=self.img)
        

#-----------------------------------

class Background(GameObject):
    def __init__(self):
        
        GameObject.__init__(self,[320,242])
        self.img= PhotoImage(file= "assets/bg.gif")
        
       
    
    def Draw(self):
        
        GameObject.Ddraw(self)       

#-----------------------------------
    
class Brick(GameObject):
    def __init__(self):
        
        GameObject.__init__(self,self.p)
        self.img= PhotoImage(file= self.f)
        self.height = 32
        self.width = 63      
    def Draw(self):
        GameObject.Ddraw(self)       


class NormalBrick(Brick):
    
    def __init__(self,pos):
        
        self.f = "assets/normalbrick.gif"
        self.p = pos
        self.health = 1
        Brick.__init__(self)
    def Draw(self):
        Brick.Draw(self)
class RedBrick(Brick):
    
    def __init__(self,pos):
        
        self.f = "assets/explodingbrick.gif"
        self.p = pos
        self.health = 1
        Brick.__init__(self)
    def Draw(self):
        Brick.Draw(self)
    
class MetalBrick(Brick):
    def __init__(self,pos):
        
        self.f = "assets/metalbrick.gif"
        self.p = pos
        self.health = 1
        Brick.__init__(self)
    def Draw(self):
        Brick.Draw(self)
    
class GlassBrick(Brick):
    def __init__(self,pos):
        
        self.f = "assets/glassbrick.gif"
        self.p = pos
        self.health = 1
        Brick.__init__(self)
    def Draw(self):
        Brick.Draw(self)


#-----------------------------------
    
class Ball(GameObject):
    def __init__(self,pos,vel):
        GameObject.__init__(self,pos)
        self.velocity= Vector(vel[0],vel[1])
        self.img = PhotoImage(file = "assets/ballBlue.png")
        self.width = 22
        self.height = 22

    def Draw(self):
        
        GameObject.Ddraw(self)
        


        
    
    
#-----------------------------------

class Powerup(GameObject):
    def __init__(self):
        
        GameObject.__init__(self,self.p)
        self.img= PhotoImage(file= self.f)
        self.height = 40
        self.width = 40
        
    def Draw(self):
        GameObject.Ddraw(self)       

    
class Life(Powerup):
    def __init__(self,pos):
        
        self.f = "assets/life.gif"
        self.p = pos
        self.typ = "life"
        self.health = 1
        self.velocity = Vector(0,0)
        Powerup.__init__(self)
    def Draw(self):
        Powerup.Draw(self)

    
class FastPaddle(Powerup):
    def __init__(self,pos):
        
        self.f = "assets/fastpaddle.gif"
        self.p = pos
        self.typ = "fastpaddle"
        self.health = 1
        self.velocity = Vector(0,0)
        Powerup.__init__(self)
    def Draw(self):
        Powerup.Draw(self)


class CrazyBall(Powerup):
    def __init__(self,pos):
        
        self.f = "assets/crazyball.gif"
        self.p = pos
        self.typ = "crazyball"
        self.health = 1
        self.velocity = Vector(0,0)
        Powerup.__init__(self)
    def Draw(self):
        Powerup.Draw(self)


#-----------------------------------

class Player(GameObject):
    def __init__(self, game, pos, vel):
        GameObject.__init__(self,pos)
        self.velocity= Vector(vel[0], vel[1])
        self.game= game
        self.score = 0
        self.img= PhotoImage(file="assets/paddleBlu.gif")
        self.life=3
        self.width = 104
        self.height = 24
                 

    def Draw(self):
        
        GameObject.Ddraw(self)      

        
    
#-----------------------------------

class Game:
    canvas = None
    def __init__(self, canvas):
        Game.canvas = canvas           # Save canvas for future use
        self.gameObjects = [] # A list of ALL game objects in the game
        self.bricks1 = []
        self.bricks2 = []
        self.bricks3 = []
        self.bricks4 = []
        self.powerups = []
        self.drawpw = []
        self.check = "True"
        self.check2 = "False"
        self.score = 0
        self.life=3
        self.time = 0
        self.timer()
        self.timer2()
        self.pwup = ""
        self.pweffect = 0
        self.createpowerups()
        self.bg= Background()
        self.gameObjects.append(self.bg)
        self.player= Player(self, (320,430), (4,0))
        self.gameObjects.append(self.player)
        self.ball = Ball((321,320),(0,2.5))
        self.gameObjects.append(self.ball)
        
        j = 100
        for i in range(8):
            self.brick = MetalBrick([j,120])
            self.bricks1.append(self.brick)
            j+= 64
        j = 100
        for i in range(8):
            self.brick = NormalBrick([j,150])
            self.bricks2.append(self.brick)
            j+= 64
        j = 100
        for i in range(8):
            self.brick = NormalBrick([j,180])
            self.bricks3.append(self.brick)
            j+= 64
        j = 100
        for i in range(8):
            self.brick = GlassBrick([j,210])
            self.bricks4.append(self.brick)
            j+= 64
    def timer(self):
        if self.time <30:
            self.time += 1
            if self.time == 30:
                print(self.time)
                self.chosepowerup()
        if self.check == "True" and self.time !=30:
            self.check = "False"
            self.time = 0
        self.canvas.after(1000,self.timer)
    def timer2(self):
        if self.check2 == "True" and self.pweffect !=6:
            self.pweffect +=1
            
        self.canvas.after(1000,self.timer2)
    def chosepowerup(self):
        xy = random.choice(self.powerups)
        self.drawpw.append(xy)
        
    def Draw(self):                    # This function draws ALL of the things
        Game.canvas.delete(ALL)        # First clear the screen
        for obj in self.gameObjects:   # Now the objects draw THEMSELVES one by one
            obj.Draw()
        for obj in self.bricks1:
            obj.Draw()
        for obj in self.bricks2:
            obj.Draw()
        for obj in self.bricks3:
            obj.Draw()
        for obj in self.bricks4:
            obj.Draw()
        if self.time==30:
            xy = self.drawpw[0]
            if xy.typ == "fastpaddle":
                xy.Draw()
            elif xy.typ == "crazyball":
                xy.Draw()
        Game.canvas.create_text(30, 15, text="Life: " + str(self.life), font= ("Times New Roman",14),fill="white", anchor="nw")
        Game.canvas.create_text(290,15,text="Score: " + str(self.score), font=("Times New Roman",15),fill="white", anchor= "nw")
        
    def createpowerups(self):
        #self.fastpaddle = FastPaddle((150,40))
        #self.powerups.append(self.fastpaddle)
        self.crazyball = CrazyBall((260,40))
        self.powerups.append(self.crazyball)
    def LeftKeyPressed(self):        
        #############################
        #   INSERT YOUR CODE HERE
        if self.player.position.x>60:
            
            self.player.position.x-=self.player.velocity.x
            
        #############################

    
    def RightKeyPressed(self):        
        #############################
        #   INSERT YOUR CODE HERE
        if self.player.position.x<580:
            self.player.position.x+=self.player.velocity.x
            
        #############################
            
    def Update(self):    
        if(self.ball.position.x + self.ball.velocity.x + self.ball.width//2 >= 640 or self.ball.position.x +self.ball.velocity.x < 0):
            self.ball.velocity.x = -self.ball.velocity.x
        if self.ball.position.x - self.ball.width//2 < 0:
            self.ball.velocity.x = -self.ball.velocity.x
            
        for i in range(len(self.bricks1)):
                
            if GameObject.isCollidingWith(self.ball,self.bricks1[i]):
                self.bricks1[i].health -= 1
                self.ball.velocity.y = -self.ball.velocity.y
                self.ball.velocity.x = self.ball.velocity.x
                self.score+=10
                    
            if self.bricks1[i].health == 0:
                self.bricks1.pop(i)
                break
        for i in range(len(self.bricks2)):
        
            if  GameObject.isCollidingWith(self.ball,self.bricks2[i]) : 
                self.bricks2[i].health -= 1
                self.ball.velocity.y = -self.ball.velocity.y
                self.ball.velocity.x = self.ball.velocity.x
                self.score+=10
                    
            if self.bricks2[i].health == 0:
                self.bricks2.pop(i)
                break

        for i in range(len(self.bricks3)):
                
            if GameObject.isCollidingWith(self.ball,self.bricks3[i]) :
                self.bricks3[i].health -= 1
                self.ball.velocity.y = -self.ball.velocity.y
                self.ball.velocity.x = self.ball.velocity.x
                self.score+=10
                    
            if self.bricks3[i].health == 0:
                self.bricks3.pop(i)
                break
            
        for i in range(len(self.bricks4)):
                
            if GameObject.isCollidingWith(self.ball,self.bricks4[i])  :
                self.bricks4[i].health -= 1
                self.ball.velocity.y = -self.ball.velocity.y
                self.ball.velocity.x = self.ball.velocity.x
                self.score+=10
            if self.bricks4[i].health == 0:
                self.bricks4.pop(i)
                break

        if len(self.bricks1)==0 and len(self.bricks2)==0 and len(self.bricks3) and len(self.bricks4)==0:
            
            messagebox.showinfo("Game Won", "Congratulations! You won")
        if self.life == 0:
            messagebox.showinfo("Game Over", "You lost")
        if(self.ball.position.y +self.ball.velocity.y - self.ball.height//2 < 0):
            self.ball.velocity.y = -self.ball.velocity.y
        if self.ball.position.y + self.ball.velocity.y + 22 >= 480:
            self.ball.velocity.y = -self.ball.velocity.y
            self.gameObjects.pop(2)
            self.gameObjects.pop()
            if self.life!=0:
                self.life-=1
            self.ball = Ball((321,320),(0,2.5))
            self.gameObjects.append(self.ball)
            self.player= Player(self, (320,450), (4,0))
            self.gameObjects.append(self.player)
        
        if self.time == 30:
            xy = self.drawpw[0]
            self.pwup = xy.typ
            if self.pwup == "fastpaddle":
                self.fastpaddle.velocity.y = 1
                self.fastpaddle.position.y += self.fastpaddle.velocity.y
                pw = GameObject.isCollidingWith(self.player,self.fastpaddle)
                if pw:
                    print("paddle")
                    self.player.velocity.x = self.player.velocity.x + 1.05
                    self.timer2()
                    self.time = 0
                    self.time = 31
                    self.drawpw = []
                    self.powerups = []
                    self.check2 = "True"
                    self.pweffect = 0
                
            elif self.pwup == "crazyball":
                self.crazyball.velocity.y = 1
                self.crazyball.position.y += self.crazyball.velocity.y
                pw = GameObject.isCollidingWith(self.player,self.crazyball)
                if pw:
                    print("crazay")
                    if self.ball.velocity.x < 0 and self.ball.velocity.y <0:
                        self.ball.velocity.x = -2
                        self.ball.velocity.y = -4
                    elif self.ball.velocity.x > 0 and self.ball.velocity.y > 0:
                        self.ball.velocity.x = 2
                        self.ball.velocity.y = 4                        
                    self.time = 11
                    self.drawpw = []
                    self.powerups = []
                    self.check2 = "True"
                    self.pweffect = 0
        if self.pweffect == 6:
            if self.pwup == "crazyball":
                print("t")
                if self.ball.velocity.x < 0 and self.ball.velocity.y <0:
                    self.ball.velocity.x = -1
                    self.ball.velocity.y = -2.5
                elif self.ball.velocity.x > 0 and self.ball.velocity.y > 0:
                    self.ball.velocity.x = 1
                    self.ball.velocity.y = 2.5
                elif self.ball.velocity.x > 0 and self.ball.velocity.y < 0:
                    self.ball.velocity.x = 1
                    self.ball.velocity.y = -2.5
                elif self.ball.velocity.x < 0 and self.ball.velocity.y > 0:
                    self.ball.velocity.x = -1
                    self.ball.velocity.y = 2.5
                self.pweffect = 7
                self.check = "True"
                self.drawpw = []
                self.powerups = []
                self.createpowerups()
                
            elif self.pwup == "fastpaddle":
                self.player.velocity.x = self.player.velocity.x - 1.05
        
        self.ball.position.x +=self.ball.velocity.x       
        self.ball.position.y +=self.ball.velocity.y
        x = GameObject.isCollidingWith(self.ball,self.player)
        if GameObject.isCollidingWith(self.ball, self.player):
            self.ball.velocity.y = -self.ball.velocity.y
            self.ball.velocity.x = self.ball.velocity.x 
            if self.ball.velocity.x==0:
                self.ball.velocity.x = 1
        
            
            
        #############################

        
            
#-----------------------------------


class GameWindow:
    def __init__(self):
        self.root = Tk()
        self.root.title("Project 2 -- Breakout Game")
        self.root.geometry('640x480')

        self.canvas = Canvas(self.root, width = 640, height = 480)
        self.canvas.grid(column=0, row=0)
        self.canvas.after(1, self.OneSecTimer)
        self.canvas.bind("<Key>", self.KeyPressed)
        self.canvas.focus_set()
        
        self.game = Game(self.canvas)    
        self.root.after(1, self.GameLoop)
        self.root.mainloop()
    
    def KeyPressed(self, event):
        c = str(event.char)
        if c == 'a':
            self.game.LeftKeyPressed()
        if c == 'd':
            self.game.RightKeyPressed()

    
    def GameLoop(self):        
        self.game.Update()
        self.game.Draw()
        
        self.root.after(1000//60, self.GameLoop)

    def OneSecTimer(self):
        print("One second Tick")
        self.canvas.after(1000, self.OneSecTimer)
        
#-----------------------------------


game = GameWindow()

