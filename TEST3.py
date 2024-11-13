from graphics import*
from Button import*
from datetime import date #(“How to Get Current Date and Time in Python?”)
from datetime import datetime
from TTT import*
from Finished import*
from WOS import*
from MUL import*
from REMIND import*
from RMUL import*

class CALENDAR:
    def __init__ (self, arrayN, arrayM, arrayD, arrayY, LarrayN, LarrayM, LarrayD, LarrayY, LLarray,
                  inputN2, inputM2, inputD2, inputY2, inputMM3, inputDD3, inputYY3, inputHH, inputMM, arrayMin, arrayH, LarrayH, LarrayMin): #("self in Python, Demystified")
        
        def RN(today, DAY, MONTH, YEAR, today2, Hour, Minute, month, year, inputN2, inputM2, inputD2, inputY2, inputMM3, inputDD3, inputYY3, inputHH, inputMM, OMonths):
            today = date.today() #today's date #(“How to Get Current Date and Time in Python?”)
            month = today.strftime("%B") #today's month #(“How to Get Current Date and Time in Python?”)
            year = today.strftime("%Y") #today's year #(“How to Get Current Date and Time in Python?”)
            DAY = today.strftime("%d") #(“How to Get Current Date and Time in Python?”)

            today2 = datetime.now()
            Hour = int(today2.strftime("%H"))
            Minute = int(today2.strftime("%M"))

            if (DAY[0] == "0"):
                DAY = DAY[1]

            DAY = int(DAY) #(Ronquillo)

            MONTH = month

            YEAR = int(year) #(Ronquillo)

            M = 0
            MM = 0
            MMM = False
            MMMM = 0
            MMMMM = False

            MUL1 = []
            MUL2 = []
            MUL3 = []
            MUL4 = []


            for x in range(len(inputM2)):
                for p in range (len(OMonths)):
                    if (inputM2[x] == OMonths[p]):
                        MMMM = p
                    if (inputMM3[x] == OMonths[p]):
                        M = p
                    if (MONTH == OMonths[p]):
                        MM = p
                if (inputM2[x] == MONTH and int(inputD2[x]) < DAY and int(inputY2[x]) == YEAR):
                    MMMMM = True
                if (MMMM < MM and int(inputY2[x]) == YEAR):
                    MMMMM = True
                if (int(inputY2[x]) < YEAR):
                    MMMMM = True
                if (inputMM3[x] == MONTH and inputDD3[x] == DAY and inputYY3[x] == YEAR and inputHH[x] == Hour and inputMM[x] <= Minute):
                    MMM = True
                if (inputMM3[x] == MONTH and inputDD3[x] == DAY and inputYY3[x] == YEAR and inputHH[x] < Hour):
                    MMM = True
                if (inputMM3[x] == MONTH and inputDD3[x] < DAY and inputYY3[x] == YEAR):
                    MMM = True
                if (M < MM and inputYY3[x] == YEAR):
                    MMM = True
                if (inputYY3[x] < YEAR):
                    MMM = True
                if(MMM == True and MMMMM == False):
                    inputN2.pop(x)
                    inputM2.pop(x)
                    inputD2.pop(x)
                    inputY2.pop(x)
                    inputMM3.pop(x)
                    inputDD3.pop(x)
                    inputYY3.pop(x)
                    inputHH.pop(x)
                    inputMM.pop(x)
                    MMM = False
                if(MMM == True and MMMMM == False):
                    MUL1.append(inputN2[x])
                    MUL2.append(inputM2[x])
                    MUL3.append(inputD2[x])
                    MUL4.append(inputY2[x])
                    inputN2.pop(x)
                    inputM2.pop(x)
                    inputD2.pop(x)
                    inputY2.pop(x)
                    inputMM3.pop(x)
                    inputDD3.pop(x)
                    inputYY3.pop(x)
                    inputHH.pop(x)
                    inputMM.pop(x)
                MMM = False
                MMMMM = False
            if (len(MUL1) > 0):
                Multiple2(MUL1, MUL2, MUL3, MUL4)
                    
        def AAA(arrayN, arrayM, arrayD, arrayY, LarrayN, LarrayM, LarrayD, LarrayY, LLarray, OMonths, month, year, DAY, L, L1, today, today2, Hour, Minute, arrayMin, arrayH, LarrayH, LarrayMin):
            today = date.today() #today's date #(“How to Get Current Date and Time in Python?”)
            month = today.strftime("%B") #today's month #(“How to Get Current Date and Time in Python?”)
            year = today.strftime("%Y") #today's year #(“How to Get Current Date and Time in Python?”)
            DAY = today.strftime("%d") #(“How to Get Current Date and Time in Python?”)

            today2 = datetime.now()
            Hour = int(today2.strftime("%H"))
            Minute = int(today2.strftime("%M"))

            if (DAY[0] == "0"):
                DAY = DAY[1]

            DAY = int(DAY) #(Ronquillo)

            A = False

            WOSTF = False

            
            L1 = len(arrayY)
            for n in range(L1):
                if(arrayD[n] == DAY and arrayM[n] == month and arrayY[n] == int(year) and arrayH[n] < Hour): #(Ronquillo)
                    A = True
                if(arrayD[n] == DAY and arrayM[n] == month and arrayY[n] == int(year) and arrayH[n] == Hour and arrayMin[n] < Minute): #(Ronquillo)
                    A = True
                if(arrayY[n] < int(year)): #(Ronquillo)
                    A = True
                if(arrayD[n] < DAY and arrayM[n] == month and arrayY[n] == int(year)): #(Ronquillo)
                    A = True
                L = OMonths.index(month) # ("Python List index()")
                if (L > OMonths.index(arrayM[n]) and arrayY[n] == int(year)): #(Ronquillo) # ("Python List index()")
                    A = True
                if(A == True):
                    LarrayN.append(arrayN[n])
                    LarrayM.append(arrayM[n])
                    LarrayD.append(arrayD[n])
                    LarrayY.append(arrayY[n])
                    LLarray.append("Not Done")
                    LarrayH.append(arrayH[n])
                    LarrayMin.append(arrayMin[n])
                    arrayN.pop(n) #("Remove an item from a list in Python (clear, pop, remove, del)")
                    arrayM.pop(n)
                    arrayD.pop(n)
                    arrayY.pop(n)
                    arrayMin.pop(n)
                    arrayH.pop(n)
                A = False
            for k in LLarray:
                if (k == "Not Done"):
                    WOSTF = True
            if (WOSTF == True):
                WallOS(LarrayN, LarrayM, LarrayD, LarrayY, LLarray, LarrayH, LarrayMin)
            
                            
        def DMonth(CURY, CURM, calendar, Month2020L, Month2020D, OMonths, ODays, Days, NumDay, DAY, MONTH, YEAR, arrayN, arrayM, arrayD, arrayY, arrayT, arrayT3, arrayT2, arrayT5,
                   arrayTH6, arrayTM7, arrayH, arrayMin):
            
            OffMonth = 0 #OffMonth is an integer
            IsJanuraryORFeburary = False #IsJanuraryORFeburary is a boolean
            leapYear = 0 #leapYear is an integer
            M = 0 #M is an integer
            
            DifYear = CURY - 2020 #year difference between the current year and 2020

            for g in range(len(OMonths)): #loop by the amount of months
                if (OMonths[g] == CURM): # try to find what number in order the current month is
                    OffMonth = g
                    break
                
            if (CURM == "Janurary" or CURM == "February"): #is the current month a month with a delayed effect from
                IsJanuraryORFeburary = True #a leap year?


            for y in range(len(ODays)):#loops by amount of days in a week
                if (ODays[y] == Month2020D[OffMonth]): #finds where the day places in order of the week
                    M = y + 1
                    break


            while (DifYear >= 0): #run until the year difference becomes negative
                if (IsJanuraryORFeburary == True): #if month is Jan. or Feb and there is the first leap year
                    if (leapYear == 0): #subtract by an additionall one because of the leap year delay
                        DifYear = DifYear - 5
                    
                    if (leapYear != 0):
                        DifYear = DifYear - 4       # don't subtract by an additionall one because the leap year delay
                                                        #already happened
                if (IsJanuraryORFeburary != True): #if month is not Jan. or Feb always subrtact by four to reach the 
                    DifYear = DifYear - 4           #the leap year
                if (DifYear < 0):                   #if it reaches a negative, there is no more leap year
                     break
                leapYear = leapYear + 1 #add an one every 4 or 5 years because of the leap year
                
            if (IsJanuraryORFeburary == True):
                leapYear = leapYear + 1


            DifYear = CURY - 2020 #redo DifYear because it got changed
            MM = DifYear + leapYear + M #all of the days added together

            while (MM >= 8): #subtract by weeks to get a specific day
                MM = MM - 7 #MM now represents a specific day from sunday to saturday or from 0 to 6
                

            shiftX = 0 #the number necessary to shift the day cell horozontally
            shiftY = 0 #the number necessary to shift the day cell vertically
            
            MMM = 0 # counting number for knowing when to start and end days
            
            Num = 0 # counting number for day numbers

            TAsk = ""

            TASk = 0

            RET = 0

            RET2 = 0

            for w in range(len(arrayT3)):
                arrayT3.pop(0)
                arrayT2.pop(0)
                arrayTH6.pop(0)
                arrayTM7.pop(0)
                
            for e in range (len(arrayT5)):
                arrayT5.pop(0)

            
            for i in range(6):
                for j in range(7):
                    shiftX = 120 * j
                    shiftY = 120 * i
                    RET = 0
                    if (MM -1 <= MMM): #if specific day is less or equal to amount it loops start to create day cells
                        if (DAY == Num + 1 and MONTH == CURM and YEAR == CURY):
                            Days.append(Square(calendar, "grey", "", Point(60 + shiftX, 210 + shiftY), 60))
                        else:
                            Days.append(Square(calendar, "white", "", Point(60 + shiftX, 210 + shiftY), 60))
                        Num = Num + 1
                        NumDay.append(Square(calendar, "grey", str(Num), Point(15 + shiftX, 165 + shiftY), 15))
                    for l in range(len(arrayD)):
                        if(arrayD[l] == Num):
                            if(arrayM[l] == CURM):
                                if(arrayY[l] == CURY):
                                    arrayT3.append(arrayD[l])
                                    arrayT2.append(arrayN[l])
                                    arrayTH6.append(arrayH[l])
                                    arrayTM7.append(arrayMin[l])
                                    TASk = l
                                    RET = RET + 1
                    if (RET == 1):
                        arrayT.append(TasK(calendar, "grey", arrayN[TASk], Point(60 + shiftX, 210 + shiftY), 60))
                        arrayT5.append(Num)
                    if (RET > 1):
                        arrayT.append(TasK(calendar, "grey", "...", Point(60 + shiftX, 210 + shiftY), 60))
                        arrayT5.append(Num)
                    if (CURM != "February"): #if not Feburary, end when the number of loops = the amount of days there are
                        if (Num == Month2020L[OffMonth]):
                            break
                    if (CURM == "February"): #if Feburary during a non leap year, end when the number of loops 
                        if (DifYear % 4 != 0):      # = the amount of days there are minus one because the array contains the amount # (Carnes)
                            if (Num == Month2020L[OffMonth] - 1): # of days during a leap year
                                break
                    if (CURM == "February"): #if Feburary during a leap year, end when the number of loops =
                        if (DifYear % 4 == 0): #  the amount of days there are # (Carnes)
                            if (Num == Month2020L[OffMonth]):
                                break
                    MMM = MMM + 1 #add one every time it loops
                if (CURM != "February"): #if not Feburary, end when the number of loops = the amount of days there are
                    if (Num == Month2020L[OffMonth]):
                        break
                if (CURM == "February"): #if Feburary during a non leap year, end when the number of loops 
                    if (DifYear % 4 != 0):      # = the amount of days there are minus one because the array contains the amount # (Carnes)
                        if (Num == Month2020L[OffMonth] - 1): # of days during a leap year
                            break
                if (CURM == "February"): #if Feburary during a leap year, end when the number of loops =
                    if (DifYear % 4 == 0): #  the amount of days there are # (Carnes)
                        if (Num == Month2020L[OffMonth]):
                            break
            '''print(arrayT3)
            print(arrayT2)
            print(arrayTH6)
            print(arrayTM7)
            print(arrayT5)'''


        def Calendar():

            calendar = GraphWin("Calendar", 1000, 870) #create and open window

            today = date.today() #today's date #(“How to Get Current Date and Time in Python?”)
            month = today.strftime("%B") #today's month #(“How to Get Current Date and Time in Python?”)
            year = today.strftime("%Y") #today's year #(“How to Get Current Date and Time in Python?”)
            DAY = today.strftime("%d") #(“How to Get Current Date and Time in Python?”)

            today2 = datetime.now()
            Hour = int(today2.strftime("%H"))
            Minute = int(today2.strftime("%M"))

            if (DAY[0] == "0"):
                DAY = DAY[1]

            DAY = int(DAY) #(Ronquillo)

            MONTH = month

            YEAR = int(year) #(Ronquillo)

            AMonthYear = []

            AMonthYear.append(WDII(calendar, "grey", year + " " + month, Point(420, 30), 60)) #current month and year GUI
            
            Sunday = WDII(calendar, "grey", "Sunday", Point(60, 120), 60) #week GUI
            Monday = WDII(calendar, "grey", "Monday", Point(180, 120), 60)
            Tuesday = WDII(calendar, "grey", "Tuesday", Point(300, 120), 60)
            Wednesday = WDII(calendar, "grey", "Wednesday", Point(420, 120), 60)
            Thursday = WDII(calendar, "grey", "Thursday", Point(540, 120), 60)
            Friday = WDII(calendar, "grey", "Friday", Point(660, 120), 60)
            Saturday = WDII(calendar, "grey", "Saturday", Point(780, 120), 60)

            NextM = WDII(calendar, "grey", "Next Month", Point(920, 100), 65) #next month button
            PreviousM = WDII(calendar, "grey", "", Point(920, 210), 65) #previous month button
            Tasks = WDII(calendar, "grey", "Upcoming Tasks", Point(920, 320), 65) #button to display task window
            Close = WDII(calendar, "grey", "Back", Point(920, 630), 65) #back button
            F = WDII(calendar, "grey", "Finish", Point(920, 430), 65) #next month button
            R = WDII(calendar, "grey", "Remind", Point(920, 530), 65) #next month button

            Month2020L = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] #the amount of days in a month in order in 2020
            
            Month2020D = ["Wednesday", "Saturday", "Sunday", "Wednesday", "Friday", "Monday", "Wednesday", "Saturday",
                           "Tuesday", "Thursday", "Sunday", "Tuesday"] #what day each month started in 2020

            OMonths = ["Janurary", "February", "March", "April", "May", "June", "July", "August", "September",
                       "October", "November", "December"] #months in order
            
            ODays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"] #days in order

            Days = [] #array of day cells
            NumDay = [] #array of week cells

            arrayT = []
            arrayT2 = []
            arrayT3 = []
            arrayT4 = []
            arrayT5 = []
            arrayTH6 = []
            arrayTM7 = []
            arrayTH8 = []
            arrayTM9 = []

            DMonth(int(year), month, calendar, Month2020L, Month2020D, OMonths, ODays, Days, NumDay, DAY, MONTH, YEAR, arrayN, arrayM, arrayD, arrayY, arrayT, arrayT3, arrayT2, arrayT5,
                   arrayTH6, arrayTM7, arrayH, arrayMin)
                

            REPEAT = 0
            REPEAT2 = 0
            BREPEAT = False

            
            REMONTH = 0
            REMONTH2 = 0

            L = 0
            L1 = 0



            for g in range(len(OMonths)): #loop by the amount of months
                if (OMonths[g] == month): # try to find what number in order the current month is
                    REMONTH = g
                    REMONTH2 = g
                    break
                
            RN(today, DAY, MONTH, YEAR, today2, Hour, Minute, month, year, inputN2, inputM2, inputD2, inputY2, inputMM3, inputDD3, inputYY3, inputHH, inputMM, OMonths)
            AAA(arrayN, arrayM, arrayD, arrayY, LarrayN, LarrayM, LarrayD, LarrayY, LLarray, OMonths, month, year, DAY, L, L1, today, today2, Hour, Minute, arrayMin, arrayH
                        , LarrayH, LarrayMin)
                

            while True:
                m = calendar.getMouse()
                if Close.isClicked(m):
                    AAA(arrayN, arrayM, arrayD, arrayY, LarrayN, LarrayM, LarrayD, LarrayY, LLarray, OMonths, month, year, DAY, L, L1, today, today2, Hour, Minute, arrayMin, arrayH
                        , LarrayH, LarrayMin)
                    RN(today, DAY, MONTH, YEAR, today2, Hour, Minute, month, year, inputN2, inputM2, inputD2, inputY2, inputMM3, inputDD3, inputYY3, inputHH, inputMM, OMonths)
                    break
                if NextM.isClicked(m):
                    AAA(arrayN, arrayM, arrayD, arrayY, LarrayN, LarrayM, LarrayD, LarrayY, LLarray, OMonths, month, year, DAY, L, L1, today, today2, Hour, Minute, arrayMin, arrayH
                        , LarrayH, LarrayMin)
                    RN(today, DAY, MONTH, YEAR, today2, Hour, Minute, month, year, inputN2, inputM2, inputD2, inputY2, inputMM3, inputDD3, inputYY3, inputHH, inputMM, OMonths)
                    PreviousM = WDII(calendar, "grey", "Previous Month", Point(920, 210), 65) #previous month button
                    REPEAT = REPEAT + 1
                    if (OMonths[REMONTH + REPEAT - 1] == "December"):
                        REPEAT2 = REPEAT2 + 1
                        REPEAT = 0
                        REMONTH = 0
                    for l in range(len(Days)):
                        Days[0].undraw("F") # Undraw
                        Days.pop(0)
                        NumDay[0].undraw("F")#Undraw
                        NumDay.pop(0)
                    for r in range(len(arrayT)):
                        arrayT[0].undraw("F")
                        arrayT.pop(0)
                    Days = [] #array of day cells
                    NumDay = [] #array of week cells
                    AMonthYear[0].undraw("F")#Undraw
                    AMonthYear.pop(0)
                    AMonthYear.append(WDII(calendar, "grey", str(int(year) + REPEAT2) + " " + OMonths[REMONTH + REPEAT], Point(420, 30), 60)) #(Ronquillo)
                    DMonth(int(year) + REPEAT2, OMonths[REMONTH + REPEAT], calendar, Month2020L, Month2020D, OMonths, ODays, Days, NumDay, DAY, MONTH, YEAR, arrayN, arrayM, arrayD, arrayY, arrayT
                           , arrayT3, arrayT2, arrayT5, arrayTH6, arrayTM7, arrayH, arrayMin) #(Ronquillo)

                    
                if PreviousM.isClicked(m):
                    BREPEAT = False
                    AAA(arrayN, arrayM, arrayD, arrayY, LarrayN, LarrayM, LarrayD, LarrayY, LLarray, OMonths, month, year, DAY, L, L1, today, today2, Hour, Minute, arrayMin, arrayH
                        , LarrayH, LarrayMin)
                    RN(today, DAY, MONTH, YEAR, today2, Hour, Minute, month, year, inputN2, inputM2, inputD2, inputY2, inputMM3, inputDD3, inputYY3, inputHH, inputMM, OMonths)
                    if (OMonths[REMONTH + REPEAT] == month and str(int(year) + REPEAT2) == year): #(Ronquillo)
                        BREPEAT = True
                    if (BREPEAT == False):
                        REPEAT = REPEAT - 1
                        if (OMonths[REMONTH + REPEAT + 1] == "Janurary"):
                            REPEAT2 = REPEAT2 - 1
                            REPEAT = 11
                            REMONTH = 0
                        for l in range(len(Days)):
                            Days[0].undraw("F")#it UNDREWWWWWW!!!!!!!!!!!!!!!
                            Days.pop(0) #("Remove an item from a list in Python (clear, pop, remove, del)")
                            NumDay[0].undraw("F")#it UNDREWWWWWW!!!!!!!!!!!!!!!
                            NumDay.pop(0) #("Remove an item from a list in Python (clear, pop, remove, del)")
                        for r in range(len(arrayT)):
                            arrayT[0].undraw("F")
                            arrayT.pop(0) #("Remove an item from a list in Python (clear, pop, remove, del)")
                        Days = [] #array of day cells
                        NumDay = [] #array of week cells
                        AMonthYear[0].undraw("F")#it UNDREWWWWWW!!!!!!!!!!!!!!!
                        AMonthYear.pop(0)
                        AMonthYear.append(WDII(calendar, "grey", str(int(year) + REPEAT2) + " " + OMonths[REMONTH + REPEAT], Point(420, 30), 60)) #(Ronquillo)
                        DMonth(int(year) + REPEAT2, OMonths[REMONTH + REPEAT], calendar, Month2020L, Month2020D, OMonths, ODays, Days, NumDay, DAY, MONTH, YEAR, arrayN, arrayM, arrayD, arrayY, arrayT,
                               arrayT3, arrayT2, arrayT5, arrayTH6, arrayTM7, arrayH, arrayMin) #(Ronquillo)
                    if (OMonths[REMONTH + REPEAT] == "Janurary" and str(int(year) + REPEAT2) == str(int(year) + 1)): #(Ronquillo)
                        PreviousM = WDII(calendar, "grey", "", Point(920, 210), 65) #previous month button
                    if (OMonths[REMONTH + REPEAT] != "Janurary" and str(int(year) + REPEAT2) != str(int(year) + 1)): #(Ronquillo)
                        if (OMonths[REMONTH + REPEAT] == OMonths[REMONTH2] and str(int(year) + REPEAT2) == str(int(year))): #(Ronquillo)
                            PreviousM = WDII(calendar, "grey", "", Point(920, 210), 65) #previous month button
                            
                if Tasks.isClicked(m):
                    AAA(arrayN, arrayM, arrayD, arrayY, LarrayN, LarrayM, LarrayD, LarrayY, LLarray, OMonths, month, year, DAY, L, L1, today, today2, Hour, Minute, arrayMin, arrayH
                        , LarrayH, LarrayMin)
                    RN(today, DAY, MONTH, YEAR, today2, Hour, Minute, month, year, inputN2, inputM2, inputD2, inputY2, inputMM3, inputDD3, inputYY3, inputHH, inputMM, OMonths)
                    TT(arrayN, arrayM, arrayD, arrayY, arrayMin, arrayH)
                    AAA(arrayN, arrayM, arrayD, arrayY, LarrayN, LarrayM, LarrayD, LarrayY, LLarray, OMonths, month, year, DAY, L, L1, today, today2, Hour, Minute, arrayMin, arrayH
                        , LarrayH, LarrayMin)
                    RN(today, DAY, MONTH, YEAR, today2, Hour, Minute, month, year, inputN2, inputM2, inputD2, inputY2, inputMM3, inputDD3, inputYY3, inputHH, inputMM, OMonths)
                    for l in range(len(Days)):
                        Days[0].undraw("F") # Undraw
                        Days.pop(0)
                        NumDay[0].undraw("F")#Undraw
                        NumDay.pop(0)
                    for r in range(len(arrayT)):
                        arrayT[0].undraw("F")
                        arrayT.pop(0)
                    Days = [] #array of day cells
                    NumDay = [] #array of week cells
                    DMonth(int(year) + REPEAT2, OMonths[REMONTH + REPEAT], calendar, Month2020L, Month2020D, OMonths, ODays, Days, NumDay, DAY, MONTH, YEAR, arrayN, arrayM, arrayD, arrayY, arrayT
                           , arrayT3, arrayT2, arrayT5, arrayTH6, arrayTM7, arrayH, arrayMin) #(Ronquillo)

                    
                if F.isClicked(m):
                    AAA(arrayN, arrayM, arrayD, arrayY, LarrayN, LarrayM, LarrayD, LarrayY, LLarray, OMonths, month, year, DAY, L, L1, today, today2, Hour, Minute, arrayMin, arrayH
                        , LarrayH, LarrayMin)
                    RN(today, DAY, MONTH, YEAR, today2, Hour, Minute, month, year, inputN2, inputM2, inputD2, inputY2, inputMM3, inputDD3, inputYY3, inputHH, inputMM, OMonths)
                    Finish(arrayN, arrayM, arrayD, arrayY, LLarray, LarrayN, LarrayM, LarrayD, LarrayY, arrayMin, arrayH, LarrayH, LarrayMin
                           , inputN2, inputM2, inputD2, inputY2, inputMM3, inputDD3, inputYY3, inputHH, inputMM)
                    AAA(arrayN, arrayM, arrayD, arrayY, LarrayN, LarrayM, LarrayD, LarrayY, LLarray, OMonths, month, year, DAY, L, L1, today, today2, Hour, Minute, arrayMin, arrayH
                        , LarrayH, LarrayMin)
                    RN(today, DAY, MONTH, YEAR, today2, Hour, Minute, month, year, inputN2, inputM2, inputD2, inputY2, inputMM3, inputDD3, inputYY3, inputHH, inputMM, OMonths)
                    for l in range(len(Days)):
                        Days[0].undraw("F") # Undraw
                        Days.pop(0)
                        NumDay[0].undraw("F")#Undraw
                        NumDay.pop(0)
                    for r in range(len(arrayT)):
                        arrayT[0].undraw("F")
                        arrayT.pop(0)
                    Days = [] #array of day cells
                    NumDay = [] #array of week cells
                    DMonth(int(year) + REPEAT2, OMonths[REMONTH + REPEAT], calendar, Month2020L, Month2020D, OMonths, ODays, Days, NumDay, DAY, MONTH, YEAR, arrayN, arrayM, arrayD, arrayY, arrayT
                           , arrayT3, arrayT2, arrayT5, arrayTH6, arrayTM7, arrayH, arrayMin) #(Ronquillo)
                for p in range(len(arrayT)):
                    if arrayT[p].isClicked(m):
                        '''print(arrayT3)
                        print(arrayT5)
                        print(arrayT2)'''
                        for u in range(len(arrayT4)):
                            arrayT4.pop(0) #("Remove an item from a list in Python (clear, pop, remove, del)")
                            arrayTH8.pop(0)
                            arrayTM9.pop(0)
                        for y in range(len(arrayT3)):
                            if (arrayT3[y] == arrayT5[p]):
                                arrayT4.append(arrayT2[y])
                                arrayTH8.append(arrayTH6[y])
                                arrayTM9.append(arrayTM7[y])
                        AAA(arrayN, arrayM, arrayD, arrayY, LarrayN, LarrayM, LarrayD, LarrayY, LLarray, OMonths, month, year, DAY, L, L1, today, today2, Hour, Minute, arrayMin, arrayH
                            , LarrayH, LarrayMin)
                        RN(today, DAY, MONTH, YEAR, today2, Hour, Minute, month, year, inputN2, inputM2, inputD2, inputY2, inputMM3, inputDD3, inputYY3, inputHH, inputMM, OMonths)
                        Multiple(arrayT4, arrayTH8, arrayTM9)
                        AAA(arrayN, arrayM, arrayD, arrayY, LarrayN, LarrayM, LarrayD, LarrayY, LLarray, OMonths, month, year, DAY, L, L1, today, today2, Hour, Minute, arrayMin, arrayH,
                            LarrayH, LarrayMin)
                        RN(today, DAY, MONTH, YEAR, today2, Hour, Minute, month, year, inputN2, inputM2, inputD2, inputY2, inputMM3, inputDD3, inputYY3, inputHH, inputMM, OMonths)
                if R.isClicked(m):
                    RN(today, DAY, MONTH, YEAR, today2, Hour, Minute, month, year, inputN2, inputM2, inputD2, inputY2, inputMM3, inputDD3, inputYY3, inputHH, inputMM, OMonths)
                    remind(arrayN, arrayM, arrayD, arrayY, inputN2, inputM2, inputD2, inputY2, inputMM3, inputDD3, inputYY3, inputHH, inputMM)
                    RN(today, DAY, MONTH, YEAR, today2, Hour, Minute, month, year, inputN2, inputM2, inputD2, inputY2, inputMM3, inputDD3, inputYY3, inputHH, inputMM, OMonths)
            calendar.close()
        Calendar()
            
