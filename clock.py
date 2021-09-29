import pygame
from pygame import *
import math
import datetime

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

# Set a display size/resolution
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# Clock sets the FPS in the game
clock = pygame.time.Clock()
# Set the app window caption/name
pygame.display.set_caption("Analog Clock")
# Load the background image
bg = pygame.image.load("clock_bg.jpg")
# Frames per second
FPS = 50

def convert_degrees(radius, angle):
    """Convert degrees into pygame angles"""
    y = math.cos(2 * math.pi * angle / 360) * radius
    x = math.sin(2 * math.pi * angle / 360) * radius
    return x + 400, -(y - 400)


def game():
    """Main app loop"""
    while True:
        for event in pygame.event.get():
            # Enable quiting the app by clicking X in right/top window corner
            if event.type == pygame.QUIT:
                return

        # Store the current time in variable
        time = datetime.datetime.now()
        seconds = time.second
        minutes = time.minute
        hours = time.hour
        
        # Draw the background image at the given coordinates
        screen.blit(bg, (0, 0))

        # Minute hand
        RADIUS = 200 
        angle = minutes * (360/60)
        pygame.draw.line(screen, (0, 0, 255), (400, 400), convert_degrees(RADIUS, angle), 6)
        
        # Second hand
        RADIUS = 250
        angle = seconds * (360/60)
        pygame.draw.line(screen, (30, 30, 30), (400, 400), convert_degrees(RADIUS, angle), 3)

        # Hour hand
        RADIUS = 150
        angle = hours * (360/12)
        pygame.draw.line(screen, (150, 30, 60), (400, 400), convert_degrees(RADIUS, angle), 8)

        # Refresh the display each frame
        pygame.display.update()
        # Set main FPS in the app
        clock.tick(FPS)
        

game()
# Stop the app
pygame.quit()