class Change():
    def getString(self):
        print("Input: ")
        self.string = input()

    def printString(self):
        print("Output: " + self.string.upper())

stringManipulator = Change()
stringManipulator.getString()
stringManipulator.printString()
