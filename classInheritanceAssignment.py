import datetime

class Game:
    title = "N/A"
    developer = "N/A"
    publisher = "N/A"
    releaseDate = datetime.datetime(0, 0, 0)

class Strategy(Game):
    gameSpeed = "Turn Based" #can also be realtime, or time variable (pause, fast forward, etc.)
    multipleLayers = True #if the game has multiple strategic layers or not

class Shooter(Game):
    POV = "First Person" #the point of view of the player, usually first person or thrid person
    style = "Arena Shooter" #style of shooter, other sytles include battle royals, survival, etc.
