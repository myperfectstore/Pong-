import pygame 
import bouton
import dificult
import song
import random
import sys

pygame.init()

pygame.mixer.init()

song.Song.bubble()

screen_width = 1350
screen_height = 800

lobby = pygame.display.set_caption("Pong")
lobby = pygame.display.set_mode((screen_width,screen_height))

boutonquitter = pygame.image.load("dessin/boutonquiter.png").convert_alpha()
bouton1v1 = pygame.image.load("dessin/bouton1v1.png").convert_alpha()
bouton2v2 = pygame.image.load("dessin/bouton2v2.png").convert_alpha()

lesboutons = pygame.image.load("dessin/lesboutons.png").convert_alpha()
lesboutons = pygame.transform.scale(lesboutons, (700, 700))

FondEcran = 0, 85, 0

button1v1 = bouton.Button(525, 254, bouton1v1, 1.9) 
button2v2 = bouton.Button(525, 355, bouton2v2, 1.9)
buttonquitter = bouton.Button(525, 457, boutonquitter, 1.9)

continuer = True

while continuer:
            
    lobby.fill(FondEcran)

    lobby.blit(lesboutons, (310, 50))  
            
    if buttonquitter.draw(lobby):
        continuer = False
            
    if button1v1.draw(lobby):
        dificult.Dificultonevone.fenetre_dificult()
                
    if button2v2.draw(lobby):
        dificult.Dificulttwovtwo.fenetre_dificult()
            
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = False
    pygame.display.flip()

# Arrêter la musique
pygame.mixer.music.stop()

pygame.quit()