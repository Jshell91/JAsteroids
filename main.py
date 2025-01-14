import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
	pygame.init()
	print("Starting asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	running = True

	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

	clock = pygame.time.Clock()
	dt = 0

	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()

	
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = (updatable)
	field = AsteroidField()
	Shot.containers = (shots, updatable, drawable)

	Player.containers = (updatable, drawable)

	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

	

	while running:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
			

		for upd in updatable:
			upd.update(dt)
		
		for ast in asteroids:
			if ast.colliding(player):
				print("GAME OVER")
				sys.exit()
			for shot in shots:
				if shot.colliding(ast):
					shot.kill()
					ast.split()

		

		screen.fill("black")

		for draw in drawable:
			draw.draw(screen)		
		
		pygame.display.flip()	

		dt = clock.tick(60) / 1000

if __name__ == "__main__":
	main()
