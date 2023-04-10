
import pgzrun
import pygame
import pgzero
from random import randint
from pgzero.builtins import Actor
import time


WIDTH = 800
HEIGHT = 600
CENTER_X = WIDTH / 2
CENTER_Y = HEIGHT / 2
pygame.display.set_mode((WIDTH, HEIGHT))

# Flag Variables
game_over = False
finalized = False
garden_happy = True
fangflower_collision = False
raining = False

time_elapsed = 0
start_time = time.time()

cow = Actor("cow")
cow.pos = 100, 500 # Starting position

flower_list = []
wilted_list = []
fangflower_list = []

fangflower_vy_list = [] # generates motion of fangflower on y axis.
fangflower_vx_list = [] # generates motion of fangflower on x axis.

def draw():
    global game_over, time_elapsed, finalized, raining # global variable rain
    if not game_over:
        raining = True # enable rain for entire duration
        screen.clear()
        screen.blit("garden-raining", (0, 0))
        cow.draw()
        for flower in flower_list:
            flower.draw()
        for fangflower in fangflower_list:
            fangflower.draw()
        time_elapsed = int(time.time() - start_time)
        screen.draw.text(
            "Garden happy for: " +
            str(time_elapsed) + " seconds",
            topleft=(10, 10), color="black"
        )
    else:
        if not finalized:
            cow.draw()
            screen.draw.text(
                "Garden happy for: " +
                str(time_elapsed) + " seconds",
                topleft=(10, 10), color="black"
            )
        if (not garden_happy):
            #game over indicator
            screen.draw.text(
                "GARDEN UNHAPPY... GAME OVER!", color="black",
                topleft=(10, 50)
            )
            finalized = True
        else:  
            # game over due to fangflower
            screen.draw.text(
                "FANGFLOWER ATTACK... GAME OVER!", color="black",
                topleft=(10, 50)
            )
            finalized = True # makes sure the code is not run again
    return
# Add a Flower
def new_flower():
    global flower_list, wilted_list 
    flower_new = Actor("flower")
    flower_new.pos = randint(50, WIDTH - 50), randint(150, HEIGHT - 100) 
    flower_list.append(flower_new) 
    wilted_list.append("happy") 
    return

# Adding more flowers to the garden
def add_flowers():
    global game_over
    if not game_over:
        new_flower() 
        clock.schedule(add_flowers, 2) # Calls for new flowers and for every 2 seconds
    return

def check_wilt_times():
    global wilted_list, game_over, garden_happy
    if wilted_list: 
        for wilted_since in wilted_list: 
            if (not wilted_since == "happy"):
                time_wilted = int(time.time() - wilted_since)
                if (time_wilted) > 30.0: 
                    garden_happy = False
                    game_over = True
                    break
    return

def wilt_flower():
    global flower_list, wilted_list, game_over
    if not game_over:
        if flower_list:
            rand_flower = randint(0, len(flower_list) - 1) 
        if (flower_list[rand_flower].image == "flower"): 
            flower_list[rand_flower].image = "flower-wilt" 
            wilted_list[rand_flower] = time.time() 
        clock.schedule(wilt_flower, 3) 
    return

def check_flower_collision():
    global cow, flower_list, wilted_list 
    index = 0 
    for flower in flower_list: # loops through all the flowers in the list
        if(flower.colliderect(cow) and flower.image == "flower-wilt"): 
            flower.image = "flower" 
            wilted_list[index] = "happy" 
            break 
        index = index + 1 
    return

def check_fangflower_collision():
    # Global Variables
    global cow, fangflower_list, fangflower_collision
    global game_over
    for fangflower in fangflower_list:
        if fangflower.colliderect(cow): #collision detection between fangflower and cow
            cow.image = "zap" 
            game_over = True 
            break 
    return

def velocity():
     random_dir = randint(0, 1)
     random_velocity = randint(2, 3)
     if random_dir == 0: 
         return -random_velocity
     else: #
         return random_velocity

def mutate():
      # global variables
      global flower_list, fangflower_list, fangflower_vy_list
      global fangflower_vx_list, game_over
     
      if not game_over and flower_list:
          rand_flower = randint(0, len(flower_list) - 1) 
          fangflower_pos_x = flower_list[rand_flower].x
          fangflower_pos_y = flower_list[rand_flower].y
          del flower_list[rand_flower] 
          fangflower = Actor("fangflower")
          fangflower.pos = fangflower_pos_x, fangflower_pos_y 
          fangflower_vx = velocity() 
          fangflower_vy = velocity() 
          fangflower = fangflower_list.append(fangflower) 
          # fangflower’s velocities are added to these lists.
          fangflower_vx_list.append(fangflower_vx)
          fangflower_vy_list.append(fangflower_vy)
          clock.schedule(mutate, 5) # schedules ever 5 seconds
          return

def update_fangflowers():
    # Global Variables
    global fangflower_list, game_over
    if not game_over:
        index = 0 
        for fangflower in fangflower_list: 
           
            fangflower_vx = fangflower_vx_list[index]
            fangflower_vy = fangflower_vy_list[index]
            
            fangflower.x = fangflower.x + fangflower_vx
            fangflower.y = fangflower.y + fangflower_vy
            if fangflower.left < 0: 
                fangflower_vx_list[index] = -fangflower_vx
            if fangflower.right > WIDTH:
                fangflower_vx_list[index] = -fangflower_vx
            if fangflower.top < 150:
                fangflower_vy_list[index] = -fangflower_vy
            if fangflower.bottom > HEIGHT: 
                fangflower_vy_list[index] = -fangflower_vy
            index = index + 1
            return


def reset_cow():
    global game_over
    if not game_over:
        cow.image = "cow" 
    return

add_flowers()

wilt_flower()


# Updates the Actor Cow to move around the GUI window
def update():
    global score, game_over, fangflower_collision
    global flower_list, fangflower_list, time_elapsed
    fangflower_collision = check_fangflower_collision()
    check_wilt_times() # Checks how long flowers have been wilted
    if not game_over:
        if keyboard.space: 
            cow.image = "cow-water" # changes to watering cow
            clock.schedule(reset_cow, 0.5) # reset cow
            check_flower_collision() # checks proximity distance between flower and cow
        if keyboard.left and cow.x > 0:
            cow.x -= 5
        elif keyboard.right and cow.x < WIDTH:
            cow.x += 5
        elif keyboard.up and cow.y > 150:
            cow.y -= 5
        elif keyboard.down and cow.y < HEIGHT:
            cow.y += 5

        if time_elapsed > 15 and not fangflower_list:
            mutate() # Calls function to update
        update_fangflowers() 

pgzrun.go()
