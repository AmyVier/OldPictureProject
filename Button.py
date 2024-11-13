from graphics import*

class Square():
    def __init__(self, win, color, text, center, size): #("self in Python, Demystified")

        self.p1 = Point(center.x - size, center.y - size)
        self.p2 = Point(center.x + size, center.y + size)
        self.r = Rectangle(self.p1, self.p2)
        self.r.draw(win)
        self.r.setFill(color)
        self.t = Text(center, text)
        self.t.setSize(18)
        self.t.draw(win)

    def undraw(self, UnD): #("self in Python, Demystified")
        self.UnD = UnD
        if "F" in UnD:
            self.t.undraw()
            self.r.undraw()
            return True
        else:
            return False

    def changeColor(self, newColor): #("self in Python, Demystified")
        self.r.setFill(newColor) #("self in Python, Demystified")

    def isClicked(self, p): #("self in Python, Demystified")
        minX = self.p1.x #("self in Python, Demystified")
        maxX = self.p2.x
        minY = self.p1.y
        maxY = self.p2.y

        if p.x > minX:
            if p.x < maxX:
                if p.y > minY:
                    if p.y < maxY:
                        return True         
        return False
    
class WDII():
    def __init__(self, win, color, text, center, size): #("self in Python, Demystified")

        self.p1 = Point(center.x - size, center.y - size/2)
        self.p2 = Point(center.x + size, center.y + size/2)
        self.r = Rectangle(self.p1, self.p2)
        self.r.draw(win)
        self.r.setFill(color)
        self.t = Text(center, text)
        self.t.setSize(18)
        self.t.draw(win)

    def undraw(self, UnD):
        self.UnD = UnD
        if "F" in UnD:
            self.t.undraw()
            self.r.undraw()
            return True
        else:
            return False

    def changeColor(self, newColor):
        self.r.setFill(newColor)

    def isClicked(self, p):
        minX = self.p1.x
        maxX = self.p2.x
        minY = self.p1.y
        maxY = self.p2.y

        if p.x > minX:
            if p.x < maxX:
                if p.y > minY:
                    if p.y < maxY:
                        return True          
        return False

class TasK():
    def __init__(self, win, color, text, center, size): #("self in Python, Demystified")

        self.p1 = Point(center.x - size, center.y - size/3)
        self.p2 = Point(center.x + size, center.y + size/3)
        self.r = Rectangle(self.p1, self.p2)
        self.r.draw(win)
        self.r.setFill(color)
        self.t = Text(center, text)
        self.t.setSize(18)
        self.t.draw(win)

    def undraw(self, UnD):
        self.UnD = UnD
        if "F" in UnD:
            self.t.undraw()
            self.r.undraw()
            return True
        else:
            return False

    def changeColor(self, newColor):
        self.r.setFill(newColor)

    def isClicked(self, p):
        minX = self.p1.x
        maxX = self.p2.x
        minY = self.p1.y
        maxY = self.p2.y

        if p.x > minX:
            if p.x < maxX:
                if p.y > minY:
                    if p.y < maxY:
                        return True          
        return False
    




