import sys
import math
import pygame
from pygame.locals import *

# Constants
S_WIDTH = 640
S_HEIGHT = 480
FPS = 60
BALL_R = 7
P_WIDTH = 10
P_HEIGHT = 100
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Init
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((S_WIDTH, S_HEIGHT))

# Initial conditions
ball_pos = [S_WIDTH//2, S_HEIGHT//2] # must be int
ball_delta = [1, -1];
p1 = pygame.Rect(0, (S_HEIGHT-P_HEIGHT)/2, P_WIDTH, P_HEIGHT)
p1_move = 0
p2 = pygame.Rect((S_WIDTH-P_WIDTH), (S_HEIGHT-P_HEIGHT)/2, P_WIDTH, P_HEIGHT)
p2_move = 0

def checkCollision(ball_pos, p1, p2):
	# y = y0 +/- sqrt(R^2 - (x-x0)^2)
	# p = p1 if (S_WIDTH - ball_pos[0]) > ball_pos[0] else p2
	if (ball_pos[0] - BALL_R == p1.right) and (ball_pos[1] in range(p1.top, p1.bottom)):
		return True
	elif (ball_pos[0] + BALL_R == p2.left) and (ball_pos[1] in range(p2.top, p2.bottom)):
		return True
	else:
		return False

# Loop
while True:
	# Clear screen
	screen.fill(BLACK)
	pygame.display.set_caption('PONG')
	pygame.mouse.set_visible(0)

	# Inputs
	for event in pygame.event.get():
		if event.type == KEYDOWN:
			if event.key == K_w:
				p1_move = -1
			elif event.key == K_s:
				p1_move = +1
			elif event.key == K_UP:
				p2_move = -1
			elif event.key == K_DOWN:
				p2_move = +1
		elif event.type == KEYUP:
			if event.key == K_w:
				p1_move = 0
			elif event.key == K_s:
				p1_move = 0
			elif event.key == K_UP:
				p2_move = 0
			elif event.key == K_DOWN:
				p2_move = 0
		elif event.type == QUIT:
			pygame.quit()
			sys.exit()
	
	# Handle input
	p1.y += p1_move * 5;
	p2.y += p2_move * 5;

	# Keep elements in place
	if p1.bottom > S_HEIGHT:
		p1.bottom = S_HEIGHT
	elif p1.top < 0:
		p1.top = 0
	if p2.bottom > S_HEIGHT:
		p2.bottom = S_HEIGHT
	elif p2.top < 0:
		p2.top = 0

	# Render elements
	pygame.draw.rect(screen, WHITE, p1)
	pygame.draw.rect(screen, WHITE, p2)
	pygame.draw.circle(screen, WHITE, ball_pos, BALL_R)

	# Wall collisions
	if (ball_pos[0] - BALL_R) == 0 or (ball_pos[0] + BALL_R) == S_WIDTH:
		ball_delta[0] *= -1
	if (ball_pos[1] - BALL_R) == 0 or (ball_pos[1] + BALL_R) == S_HEIGHT:
		ball_delta[1] *= -1

	# Paddle collisions
	if checkCollision(ball_pos, p1, p2):
		ball_delta[0] *= -1

	# Bounce
	ball_pos[0] += ball_delta[0];
	ball_pos[1] += ball_delta[1];

	# Update
	pygame.display.update()
	clock.tick(FPS)
