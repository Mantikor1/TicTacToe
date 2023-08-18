 # TODO
 # -> Retry button
 # -> Fix screen size
 # -> Fix grid layout corners
 # -> Add player indicator
 # -> Multiplayer!?!?!?!!
  
import pygame
from Grid import Grid
from RetryButton import RetryButton

# pygame setup
pygame.init()
screen = pygame.display.set_mode((150, 210))
clock = pygame.time.Clock()

running = True

# Create initial grid
grid = Grid(screen)

retryButton = RetryButton(5, 155, 140, 50, screen)
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         running = False
      if event.type == pygame.MOUSEBUTTONDOWN:
         # Determine mouse position and update correct field in grid if clicked
         mouseX, mouseY = pygame.mouse.get_pos()
         grid.click(mouseX, mouseY)
         if retryButton.clicked(mouseX, mouseY):
            grid.clear()

    # fill the screen with a color to wipe away anything from last frame
   screen.fill("white") 

   # Render the updated grid
   grid.update()
   
   retryButton.update()
    # flip() the display to put your work on screen
   pygame.display.flip()

pygame.quit()
