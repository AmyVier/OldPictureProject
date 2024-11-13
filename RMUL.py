from graphics import*
from Button import*

class Multiple2():
    def __init__ (self, MUL1, MUL2, MUL3, MUL4): #("self in Python, Demystified")
        
        NAMarray = []

        
        M = GraphWin("Tasks", 630, 300) #create and open window

        BU = WDII(M, "grey", "Back", Point(530, 70), 30) #back button

        title = Text(Point(310, 15), "JUST DO IT:")
        title.draw(M)
        title.setSize(20)

        for q in range(len(MUL1)):
            LA = 15 * q
            NAMarray.append(Text(Point(310, 70 + LA), MUL1[q] + " due: " + MUL2[q] + " " + str(MUL3[q]) + ", " + str(MUL4[q]))) 
            NAMarray[q].draw(M)

        while True:
            m = M.getMouse()
            if BU.isClicked(m):
                break
        M.close()
