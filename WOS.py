from graphics import*
from Button import*

class WallOS():
    def __init__ (self, LarrayN, LarrayM, LarrayD, LarrayY, LLarray, LarrayH, LarrayMin): #("self in Python, Demystified")
        WALL = GraphWin("The Wall of Shame", 630, 300) #create and open window

        Bbutton = WDII(WALL, "grey", "Back", Point(530, 70), 30) #back button

        cats = Image(Point(520,190), "Cat1.png") #Picture from Kuzmin on Alamy Website
        cat = Image(Point(520,190), "Cat2.png") #Picture from Kuzmin on Alamy Website

        LarrayNN = []
        LarrayMM = []
        LarrayDD = []
        LarrayYY = []
        LLarrayLL = []
        LLarrayH = []

        LA = 0
        ampm = ""


        title = Text(Point(310, 15), "Welcome to 'The Wall of Shame'")
        title.draw(WALL)
        title.setSize(20)

        title1 = Text(Point(310, 100), "Nothing is on 'The Wall of Shame' yet...")

        if (len(LarrayN) == 0):
            cat.draw(WALL)
            title1.draw(WALL)
            title.setSize(20)

        else:
            cats.draw(WALL)
            for q in range(len(LarrayN)):
                if (LarrayH[q] >= 12):
                    ampm = "pm"
                if (LarrayH[q] < 12):
                    ampm = "am"
                LA = 15 * q
                LLarrayLL.append(Text(Point(100, 50 + LA), LLarray[q]))
                LLarrayLL[q].draw(WALL)
                LarrayNN.append(Text(Point(150, 50 + LA), LarrayN[q]  + ":"))
                LarrayNN[q].draw(WALL)
                LarrayMM.append(Text(Point(210, 50 + LA), LarrayM[q] + " /"))
                LarrayMM[q].draw(WALL)
                LarrayDD.append(Text(Point(255, 50 + LA), str(LarrayD[q]) + " /")) #(Ronquillo)
                LarrayDD[q].draw(WALL)
                LarrayYY.append(Text(Point(290, 50 + LA), LarrayY[q]))
                LarrayYY[q].draw(WALL)
                LLarrayH.append(Text(Point(340, 50 + LA), str(LarrayH[q]) + ":" + str(LarrayMin[q]) + " " + ampm))
                LLarrayH[q].draw(WALL)

        
        while True:
            m = WALL.getMouse()
            if Bbutton.isClicked(m):
                break
        WALL.close()

    

