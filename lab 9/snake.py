import pygame  
import random  
import time  

# Initialize Pygame  
pygame.init()  

# Set dimensions for the game window  
WIDTH, HEIGHT = 600, 600  
CELL = 30  # Size of each cell in the grid  
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Create the display screen  

# Define color constants  
colorWHITE = (255, 255, 255)  
colorGRAY = (200, 200, 200)  
colorBLACK = (0, 0, 0)  
colorRED = (255, 0, 0)  
colorGREEN = (0, 255, 0)  
colorBLUE = (0, 0, 255)  
colorYELLOW = (255, 255, 0)  

def draw_grid_chess():  
    """Draw a checkerboard grid on the screen."""  
    colors = [colorWHITE, colorGRAY]  
    # Loop through half the height and half the width to draw the grid  
    for i in range(HEIGHT // CELL):  
        for j in range(WIDTH // CELL):  
            pygame.draw.rect(screen, colors[(i + j) % 2], (i * CELL, j * CELL, CELL, CELL))  # Alternating colors  

class Point:  
    """Class representing a point in the grid."""  
    def __init__(self, x, y):  
        self.x = x  # X-coordinate  
        self.y = y  # Y-coordinate  

class Snake:  
    """Class representing the snake in the game."""  
    def __init__(self):  
        # Initialize snake body with three segments  
        self.body = [Point(10, 11), Point(10, 12), Point(10, 13)]  
        self.dx, self.dy = 1, 0  # Initial direction of movement  
        self.grow = False  # Flag to indicate if the snake should grow  

    def move(self):  
        """Move the snake in the current direction."""  
        if self.grow:  # If the snake should grow  
            self.body.append(Point(self.body[-1].x, self.body[-1].y))  # Add a new segment at the tail  
            self.grow = False  # Reset the grow flag  
            
        # Move each segment to the position of the segment in front of it  
        for i in range(len(self.body) - 1, 0, -1):  
            self.body[i].x = self.body[i - 1].x  
            self.body[i].y = self.body[i - 1].y  
        
        # Move the head of the snake  
        self.body[0].x += self.dx  
        self.body[0].y += self.dy  

    def draw(self):  
        """Draw the snake on the screen."""  
        pygame.draw.rect(screen, colorRED, (self.body[0].x * CELL, self.body[0].y * CELL, CELL, CELL))  # Draw the head  
        for segment in self.body[1:]:  
            pygame.draw.rect(screen, colorYELLOW, (segment.x * CELL, segment.y * CELL, CELL, CELL))  # Draw the body segments  

    def check_collision(self, food):  
        """Check if the snake's head collides with food."""  
        if self.body[0].x == food.pos.x and self.body[0].y == food.pos.y:  
            self.grow = True  # Set flag to grow the snake  
            return True  # Collision occurred  
        return False  # No collision  

    def check_self_collision(self):  
        """Check if the snake collides with itself."""  
        head = self.body[0]  # Head of the snake  
        # Return True if any body segment is at the same position as the head  
        return any(segment.x == head.x and segment.y == head.y for segment in self.body[1:])  

    def check_wall_collision(self):  
        """Check if the snake collides with the walls."""  
        head = self.body[0]  # Head of the snake  
        # Return True if the head is out of the screen bounds  
        return head.x < 0 or head.x >= WIDTH // CELL or head.y < 0 or head.y >= HEIGHT // CELL  

class Food:  
    """Class representing the food in the game."""  
    def __init__(self):  
        self.randomize()  # Randomly place food on the grid  
        self.spawn_time = time.time()  # Store the time when the food was spawned  

    def randomize(self):  
        """Randomize the position and value of the food."""  
        self.pos = Point(random.randint(0, WIDTH // CELL - 1), random.randint(0, HEIGHT // CELL - 1))  
        self.value = random.choice([1, 2, 3])  # Select a random weight for the food (1, 2 or 3)  
        self.spawn_time = time.time()  # Update spawn time  

    def draw(self):  
        """Draw the food on the screen with color based on its value."""  
        # Determine color based on the food's value  
        color = colorGREEN if self.value == 1 else colorBLUE if self.value == 2 else colorRED  
        pygame.draw.rect(screen, color, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))  # Draw the food  

    def expired(self):  
        """Check if the food has expired (lived for more than 5 seconds)."""  
        return time.time() - self.spawn_time > 5  # Food disappears after 5 seconds  

def draw_text(text, x, y, color):  
    """Draw text on the screen."""  
    font = pygame.font.Font(None, 36)  # Use the default font with a size of 36  
    surface = font.render(text, True, color)  # Render the text surface  
    screen.blit(surface, (x, y))  # Blit the text surface onto the screen at specified coordinates  

# Set initial game parameters  
FPS = 5  # Frames per second  
score = 0  # Initialize the score  
level = 1  # Initialize the level  
clock = pygame.time.Clock()  # Create a clock to manage the frame rate  
food = Food()  # Create a Food object  
snake = Snake()  # Create a Snake object  

# Prepare the game over message  
game_over = pygame.font.SysFont("Verdana", 60).render("Game Over", True, "red")  

# Main game loop  
running = True  
while running:  
    screen.fill(colorBLACK)  # Clear the screen with black color  
    draw_grid_chess()  # Draw the checkerboard grid  
    
    for event in pygame.event.get():  # Handle events  
        if event.type == pygame.QUIT:  # Check for quit event  
            running = False  # Exit the loop  
        elif event.type == pygame.KEYDOWN:  # Check for key presses  
            # Change snake direction based on arrow key input  
            if event.key == pygame.K_RIGHT and snake.dx == 0:  
                snake.dx, snake.dy = 1, 0  # Move right  
            elif event.key == pygame.K_LEFT and snake.dx == 0:  
                snake.dx, snake.dy = -1, 0  # Move left  
            elif event.key == pygame.K_DOWN and snake.dy == 0:  
                snake.dx, snake.dy = 0, 1  # Move down  
            elif event.key == pygame.K_UP and snake.dy == 0:  
                snake.dx, snake.dy = 0, -1  # Move up  

    snake.move()  # Update the snake's position  
    
    # Check for game over conditions  
    if snake.check_self_collision() or snake.check_wall_collision():  
        screen.fill(colorBLACK)  # Clear the screen  
        center_rect = game_over.get_rect(center=(WIDTH // 2, HEIGHT // 2))  # Center the game over text  
        screen.blit(game_over, center_rect)  # Draw game over text  
        pygame.display.flip()  # Update the display  
        pygame.time.delay(2000)  # Wait for 2 seconds  
        running = False  # End the game loop  
        continue  

    # Check if the snake has collided with food  
    if snake.check_collision(food):  
        score += food.value  # Increase score based on food value  
        food.randomize()  # Randomize food position  
        if score % 4 == 0:  # Every 4 points increases level  
            level += 1  # Increase level  
            FPS += 1  # Increase game speed  

    # Check if the food has expired  
    if food.expired():  
        food.randomize()  # Randomly reposition expired food  

    snake.draw()  # Draw the snake  
    food.draw()  # Draw the food  
    draw_text(f"Score: {score}", 10, 10, colorBLACK)  # Display the score  
    draw_text(f"Level: {level}", 10, 40, colorBLACK)  # Display the level  
    
    pygame.display.flip()  # Update the display  
    clock.tick(FPS)  # Control the game speed by managing the frame rate  

pygame.quit()  # Cleanly exit Pygame  