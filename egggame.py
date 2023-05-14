import os
import random
import pygame
import sys
from pygame.locals import *

# pygame setup
pygame.init()
width, height = 800, 500
screen = pygame.display.set_mode((width, height))
background = pygame.image.load(os.path.join('background.jpg'))
background = pygame.transform.scale(background, (width, height))
nest = pygame.image.load(os.path.join('nwst.png'))
nest_size = pygame.transform.scale(nest, (200, 200))

x = 200
y = 200
vel = 10
vele = 3

def spawn_egg():
    egg_image = pygame.image.load(os.path.join('egg2.png'))
    egg_size = pygame.transform.scale(egg_image, (60, 70))
    egg_x = random.randint(0, width - 50)
    egg_y = -50
    egg_rect = pygame.Rect(egg_x, egg_y, 50, 50)
   
    return egg_rect, egg_size

score = 0
font = pygame.font.Font(None, 36)

def egg_hit(nest_rect, eggs):
    global score
    for obj_rect, obj_size  in eggs:
        if obj_rect.colliderect(nest_rect):
            eggs.remove((obj_rect, obj_size))
            score += 1

def draw_window(nest_move, egg_move):
    screen.blit(nest_size, (nest_move.x, nest_move.y))
    
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
    
    pygame.display.update()

def main():
    clock = pygame.time.Clock() 
    running = True
    nest_move = pygame.Rect(300, 340, 200, 155)
    egg_move = pygame.Rect(30, 40, 200, 155)
    eggs = []
    SPAWN_INTERVAL = 120
    spawn_counter = 0

    while running:
        screen.blit(background, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        keys = pygame.key.get_pressed()
        egg_move.y += vel
        if keys[pygame.K_LEFT] and nest_move.x > -50:
            nest_move.x -= vel
            
        if keys[pygame.K_RIGHT] and nest_move.x < 1450 - width:
            nest_move.x += vel
        
        egg_hit(nest_move, eggs)
        
        draw_window(nest_move, egg_move)
        
        spawn_counter += 1
        if spawn_counter >= SPAWN_INTERVAL:
            new_egg_rect, new_egg_size = spawn_egg()
            eggs.append((new_egg_rect, new_egg_size))
            spawn_counter = 3

        for obj_rect, obj_size in eggs:
            obj_rect.y += vele
            screen.blit(obj_size, (obj_rect.x, obj_rect.y))

        pygame.display.update()
        clock.tick(60)  

    pygame.quit()
    
if __name__ == "__main__":
    main()
