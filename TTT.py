from graphics import*
from Button import*

class TT ():
    def __init__ (self, arrayN, arrayM, arrayD, arrayY, arrayMin, arrayH): #("self in Python, Demystified")

        OMonths = ["Janurary", "February", "March", "April", "May", "June", "July", "August", "September",
                       "October", "November", "December"] #months in order

        OMonthsB = False
        
        Tas = GraphWin("Event", 630, 230) #create and open window

        TEX = Text(Point(310, 15), "Name: Month/Day/Year Hour:Minutes")
        TEX.draw(Tas)

        TEX1 = Text(Point(220, 50), ":")
        TEX1.draw(Tas)

        TEX2 = Text(Point(280, 50), "/")
        TEX2.draw(Tas)

        TEX3 = Text(Point(340, 50), "/")
        TEX3.draw(Tas)

        TEX3 = Text(Point(460, 50), ":")
        TEX3.draw(Tas)

        Enter = Entry(Point(150,50), 15)
        Enter.draw(Tas)
        Enter.setFill("white")

        Enter1 = Entry(Point(250,50), 5)
        Enter1.draw(Tas)
        Enter1.setFill("white")

        Enter2 = Entry(Point(310,50), 5)
        Enter2.draw(Tas)
        Enter2.setFill("white")

        Enter3 = Entry(Point(370,50), 5)
        Enter3.draw(Tas)
        Enter3.setFill("white")

        Enter4 = Entry(Point(430,50), 5)
        Enter4.draw(Tas)
        Enter4.setFill("white")

        Enter5 = Entry(Point(490,50), 5)
        Enter5.draw(Tas)
        Enter5.setFill("white")

        CL = WDII(Tas, "grey", "Start", Point(310, 150), 25) #back button

        CL2 = WDII(Tas, "grey", "Back", Point(310, 200), 25) #back button

        TEX4 = Text(Point(310, 100), "")
        TEX4.draw(Tas)

        inputN = ""
        inputM = ""
        inputD = ""
        inputY = ""
        inputMin = ""
        inputH = ""

        while True:
            m = Tas.getMouse()
            if CL2.isClicked(m):
                break
            if CL.isClicked(m):
                TEX4.setText("")
                try: 
                    inputN = Enter.getText()
                    inputM = Enter1.getText()
                    inputD = int(Enter2.getText()) #(Ronquillo)
                    inputY = int(Enter3.getText()) #(Ronquillo)
                    inputMin = int(Enter5.getText()) #(Ronquillo)
                    inputH = int(Enter4.getText()) #(Ronquillo)
                    for l in OMonths:
                        if (l == inputM):       
                            arrayN.append(inputN)
                            arrayM.append(inputM)
                            arrayD.append(inputD)
                            arrayY.append(inputY)
                            arrayMin.append(inputMin)
                            arrayH.append(inputH)
                            Enter.setText("")
                            Enter1.setText("")
                            Enter2.setText("")
                            Enter3.setText("")
                            Enter4.setText("")
                            Enter5.setText("")
                            OMonthsB = True
                    if (OMonthsB == True):
                        TEX4.setText("Event Started.")
                    if (OMonthsB == False):
                        TEX4.setText("The values in the text box have been typed incorrectly.")
                    
                except:
                    TEX4.setText("The values in the text box have been typed incorrectly.")
            
        Tas.close()
