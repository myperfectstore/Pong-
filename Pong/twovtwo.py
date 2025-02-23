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
cpu_speed = 6
cpu_points, player_points = 0, 0

class Facile():
    def fenetre_game():

        def reset_ball():
            global ball_speed_x, ball_speed_y
            ball.x = screen_width/2 - 10
            ball.y = random.randint(10,100)
            ball_speed_x *= random.choice([-1,1])
            ball_speed_y *= random.choice([-1,1])

        def point_won(winner):
            global cpu_points, player_points
            if winner == "cpu":
                cpu_points += 1
                song.Song.crie()
            if winner == "player":
                player_points += 1
                song.Song.crie()
            if winner == "reset":
                player_points = 0
                cpu_points = 0 

            reset_ball()

        def animate_ball():
            global ball_speed_x, ball_speed_y
            ball.x += ball_speed_x
            ball.y += ball_speed_y

            if ball.bottom >= screen_height or ball.top <= 0:
                ball_speed_y *= -1
                song.Song.ballerebondie()

            if ball.right >= screen_width:
                point_won("cpu")
                song.Song.ballerebondie()

            if ball.left <= 0:
                point_won("player")
                song.Song.ballerebondie()
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
            if ball.colliderect(player) or ball.colliderect(cpu):
                ball_speed_x *= -1

        player_speed = 6

        def animate_player():
            player.y += player_speed

            if player.top <= 0:
                player.top = 0

            if player.bottom >= screen_height:
                player.bottom = screen_height

        def animate_cpu():
            global cpu_speed
            cpu.y += cpu_speed

            if cpu.top <= 0:
                cpu.top = 0
            if cpu.bottom >= screen_height:
                cpu.bottom = screen_height

        pygame.init()

        screen_width = 1280
        screen_height = 800

        screen = pygame.display.set_mode((screen_width,screen_height))
        pygame.display.set_caption("pong")

        boutonrevenir = pygame.image.load("dessin/boutonrevenir.png").convert_alpha()

        boutonrevenir = bouton.Button(10, 10, boutonrevenir, 1)

        clock = pygame.time.Clock()

        # table bleu
        table_blue = pygame.Rect(0,0,925,1000)
        table_blue.centerx = screen_height/1.2

        # ligne blanche
        line_white = pygame.Rect(0,0,35,1000)
        line_white.centerx = screen_height/1.23

        # ligne blanche player 2
        line_white_player2 = pygame.Rect(0,0,35,1000)
        line_white_player2.centerx = screen_height/3.7

        # ligne blanche player 
        line_white_player = pygame.Rect(0,0,35,1000)
        line_white_player.centerx = screen_height/0.7

        #mesure de la balle 
        ball = pygame.Rect(0,0,52,52)
        ball.center = (screen_width/2, screen_height/2)

        #player 2 mesure
        cpu = pygame.Rect(0,0,25,150)
        cpu.centerx = screen_width/13

        #player mesure
        player = pygame.Rect(0,0,25,150)
        player.midright = (screen_width, screen_height/2)

        score_font = pygame.font.Font(None, 100)

        running = True

        while running:
            #Check for events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        player_speed = -6
                    if event.key == pygame.K_DOWN:
                        player_speed = 6

                if event.type == pygame.KEYDOWN:
                    global cpu_speed
                    if event.key == pygame.K_z:
                        cpu_speed = -6
                    if event.key == pygame.K_s:
                        cpu_speed = 6

            #Change the positions of the game objects
            animate_ball()
            animate_player()
            animate_cpu()
                
            #Clear the screen
            screen.fill(FOND)

            if boutonrevenir.draw(screen):
                running = False
                point_won("reset")


            #Draw the game objects
            pygame.draw.rect(screen, BLUEx1, table_blue)
            pygame.draw.rect(screen, WHITEx1, line_white_player)
            pygame.draw.rect(screen, WHITEx1, line_white_player2)
            pygame.draw.rect(screen, WHITEx1, line_white)
            pygame.draw.ellipse(screen, RED, ball)
            pygame.draw.rect(screen, BLUE, cpu)
            pygame.draw.rect(screen, BLUE, player)

            #Draw the score
            cpu_score_surface = score_font.render(str(cpu_points), True, BLUE)
            player_score_surface = score_font.render(str(player_points), True, BLUE)
            screen.blit(cpu_score_surface,(screen_width/10,20))
            screen.blit(player_score_surface,(3*screen_width/3.2,20))

            #Update the display
            pygame.display.update()
            clock.tick(100)

