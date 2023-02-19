import pygame
import random

# Initialize Pygame
pygame.init()

# Set the window size
size = (700, 500)
screen = pygame.display.set_mode(size)

# Set the title of the window
pygame.display.set_caption("Sort Visualizer")

# Create an empty list to hold the values
values = []

# Fill the list with random values
for i in range(100):
    values.append(random.randint(0, 100))

# Set the sorting algorithm
sorting_algorithm = "bubble"

# Run the sorting algorithm
if sorting_algorithm == "bubble":
    for i in range(len(values)):
        for j in range(len(values) - 1):
            if values[j] > values[j + 1]:
                values[j], values[j + 1] = values[j + 1], values[j]
                # Draw the current state of the list
                for k in range(len(values)):
                    pygame.draw.rect(screen, (255, 255, 255), (k * 7, 0, 7, values[k]))
                pygame.display.update()
                pygame.time.wait(10)

# Quit Pygame
pygame.quit()
