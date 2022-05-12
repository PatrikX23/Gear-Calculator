######################
# Created by PatrikX #
# Tested by Csanaboy #
######################

import os, time, sys, math
clear = lambda: os.system('cls')
clear()

kompActive = False
defaultActive = False

datasdone = False
menuActive = False
typeInput = False
navInput = False

loading = 0
loadtime = 5

class bcolors:
    BLUE = "\033[94m"
    WHITE = "\033[1;37;40m"
    YELLOW = "\033[1;33;40m"
    GREEN = "\033[1;32;40m"
    RED = "\033[1;31;40m"
    BG = "\033[0;37;41m"
    BG2 = "\033[0;37;44m"
    BG3 = "\033[0;37;42m"

def loadElemi():
    global loading

    while (loading < loadtime):
        loading += 0.25
        sys.stdout.write(bcolors.BG2 + '\rSzámítás |'+ bcolors.WHITE)
        time.sleep(0.1)
        loading += 0.25
        sys.stdout.write(bcolors.BG2 + '\rSzámítás /'+ bcolors.WHITE)
        time.sleep(0.1)
        loading += 0.25
        sys.stdout.write(bcolors.BG2 + '\rSzámítás -'+ bcolors.WHITE)
        time.sleep(0.1)
        loading += 0.25
        sys.stdout.write(bcolors.BG2 + '\rSzámítás \\'+ bcolors.WHITE)
        time.sleep(0.1)
    else:
        clear()
        time.sleep(0.5)
        calcElemi()

def loadKomp():
    global loading

    while (loading < loadtime):
        loading += 0.25
        sys.stdout.write(bcolors.BG2 + '\rSzámítás |'+ bcolors.WHITE)
        time.sleep(0.1)
        loading += 0.25
        sys.stdout.write(bcolors.BG2 + '\rSzámítás /'+ bcolors.WHITE)
        time.sleep(0.1)
        loading += 0.25
        sys.stdout.write(bcolors.BG2 + '\rSzámítás -'+ bcolors.WHITE)
        time.sleep(0.1)
        loading += 0.25
        sys.stdout.write(bcolors.BG2 + '\rSzámítás \\'+ bcolors.WHITE)
        time.sleep(0.1)
    else:
        clear()
        time.sleep(0.5)
        calcKomp()

def menu():
    global menuActive
    global typeInput
    global datasdone
    global navInput
   
    datasdone = False
    typeInput = False
    navInput = False
    menuActive = False
    print(bcolors.GREEN +"\n######################\n# Created by PatrikX #\n# Tested by Csanaboy #\n######################"+ bcolors.WHITE)
    print(bcolors.YELLOW +"\nVálasztási lehetőségek:\n\n" + bcolors.BLUE + "Elemi (z1 > 16) >> 1"+ bcolors.GREEN +" (Elérhető)\n\n" + bcolors.BLUE + "Kompenzált (z1 < 17) >> 2 "+ bcolors.GREEN +"(Elérhető)" + bcolors.WHITE)
    time.sleep(0.5)
    menuActive = True
    typeInput = input(bcolors.BLUE + "\nVálasztott típus: " + bcolors.WHITE)

time.sleep(0.5)
menu()

