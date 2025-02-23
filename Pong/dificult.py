import pygame 
import bouton
import onevone
import sys
import twovtwo

pygame.init()

screen_width = 1350
screen_height = 800

class Dificultonevone(pygame.sprite.Sprite):
    
    def fenetre_dificult():

        lobby = pygame.display.set_caption("dificult")
        lobby = pygame.display.set_mode((screen_width,screen_height))

        boutonrevenir = pygame.image.load("dessin/boutonrevenir.png").convert_alpha()
        boutonfacile = pygame.image.load("dessin/boutonfacile.png").convert_alpha()
        boutonmoyen = pygame.image.load("dessin/boutonmoyen.png").convert_alpha()
        boutonextreme = pygame.image.load("dessin/boutonextreme.png").convert_alpha()

        FondEcran = 0, 85, 0

        boutonrevenir = bouton.Button(10, 10, boutonrevenir, 1)
        buttonfacile = bouton.Button(225, 355, boutonfacile, 1.9) 
        buttonmoyen = bouton.Button(525, 355, boutonmoyen, 1.9)
        buttonextreme = bouton.Button(825, 355, boutonextreme, 1.9)

        clock = pygame.time.Clock()

        continuer1 = True

        while continuer1:
                    
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    continuer1 = False
                    pygame.display.flip()
                    pygame.quit()
                    sys.exit()

            lobby.fill(FondEcran)
                    
            if buttonfacile.draw(lobby):
                onevone.Facile.fenetre_game()
                        
            if buttonmoyen.draw(lobby):
                onevone.Moyen.fenetre_game()

            if buttonextreme.draw(lobby):
                onevone.Extreme.fenetre_game()

            if boutonrevenir.draw(lobby):
                continuer1 = False

            pygame.display.update()

        clock.tick(60)

class Dificulttwovtwo(pygame.sprite.Sprite):
    
    def fenetre_dificult():

        lobby = pygame.display.set_caption("dificult")
        lobby = pygame.display.set_mode((screen_width,screen_height))

        boutonrevenir = pygame.image.load("dessin/boutonrevenir.png").convert_alpha()
        boutonfacile = pygame.image.load("dessin/boutonfacile.png").convert_alpha()
        boutonmoyen = pygame.image.load("dessin/boutonmoyen.png").convert_alpha()
        boutonextreme = pygame.image.load("dessin/boutonextreme.png").convert_alpha()

        FondEcran = 0, 85, 0

        boutonrevenir = bouton.Button(10, 10, boutonrevenir, 1)
        buttonfacile = bouton.Button(225, 255, boutonfacile, 1.9) 
        buttonmoyen = bouton.Button(525, 255, boutonmoyen, 1.9)
        buttonextreme = bouton.Button(825, 255, boutonextreme, 1.9)

        clock = pygame.time.Clock()

        continuer1 = True

        while continuer1:
                    
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    continuer1 = False
                    pygame.display.flip()
                    pygame.quit()
                    sys.exit()

            lobby.fill(FondEcran)
                    
            if buttonfacile.draw(lobby):
                twovtwo.Facile.fenetre_game()

            if buttonmoyen.draw(lobby):
                twovtwo.Moyen.fenetre_game()

            if buttonextreme.draw(lobby):
                twovtwo.Extreme.fenetre_game()

            if boutonrevenir.draw(lobby):
                continuer1 = False

            pygame.display.update()

        clock.tick(60)
