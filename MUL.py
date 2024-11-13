from graphics import*
from Button import*

class Multiple():
    def __init__ (self, arrayn, arrayTH8, arrayTM9): #("self in Python, Demystified")
        
        NAMarray = []

        
        M = GraphWin("Tasks", 630, 300) #create and open window

        BU = WDII(M, "grey", "Back", Point(530, 70), 30) #back button

        title = Text(Point(310, 15), "Tasks Due This Day:")
        title.draw(M)
        title.setSize(20)

        ampm = ""

        for q in range(len(arrayn)):
            if (arrayTH8[q] >= 12):
                ampm = "pm"
            if (arrayTH8[q] < 12):
                ampm = "am"
            LA = 15 * q
            NAMarray.append(Text(Point(310, 70 + LA), arrayn[q] + " due at: " + str(arrayTH8[q]) + ":" + str(arrayTM9[q]) + " " + ampm))
            NAMarray[q].draw(M)

        while True:
            m = M.getMouse()
            if BU.isClicked(m):
                break
        M.close()
