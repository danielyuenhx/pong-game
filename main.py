import pygame, sys
import random

pygame.init()

# setting up the window
clock = pygame.time.Clock()
SCREEN_WIDTH = 666
SCREEN_HEIGHT = 500
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Pong Game')

# setting up the shapes
ball = pygame.Rect(SCREEN_WIDTH/2-7.5, SCREEN_HEIGHT/2-7.5, 15, 15)
player = pygame.Rect(5, SCREEN_HEIGHT/2-35, 5, 70)
bot = pygame.Rect(SCREEN_WIDTH-10, SCREEN_HEIGHT/2-35, 5, 70)

# colours
white = (255,255,255)
gray = pygame.Color('grey12')

# speeds
x_ball_speed = 3.5 * random.choice((1,-1))
y_ball_speed = 3.5 * random.choice((1,-1))

player_speed = 0 
bot_speed = 7

def animate_ball():
    global x_ball_speed
    global y_ball_speed

    # animating the ball
    ball.x += x_ball_speed
    ball.y += y_ball_speed

    # out of bounds
    if ball.top <= 0 or ball.bottom >= SCREEN_HEIGHT:
        y_ball_speed *= -1
    if ball.left <= 0 or ball.right >= SCREEN_WIDTH:
        restart_game()

    if ball.colliderect(player) or ball.colliderect(bot):
        x_ball_speed *= -1

def animate_player():
    global player_speed
    player.y += player_speed
    prevent_out_of_bounds(player)

def animate_bot():
    global bot_speed
    if bot.top <= ball.y:
        bot.y += bot_speed
    elif bot.bottom >= ball.y:
        bot.y -= bot_speed
    prevent_out_of_bounds(bot)

def prevent_out_of_bounds(player):
    if player.top <= 0: 
        player.top = 0
    elif player.bottom >= SCREEN_HEIGHT:
        player.bottom = SCREEN_HEIGHT

def restart_game():
    global x_ball_speed
    global y_ball_speed

    ball.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    x_ball_speed *= random.choice((1,-1))
    y_ball_speed *= random.choice((1,-1))

while True:
    for event in pygame.event.get():
        # user quit
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # on key down
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 7
            if event.key == pygame.K_UP:
                player_speed -= 7
        # on key up
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 7
            if event.key == pygame.K_UP:
                player_speed += 7

    animate_ball()
    animate_player()
    animate_bot()

    # drawing objects on screen
    screen.fill(gray)
    pygame.draw.ellipse(screen, white, ball)
    pygame.draw.rect(screen, white, player)
    pygame.draw.rect(screen, white, bot)
    pygame.draw.aaline(screen, white, (SCREEN_WIDTH/2,0), (SCREEN_WIDTH/2, SCREEN_HEIGHT))

    pygame.display.update()
    clock.tick(60)

        