import pygame  
import datetime  

# Initialize Pygame  
pygame.init()  

# Set up screen and clock  
screen = pygame.display.set_mode((400, 400))  
pygame.display.set_caption("Mickey Mouse Clock & Music Player")  
clock = pygame.time.Clock()  

# Load images and sounds  
mickey_image = pygame.image.load("mickeyclock.jpeg")  # Ensure you have this image  
music_file = "musicforlabwork.mp3"  # Ensure you have a valid music file  

# Music state  
pygame.mixer.music.load(music_file)  
is_playing = False  

# Ball settings  
ball_color = (255, 0, 0)  
ball_radius = 25  
ball_x, ball_y = 200, 200  
step = 20  
background_color = (255, 255, 255)  

done = False  
while not done:  
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            done = True  
            
        # Music controls  
        if event.type == pygame.KEYDOWN:  
            if event.key == pygame.K_p:  # Play  
                if not is_playing:  
                    pygame.mixer.music.play()  
                    is_playing = True  
            if event.key == pygame.K_s:  # Stop  
                pygame.mixer.music.stop()  
                is_playing = False  
            
            # Ball movement  
            if event.key == pygame.K_UP:  
                ball_y -= step  
            if event.key == pygame.K_DOWN:  
                ball_y += step  
            if event.key == pygame.K_LEFT:  
                ball_x -= step  
            if event.key == pygame.K_RIGHT:  
                ball_x += step  
            
            # Prevent the ball from going off the screen  
            if ball_x < ball_radius:  
                ball_x = ball_radius  
            elif ball_x > 400 - ball_radius:  
                ball_x = 400 - ball_radius  
            if ball_y < ball_radius:  
                ball_y = ball_radius  
            elif ball_y > 400 - ball_radius:  
                ball_y = 400 - ball_radius  

    # Draw clock  
    now = datetime.datetime.now()  
    screen.fill(background_color)  

    # Draw circle  
    pygame.draw.circle(screen, ball_color, (ball_x, ball_y), ball_radius)  

    # Draw the clock  
    minute_angle = -(now.minute + now.second / 60) * 6  # Calculate minute hand  
    second_angle = -now.second * 6  # Calculate second hand  
    mickey_minute = pygame.transform.rotate(mickey_image, minute_angle)  
    mickey_second = pygame.transform.rotate(mickey_image, second_angle)  
    screen.blit(mickey_minute, (200 - mickey_minute.get_width() // 2, 200 - mickey_minute.get_height() // 2))  
    screen.blit(mickey_second, (200 - mickey_second.get_width() // 2, 200 - mickey_second.get_height() // 2))  

    pygame.display.flip()  
    clock.tick(60)  

pygame.quit()  