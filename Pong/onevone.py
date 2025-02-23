import pygame
import sys
import random
import bouton
import song

# couleur
FOND = (0, 85, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
WHITEx1 = (200, 200, 200)
BLACK = (0, 0, 0)
BLUEx1 = (0, 0, 100)
WHITE = (255, 255, 255)

ball_speed_x = 6
ball_speed_y = 6

player_points = 0

pygame.init()

class Facile(pygame.sprite.Sprite):

    def fenetre_game():

        boutonrevenir = pygame.image.load("dessin/boutonrevenir.png").convert_alpha()

        pygame.init()
        screen_width = 1350
        screen_height = 800
        screen = pygame.display.set_mode((screen_width,screen_height))
        pygame.display.set_caption("Game")

        boutonrevenir = bouton.Button(10, 10, boutonrevenir, 1)

        clock = pygame.time.Clock()
        ball = pygame.Rect(0,0,52,52)
        ball.center = (screen_width/2, screen_height/2)

        player = pygame.Rect(0,0,25,150)
        player.centerx = screen_width/11
        player.x = 25
        player.y = 150

        # ligne blanche
        line_white = pygame.Rect(0,0,35,1000)
        line_white.centerx = screen_height/3

        # ligne noir
        line_black = pygame.Rect(0,0,35,1000)
        line_black.centerx = screen_width/1

        # ligne reset
        line_reset = pygame.Rect(0,0,35,1000)
        line_reset.centerx = screen_width/200

        # table bleu
        table_blue = pygame.Rect(0,0,1300,1000)
        table_blue.centerx = screen_width/1.5

        score_font = pygame.font.Font(None, 100)

        player_speed = 6

        def reset_ball():
            global ball_speed_x, ball_speed_y
            ball.x = screen_width/2 
            ball.y = random.randint(10,100)
            ball_speed_y *= random.choice([-1,1])

        def point_won(winner):
            global player_points
            if winner == "player":
                player_points += 1
            if winner == "reset":
                player_points = 0 
                song.Song.crie()
            if winner == "resetball":
                player_points = 0 

        def animate_ball():
            global ball_speed_x, ball_speed_y
            ball.x += ball_speed_x
            ball.y += ball_speed_y
            if ball.bottom >= screen_height or ball.top <= 0:
                ball_speed_y *= -1
                song.Song.ballerebondie()
            if ball.colliderect(line_black):
                point_won("player")
            if ball.left <= 0:
                song.Song.ballerebondie()
                point_won("reset")
                reset_ball()
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
            if ball.colliderect(player) or ball.colliderect(line_black):
                ball_speed_x *= -1
                song.Song.ballerebondie()

            if ball.colliderect(line_reset):
                point_won("reset")
                reset_ball()

        def animate_player():
            player.y += player_speed
            if player.top <= 0:
                player.top = 0
            if player.bottom >= screen_height:
                player.bottom = screen_height

        continuer = True

        while continuer:
            #Check for events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_z:
                        player_speed = -6
                    if event.key == pygame.K_s:
                        player_speed = 6
            
            #Change the positions of the game objects
            animate_ball()
            animate_player()

            #le fond 
            screen.fill(FOND)

            # afficher le score
            player_score_surface = score_font.render(str(player_points), True, BLUE)
            screen.blit(player_score_surface,(screen_width/10,20))
            
            # afficher les objets

            pygame.draw.rect(screen, BLUEx1, table_blue)
            pygame.draw.rect(screen, FOND, line_reset)
            pygame.draw.rect(screen, WHITEx1, line_white)
            pygame.draw.ellipse(screen,RED, ball)
            pygame.draw.rect(screen,BLUE, player)
            pygame.draw.rect(screen, WHITEx1, line_black)

            if boutonrevenir.draw(screen):
                continuer = False
                point_won("resetball")

            #Update the display
            pygame.display.update()
            clock.tick(100)

class Moyen(pygame.sprite.Sprite):

    def fenetre_game():

        boutonrevenir = pygame.image.load("dessin/boutonrevenir.png").convert_alpha()

        pygame.init()
        screen_width = 1350
        screen_height = 800
        screen = pygame.display.set_mode((screen_width,screen_height))
        pygame.display.set_caption("Game")

        boutonrevenir = bouton.Button(10, 10, boutonrevenir, 1)

        clock = pygame.time.Clock()
        ball = pygame.Rect(0,0,52,52)
        ball.center = (screen_width/2, screen_height/2)

        player = pygame.Rect(0,0,25,150)
        player.centerx = screen_width/11
        player.x = 25
        player.y = 150

        # ligne blanche
        line_white = pygame.Rect(0,0,35,1000)
        line_white.centerx = screen_height/3

        # ligne noir
        line_black = pygame.Rect(0,0,35,1000)
        line_black.centerx = screen_width/1

        # ligne reset
        line_reset = pygame.Rect(0,0,35,1000)
        line_reset.centerx = screen_width/200

        # table bleu
        table_blue = pygame.Rect(0,0,1300,1000)
        table_blue.centerx = screen_width/1.5

        score_font = pygame.font.Font(None, 100)

        player_speed = 6

        def reset_ball():
            global ball_speed_x, ball_speed_y
            ball.x = screen_width/2 
            ball.y = random.randint(10,100)
            ball_speed_y *= random.choice([-1,1])

        def point_won(winner):
            global player_points
            if winner == "player":
                player_points += 1
            if winner == "reset":
                player_points = 0 
                song.Song.crie()
            if winner == "resetball":
                player_points = 0 

        def animate_ball():
            global ball_speed_x, ball_speed_y
            ball.x += ball_speed_x
            ball.y += ball_speed_y
            if ball.bottom >= screen_height or ball.top <= 0:
                ball_speed_y *= -1
                song.Song.ballerebondie()
            if ball.colliderect(line_black):
                point_won("player")
            if ball.left <= 0:
                song.Song.ballerebondie()
                point_won("reset")
                reset_ball()
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
            if ball.colliderect(player) or ball.colliderect(line_black):
                ball_speed_x *= -1

            if ball.colliderect(line_reset):
                point_won("reset")
                reset_ball()

        def animate_player():
            player.y += player_speed
            if player.top <= 0:
                player.top = 0
            if player.bottom >= screen_height:
                player.bottom = screen_height

        continuer = True

        while continuer:
            #Check for events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_z:
                        player_speed = -6
                    if event.key == pygame.K_s:
                        player_speed = 6
            
            #Change the positions of the game objects
            animate_ball()
            animate_player()

            #le fond 
            screen.fill(FOND)

            # afficher le score
            player_score_surface = score_font.render(str(player_points), True, BLUE)
            screen.blit(player_score_surface,(screen_width/10,20))
            
            # afficher les objets

            pygame.draw.rect(screen, BLUEx1, table_blue)
            pygame.draw.rect(screen, FOND, line_reset)
            pygame.draw.rect(screen, WHITEx1, line_white)
            pygame.draw.ellipse(screen,RED, ball)
            pygame.draw.rect(screen,BLUE, player)
            pygame.draw.rect(screen, WHITEx1, line_black)

            if boutonrevenir.draw(screen):
                continuer = False
                point_won("resetball")

            #Update the display
            pygame.display.update()
            clock.tick(200)

class Extreme(pygame.sprite.Sprite):

    def fenetre_game():

        boutonrevenir = pygame.image.load("dessin/boutonrevenir.png").convert_alpha()

        pygame.init()
        screen_width = 1350
        screen_height = 800
        screen = pygame.display.set_mode((screen_width,screen_height))
        pygame.display.set_caption("Game")

        boutonrevenir = bouton.Button(10, 10, boutonrevenir, 1)

        clock = pygame.time.Clock()
        ball = pygame.Rect(0,0,52,52)
        ball.center = (screen_width/2, screen_height/2)

        player = pygame.Rect(0,0,25,150)
        player.centerx = screen_width/11
        player.x = 25
        player.y = 150

        # ligne blanche
        line_white = pygame.Rect(0,0,35,1000)
        line_white.centerx = screen_height/3

        # ligne noir
        line_black = pygame.Rect(0,0,35,1000)
        line_black.centerx = screen_width/1

        # ligne reset
        line_reset = pygame.Rect(0,0,35,1000)
        line_reset.centerx = screen_width/200

        # table bleu
        table_blue = pygame.Rect(0,0,1300,1000)
        table_blue.centerx = screen_width/1.5

        score_font = pygame.font.Font(None, 100)

        player_speed = 6

        def reset_ball():
            global ball_speed_x, ball_speed_y
            ball.x = screen_width/2 
            ball.y = random.randint(10,100)
            ball_speed_y *= random.choice([-1,1])

        def point_won(winner):
            global player_points
            if winner == "player":
                player_points += 1
            if winner == "reset":
                player_points = 0
                song.Song.crie()
            if winner == "resetball":
                player_points = 0  

        def animate_ball():
            global ball_speed_x, ball_speed_y
            ball.x += ball_speed_x
            ball.y += ball_speed_y
            if ball.bottom >= screen_height or ball.top <= 0:
                ball_speed_y *= -1
                song.Song.ballerebondie()
            if ball.colliderect(line_black):
                point_won("player")
            if ball.left <= 0:
                song.Song.ballerebondie()
                point_won("reset")
                reset_ball()
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
            if ball.colliderect(player) or ball.colliderect(line_black):
                ball_speed_x *= -1

            if ball.colliderect(line_reset):
                point_won("reset")
                reset_ball()

        def animate_player():
            player.y += player_speed
            if player.top <= 0:
                player.top = 0
            if player.bottom >= screen_height:
                player.bottom = screen_height

        continuer = True

        while continuer:
            #Check for events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_z:
                        player_speed = -6
                    if event.key == pygame.K_s:
                        player_speed = 6
            
            #Change the positions of the game objects
            animate_ball()
            animate_player()

            #le fond 
            screen.fill(FOND)

            # afficher le score
            player_score_surface = score_font.render(str(player_points), True, BLUE)
            screen.blit(player_score_surface,(screen_width/10,20))
            
            # afficher les objets

            pygame.draw.rect(screen, BLUEx1, table_blue)
            pygame.draw.rect(screen, FOND, line_reset)
            pygame.draw.rect(screen, WHITEx1, line_white)
            pygame.draw.ellipse(screen,RED, ball)
            pygame.draw.rect(screen,BLUE, player)
            pygame.draw.rect(screen, WHITEx1, line_black)

            if boutonrevenir.draw(screen):
                continuer = False
                point_won("resetball")

            #Update the display
            pygame.display.update()
            clock.tick(300)

