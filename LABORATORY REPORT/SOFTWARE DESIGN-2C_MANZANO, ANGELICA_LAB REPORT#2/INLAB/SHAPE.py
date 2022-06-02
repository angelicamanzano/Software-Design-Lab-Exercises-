class Shape:
    def __init__(self, pname, lname):
        self.shapename = pname
        self.sides = lname
    def printshape(self):
       print(self.shapename, self.sides)


x = Shape("Square", "4 sides")
x.printshape()