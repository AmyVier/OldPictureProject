from graphics import*
from Button import*

class Finish():
    def __init__ (self, arrayN, arrayM, arrayD, arrayY, LLarray, LarrayN, LarrayM, LarrayD, LarrayY, arrayMin, arrayH, LarrayH, LarrayMin
                  , inputN2, inputM2, inputD2, inputY2, inputMM3, inputDD3, inputYY3, inputHH, inputMM): #("self in Python, Demystified")
        Fin = GraphWin("Finished?", 630, 300) #create and open window

        title = Text(Point(310, 15), "Mark assignents as finished here")
        title.draw(Fin)
        title.setSize(15)

        TEX = Text(Point(310, 40), "Name: Month/Day/Year")
        TEX.draw(Fin)

        TEX1 = Text(Point(290, 70), ":")
        TEX1.draw(Fin)

        TEX2 = Text(Point(250, 70), "/")
        TEX2.draw(Fin)

        TEX3 = Text(Point(410, 70), "/")
        TEX3.draw(Fin)

        Enter = Entry(Point(220,70), 15)
        Enter.draw(Fin)
        Enter.setFill("white")

        Enter1 = Entry(Point(320,70), 5)
        Enter1.draw(Fin)
        Enter1.setFill("white")

        Enter2 = Entry(Point(380,70), 5)
        Enter2.draw(Fin)
        Enter2.setFill("white")

        Enter3 = Entry(Point(440,70), 5)
        Enter3.draw(Fin)
        Enter3.setFill("white")


        inputN = ""
        inputM = ""
        inputD = ""
        inputY = ""
        inputL = ""

        a = 0
        b = False

        TEX4 = Text(Point(310, 100), "")
        TEX4.draw(Fin)
        
        button = WDII(Fin, "grey", "Finish", Point(310, 150), 30) #back button
        Bbutton = WDII(Fin, "grey", "Done", Point(310, 230), 30) #back button

        while True:
            m = Fin.getMouse()
            if Bbutton.isClicked(m):
                break
            if button.isClicked(m):
                TEX4.setText(" ")
                try:
                    inputN = Enter.getText()
                    inputM = Enter1.getText()
                    inputD = int(Enter2.getText()) #(Ronquillo)
                    inputY = int(Enter3.getText()) #(Ronquillo)

                    
                    for l in range(len(inputN2)):
                        if (inputN == inputN2[l]):
                            if (inputM == inputM2[l]):
                                if (inputD == inputD2[l]):
                                    if (inputY == inputY2[l]):
                                        inputN2.pop(l)
                                        inputM2.pop(l)
                                        inputD2.pop(l)
                                        inputY2.pop(l)
                                        
                                        inputMM3.pop(l)
                                        inputDD3.pop(l)
                                        inputYY3.pop(l)
                                        inputHH.pop(l)
                                        inputMM.pop(l)

                    for l in arrayD:
                        if(l == inputD):
                            a = arrayD.index(inputD)# ("Python List index()")
                            if(arrayM[a] == inputM):
                                if(arrayY[a] == inputY):
                                    if (arrayN[a] == inputN):
                                        b = True
                                        arrayN.pop(a) #("Remove an item from a list in Python (clear, pop, remove, del)")
                                        arrayM.pop(a)
                                        arrayD.pop(a)
                                        arrayY.pop(a)
                                        arrayMin.pop(a)
                                        arrayH.pop(a)
                    for l in LarrayD:
                        if(l == inputD):
                            a = LarrayD.index(inputD) # ("Python List index()")
                            if(LarrayM[a] == inputM):
                                if(LarrayY[a] == inputY):
                                    if (LarrayN[a] == inputN):
                                        b = True
                                        LLarray[a] = "Done"
                except:
                    b = False
                                                    
                if (b == False):
                    TEX4.setText("Event Cannot be Found")
                if (b == True):
                    TEX4.setText("Event Found and Finished")
                    Enter.setText("")
                    Enter1.setText("")
                    Enter2.setText("")
                    Enter3.setText("")
                    
        Fin.close()
                    
            

    
        

