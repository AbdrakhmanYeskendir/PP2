import pygame  
import random  
import time  

# Initialize Pygame and the mixer for sound  
pygame.init()  
pygame.mixer.init()  

# Set up game clock and frames per second (FPS)  
clock = pygame.time.Clock()  
FPS = 60  

# Set display dimensions  
WIDTH, HEIGHT = 400, 600  
screen = pygame.display.set_mode((WIDTH, HEIGHT))  

# Load images for the background, player, enemy, and coin  
background = pygame.image.load(r"C:\Users\Acer\Desktop\Python\AnimatedStreet.png")  
player_img = pygame.image.load(r"C:\Users\Acer\Desktop\Python\Player.png")  
enemy_img = pygame.image.load(r"C:\Users\Acer\Desktop\Python\Enemy.png")  
coin_img = pygame.image.load(r"C:\Users\Acer\Desktop\Python\coin.png")  

# Load and play background music  
pygame.mixer.music.load(r"C:\Users\Acer\Desktop\Python\background.wav")  
crash_sound = pygame.mixer.Sound(r"C:\Users\Acer\Desktop\Python\crash.wav")  
pygame.mixer.music.play(-1)  # Loop background music indefinitely  

# Set up fonts for text display  
font = pygame.font.SysFont("Verdana", 60)  
game_over = font.render("Game Over", True, "red")  # Game Over text  
coin_count_font = pygame.font.SysFont("Verdana", 20)  # Font for showing coins  

# Define speeds and coin count  
PLAYER_SPEED = 5  # Speed for the player  
ENEMY_SPEED = 4   # Initial speed for enemies  
COIN_SPEED = 2    # Speed for coins  
COIN_COUNT_TO_INCREASE_SPEED = 5  # Every five coins increase enemy speed  
coin_count = 0    # Counter for collected coins  

def increase_enemy_speed():  
    """Increase the speed of all enemies."""  
    for enemy in enemy_sprites:  
        enemy.speed += 1  

class Player(pygame.sprite.Sprite):  
    """Player class representing the player character."""  
    def __init__(self):  
        super().__init__()  
        self.image = player_img  # Load player image  
        self.rect = self.image.get_rect(center=(WIDTH // 2, HEIGHT - 50))  # Set initial position  
    
    def move(self):  
        """Handle player movement based on keyboard input."""  
        keys = pygame.key.get_pressed()  
        if keys[pygame.K_LEFT]:  
            self.rect.x -= PLAYER_SPEED  
        if keys[pygame.K_RIGHT]:  
            self.rect.x += PLAYER_SPEED  
        self.rect.clamp_ip(screen.get_rect())  # Keep player within screen boundaries  

class Enemy(pygame.sprite.Sprite):  
    """Enemy class representing the enemies in the game."""  
    def __init__(self):  
        super().__init__()  
        self.image = enemy_img  # Load enemy image  
        self.rect = self.image.get_rect()  
        self.speed = ENEMY_SPEED  # Initial enemy speed  
        self.generate_random_position()  # Generate initial enemy position  
    
    def move(self):  
        """Move the enemy down the screen."""  
        self.rect.y += self.speed  
        if self.rect.top > HEIGHT:  # If the enemy goes off the screen  
            self.generate_random_position()  # Reposition it at the top  
    
    def generate_random_position(self):  
        """Generate a random starting position for the enemy."""  
        self.rect.x = random.randint(0, WIDTH - self.rect.w)  # Random horizontal position  
        self.rect.y = -self.rect.h  # Spawn above the screen  

class Coin(pygame.sprite.Sprite):  
    """Coin class representing collectible coins in the game."""  
    def __init__(self):  
        super().__init__()  
        self.generate_random_coin()  # Initialize the coin's starting position  
    
    def move(self):  
        """Move the coin down the screen."""  
        self.rect.y += COIN_SPEED  
        if self.rect.top > HEIGHT:  # If the coin goes off the screen  
            self.generate_random_coin()  # Reposition it at the top  
    
    def generate_random_coin(self):  
        """Generate a random position and size for the coin."""  
        size = random.randint(30, 60)  # Random size for coins  
        self.image = pygame.transform.scale(coin_img, (size, size))  # Scale image  
        self.rect = self.image.get_rect()  
        self.rect.x = random.randint(0, WIDTH - self.rect.w)  # Random horizontal position  
        self.rect.y = -self.rect.h  # Spawn above the screen  

# Create game objects  
player = Player()  
enemies = [Enemy() for _ in range(1)]  # Initial enemy  
coin = Coin()  

# Create sprite groups for efficient management  
# Create sprite groups for efficient management  
all_sprites = pygame.sprite.Group(player, *enemies, coin)  # Group all sprites  
enemy_sprites = pygame.sprite.Group(*enemies)  # Group for enemies  
coin_sprites = pygame.sprite.Group(coin)  # Group for coins  

# Main game loop  
running = True  
while running:  
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            running = False  # Exit the loop if the window is closed  

    # Draw the background  
    screen.blit(background, (0, 0))  
    
    # Move game objects  
    player.move()  # Move the player  
    for enemy in enemy_sprites:  
        enemy.move()  # Move each enemy  
    coin.move()  # Move the coin  
    
    # Draw all sprites on the screen  
    all_sprites.draw(screen)  
    
    # Check for collisions with the coin  
    if pygame.sprite.spritecollideany(player, coin_sprites):  
        coin_count += 1  # Increase coin count  
        coin.generate_random_coin()  # Reposition the coin  
        if coin_count % COIN_COUNT_TO_INCREASE_SPEED == 0:  # Check if it's time to increase speed  
            increase_enemy_speed()  # Increase enemy speed  
            new_enemy = Enemy()  # Create a new enemy  
            enemy_sprites.add(new_enemy)  # Add new enemy to the enemy group  
            all_sprites.add(new_enemy)  # Add new enemy to the all_sprites group  
    
    # Check for collisions with enemies  
    if pygame.sprite.spritecollideany(player, enemy_sprites):  
        crash_sound.play()  # Play crash sound effect  
        time.sleep(1)  # Pause for a moment  
        screen.fill("black")  # Fill screen with black for Game Over effect  
        screen.blit(game_over, game_over.get_rect(center=(WIDTH // 2, HEIGHT // 2)))  # Draw Game Over message  
        pygame.display.flip()  # Update the display  
        time.sleep(2)  # Wait before exiting  
        running = False  # End the game loop  
    
    # Display the current coin count  
    counting = coin_count_font.render(f"Coins: {coin_count}", True, "black")  # Render the coin count  
    screen.blit(counting, (WIDTH - 100, 10))  # Draw the coin count on the screen  

    # Update the display  
    pygame.display.flip()  
    clock.tick(FPS)  # Maintain the frame rate at 60 frames per second  

pygame.quit()  # Cleanly exit Pygame  