# v1 : pareil mais au moins on peut sortir du programme
# avec la touche 'q', ou avec la souris en fermant la fenêtre

#Importation des différents modules 
import pygame as pg 
from random import randint, random
from pygame.constants import K_LEFT, K_RIGHT
import random


pg.init()

#Initialisation des variables 
NX=500 #nb de pixel en x
NY=500 #nb de pixel en y 
width = 25 # largeur du rectangle en pixels
height = 25 # hauteur du rectangle en pixels
score=0 # comptabilisation du score 
taille=3 #choix de la taille du serpent 
direction = (0, 0) #direction initiale du snake 

win=pygame.display.set_mode((NX, NY)) 
pygame.display.set_caption("Scrolling Text") 
Font=pygame.font.SysFont('timesnewroman',  30)

#Génération du serpent 
snake=[]
for i in range (taille):
    snake.append((i,15))




#génération de la fenêtre du jeux 
screen = pg.display.set_mode((NX, NY))

clock = pg.time.Clock()

# on rajoute une condition à la boucle: si on la passe à False le programme s'arrête
running = True

while running:
    clock.tick(15)

    # on itère sur tous les évênements qui ont eu lieu depuis le précédent appel
    # ici donc tous les évènements survenus durant la seconde précédente
    for event in pg.event.get():
        # chaque évênement à un type qui décrit la nature de l'évênement
        # un type de pg.QUIT signifie que l'on a cliqué sur la "croix" de la fenêtre
        if event.type == pg.QUIT:
            running = False
        # un type de pg.KEYDOWN signifie que l'on a appuyé une touche du clavier
        elif event.type == pg.KEYDOWN:
            # si la touche est "Q" on veut quitter le programme
            if event.key == pg.K_q:
                running = False

            #détection des touches du claviers pour la direction et impossibilité de reculer sur soit même 
            elif event.key == pg.K_UP and direction!=(0,1):
                direction=(0,-1)
                
            elif event.key == pg.K_DOWN and direction!=(0,-1):
                direction=(0,1)
                               
            elif event.key == pg.K_LEFT and direction!=(1,0):
                direction=(-1,0)
                
            elif event.key == pg.K_RIGHT and direction!=(-1,0):
                direction=(1,0)
                

    # Déplacer le serpent en continue sur la fenêtre 
    snake.pop(0)
    a=snake[-1][0]+direction[0]
    b=snake[-1][1]+direction[1]
    direction = (0, 0)
    snake.append((a,b))

        
    #réinitialisation du fond 
    screen.fill(color=(0, 0, 0))
    
    
    #affichage du donjon 
    for line,floor in enumerate(donjon) :
        for column, caractere in enumerate(floor) : 
            win.blit(Font.render(caractere, False,(0,0,0)), (column*width, line*height))


    
    #affichage du serpent, du score et de la pomme 
    for i in snake:
        pg.draw.rect(screen,color = (255,255,255), rect = pg.Rect(i[0]*width,i[1]*height, width, height))        
        pg.display.set_caption(f"Score: {score}")        
            
    pg.display.update() 

# Enfin on rajoute un appel à pg.quit()
# Cet appel va permettre à Pygame de "bien s'éteindre" et éviter des bugs sous Windows
pg.quit()


