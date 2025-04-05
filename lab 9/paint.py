import pygame  

# Initialize Pygame  
pygame.init()  

# Set the dimensions of the window  
WIDTH, HEIGHT = 800, 600  
screen = pygame.display.set_mode((WIDTH, HEIGHT))  
pygame.display.set_caption("PAINT")  # Set the window title  

# Color definitions  
colorWHITE = (255, 255, 255)  
colorBLACK = (0, 0, 0)  
colorRED = (255, 0, 0)  
colorGREEN = (0, 255, 0)  
colorBLUE = (0, 0, 255)  

# Initial parameters  
screen.fill(colorBLACK)  # Fill the screen with black color  
LMBpressed = False  # Track left mouse button state  
RMBpressed = False  # Track right mouse button state  
THICKNESS = 5  # Brush thickness  
mode = "brush"  # Initial drawing mode  
prevX = prevY = 0  # Previous mouse position  
startX = startY = 0  # Starting position for shapes  

# Lists for saving drawn shapes  
rects = []  
circles = []  
squares = []  
right_triangles = []  
equilateral_triangles = []  
rhombuses = []  

# Copy the current state of the drawing surface  
drawing_surface = screen.copy()  
curr_color = colorRED  # Initial brush color  
clock = pygame.time.Clock()  # Create a timer for controlling frame rate  

done = False  # Main game loop flag  
while not done:  
    for event in pygame.event.get():  # Process events  
        if event.type == pygame.QUIT:  
            done = True  # Exit the loop if the window is closed  
        elif event.type == pygame.KEYDOWN:  # Handle key presses  
            if event.key == pygame.K_1:  
                mode = "brush"  # Set mode to brush  
            elif event.key == pygame.K_2:  
                mode = "rect"  # Set mode to rectangle  
            elif event.key == pygame.K_3:  
                mode = "circle"  # Set mode to circle  
            elif event.key == pygame.K_4:  
                mode = "square"  # Set mode to square  
            elif event.key == pygame.K_5:  
                mode = "right_triangle"  # Set mode to right triangle  
            elif event.key == pygame.K_6:  
                mode = "equilateral_triangle"  # Set mode to equilateral triangle  
            elif event.key == pygame.K_7:  
                mode = "rhombus"  # Set mode to rhombus  
            elif event.key == pygame.K_EQUALS:  
                THICKNESS += 1  # Increase brush thickness  
            elif event.key == pygame.K_MINUS:  
                THICKNESS = max(1, THICKNESS - 1)  # Decrease thickness but keep it at least 1  
            elif event.key == pygame.K_c:  # Clear the screen  
                screen.fill(colorBLACK)  # Fill with black  
                # Clear all shape lists  
                rects.clear()  
                circles.clear()  
                squares.clear()  
                right_triangles.clear()  
                equilateral_triangles.clear()  
                rhombuses.clear()  
                drawing_surface = screen.copy()  # Reset drawing surface  
            elif event.key == pygame.K_r:  
                curr_color = colorRED  # Set current color to red  
            elif event.key == pygame.K_g:  
                curr_color = colorGREEN  # Set current color to green  
            elif event.key == pygame.K_b:  
                curr_color = colorBLUE  # Set current color to blue  
        
        elif event.type == pygame.MOUSEBUTTONDOWN:  # Handle mouse button presses  
            if event.button == 1:  # Left mouse button  
                LMBpressed = True  
                prevX, prevY = event.pos  # Store the position of the mouse click  
                startX, startY = event.pos  # Store the start position for shapes  
            
        elif event.type == pygame.MOUSEMOTION:  # Handle mouse movement  
            currX, currY = event.pos  # Get current mouse position  
            if LMBpressed:  # If left mouse button is pressed  
                if mode == "brush":  # Brush mode  
                    pygame.draw.line(drawing_surface, curr_color, (prevX, prevY), (currX, currY), THICKNESS)  
                    prevX, prevY = currX, currY  # Update previous position  
                elif mode in ["rect", "square"]:  # Rectangle and square modes  
                    size = abs(currX - startX)  # Calculate size based on current position  
                    rect = pygame.Rect(min(startX, currX), min(startY, currY),   
                                       size if mode == "square" else abs(currX - startX),   
                                       size if mode == "square" else abs(currY - startY))  
                elif mode == "circle":  # Circle mode  
                    radius = max(abs(currX - startX), abs(currY - startY)) // 2  
                    circle = pygame.Rect(startX - radius, startY - radius, radius * 2, radius * 2)  
                elif mode == "right_triangle":  # Right triangle mode  
                    right_tri = [(startX, startY), (currX, startY), (startX, currY)]  
                elif mode == "equilateral_triangle":  # Equilateral triangle mode  
                    side = abs(currX - startX)  
                    equilateral_tri = [(startX, startY), (startX + side, startY),   
                                       (startX + side // 2, startY - int(side * (3 ** 0.5) / 2))]  
                elif mode == "rhombus":  # Rhombus mode  
                    rhombus = [(startX, startY - 50), (startX + 50, startY),   
                                (startX, startY + 50), (startX - 50, startY)]  
        
        elif event.type == pygame.MOUSEBUTTONUP:  # Handle mouse button releases  
            if event.button == 1:  # Left mouse button  
                LMBpressed = False  # Release the left mouse button  
                if mode == "rect":  
                    rects.append((rect.copy(), curr_color))  # Store rectangle  
                elif mode == "square":  
                    squares.append((rect.copy(), curr_color))  # Store square  
                elif mode == "circle":  
                    circles.append((circle.copy(), curr_color))  # Store circle  
                elif mode == "right_triangle":  
                    right_triangles.append((right_tri.copy(), curr_color))  # Store right triangle  
                elif mode == "equilateral_triangle":  
                    equilateral_triangles.append((equilateral_tri.copy(), curr_color))  # Store equilateral triangle  
                elif mode == "rhombus":  
                    rhombuses.append((rhombus.copy(), curr_color))  # Store rhombus  

    # Drawing all shapes on the screen  
    screen.blit(drawing_surface, (0, 0))  # Blit the current drawing surface  
    for r, color in rects:  # Draw all rectangles  
        pygame.draw.rect(screen, color, r, 2)  # Draw rectangle outlines  
    for s, color in squares:  # Draw all squares  
        pygame.draw.rect(screen, color, s, 2)  # Draw square outlines  
    for c, color in circles:  # Draw all circles  
        pygame.draw.ellipse(screen, color, c, 2)  # Draw circle outlines  
    for tri, color in right_triangles:  # Draw all right triangles  
        pygame.draw.polygon(screen, color, tri, 2)  # Draw triangle outlines  
    for tri, color in equilateral_triangles:  # Draw all equilateral triangles  
        pygame.draw.polygon(screen, color, tri, 2)  # Draw triangle outlines  
    for rhomb, color in rhombuses:  # Draw all rhombuses  
        pygame.draw.polygon(screen, color, rhomb, 2)  # Draw rhombus outlines  

    pygame.display.flip()  # Update the full display Surface to the screen  
    clock.tick(60)  # Maintain the frame rate at 60 frames per second  

pygame.quit()  # Cleanly exit Pygame  