import pygame
import random
import sys
import os


dirpath = os.getcwd()
sys.path.append(dirpath)

if getattr(sys, "frozen", False):
    os.chdir(sys._MEIPASS)


def ball_animation():
    global ball_speed_x, ball_speed_y, player_points, opponent_points
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1

    if ball.left <= 0:
        player_points += 1
        print(f'Players {player_points} VS {opponent_points} Opponent')
        ball_restart_opponent()

    if ball.right >= screen_width:
        opponent_points += 1
        print(f'Players {player_points} VS {opponent_points} Opponent')
        ball_restart_player()

    if ball.colliderect(player) or ball.colliderect(opponent):
        bip.play()
        ball_speed_x *= -1


def player_animation():
    global player_speed
    player.y += player_speed

    if player.top <= 0:
        player_speed = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height


def opponent_animation():
    global opponent_speed
    opponent.y += opponent_speed

    if opponent.top <= 0:
        opponent_speed = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height


def ball_restart_player():
    global ball_speed_x, ball_speed_y
    point.play()

    Qhalf_x = 1280 / 1.5
    Qhalf_y = 960 / 1.5

    ball.x = random.randint(int(Qhalf_x), 1280)
    ball.y = random.randint(int(Qhalf_y), 960)
    ball_speed_x *= -1
    ball_speed_y *= random.choice([-1, 1])


def ball_restart_opponent():
    global ball_speed_x, ball_speed_y
    point.play()

    Qhalf_x = 1280 / 4
    Qhalf_y = 960 / 4
    half_x = 1280 / 2
    half_y = 960 / 2

    ball.x = random.randint(int(Qhalf_x), int(half_x))
    ball.y = random.randint(int(Qhalf_y), int(half_y))
    ball_speed_x *= -1
    ball_speed_y *= random.choice([-1, 1])


# General Setup
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('data/awesomeness.wav')
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)
bip = pygame.mixer.Sound('data/bip.wav')
point = pygame.mixer.Sound('data/point.wav')
bip.set_volume(0.2)
point.set_volume(0.2)
clock = pygame.time.Clock()

# Setting up the main window

screen_width = 1280
screen_height = 960

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong')

ball = pygame.Rect(screen_width/2 - 15, screen_height/2 - 15, 30, 30)
player = pygame.Rect(screen_width - 20, screen_height/2 - 70,  10, 140)
opponent = pygame.Rect(10, screen_height/2 - 70, 10, 140)

Player_rect_points = pygame.Rect(screen_width/2 - 50, screen_height - 15, 30, 30)
Opponent_rect_points = pygame.Rect(screen_width/2 + 50, screen_height - 15, 30, 30)

bg_color = pygame.Color('grey12')
light_grey = (200, 200, 200)

ball_speed_x = 7
ball_speed_y = 7

player_speed = 0
opponent_speed = 0

player_points = 0
opponent_points = 0

while True:
    # Handling input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 7
            if event.key == pygame.K_UP:
                player_speed -= 7

        if event.type == pygame.KEYUP:

            if event.key == pygame.K_DOWN:
                player_speed -= 7
            if event.key == pygame.K_UP:
                player_speed += 7

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                opponent_speed += 7
            if event.key == pygame.K_w:
                opponent_speed -= 7

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                opponent_speed = 0
            if event.key == pygame.K_s:
                opponent_speed = 0

        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_SPACE:
        #         ball_speed_x == 7
        #         ball_speed_y == 7
        #         if ball_speed_x == 7 and ball_speed_y == 7:
        #             pass

    ball_animation()
    player_animation()
    opponent_animation()

    # Visuals
    screen.fill(bg_color)
    # pygame.draw.rect(screen, light_grey, player_points)
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, opponent)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.aaline(screen, light_grey, (screen_width/2, 0), (screen_width/2, screen_height))

    # Updating the window
    pygame.display.flip()
    clock.tick(60)
