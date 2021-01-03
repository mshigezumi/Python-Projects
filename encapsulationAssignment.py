class Protected:
    def __init__(self):
        #initializing the two variables
        self._protectedVar = 0
        self.__privateVar = 0

    def getPrivate(self):
        #getter for the private variable
        print(self.__privateVar)

    def setPrivate(self, private):
        #setter for the private variable
        self.__privateVar = private

obj = Protected() #creating the object
obj._protectedVar = 42
print(obj._protectedVar)
obj.setPrivate(11)
obj.getPrivate()
