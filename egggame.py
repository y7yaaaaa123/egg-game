import os
import random
import pygame
import sys
from pygame.locals import *

# Pygame setup
pygame.init()
pygame.mixer.init()
width, height = 800, 500
screen = pygame.display.set_mode((width, height))
background = pygame.image.load(os.path.join('background.jpg'))
background = pygame.transform.scale(background, (width, height))
nest = pygame.image.load(os.path.join('nwst.png'))
nest_size = pygame.transform.scale(nest, (200, 200))
crash_sound = pygame.mixer.Sound("bck.wav")
crash_sound.play(-1)

crash_sound.set_volume(0.3)

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
    for egg_rect, egg_size in eggs:
        if nest_rect.colliderect(egg_rect):
            eggs.remove((egg_rect, egg_size))
            score += 1
            crash_sound = pygame.mixer.Sound("egg_hit.wav")
            crash_sound.play()
            # Check if the egg hits the center of the nest

def draw_window(nest_move, eggs):
    screen.blit(background, (0, 0))
    
    # Draw bounding box around nest
   # pygame.draw.rect(screen, (255, 10, 0), nest_move)
    
    # Calculate the center position of the nest
    nest_center_x = nest_move.centerx - nest_size.get_width() // 2
    nest_center_y = nest_move.centery - nest_size.get_height() // 2
    
    # Blit the nest at the calculated center position
    screen.blit(nest_size, (nest_center_x, nest_center_y))
    
    for obj_rect, obj_size in eggs:
        screen.blit(obj_size, (obj_rect.x, obj_rect.y))
    
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
    
    pygame.display.update()

def main():
    clock = pygame.time.Clock() 
    running = True
    nest_move = pygame.Rect(300, 360, 120, 90)
    eggs = []
    SPAWN_INTERVAL = 60  # Adjusted spawn interval
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_LEFT] and nest_move.x > -0.5:
            nest_move.x -= vel
            
        if keys[pygame.K_RIGHT] and nest_move.x < 1460 - width:
            nest_move.x += vel
        
        egg_hit(nest_move, eggs)
        
        egg_move = pygame.Rect(30, 40, 200, 155)
        egg_move.y += vel
        
        draw_window(nest_move, eggs)
        
        if len(eggs) < 5:  # Spawn more eggs if the current count is less than 5
            spawn_counter = random.randint(0, SPAWN_INTERVAL)
            if spawn_counter == 0:
                new_egg_rect, new_egg_size = spawn_egg()
                eggs.append((new_egg_rect, new_egg_size))

        for obj_rect, obj_size in eggs:
            obj_rect.y += vele
        
        pygame.display.update()
        clock.tick(60)  

    pygame.quit()
    
if __name__ == "__main__":
    main()