def calcElemi():
    global datasdone
    global navInput

    kszog = math.radians(20)
    c = float(m) * float(cstar)
    d1 = float(m) * float(z1)
    d2 = float(m) * float(z2)
    da1 = (float(d1) + (2*float(m)))
    da2 = (float(d2) + (2*float(m)))
    db1 = (float(d1) * (math.cos(kszog)))
    db2 = (float(d2) * (math.cos(kszog)))
    df1 = (float(d1) - (2*float(m)) - (2*float(c)))
    df2 = (float(d2) - (2*float(m)) - (2*float(c)))
    h1 = (float(m)*2)+float(c)
    h2 = (float(m)*2)+float(c)
    ha1 = float(m)
    ha2 = float(m)
    hf1 = (float(m)+float(c))
    hf2 = (float(m)+float(c))
    p = (float(m)*3.14)
    s0 = (float(p)/2)
    s1 = ((float(p)/2))*(math.tan(kszog))
    s2 = ((float(p)/2))*(math.tan(kszog))
    hw = (float(m)*2)
    aw = (float(d1)+float(d2))/2

    datasE = []
    datasE.append("\nAlap adatok:\nz1: " + str(z1) + "\nz2: " + str(z2) + "\nm: " + str(m) + "mm\nc*: " + str(cstar) + "\n-------------")

    datasE.append("\nSzín magyarázat:\n" + bcolors.BLUE + "Jelölés, eredmény\n" + bcolors.YELLOW + "[Képlet]" + bcolors.WHITE)
    
    datasE.append(bcolors.BLUE +"\nc: "+ str(float(str(kerekites).format(c)))+"mm" + bcolors.YELLOW + " [(c*) * m]"+ bcolors.WHITE)
    datasE.append(bcolors.BLUE +"\nd1: "+ str(float(str(kerekites).format(d1)))+"mm" + bcolors.YELLOW + " [m * z1]"+ bcolors.WHITE)
    datasE.append(bcolors.BLUE +"d2: "+ str(float(str(kerekites).format(d2)))+"mm" + bcolors.YELLOW + " [m * z2]"+ bcolors.WHITE)
    datasE.append(bcolors.BLUE +"\nda1: "+ str(float(str(kerekites).format(da1)))+"mm" + bcolors.YELLOW + " [d1 + 2m]"+ bcolors.WHITE)
    datasE.append(bcolors.BLUE +"da2: "+ str(float(str(kerekites).format(da2)))+"mm" + bcolors.YELLOW + " [d2 + 2m]"+ bcolors.WHITE)
    datasE.append(bcolors.BLUE +"\ndb1: "+ str(float(str(kerekites).format(db1)))+"mm" + bcolors.YELLOW + " [d1 * cos α]"+ bcolors.WHITE)
    datasE.append(bcolors.BLUE +"db2: "+ str(float(str(kerekites).format(db2)))+"mm" + bcolors.YELLOW + " [d2 * cos α]"+ bcolors.WHITE)
    datasE.append(bcolors.BLUE +"\ndf1: "+ str(float(str(kerekites).format(df1)))+"mm" + bcolors.YELLOW + " [d1 - 2m - 2c]"+ bcolors.WHITE)
    datasE.append(bcolors.BLUE +"df2: "+ str(float(str(kerekites).format(df2)))+"mm" + bcolors.YELLOW + " [d2 - 2m - 2c]"+ bcolors.WHITE)
    datasE.append(bcolors.BLUE +"\nh1: "+ str(float(str(kerekites).format(h1)))+"mm" + bcolors.YELLOW + " [2m + c]"+ bcolors.WHITE)
    datasE.append(bcolors.BLUE +"h2: "+ str(float(str(kerekites).format(h2)))+"mm" + bcolors.YELLOW + " [2m + c]"+ bcolors.WHITE)
    datasE.append(bcolors.BLUE +"\nha1: "+ str(float(str(kerekites).format(ha1)))+"mm" + bcolors.YELLOW + " (m]"+ bcolors.WHITE)
    datasE.append(bcolors.BLUE +"ha2: "+ str(float(str(kerekites).format(ha2)))+"mm" + bcolors.YELLOW + " [m]"+ bcolors.WHITE)
    datasE.append(bcolors.BLUE +"\nhf1: "+ str(float(str(kerekites).format(hf1)))+"mm" + bcolors.YELLOW + " [m + c]"+ bcolors.WHITE)
    datasE.append(bcolors.BLUE +"hf2: "+ str(float(str(kerekites).format(hf2)))+"mm" + bcolors.YELLOW + " [m + c]"+ bcolors.WHITE)
    datasE.append(bcolors.BLUE +"\nhw: "+ str(float(str(kerekites).format(hw)))+"mm" + bcolors.YELLOW + " [2m]"+ bcolors.WHITE)
    datasE.append(bcolors.BLUE +"aw: "+ str(float(str(kerekites).format(aw)))+"mm" + bcolors.YELLOW + " [(d1 + d2) / 2]"+ bcolors.WHITE)
    datasE.append(bcolors.BLUE +"\nP: "+ str(float(str(kerekites).format(p)))+"mm" + bcolors.YELLOW + " [m * π]"+ bcolors.WHITE)
    datasE.append(bcolors.BLUE +"S: "+ str(float(str(kerekites).format(s0)))+"mm" + bcolors.YELLOW + " [P / 2]"+ bcolors.WHITE)
    datasE.append(bcolors.BLUE +"s1: "+ str(float(str(kerekites).format(s1)))+"mm" + bcolors.YELLOW + " [S * tg α]"+ bcolors.WHITE)
    datasE.append(bcolors.BLUE +"s2: "+ str(float(str(kerekites).format(s2)))+"mm" + bcolors.YELLOW + " [S * tg α]"+ bcolors.WHITE)

    for data in datasE:
        print(data)

    time.sleep(0.5)
    datasdone = True
    print(bcolors.BG3 + '\nSzámítás kész!'+ bcolors.WHITE)
    print(bcolors.YELLOW + "\nNavigálási lehetőségek:\n"+bcolors.BG2 +"Főmenü - 1"+ bcolors.WHITE)
    print(bcolors.BG2 +"Kilépés - 2"+ bcolors.WHITE)
    navInput = input(bcolors.BLUE + "\nNavigáció: " + bcolors.WHITE)
    #navigate()