class Moyen():
    def fenetre_game():

        def reset_ball():
            global ball_speed_x, ball_speed_y
            ball.x = screen_width/2 - 10
            ball.y = random.randint(10,100)
            ball_speed_x *= random.choice([-1,1])
            ball_speed_y *= random.choice([-1,1])

        def point_won(winner):
            global cpu_points, player_points
            if winner == "cpu":
                cpu_points += 1
                song.Song.crie()
            if winner == "player":
                player_points += 1
                song.Song.crie()
            if winner == "reset":
                player_points = 0
                cpu_points = 0 

            reset_ball()

        def animate_ball():
            global ball_speed_x, ball_speed_y
            ball.x += ball_speed_x
            ball.y += ball_speed_y

            if ball.bottom >= screen_height or ball.top <= 0:
                ball_speed_y *= -1
                song.Song.ballerebondie()

            if ball.right >= screen_width:
                point_won("cpu")
                song.Song.ballerebondie()

            if ball.left <= 0:
                point_won("player")
                song.Song.ballerebondie()
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
            if ball.colliderect(player) or ball.colliderect(cpu):
                ball_speed_x *= -1

        player_speed = 6

        def animate_player():
            player.y += player_speed

            if player.top <= 0:
                player.top = 0

            if player.bottom >= screen_height:
                player.bottom = screen_height

        def animate_cpu():
            global cpu_speed
            cpu.y += cpu_speed

            if cpu.top <= 0:
                cpu.top = 0
            if cpu.bottom >= screen_height:
                cpu.bottom = screen_height

        pygame.init()

        screen_width = 1280
        screen_height = 800

        screen = pygame.display.set_mode((screen_width,screen_height))
        pygame.display.set_caption("pong")

        boutonrevenir = pygame.image.load("dessin/boutonrevenir.png").convert_alpha()

        boutonrevenir = bouton.Button(10, 10, boutonrevenir, 1)

        clock = pygame.time.Clock()

        # table bleu
        table_blue = pygame.Rect(0,0,925,1000)
        table_blue.centerx = screen_height/1.2

        # ligne blanche
        line_white = pygame.Rect(0,0,35,1000)
        line_white.centerx = screen_height/1.23

        # ligne blanche player 2
        line_white_player2 = pygame.Rect(0,0,35,1000)
        line_white_player2.centerx = screen_height/3.7

        # ligne blanche player 
        line_white_player = pygame.Rect(0,0,35,1000)
        line_white_player.centerx = screen_height/0.7

        #mesure de la balle 
        ball = pygame.Rect(0,0,52,52)
        ball.center = (screen_width/2, screen_height/2)

        #player 2 mesure
        cpu = pygame.Rect(0,0,25,150)
        cpu.centerx = screen_width/13

        #player mesure
        player = pygame.Rect(0,0,25,150)
        player.midright = (screen_width, screen_height/2)

        score_font = pygame.font.Font(None, 100)

        running = True

        while running:
            #Check for events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        player_speed = -6
                    if event.key == pygame.K_DOWN:
                        player_speed = 6

                if event.type == pygame.KEYDOWN:
                    global cpu_speed
                    if event.key == pygame.K_z:
                        cpu_speed = -6
                    if event.key == pygame.K_s:
                        cpu_speed = 6

            #Change the positions of the game objects
            animate_ball()
            animate_player()
            animate_cpu()
                
            #Clear the screen
            screen.fill(FOND)

            if boutonrevenir.draw(screen):
                running = False
                point_won("reset")


            #Draw the game objects
            pygame.draw.rect(screen, BLUEx1, table_blue)
            pygame.draw.rect(screen, WHITEx1, line_white_player)
            pygame.draw.rect(screen, WHITEx1, line_white_player2)
            pygame.draw.rect(screen, WHITEx1, line_white)
            pygame.draw.ellipse(screen, RED, ball)
            pygame.draw.rect(screen, BLUE, cpu)
            pygame.draw.rect(screen, BLUE, player)

            #Draw the score
            cpu_score_surface = score_font.render(str(cpu_points), True, BLUE)
            player_score_surface = score_font.render(str(player_points), True, BLUE)
            screen.blit(cpu_score_surface,(screen_width/10,20))
            screen.blit(player_score_surface,(3*screen_width/3.2,20))

            #Update the display
            pygame.display.update()
            clock.tick(200)

