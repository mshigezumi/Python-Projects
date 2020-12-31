import datetime

class Game:
    title = "N/A"
    developer = "N/A"
    publisher = "N/A"
    releaseDate = datetime.datetime(2000, 1, 1)

    def setInfo(self): #sets the info for the Game class
        title = input("Enter a title: ")
        developer = input("Enter a developer: ")
        publisher = input("Enter a publisher: ")
        year = input("Enter the year of release: ")
        month = input("Enter the month of release: ")
        day = input("Enter the day of release: ")
        releaseDate = datetime.datetime(int(year), int(month), int(day))
        print(title)
        print(developer)
        print(publisher)
        print(releaseDate)

class Strategy(Game):
    gameSpeed = "Turn Based" #can also be realtime, or time variable (pause, fast forward, etc.)
    multipleLayers = True #if the game has multiple strategic layers or not

    def setInfo(self): #sets the info for the Strategy class
        gameSpeed = input("Enter the speed of the game: ")
        multipleLayers = input("Enter \"True\" or \"False\" if the game has multiple strategic layers: ")
        print(gameSpeed)
        print(multipleLayers)
        
class Shooter(Game):
    POV = "First Person" #the point of view of the player, usually first person or thrid person
    style = "Arena Shooter" #style of shooter, other sytles include battle royals, survival, etc.

    def setInfo(self): #sets the info for the Shooter class
        POV = input("Enter the perspective of the player: ")
        style = input("Enter the style of shooter: ")
        print(POV)
        print(style)


#runs the methods
game = Game()
game.setInfo()

strategyGame = Strategy()
strategyGame.setInfo()

shooterGame = Shooter()
shooterGame.setInfo()
