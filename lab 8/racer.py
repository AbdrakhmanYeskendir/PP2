# Imports  
import pygame, sys  
from pygame.locals import *  
import random, time  

# Initializing Pygame  
pygame.init()  

# Setting up FPS (Frames Per Second)  
FPS = 60  
FramePerSec = pygame.time.Clock()  

# Creating colors  
BLUE  = (0, 0, 255)  
RED   = (255, 0, 0)  
GREEN = (0, 255, 0)  
BLACK = (0, 0, 0)  
WHITE = (255, 255, 255)  

# Other Variables for use in the program  
SCREEN_WIDTH = 400  
SCREEN_HEIGHT = 600  
SPEED = 5  # Speed at which enemies fall  
SCORE = 0  # Player's score  

# Setting up Fonts  
font = pygame.font.SysFont("Verdana", 60)  
font_small = pygame.font.SysFont("Verdana", 20)  
game_over = font.render("Game Over", True, BLACK)  

# Load background image  
background = pygame.image.load("AnimatedStreet.png")  

# Create a white screen  
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  
DISPLAYSURF.fill(WHITE)  
pygame.display.set_caption("Game")  


class Enemy(pygame.sprite.Sprite):  
    def __init__(self):  
        super().__init__()  
        self.image = pygame.image.load("Enemy.png")  # Load enemy image  
        self.rect = self.image.get_rect()  
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)  # Start position at the top  

    def move(self):  
        global SCORE  
        self.rect.move_ip(0, SPEED)  # Move the enemy down by SPEED  
        if self.rect.bottom > SCREEN_HEIGHT:  
            SCORE += 1  # Increase score when enemy goes off screen  
            self.rect.top = 0  # Reset position to the top  
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)  # Randomize horizontal position  


class Player(pygame.sprite.Sprite):  
    def __init__(self):  
        super().__init__()  
        self.image = pygame.image.load("Player.png")  # Load player image  
        self.rect = self.image.get_rect()  
        self.rect.center = (160, 520)  # Set initial position  

    def move(self):  
        pressed_keys = pygame.key.get_pressed()  # Get the currently pressed keys  
        
        # Move left  
        if self.rect.left > 0 and pressed_keys[K_LEFT]:  
            self.rect.move_ip(-5, 0)  
        # Move right  
        if self.rect.right < SCREEN_WIDTH and pressed_keys[K_RIGHT]:  
            self.rect.move_ip(5, 0)  


# Setting up Sprites        
P1 = Player()  # Create player object  
E1 = Enemy()   # Create enemy object  

# Creating Sprite Groups  
enemies = pygame.sprite.Group()  
enemies.add(E1)  # Add enemy to the group  
all_sprites = pygame.sprite.Group()  
all_sprites.add(P1)  # Add player to the group  
all_sprites.add(E1)  # Add enemy to the group  

# Adding a new User event for increasing speed  
INC_SPEED = pygame.USEREVENT + 1  
pygame.time.set_timer(INC_SPEED, 1000)  # Increment speed every second  

# Game Loop  
while True:  
    # Cycles through all events occurring  
    for event in pygame.event.get():  
        if event.type == INC_SPEED:  
            SPEED += 0.5  # Increase speed of enemies  
        if event.type == QUIT:  
            pygame.quit()  # Quit game on exit  
            sys.exit()  

    # Draw background  
    DISPLAYSURF.blit(background, (0, 0))  
    scores = font_small.render(str(SCORE), True, BLACK)  # Render score text  
    DISPLAYSURF.blit(scores, (10, 10))  

    # Moves and Re-draws all Sprites  
    for entity in all_sprites:  
        entity.move()  # Move each sprite  
        DISPLAYSURF.blit(entity.image, entity.rect)  # Draw each sprite  

    # Check for collision between Player and Enemy  
    if pygame.sprite.spritecollideany(P1, enemies):  
        pygame.mixer.Sound('crash.wav').play()  # Play crash sound  
        time.sleep(1)  # Delay for dramatic effect  
                   
        DISPLAYSURF.fill(RED)  # Fill screen with red for Game Over  
        DISPLAYSURF.blit(game_over, (30, 250))  # Display Game Over message  

        pygame.display.update()  # Update display  
        for entity in all_sprites:  
            entity.kill()  # Remove all sprites  
        time.sleep(2)  # Wait before closing  
        pygame.quit()  # Quit Pygame  
        sys.exit()        
        
    pygame.display.update()  # Update display for the current frame  
    FramePerSec.tick(FPS)  # Maintain the specified frames per second  