import pygame
import sqlite3
import sys
import time
import random

# Database setup
conn = sqlite3.connect("snake_game.db")
cursor = conn.cursor()

# Create tables
cursor.execute("""
CREATE TABLE IF NOT EXISTS user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL
)
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS user_score (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    score INTEGER DEFAULT 0,
    level INTEGER DEFAULT 1,
    FOREIGN KEY (user_id) REFERENCES user (id)
)
""")
conn.commit()

# User authentication
def get_user():
    username = input("Enter your username: ")
    cursor.execute("SELECT id FROM user WHERE username = ?", (username,))
    user = cursor.fetchone()
    if user:
        user_id = user[0]
        cursor.execute("SELECT score, level FROM user_score WHERE user_id = ?", (user_id,))
        score_data = cursor.fetchone()
        if score_data:
            print(f"Welcome back, {username}! Current score: {score_data[0]}, Level: {score_data[1]}")
            return user_id, score_data[0], score_data[1]
        else:
            cursor.execute("INSERT INTO user_score (user_id) VALUES (?)", (user_id,))
            conn.commit()
            return user_id, 0, 1
    else:
        cursor.execute("INSERT INTO user (username) VALUES (?)", (username,))
        conn.commit()
        user_id = cursor.lastrowid
        cursor.execute("INSERT INTO user_score (user_id) VALUES (?)", (user_id,))
        conn.commit()
        print(f"Welcome, {username}! Starting a new game.")
        return user_id, 0, 1

# Snake game setup
def snake_game(user_id, initial_score, initial_level):
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Snake Game")
    clock = pygame.time.Clock()

    # Game variables
    snake_pos = [100, 50]
    snake_body = [[100, 50], [90, 50], [80, 50]]
    food_pos = [400, 300]
    food_spawn = True
    direction = 'RIGHT'
    change_to = direction
    score = initial_score
    level = initial_level
    speed = 15 + (level - 1) * 5

    def save_game():
        cursor.execute("UPDATE user_score SET score = ?, level = ? WHERE user_id = ?", (score, level, user_id))
        conn.commit()
        print("Game saved!")

    # Main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and not direction == 'DOWN':
                    change_to = 'UP'
                elif event.key == pygame.K_DOWN and not direction == 'UP':
                    change_to = 'DOWN'
                elif event.key == pygame.K_LEFT and not direction == 'RIGHT':
                    change_to = 'LEFT'
                elif event.key == pygame.K_RIGHT and not direction == 'LEFT':
                    change_to = 'RIGHT'
                elif event.key == pygame.K_p:  # Pause and save
                    save_game()
                    print("Game paused. Press any key to continue.")
                    paused = True
                    while paused:
                        for pause_event in pygame.event.get():
                            if pause_event.type == pygame.KEYDOWN:
                                paused = False

        # Update direction
        direction = change_to

        # Move the snake
        if direction == 'UP':
            snake_pos[1] -= 10
        if direction == 'DOWN':
            snake_pos[1] += 10
        if direction == 'LEFT':
            snake_pos[0] -= 10
        if direction == 'RIGHT':
            snake_pos[0] += 10

        # Snake body growing mechanism
        snake_body.insert(0, list(snake_pos))
        if snake_pos == food_pos:
            score += 10
            food_spawn = False
            if score % 50 == 0:  # Level up every 50 points
                level += 1
                speed += 5
                print(f"Level up! Current level: {level}")
        else:
            snake_body.pop()

        if not food_spawn:
            food_pos = [random.randrange(1, 80) * 10, random.randrange(1, 60) * 10]
        food_spawn = True

        # Game over conditions
        if snake_pos[0] < 0 or snake_pos[0] > 790 or snake_pos[1] < 0 or snake_pos[1] > 590:
            save_game()
            print("Game Over!")
            pygame.quit()
            sys.exit()
        for block in snake_body[1:]:
            if snake_pos == block:
                save_game()
                print("Game Over!")
                pygame.quit()
                sys.exit()

        # Graphics
        screen.fill(pygame.Color(0, 0, 0))
        for pos in snake_body:
            pygame.draw.rect(screen, pygame.Color(0, 255, 0), pygame.Rect(pos[0], pos[1], 10, 10))
        pygame.draw.rect(screen, pygame.Color(255, 0, 0), pygame.Rect(food_pos[0], food_pos[1], 10, 10))

        # Display score and level
        font = pygame.font.SysFont('times new roman', 20)
        score_text = font.render(f"Score: {score}  Level: {level}", True, pygame.Color(255, 255, 255))
        screen.blit(score_text, [10, 10])

        pygame.display.flip()
        clock.tick(speed)

if __name__ == "__main__":
    user_id, initial_score, initial_level = get_user()
    snake_game(user_id, initial_score, initial_level)