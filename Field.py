import pygame

# Set the font for the sign inside the field
pygame.font.init()
font = pygame.font.SysFont('Comic Sans MS', 50)

class Field:
    def __init__(self, posX, posY, width, height, screen):
        self.__posX = posX
        self.__posY = posY
        self.__width = width
        self.__height = height
        self.__clicked = False
        self.__playerSign = "" # Gets set when the field gets clicked
        self.__screen = screen

    # Draws a rectangle on the screen and a sign if the field got clicked
    def update(self):
        pygame.draw.rect(self.__screen, "black", (self.__posX, self.__posY, self.__width, self.__height), 3)
        # Render sign if clicked
        if self.__clicked:
            sign = font.render(self.__playerSign, True, "Black")
            self.__screen.blit(sign, (self.__posX+13, self.__posY+11))

    def clear(self):
        self.__clicked = False
        self.__playerSign = ""
        
    # Set the player sign and mark the field as "clicked"
    def setClicked(self, playerSign):
        self.__clicked = True
        self.__playerSign = playerSign
            
    # Return the position of the field on the screen
    def getPos(self):
        return [self.__posX, self.__posY]

    # Return the dimensions of the field
    def getDimensions(self):
        return [self.__width, self.__height]