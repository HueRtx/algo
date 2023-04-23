#Подключение модулей--------------------------------------------------
import pygame
from random import randint
import sys
#Стат переменные--------------------------------------------------
run = True          #Идёт ли игра
w = 10              #Ширина платформ
h = 100             #Высота платформ
ws = 700            #Ширина окна
hs = 500            #Высота окна
x1 = 0 + 10         #позиция x первого игрока 
x2 = ws - w - 10    #позиция x второго игрока
y1 = 250 - h/2      #позиция y первого игрока
y2 = 250 - h/2      #позиция y второго игрока
x3 = ws/2
y3 = hs/2
speedx = 0
speedy = 0
score1 = 0
score2 = 0
particles = []
def randommove():
    global speedx
    global speedy
    speedx = randint(1,4)
    speedy = randint(1,4)
def circle_surf(radius, color):
    surf = pygame.Surface((radius * 2, radius * 2))
    pygame.draw.circle(surf, color, (radius, radius), radius)
    surf.set_colorkey((0, 0, 0))
    return surf
#Создание окна--------------------------------------------------
pygame.init()
scr = pygame.display.set_mode((ws, hs))
bg = pygame.transform.scale(pygame.image.load('brick-wall-texture-3-1194786.jpg'), (ws,hs))
pygame.display.set_caption('Maded by abik')
pygame.init()
speedx = randint(1,2)
speedy = randint(1,2)
if randint(1,2) == 1:
    speedx *= -1
if randint(1,2) == 1:
    speedy *= -1
#Цикл игры--------------------------------------------------
while run:
    pygame.time.delay(5)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    #Rect--------------------------------------------------------------------------
    rr1 = (0, -15, ws, 20)                             
    rr2 = (0, hs - 5 , ws, 20)                         
    r1 = (x1,y1, w, h)                                               
    r2 = (x2,y2, w, h)                                                 
    balln = pygame.draw.circle(scr, (0, 255, 0), (x3 + speedx, y3 + speedy), 25)
    wall2 = pygame.draw.rect(scr, (255,0,0), rr2)                     
    wall1 = pygame.draw.rect(scr, (255,0,0), rr1)      
    scr.blit(bg, (0,0))                                                 
    ball = pygame.draw.circle(scr, (0, 255, 0), (x3, y3), 25)       
    player1 = pygame.draw.rect(scr, (255,0,0), r1)                      
    player2 = pygame.draw.rect(scr, (255,0,0), r2)                                     
    f1 = pygame.font.Font(None, 72)
    text1 = f1.render(str(score1), 1, (10, 194, 250))
    text2 = f1.render(str(score2), 1, (10, 194, 250))
    scr.blit(text1, (ws/2 - 55, 10))
    scr.blit(text2, (ws/2 + 55, 10))
    for particle in particles:
        particle[0][0] += particle[1][0]
        particle[0][1] += particle[1][1]
        particle[2] -= 0.1
        particle[1][1] += 0.15
        pygame.draw.circle(scr, (255, 255, 255), [int(particle[0][0]), int(particle[0][1])], int(particle[2]))

        radius = particle[2] * 2
        scr.blit(circle_surf(radius, (10, 194, 250)), (int(particle[0][0] - radius), int(particle[0][1] - radius)))

        if particle[2] <= 0:
            particles.remove(particle)          
    #Мячь касается игрока--------------------------------------------------
    if ball.colliderect(player2) or ball.colliderect(player1) and x3 > x1 + 10 and x3 < x2:
        if speedx >= 0:
            ax = -1
        if speedx <= 0:
            ax = 1
        if speedy >= 0:
            ay = -1
        if speedy <= 0:
            ay = 1
        randommove()
        speedx *= ax
        speedy *= ay
        for i in range(10):
            particles.append([[x3, y3], [randint(0, 20) / 10 - 1, -5], randint(6, 11)])
    #Мячь касается стенки--------------------------------------------------
    if ball.colliderect(wall1) or ball.colliderect(wall2):
        if speedx > 0:
            ax = 1
        if speedx < 0:
            ax = -1
        if speedy >= 0:
            ay = -1
        if speedy <= 0:
            ay = 1
        randommove()
        speedx *= ax
        speedy *= ay
        for i in range(10):
            particles.append([[x3, y3], [randint(0, 20) / 10 - 1, -5], randint(6, 11)])
    #Мячь касается игрока--------------------------------------------------
    if balln.colliderect(player2) or balln.colliderect(player1) and x3 > x1 + 10 and x3 < x2: 
        if speedx >= 0:
            ax = -1
        if speedx <= 0:
            ax = 1
        if speedy >= 0:
            ay = -1
        if speedy <= 0:
            ay = 1
        randommove()
        speedx *= ax
        speedy *= ay
        for i in range(10):
            particles.append([[x3, y3], [randint(0, 20) / 10 - 1, -5], randint(6, 11)])
    #Мячь касается стенки--------------------------------------------------
    if balln.colliderect(wall1) or balln.colliderect(wall2):
        if speedx > 0:
            ax = 1
        if speedx < 0:
            ax = -1
        if speedy >= 0:
            ay = -1
        if speedy <= 0:
            ay = 1
        randommove()
        speedx *= ax
        speedy *= ay
        for i in range(10):
            particles.append([[x3, y3], [randint(0, 20) / 10 - 1, -5], randint(6, 11)])
    #Изменение скорости--------------------------------------------------
    x3 += speedx
    y3 += speedy
    #Проверка на победу--------------------------------------------------
    if x3 <= 0:
        print("Player 2 win!")
        x3 = ws/2
        y3 = hs/2
        randommove()
        score2 += 1
        for i in range(30):
            particles.append([[ws/2 + 70, 100], [randint(0, 20) / 10 - 1, -5], randint(6, 11)])
    if x3 >= 700:
        print("Player 1 win!")
        x3 = ws/2
        y3 = hs/2
        randommove()
        score1 += 1
        for i in range(30):
            particles.append([[ws/2 - 40, 100], [randint(0, 20) / 10 - 1, -5], randint(6, 11)])
    #Движение пsssssервого игрока--------------------------------------------------
    keys = pygame.key.get_pressed()
    #Верх
    if keys[pygame.K_UP] and y2 > 0: 
        y2 -= 5
    #Низ
    if keys[pygame.K_DOWN] and y2 < hs - h:
        y2 += 5
    #Движение второго игрока--------------------------------------------------
    #Верх
    if keys[pygame.K_w] and y1 > 0: 
        y1 -= 5
    #Низ
    if keys[pygame.K_s] and y1 < hs - h:
        y1 += 5
    #Обновление екрана--------------------------------------------------
    pygame.display.update()
