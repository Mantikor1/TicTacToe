from Field import Field

class Grid:
    def __init__(self, screen):
        self.__screen = screen
        self.__fields = []
        self.__playerCount = 0 # Even numbers for player 1, uneven for player 2
        
        # Create a list of Fields with 3 rows and 3 columns each
        for row in range(3):
            self.__fields.append([])
            for column in range(3):
                self.__fields[row].append(Field(50*column, 50*row, 50, 50, self.__screen))

    # Call the update method for every field in the grid
    def update(self):
        for row in range(3):
            for column in range(3):
                self.__fields[row][column].update()

    # Check the mouse position when clicked if it's on a field in the grid
    # If yes, update the player count and set the field as "clicked"
    def click(self, mouseX, mouseY):
        # Iterating over every field
        for row in range(3):
            for column in range(3):
                # Get the position and height of the field
                posX, posY = self.__fields[row][column].getPos()
                width, height = self.__fields[row][column].getDimensions()
                # Chekc if the cursor is on the field
                if mouseX >= posX and mouseX <= posX + width and mouseY >= posY and mouseY <= posY + height:
                    self.updatePlayerCount()
                    # Set the sign in the field dependent on the player
                    if self.__playerCount % 2 != 0:
                        self.__fields[row][column].setClicked("X")
                    else:
                        self.__fields[row][column].setClicked("O")

    # Update the player count
    def updatePlayerCount(self):
        self.__playerCount += 1

    def clear(self):
        self.__playerCount = 0
        for row in range(3):
            for column in range(3):
                self.__fields[row][column].clear()
