# ==========================================================
#  KAHOOT DEMO - question 12 (Bug hunt)
#  CHANGE: pygame.QUIT -> pygame.quit in the game loop
#  Look for "# <-- changed" (or "# <-- new") to find it.
#  Run this file after the question to reveal the answer.
# ==========================================================

# ==========================================================
#  DINO RUN - a small running game made with pygame
#
#  The dinosaur runs through the desert.
#  Plants and birds come towards it from the right side.
#    - Press SPACE to JUMP over a plant (or a bird).
#    - Press DOWN (arrow key) to DUCK under a bird.
#  If an obstacle hits the dinosaur - GAME OVER.
#  Press R to play again, or close the window to quit.
#
#  How the screen works:
#    The window is 1000 pixels wide and 500 pixels tall.
#    x = how far from the LEFT edge (0 is the left side).
#    y = how far from the TOP edge (0 is the top, so a BIGGER y is LOWER).
# ==========================================================

# "import" brings in ready-made tools that other people wrote for us.
import os # tools for working with folders and files
import pygame # the game library: windows, pictures, keyboard...
from sys import exit # exit() closes the program


# Make Python look for the pictures (the "res" folder) in lesson6 - the folder above this demo -
# no matter from which folder we started the game.
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

# Start pygame - we must do this before using anything else in pygame.
pygame.init()

# The clock controls how fast the game runs (how many frames per second).
clock = pygame.time.Clock()

# Open the game window: 1000 pixels wide, 500 pixels tall.
# "win" is the window - everything we draw goes on it.
win = pygame.display.set_mode((1000,500))

# ---------- Load all the pictures (only once, before the game starts) ----------

# The desert background, stretched to fill the whole window.
bm_img = pygame.image.load("res/desert.jpg")
bm_img = pygame.transform.scale(bm_img,(1000,500))

# Two pictures of the walking dinosaur. Switching between them
# again and again makes it look like the legs are moving (animation!).
dino_walking1_img = pygame.image.load("res/dino1.png")
dino_walking2_img = pygame.image.load("res/dino2.png")
dino_walking1_img = pygame.transform.scale(dino_walking1_img,(70,70)) # make it 70x70 pixels
dino_walking2_img = pygame.transform.scale(dino_walking2_img,(70,70))
current_walking = dino_walking1_img # the picture we show right now
dino_stopping_img = pygame.image.load("res/dino3.png") # (not used yet)

# Two kinds of plants. Each time a plant leaves the screen, the next one is the other kind.
plant1_img = pygame.image.load("res/plant1.png")
plant2_img = pygame.image.load("res/plant2.png")
current_plant = plant1_img

# Two bird pictures: wings up and wings down, to make the bird flap.
bird1_img = pygame.image.load("res/bird1.png")
bird2_img = pygame.image.load("res/bird2.png")
current_bird = bird1_img

# The dinosaur ducking (bending down) - used when we press DOWN.
bend_down_img = pygame.image.load("res/dino_down.png")
bend_down_img = pygame.transform.scale(bend_down_img,(70,70))

# A font (letters style and size 60) for writing "Game Over" on the screen.
font = pygame.font.SysFont(None, 60)