class Extreme():
    def fenetre_game():

        def reset_ball():
            global ball_speed_x, ball_speed_y
            ball.x = screen_width/2 - 10
            ball.y = random.randint(10,100)
            ball_speed_x *= random.choice([-1,1])
            ball_speed_y *= random.choice([-1,1])

        def point_won(winner):
            global cpu_points, player_points
            if winner == "cpu":
                cpu_points += 1
                song.Song.crie()
            if winner == "player":
                player_points += 1
                song.Song.crie()
            if winner == "reset":
                player_points = 0
                cpu_points = 0 

            reset_ball()

        def animate_ball():
            global ball_speed_x, ball_speed_y
            ball.x += ball_speed_x
            ball.y += ball_speed_y

            if ball.bottom >= screen_height or ball.top <= 0:
                ball_speed_y *= -1
                song.Song.ballerebondie()

            if ball.right >= screen_width:
                point_won("cpu")
                song.Song.ballerebondie()

            if ball.left <= 0:
                point_won("player")
                song.Song.ballerebondie()
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
            if ball.colliderect(player) or ball.colliderect(cpu):
                ball_speed_x *= -1

        player_speed = 6

        def animate_player():
            player.y += player_speed

            if player.top <= 0:
                player.top = 0

            if player.bottom >= screen_height:
                player.bottom = screen_height

        def animate_cpu():
            global cpu_speed
            cpu.y += cpu_speed

            if cpu.top <= 0:
                cpu.top = 0
            if cpu.bottom >= screen_height:
                cpu.bottom = screen_height

        pygame.init()

        screen_width = 1280
        screen_height = 800

        screen = pygame.display.set_mode((screen_width,screen_height))
        pygame.display.set_caption("pong")

        boutonrevenir = pygame.image.load("dessin/boutonrevenir.png").convert_alpha()

        boutonrevenir = bouton.Button(10, 10, boutonrevenir, 1)

        clock = pygame.time.Clock()

        # table bleu
        table_blue = pygame.Rect(0,0,925,1000)
        table_blue.centerx = screen_height/1.2

        # ligne blanche
        line_white = pygame.Rect(0,0,35,1000)
        line_white.centerx = screen_height/1.23

        # ligne blanche player 2
        line_white_player2 = pygame.Rect(0,0,35,1000)
        line_white_player2.centerx = screen_height/3.7

        # ligne blanche player 
        line_white_player = pygame.Rect(0,0,35,1000)
        line_white_player.centerx = screen_height/0.7

        #mesure de la balle 
        ball = pygame.Rect(0,0,52,52)
        ball.center = (screen_width/2, screen_height/2)

        #player 2 mesure
        cpu = pygame.Rect(0,0,25,150)
        cpu.centerx = screen_width/13

        #player mesure
        player = pygame.Rect(0,0,25,150)
        player.midright = (screen_width, screen_height/2)

        score_font = pygame.font.Font(None, 100)

        running = True

        while running:
            #Check for events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        player_speed = -6
                    if event.key == pygame.K_DOWN:
                        player_speed = 6

                if event.type == pygame.KEYDOWN:
                    global cpu_speed
                    if event.key == pygame.K_z:
                        cpu_speed = -6
                    if event.key == pygame.K_s:
                        cpu_speed = 6

            #Change the positions of the game objects
            animate_ball()
            animate_player()
            animate_cpu()
                
            #Clear the screen
            screen.fill(FOND)

            if boutonrevenir.draw(screen):
                running = False
                point_won("reset")


            #Draw the game objects
            pygame.draw.rect(screen, BLUEx1, table_blue)
            pygame.draw.rect(screen, WHITEx1, line_white_player)
            pygame.draw.rect(screen, WHITEx1, line_white_player2)
            pygame.draw.rect(screen, WHITEx1, line_white)
            pygame.draw.ellipse(screen, RED, ball)
            pygame.draw.rect(screen, BLUE, cpu)
            pygame.draw.rect(screen, BLUE, player)

            #Draw the score
            cpu_score_surface = score_font.render(str(cpu_points), True, BLUE)
            player_score_surface = score_font.render(str(player_points), True, BLUE)
            screen.blit(cpu_score_surface,(screen_width/10,20))
            screen.blit(player_score_surface,(3*screen_width/3.2,20))

            #Update the display
            pygame.display.update()
            clock.tick(300)
