import numpy as np
import cv2
from random import randint
from time import time

game = np.zeros((700, 500, 3), dtype= np.uint8() )
dmg_field = np.zeros( (game.shape[0], game.shape[1]), dtype = np.uint8())

class Controller:
    CONTROLLER = 430

class Player:
    x_pos = 250
    y_pos = 650
    
    size_x = 100
    size_y = 30

    x = int(x_pos - size_x/2)
    y = int(y_pos - size_y/2)

    speed = 50

    shoot_delay = 1
    SHOOT_DELAY_MAX = shoot_delay
    color = (150, 250, 0)
        
    def draw(self):
        cv2.rectangle(game, (self.x,self.y), (self.x+ self.size_x, self.y+self.size_y), self.color, -1)
        
    def destroy(self):
        cv2.rectangle(game, (self.x,self.y), (self.x+ self.size_x, self.y+self.size_y), (0,0,0), -1)

    def move(self):
        self.destroy()
        
        if CONTROLLER.CONTROLLER > self.x_pos:
            self.move_right()
        elif CONTROLLER.CONTROLLER < self.x_pos:
            self.move_left()

        if self.shoot_delay == self.SHOOT_DELAY_MAX:
            self.shoot()
            self.shoot_delay = 0
        else:
            self.shoot_delay += 1
        
        self.draw()

    
    def move_left(self):
        self.x -= self.speed
        self.x_pos -= self.speed

    def move_right(self):
        self.x += self.speed
        self.x_pos += self.speed

    def shoot(self):
        bs.append(Bullet(self.x_pos, self.y_pos) )
        
class Particle:
    def __init__(self, x, y):
        self.x = x + randint(-20, 20)
        self.y = y + randint(-20, 20)
        self.size = randint(10, 30)

        self.live_tick = 25
        
        self.color =  [randint(150, 255), randint(150, 255), randint(150, 255) ]
        self.color_dif = list( [  c * (1/self.live_tick) for c in self.color] )

        self.speedX = randint(-5, 5) 
        self.speedY = randint(-5, 5)
    
    def draw(self):
        #cv2.rectangle(game, (self.x,self.y), (self.x+ self.size, self.y+self.size), self.color, -1)
        cv2.circle( game, (self.x,self.y), self.size, self.color, -1 )
    def destroy(self):
        #cv2.rectangle(game, (self.x,self.y), (self.x+ self.size, self.y+self.size), (0,0,0), -1)
        cv2.circle( game, (self.x,self.y), self.size, (0,0,0), -1 )
        
    def move(self):
        self.destroy()
        
        self.y +=self.speedY
        self.x +=self.speedX
        self.color = list( [ self.color[i] - self.color_dif[i] for i in range(3) ] )
        self.draw()
        self.live_tick -= 1
        if self.live_tick <= 0:
            self.destroy()
        
        
class Rect:
    x = randint(50, 400)
    y = 10
    size = 50
    hp = 100
    speed = 100
    nockback = 5
    last_hit_time = time()
    start_delay = randint(0, 10)
    
    def draw(self):
        G = int(self.hp * 2.50)
        R = int(100 - self.hp * 2.50)
        cv2.rectangle(game, (self.x,self.y), (self.x+ self.size, self.y+self.size), (20,G+1,R+1), -1)
        
    def destroy(self):
        cv2.rectangle(game, (self.x,self.y), (self.x+ self.size, self.y+self.size), (0,0,0), -1)
        
    def move(self):
        if self.start_delay > 0:
            self.start_delay -= 1
            return None
        self.destroy()
        self.damage_check()
        
        self.y +=self.speed
        if self.speed != 150:
            self.speed+=1


        self.draw()
        
        if self.y > game.shape[0]:
            self.respawn()

    def respawn(self):
        for _ in range(randint(3, 7)):
            particles.append( Particle( int(self.x +self.size/2), int(self.y +self.size/2) ) )
        self.x = randint(50, 400)
        self.y = 10
        self.size = 50
        self.hp = 100
        self.speed = 1
        self.nockback = 5
        self.last_hit_time = time()
        self.start_delay = randint(0, 10)
        
    def damage_check(self):
        if (dmg_field[self.y:self.y+self.size,  self.x:self.x+ self.size] > 0).any() and time() - self.last_hit_time > 0.1:
            self.last_hit_time = time()
            self.speed = -10
            self.hp -= dmg_field[self.y:self.y+self.size,  self.x:self.x+ self.size].max()
            
            if self.hp < 0:
                self.respawn()
                
class Bullet:
    
    #y = 700
    sizeX = 10
    sizeY = 50
    dmg = randint(10, 20)
    speed = 50
    dead = False
    
    def __init__(self, x, y  ):
        self.start_delay = 0# randint( 0, 10)
        self.x = x + randint(-50, 50)
        self.y = y - self.sizeY

        
    def draw(self):
        cv2.rectangle(game, (self.x,self.y), (self.x+ self.sizeX, self.y+self.sizeY), (20,250,250), -1)
        dmg_field[self.y:self.y+self.sizeY,  self.x:self.x+ self.sizeX] += self.dmg

    def destroy(self):
        cv2.rectangle(game, (self.x,self.y), (self.x+ self.sizeX, self.y+self.sizeY), (0,0,0), -1)
        dmg_field[self.y:self.y+self.sizeY,  self.x:self.x+ self.sizeX] -= self.dmg

    def move(self):
        if self.start_delay > 0:
            self.start_delay -= 1
            return None
        self.destroy()
        self.y -= self.speed
        self.draw()

        if self.y < 0-self.sizeY:
            self.destroy()
            self.dead = True
            #self.y = 700
            #self.x = randint(50, 200)
            #self.dmg = randint(10, 20)

CONTROLLER = Controller()
particles = []
rs = [ Rect() for _ in range(5)]
bs = [] #[ Bullet() for _ in range(5)]
player = Player()


def play():
    print(' '* 100,  end='\r')
    for r in rs:
        r.move()
    for ind, b in enumerate(bs):
        b.move()
        if b.dead:
            bs.pop(ind)
    for ind, p in enumerate(particles):
        p.move()   
        if p.live_tick <= 0:
            particles.pop(ind)
    print('hp: ', r.hp, ' bullets: ', len(bs),  end='\r')

    player.move()

if __name__ == '__main__':
    r = Rect()
    while True:
        cv2.imshow('game' , game)
        cv2.imshow('dmg' , dmg_field)

        play()
        
        key = cv2.waitKey(1)
        if key == 27:
            break

    cv2.destroyAllWindows()