def calcKomp():
    global datasdone
    global navInput
    global S

    zhat = 17
    kszog = math.radians(20)
    x = (float(zhat) - float(z1)) / float(zhat)
    x12 = (float(x)*float(m))
    c = float(m) * float(cstar)
    d1 = float(m) * float(z1)
    d2 = float(m) * float(z2)
    da1 = (float(d1) + (2*float(m))) + (2*float(x12))
    da2 = (float(d2) + (2*float(m))) - (2*float(x12))
    db1 = (float(d1) * (math.cos(kszog))) + (2*float(x12))
    db2 = (float(d2) * (math.cos(kszog))) - (2*float(x12))
    df1 = (float(d1) - (2*float(m)) - (2*float(c))) + (2*float(x12))
    df2 = (float(d2) - (2*float(m)) - (2*float(c))) - (2*float(x12))
    h1 = (float(m)*2)+float(c)
    h2 = (float(m)*2)+float(c)
    ha1 = float(m)
    ha2 = float(m)
    hf1 = (float(m)+float(c)) + (float(x12))
    hf2 = (float(m)+float(c)) - (float(x12))
    p = (float(m)*math.pi)
    s0 = (float(p)/2)
    s1 = (s0) + ((2*float(x12))*(math.tan(kszog)))
    s2 = (s0) - ((2*float(x12))*(math.tan(kszog)))
    hw = (float(m)*2)
    aw = (float(d1)+float(d2))/2

    datasK = []
    datasK.append("\nAlap adatok:\nz1: " + str(z1) + "\nz2: " + str(z2) + "\nm: " + str(m) + "mm\nc*: " + str(cstar) + "\n-------------")

    datasK.append("\nSzín magyarázat:\n" + bcolors.BLUE + "Jelölés, eredmény\n" + bcolors.YELLOW + "[Képlet]" + bcolors.WHITE)
    
    datasK.append(bcolors.BLUE +"\nx: "+ str(float(str(kerekites).format(x)))+"mm" + bcolors.YELLOW + " [(zhat-z1)/zhat]"+ bcolors.WHITE)
    datasK.append(bcolors.BLUE +"x1,2: "+ str(float(str(kerekites).format(x12)))+"mm" + bcolors.YELLOW + " [x * m]"+ bcolors.WHITE)
    datasK.append(bcolors.BLUE +"c: "+ str(float(str(kerekites).format(c)))+"mm" + bcolors.YELLOW + " [(c*) * m]"+ bcolors.WHITE)
    datasK.append(bcolors.BLUE +"\nd1: "+ str(float(str(kerekites).format(d1)))+"mm" + bcolors.YELLOW + " [m * z1]"+ bcolors.WHITE)
    datasK.append(bcolors.BLUE +"d2: "+ str(float(str(kerekites).format(d2)))+"mm" + bcolors.YELLOW + " [m * z2]"+ bcolors.WHITE)
    datasK.append(bcolors.BLUE +"\nda1: "+ str(float(str(kerekites).format(da1)))+"mm" + bcolors.YELLOW + " [(d1 + 2m) + 2x1]"+ bcolors.WHITE)
    datasK.append(bcolors.BLUE +"da2: "+ str(float(str(kerekites).format(da2)))+"mm" + bcolors.YELLOW + " [(d2 + 2m) - 2x2)]"+ bcolors.WHITE)
    datasK.append(bcolors.BLUE +"\ndb1: "+ str(float(str(kerekites).format(db1)))+"mm" + bcolors.YELLOW + " [(d1 * cos α) + 2x1]"+ bcolors.WHITE)
    datasK.append(bcolors.BLUE +"db2: "+ str(float(str(kerekites).format(db2)))+"mm" + bcolors.YELLOW + " [(d2 * cos α) - 2x2]"+ bcolors.WHITE)
    datasK.append(bcolors.BLUE +"\ndf1: "+ str(float(str(kerekites).format(df1)))+"mm" + bcolors.YELLOW + " [(d1 - 2m - 2c) + 2x1]"+ bcolors.WHITE)
    datasK.append(bcolors.BLUE +"df2: "+ str(float(str(kerekites).format(df2)))+"mm" + bcolors.YELLOW + " [(d2 - 2m - 2c) - 2x2]"+ bcolors.WHITE)
    datasK.append(bcolors.BLUE +"\nh1: "+ str(float(str(kerekites).format(h1)))+"mm" + bcolors.YELLOW + " [2m + c]"+ bcolors.WHITE)
    datasK.append(bcolors.BLUE +"h2: "+ str(float(str(kerekites).format(h2)))+"mm" + bcolors.YELLOW + " [2m + c]"+ bcolors.WHITE)
    datasK.append(bcolors.BLUE +"\nha1: "+ str(float(str(kerekites).format(ha1)))+"mm" + bcolors.YELLOW + " [(m) + x1]"+ bcolors.WHITE)
    datasK.append(bcolors.BLUE +"ha2: "+ str(float(str(kerekites).format(ha2)))+"mm" + bcolors.YELLOW + " [(m) - x2]"+ bcolors.WHITE)
    datasK.append(bcolors.BLUE +"\nhf1: "+ str(float(str(kerekites).format(hf1)))+"mm" + bcolors.YELLOW + " [(m + c) - x1]"+ bcolors.WHITE)
    datasK.append(bcolors.BLUE +"hf2: "+ str(float(str(kerekites).format(hf2)))+"mm" + bcolors.YELLOW + " [(m + c) + x2]"+ bcolors.WHITE)
    datasK.append(bcolors.BLUE +"\nhw: "+ str(float(str(kerekites).format(hw)))+"mm" + bcolors.YELLOW + " [2m]"+ bcolors.WHITE)
    datasK.append(bcolors.BLUE +"aw: "+ str(float(str(kerekites).format(aw)))+"mm" + bcolors.YELLOW + " [(d1 + d2) / 2]"+ bcolors.WHITE)
    datasK.append(bcolors.BLUE +"\nP: "+ str(float(str(kerekites).format(p)))+"mm" + bcolors.YELLOW + " [m * π]"+ bcolors.WHITE)
    datasK.append(bcolors.BLUE +"S: "+ str(float(str(kerekites).format(s0)))+"mm" + bcolors.YELLOW + " [P / 2]"+ bcolors.WHITE)
    datasK.append(bcolors.BLUE +"s1: "+ str(float(str(kerekites).format(s1)))+"mm" + bcolors.YELLOW + " [(S) + (2x1 * tg α)]"+ bcolors.WHITE)
    datasK.append(bcolors.BLUE +"s2: "+ str(float(str(kerekites).format(s2)))+"mm" + bcolors.YELLOW + " [(S) - (2x2 * tg α)]"+ bcolors.WHITE)

    for data in datasK:
        print(data)

    time.sleep(0.5)
    datasdone = True
    print(bcolors.BG3 + '\nSzámítás kész!'+ bcolors.WHITE)
    print(bcolors.YELLOW + "\nNavigálási lehetőségek:\n"+bcolors.BG2 +"Főmenü - 1"+ bcolors.WHITE)
    print(bcolors.BG2 +"Kilépés - 2"+ bcolors.WHITE)
    navInput = input(bcolors.BLUE + "\nNavigáció: " + bcolors.WHITE)
    #navigate()

