import pygame

pygame.font.init()
font = pygame.font.SysFont('Comic Sans MS', 50)

class RetryButton:
    def __init__(self, posX, posY, width, height, screen):
        self.__posX = posX
        self.__posY = posY
        self.__width = width
        self.__height = height
        self.__screen = screen

    def update(self):
        pygame.draw.rect(self.__screen, "Grey", (self.__posX, self.__posY, self.__width, self.__height))
        text = font.render("Retry", True, "White")
        textRect = text.get_rect(center=(self.__posX+(self.__width/2), self.__posY+(self.__height/2)))
        self.__screen.blit(text, textRect)

    def clicked(self, mouseX, mouseY):
        if mouseX >= self.__posX and mouseX <= self.__posX + self.__width and mouseY >= self.__posY and mouseY <= self.__posY + self.__height:
            return True
        else:
            return False