#welcome to my pygame tutorial

import pygame

#lets get sound 
from pygame import mixer

mixer.init()

clock = pygame.time.Clock()

#now we will create a map by making a txt file

screen = pygame.display.set_mode((800, 600))

#first we will create the classes for the keys

class Key():
    def __init__(self,x,y,color1,color2,key):
        self.x = x
        self.y = y
        self.color1 = color1
        self.color2 = color2
        self.key = key
        self.rect = pygame.Rect(self.x,self.y,100,40)
        self.handled = False

#now we will make a list of keys

keys = [
    Key(100,500,(255,0,0),(220,0,0),pygame.K_a),
    Key(200,500,(0,255,0),(0,220,0),pygame.K_s),
    Key(300,500,(0,0,255),(0,0,220),pygame.K_d),
    Key(400,500,(255,255,0),(220,220,0),pygame.K_f),
]

#lets load the map into the game 
def load(map):
    rects = []
    mixer.music.load(map + ".mp3")
    mixer.music.play()
    f = open(map + ".txt", 'r')
    data = f.readlines()

    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] == '0':
                rects.append(pygame.Rect(keys[x].rect.centerx - 25,y * -100,50,25))
    return rects

map_rect = load("freedom dive")

while True:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    #now we will loop through the keys and handle the events
    k = pygame.key.get_pressed()
    for key in keys:
        if k[key.key]:
            pygame.draw.rect(screen,key.color1,key.rect)
            key.handled = False
        if not k[key.key]: 
            pygame.draw.rect(screen,key.color2,key.rect)
            key.handled = True
        #now when we press our keys they will change color
    for rect in map_rect:
        pygame.draw.rect(screen,(200,0,0),rect)
        rect.y += 5
        for key in keys: 
            if key.rect.colliderect(rect) and not key.handled:
                map_rect.remove(rect)
                key.handled = True
                break

        


    pygame.display.update()
    clock.tick(60)