if menuActive:
    
    if int(typeInput) > 0 and int(typeInput) <= 2:
        
        if int(typeInput) == 1:
            clear()
            print(bcolors.YELLOW + "\nElemi fogaskerék számítás" + bcolors.WHITE)
            #defaultActive = True
            inputZ1 = input("Z1: ")
            
            if int(inputZ1) > 16:
                z1 = inputZ1
                inputZ2 = input("z2: ")
            elif int(inputZ1) < 17:
                print(bcolors.RED + "Hiba z1 kisebb mint 17" + bcolors.WHITE)
                time.sleep(0.5)
                clear()
                os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)
    
            if int(inputZ2) > 16:
                z2 = inputZ2
                inputM = input("m: ")
            elif int(inputZ2) < 17:
                print(bcolors.RED + "Hiba z2 kisebb mint 17" + bcolors.WHITE)
                time.sleep(0.5)
                clear()
                os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)
    
            if int(float(inputM)) > 0:
               m = float(inputM)
               inputCstar = input("c*: ")
            elif int(inputM) < 1:
                print(bcolors.RED + "Hiba: m nem lehet 0" + bcolors.WHITE)
                time.sleep(0.5)
                clear()
                os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)
            if int(float(inputCstar)) >= 0:
                cstar = float(inputCstar)
                kerekitesInput = input("Kerekítés(2,3,4,5,6): ")

            if int(kerekitesInput) >= 2 and int(kerekitesInput) <= 6:
                kerekites = "{:."+kerekitesInput+"f}"
                print("\n")
                loadElemi()
        elif int(typeInput) == 2:
            clear()
            print(bcolors.YELLOW + "\nKompenzált fogaskerék számítás" + bcolors.WHITE)
            #defaultActive = True
            inputZ1 = input("Z1: ")
            
            if int(inputZ1) < 17:
                z1 = inputZ1
                inputZ2 = input("z2: ")
            elif int(inputZ1) > 16:
                print(bcolors.RED + "Hiba z1 nagyobb mint 16" + bcolors.WHITE)
                time.sleep(0.5)
                clear()
                os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)
    
            if int(inputZ2) > 16:
                z2 = inputZ2
                inputM = input("m: ")
            elif int(inputZ2) < 17:
                print(bcolors.RED + "Hiba z2 kisebb mint 17" + bcolors.WHITE)
                time.sleep(0.5)
                clear()
                os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)
    
            if int(float(inputM)) > 0:
               m = float(inputM)
               inputCstar = input("c*: ")
            elif int(inputM) < 1:
                print(bcolors.RED + "Hiba: m nem lehet 0" + bcolors.WHITE)
                time.sleep(0.5)
                clear()
                os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)
            if int(float(inputCstar)) >= 0:
                cstar = float(inputCstar)
                kerekitesInput = input("Kerekítés(2,3,4,5,6): ")

            if int(kerekitesInput) >= 2 and int(kerekitesInput) <= 6:
                kerekites = "{:."+kerekitesInput+"f}"
                print("\n")
                loadKomp()
    else:
        clear()
        time.sleep(0.5)
        os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)

if int(navInput) > 0 and int(navInput) <= 2:
    if int(navInput) == 1:
        time.sleep(0.5)
        os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)
    else:
        sys.exit()
else:
    sys.exit()