# ==========================================================
#  The OUTER loop - every time it goes around, a NEW game starts.
#  "while True" means: repeat forever (until the window is closed).
# ==========================================================
while True:
    # ---------- Reset everything for a new game ----------
    run = True # True = the game is still running, False = game over
    i=0 # how far the background has moved to the left
    j=0 # how far the plant has moved to the left (it starts at the right edge)
    k=400 # how far the bird has moved to the left (it starts closer than the plant)
    jump_i = 0 # how high the dinosaur is right now (0 = on the ground)
    bend_i = 0 # counts how long the dinosaur has been ducking
    # "modes" are like switches (True = on, False = off) that tell us what the dino is doing.
    jumping_up_mode = False # is the dino going UP?
    jumping_down_mode = False # is the dino falling DOWN?
    bend_down_mode = False # is the dino ducking?

    # ======================================================
    #  The GAME loop - it runs again and again, very fast.
    #  Each time around is one "frame": we move everything a tiny bit
    #  and draw a new picture. Many pictures per second = animation!
    # ======================================================
    while run:
        # Wait a little so the game runs at most 300 frames per second
        # (so it is not too fast on a fast computer).
        clock.tick(300)

        # ---------- 1. EVENTS: what did the player do? ----------
        # pygame keeps a list of everything that happened (keys pressed, mouse, closing the window).
        for event in pygame.event.get():
            # The player clicked the X to close the window -> stop the program.
            if event.type == pygame.quit: # <-- changed (was pygame.QUIT)
                pygame.quit()
                exit()
            # The player pressed a key.
            if event.type == pygame.KEYDOWN:
                # SPACE -> start a jump.
                if event.key == pygame.K_SPACE:
                    jumping_up_mode = True
                # DOWN arrow -> start ducking.
                if event.key == pygame.K_DOWN:
                    bend_down_mode = True

        # ---------- 2. THE BACKGROUND ----------
        # We draw the desert TWICE, one right after the other.
        # Both move left by "i" pixels, so it looks like the dino is running forward.
        # When the first one has moved completely out, the second one fills the screen.
        win.blit(bm_img,(-i,0)) # blit = "draw this picture at this (x, y) place"
        win.blit(bm_img,(1000-i,0))

        # When the background moved a whole screen (1000 pixels), start again from 0.
        # The picture looks the same, so the player can't notice - it looks endless!
        if i == 1000:
            i=0
        i=i+1 # move the background 1 pixel more next frame

        # ---------- 3. THE DINOSAUR ----------
        # The dino always stays at x=100. Only its height (y) changes.
        # Only ONE of these four parts runs each frame (if / elif / elif / else).

        # (a) Ducking: show the ducking picture for 120 frames, then stop ducking.
        if bend_down_mode == True:
           win.blit(bend_down_img,(100, 400))
           bend_i = bend_i + 1 # count one more frame of ducking
           if (bend_i == 120): # ducked long enough?
               bend_i = 0
               bend_down_mode = False # stand up again

        # (b) Jumping up: each frame the dino goes 1 pixel higher.
        #     Remember: a SMALLER y is HIGHER, so we draw it at 400 minus the height.
        elif jumping_up_mode == True:
            win.blit(current_walking, (100, 400-jump_i))
            jump_i = jump_i + 1
            if jump_i == 200: # reached the top (200 pixels high)?
                jumping_up_mode = False # stop going up...
                jumping_down_mode = True # ...and start falling down

        # (c) Falling down: each frame the dino goes 1 pixel lower.
        elif jumping_down_mode == True:
            win.blit(current_walking, (100, 400-jump_i))
            jump_i = jump_i - 1
            if jump_i == 0: # back on the ground?
                jumping_down_mode = False

        # (d) Walking on the ground: draw the dino and swap to the other walking picture,
        #     so the legs move.
        else:
            win.blit(current_walking, (100, 400))
            if current_walking == dino_walking1_img:
                current_walking = dino_walking2_img
            else:
                current_walking = dino_walking1_img

        # ---------- 4. THE PLANT ----------
        # The plant starts at the right edge (x=1000) and moves left 1 pixel each frame.
        win.blit(current_plant,(1000-j,350))
        j = j+1
        # When it has crossed the whole screen, bring it back to the right edge
        # and switch to the other kind of plant.
        if (j==1000):
            j=0
            if current_plant == plant1_img:
                current_plant = plant2_img
            else:
                current_plant = plant1_img

        # ---------- 5. THE BIRD ----------
        # The bird flies left 1 pixel each frame, a bit higher than the plant (y=370).
        win.blit(current_bird, (1000 - k, 370))
        k = k + 1
        # When it has crossed the whole screen, bring it back to the right edge.
        if (k == 1000):
            k = 0
        # Swap between the two bird pictures every frame, so the wings flap.
        if current_bird == bird1_img:
            current_bird = bird2_img
        else:
            current_bird = bird1_img

        # ---------- 6. DID WE CRASH? (collision check) ----------
        # The obstacle "hits" the dino when it reaches x=150 (where the dino is standing).

        # Plant: the only way to survive is to be in the air (jumping up or falling down).
        if 1000-j == 150 and jumping_up_mode == False and jumping_down_mode == False: # plant reached the dino
            run  = False # game over!
        # Bird: you survive if you are ducking OR jumping.
        if 1000 - k == 150 and bend_down_mode == False and jumping_up_mode == False and jumping_down_mode == False: # bird reached the dino
            run = False # game over!

        # ---------- 7. SHOW IT ----------
        # Everything above was drawn "behind the curtain".
        # update() opens the curtain and shows the new picture on the screen.
        pygame.display.update()

    # ==========================================================
    #  GAME OVER - we get here when "run" became False.
    # ==========================================================
    # Write the message in red. Colors are (Red, Green, Blue), each from 0 to 255.
    text = font.render("Game Over - press R to restart", True, (200, 0, 0))
    # Put the text in the middle: half the window (500) minus half the text width.
    win.blit(text, (500 - text.get_width() // 2, 200))
    pygame.display.update()

    # Wait here until the player presses R (new game) or closes the window.
    # We still have to read the events, otherwise the window "freezes".
    waiting = True
    while waiting:
        clock.tick(30) # no need to be fast here - nothing is moving
        for event in pygame.event.get():
            # Closed the window -> quit the program.
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            # Pressed R -> stop waiting. The outer loop goes around again = a new game!
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                waiting = False