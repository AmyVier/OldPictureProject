from graphics import*
from Button import*

class remind():
    def __init__ (self, arrayN, arrayM, arrayD, arrayY, inputN2, inputM2, inputD2, inputY2, inputMM3, inputDD3, inputYY3, inputHH, inputMM):
        
        RE = GraphWin("Event", 630, 300) #create and open window
        
        TEX = Text(Point(310, 15), "Name: Month/Day/Year")
        TEX.draw(RE)

        TEX1 = Text(Point(270, 50), ":")
        TEX1.draw(RE)

        TEX2 = Text(Point(330, 50), "/")
        TEX2.draw(RE)

        TEX3 = Text(Point(390, 50), "/")
        TEX3.draw(RE)

        Enter = Entry(Point(200,50), 15)
        Enter.draw(RE)
        Enter.setFill("white")

        Enter1 = Entry(Point(300,50), 5)
        Enter1.draw(RE)
        Enter1.setFill("white")

        Enter2 = Entry(Point(360,50), 5)
        Enter2.draw(RE)
        Enter2.setFill("white")

        Enter3 = Entry(Point(420,50), 5)
        Enter3.draw(RE)
        Enter3.setFill("white")

        TEX5 = Text(Point(310, 15), "Month/Day/Year, Hour:Minutes")

        TEX6 = Text(Point(200, 50), "/")

        TEX7 = Text(Point(260, 50), "/")

        TEX8 = Text(Point(420, 50), ":")

        Enter4 = Entry(Point(170,50), 5)

        Enter5 = Entry(Point(230,50), 5)

        Enter6 = Entry(Point(290,50), 5)

        Enter7 = Entry(Point(390,50), 5)

        Enter8 = Entry(Point(450,50), 5)

        Button1 = []

        Button2 = []

        Button1.append(WDII(RE, "grey", "Remind", Point(310, 150), 25)) #back button

        Button2.append(WDII(RE, "grey", "Back", Point(310, 200), 25)) #back button

        TEX4 = Text(Point(310, 100), "")
        TEX4.draw(RE)

        inputN = ""
        inputM = ""
        inputD = ""
        inputY = ""

        b = False

        a = False
        
        c = True

        OMonths = ["Janurary", "February", "March", "April", "May", "June", "July", "August", "September",
                       "October", "November", "December"] #months in order


        e = 2

        f = 2

        g = 2

        h = 2
        

        while True:
            m = RE.getMouse()
            if Button2[0].isClicked(m):
                break
            if Button1[0].isClicked(m):
                TEX4.setText(" ")
                
                if (a == False):
                    try:
                        inputN = Enter.getText()
                        inputM = Enter1.getText()
                        inputD = int(Enter2.getText()) #(Ronquillo)
                        inputY = int(Enter3.getText()) #(Ronquillo)
                            
                        for l in arrayD:
                            if(l == inputD):
                                a = arrayD.index(inputD)# ("Python List index()")
                                if(arrayM[a] == inputM):
                                    if(arrayY[a] == inputY):
                                        b = True
                                        a = False
                                        Enter.undraw()
                                        Enter1.undraw()
                                        Enter2.undraw()
                                        Enter3.undraw()
                                        
                                        TEX.undraw()
                                        TEX1.undraw()
                                        TEX2.undraw()
                                        TEX3.undraw()

                                        Enter4.draw(RE)
                                        Enter4.setFill("white")
                                        Enter5.draw(RE)
                                        Enter5.setFill("white")
                                        Enter6.draw(RE)
                                        Enter6.setFill("white")
                                        Enter7.draw(RE)
                                        Enter7.setFill("white")
                                        Enter8.draw(RE)
                                        Enter8.setFill("white")
                                        
                                        TEX5.draw(RE)
                                        TEX6.draw(RE)
                                        TEX7.draw(RE)
                                        TEX8.draw(RE)


                    except:
                        b = False
                        a = False
                        c = False
                          
                if (a == True):
                    b = False
                    try:
                        for l in OMonths:
                            if (l == Enter4.getText()):   
                                e = int(Enter5.getText()) - e
                                f = int(Enter6.getText()) - f
                                g = int(Enter7.getText()) - g
                                h = int(Enter8.getText()) - h
                                inputN2.append(inputN)
                                inputM2.append(inputM)
                                inputD2.append(inputD)
                                inputY2.append(inputY)

                                inputMM3.append(Enter4.getText())
                                inputDD3.append(int(Enter5.getText()))
                                inputYY3.append(int(Enter6.getText()))
                                inputHH.append(int(Enter7.getText()))
                                inputMM.append(int(Enter8.getText()))
                                b = True
                            
                            
                    except:
                        b = False
                        a = True
                        
                if (b == True and a == True):
                    TEX4.setText("Event Successfully Reminded")
                    inputN = ""
                    inputM = ""
                    inputD = ""
                    inputY = ""
                    b = False
                    a = False
                    Enter4.setText("")
                    Enter5.setText("")
                    Enter6.setText("")
                    Enter7.setText("")
                    Enter8.setText("")

                    Enter4.undraw()
                    Enter5.undraw()
                    Enter6.undraw()
                    Enter7.undraw()
                    Enter8.undraw()
                                        
                    TEX5.undraw()
                    TEX6.undraw()
                    TEX7.undraw()
                    TEX8.undraw()

                    Enter.draw(RE)
                    Enter1.draw(RE)
                    Enter2.draw(RE)
                    Enter3.draw(RE)
                                        
                    TEX.draw(RE)
                    TEX1.draw(RE)
                    TEX2.draw(RE)
                    TEX3.draw(RE)

                    c = True
                    
                if (b == False and a == True):
                    TEX4.setText("The values in the text box have been typed incorrectly.")
                    
                if (b == False and a == False and c == False):
                    TEX4.setText("Event Cannot be Found")
                    c = True
                    
                if (b == True and a == False):
                    TEX4.setText("Event Found")
                    Enter.setText("")
                    Enter1.setText("")
                    Enter2.setText("")
                    Enter3.setText("")
                    a = True
        RE.close()

