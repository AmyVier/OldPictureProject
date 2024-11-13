from graphics import*
from Button import*
from datetime import date #(“How to Get Current Date and Time in Python?”)
from datetime import datetime
from TEST3 import*
from WOS import*
#import threading

'''def click(menu, CAL, WOS, Exit, arrayN, arrayM, arrayD, arrayY, LLarray, LarrayN, LarrayM, LarrayD, LarrayY):
    while True:
        m = menu.getMouse()
        if Exit.isClicked(m):
            menu.close()
        if CAL.isClicked(m):
            for k in LLarray:
                if (k == "Not Done"):
                    WallOS(LarrayN, LarrayM, LarrayD, LarrayY, LLarray)
            CALENDAR(arrayN, arrayM, arrayD, arrayY, LarrayN, LarrayM, LarrayD, LarrayY, LLarray)
            for k in LLarray:
                if (k == "Not Done"):
                    WallOS(LarrayN, LarrayM, LarrayD, LarrayY, LLarray)
        if WOS.isClicked(m):
            WallOS(LarrayN, LarrayM, LarrayD, LarrayY, LLarray)'''

def time(Title):
    #while True:
        today1 = date.today() #today's date #(“How to Get Current Date and Time in Python?”)
        month1 = today1.strftime("%B") #today's month #(“How to Get Current Date and Time in Python?”)
        year1 = today1.strftime("%Y") #today's year #(“How to Get Current Date and Time in Python?”)
        DAY1 = today1.strftime("%d") #(“How to Get Current Date and Time in Python?”)
        today2 = datetime.now()
        Hour = today2.strftime("%H")
        Minute = today2.strftime("%M")
        Second = today2.strftime("%S")
        if (int(Hour) >= 12):
            ampm = "pm"
        if (int(Hour) < 12):
            ampm = "am" 
        Title.setText("Today is: " + month1 + ", " + DAY1 + ", "+ year1 + " at " + Hour + ":" + Minute + " " + ampm)
      

def Menu():

    today1 = date.today() #today's date #(“How to Get Current Date and Time in Python?”)
    month1 = today1.strftime("%B") #today's month #(“How to Get Current Date and Time in Python?”)
    year1 = today1.strftime("%Y") #today's year #(“How to Get Current Date and Time in Python?”)
    DAY1 = today1.strftime("%d") #(“How to Get Current Date and Time in Python?”)
    today2 = datetime.now()
    Hour = today2.strftime("%H")
    Minute = today2.strftime("%M")
    Second = today2.strftime("%S")
    ampm = ""
    
    if (int(Hour) >= 12):
        ampm = "pm"
    if (int(Hour) < 12):
        ampm = "am" 

    if (DAY1[0] == "0"):
        DAY1 = DAY1[1]

    menu = GraphWin("Menu", 630, 300) #create and open window


    
    Title = Text(Point(310, 15), "Today is: " + month1 + ", " + DAY1 + ", "+ year1 + " at " + Hour + ":" + Minute + " " + ampm)
    Title.draw(menu)
    Title.setSize(20)

    CAL = WDII(menu, "grey", "Calendar", Point(200, 100), 65) #next month button
    WOS = WDII(menu, "grey", "The Wall of Shame", Point(400, 100), 65) #next month button
    Exit = WDII(menu, "grey", "Exit", Point(300, 200), 65) #next month button

    arrayN = []
    arrayM = []
    arrayD = []
    arrayY = []
    arrayMin = []
    arrayH = []

    LarrayN = []
    LarrayM = []
    LarrayD = []
    LarrayY = []
    LLarray = []
    LarrayH = []
    LarrayMin = []

    inputN2 = []
    inputM2 = []
    inputD2 = []
    inputY2 = []
        
    inputMM3 = []
    inputDD3 = []
    inputYY3 = []
    inputHH = []
    inputMM = []

    '''thread1 = threading.Thread(target=time(Title))

    thread2 = threading.Thread(target=click(menu, CAL, WOS, Exit, arrayN, arrayM, arrayD, arrayY, LLarray, LarrayN, LarrayM, LarrayD, LarrayY))
    thread1.start()
    thread2.start()'''

    while True:
        m = menu.getMouse()
        if Exit.isClicked(m):
            break
        if CAL.isClicked(m):
            CALENDAR(arrayN, arrayM, arrayD, arrayY, LarrayN, LarrayM, LarrayD, LarrayY, LLarray, inputN2, inputM2, inputD2, inputY2, inputMM3,
                     inputDD3, inputYY3, inputHH, inputMM, arrayMin, arrayH, LarrayH, LarrayMin)
            time(Title)
        if WOS.isClicked(m):
            WallOS(LarrayN, LarrayM, LarrayD, LarrayY, LLarray, LarrayH, LarrayMin)
            time(Title)
    menu.close()

        
                

if __name__ == "__main__": # run the module
    Menu()
