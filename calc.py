######################
# Created by PatrikX #
# Tested by Csanaboy #
######################
import os, time, sys, math
clear = lambda: os.system('cls')
clear()

kompActive = False
defaultActive = False

z1active = False
z2active = False
iactive = False
n1active = False
n2active = False

datasdone = False

z1 = -1
z2 = -1
m = -1
i = -1
n1 = -1
n2 = -1
cstar = 0.25


class bcolors:
    BLUE = "\033[94m"
    WHITE = "\033[1;37;40m"
    YELLOW = "\033[1;33;40m"
    GREEN = "\033[1;32;40m"
    RED = "\033[1;31;40m"

print(bcolors.GREEN +"\n######################\n# Created by PatrikX #\n# Tested by Csanaboy #\n######################"+ bcolors.WHITE)
print("\n")
print(bcolors.YELLOW +"Választási lehetőségek:\n\n" + bcolors.BLUE + "Elemi (z1 > 16) >> 1"+ bcolors.RED +" (Nem elérhető)\n\n" + bcolors.BLUE + "Kompenzált (z1 < 17) >> 2 "+ bcolors.GREEN +"(Elérhető)" + bcolors.WHITE)
typeInput = input(bcolors.BLUE + "\nVálasztott típus: " + bcolors.WHITE)

if typeInput == str("1"):
    clear()
    print(bcolors.YELLOW + "\nElemi fogaskerék számítás" + bcolors.WHITE)
    #defaultActive = True
    kompActive = True
    inputZ1 = input("Z1: ")
elif typeInput == str("2"):
    clear()
    print(bcolors.YELLOW + "\nKompenzált fogaskerék számítás" + bcolors.WHITE)
    kompActive = True
    inputZ1 = input("Z1: ")

# elemi
if defaultActive:
    if int(inputZ1) >= 17:
        z1 = inputZ1
        z1active = True
        inputZ2 = input("Z2: ")
    elif int(inputZ1) == -1:
        z1 = -1
        z1active = False
        inputZ2 = input("Z2: ")
    elif int(inputZ1) < 17:
        print(bcolors.RED + "Hiba Z1 kisebb mint 17" + bcolors.WHITE)
        sys.exit()
    
    if int(inputZ2) >= 17:
        z2 = inputZ2
        z2active = True
        inputM = input("m: ")
    elif int(inputZ2) == -1:
        z2 = -1
        z2active = False
        inputM = input("m: ")
    elif int(inputZ2) < 17:
        print(bcolors.RED + "Hiba Z2 kisebb mint 17" + bcolors.WHITE)
        sys.exit()
    
    if int(float(inputM)) > 0.0:
        m = float(inputM)
        inputI = input("i: ")
    elif inputM == 0:
        m = -1
        inputI = input("i: ")
    elif int(float(inputM)) < 1.0:
        print(bcolors.RED + "Hiba: m nem lehet 0" + bcolors.WHITE)
        sys.exit()
    
    if int(float(inputI)) > 0.0:
        i = float(inputI)
        iactive = True
        inputN1 = input("n1: ")
    elif int(inputI) == 0:
        i = -1
        iactive = False
        inputN1 = input("n1: ")
    
    if int(inputN1) > 0:
        n1 = inputN1
        n1active = True
        inputN2 = input("n2: ")
    elif int(inputN1) == 0:
        n1 = -1
        n1active = False
        inputN2 = input("n2: ")
    
    if int(inputN2) > 0:
        n2 = inputN2
        n2active = True
        inputCstar = input("c*: ")
        #datasdone = True
    elif int(inputN2) == 0:
        n2 = -1
        inputCstar = input("c*: ")
        n2active = False
        #datasdone = True
    
    if int(float(inputCstar)) >= 0:
        cstar = float(inputCstar)
        datasdone = True

    if datasdone:
        if z1active and z2active == False and iactive:
            z2 = int(z1) * float(i)
            print("\nEredmények:\nz2: "+ str(z2))
        elif z1active == False and z2active and iactive:
            z1 = int(z2) / float(i)
            print("\nEredmények:\nz1: "+ str(z1))
        elif z1active == False and z2active and iactive == False and n1active and n2active:
            i = int(n1) / float(n2)
            z1 = int(z2) / float(i)
            print("\nEredmények:\nz1: "+ str(z1) + "\ni: "+ str(i))
        elif z1active and z2active == False and iactive == False and n1active and n2active:
            i = int(n1) / float(n2)
            c = float(cstar) * float(m)
            z2 = int(z1) * float(i)
            time.sleep(1)
            d1 = int(m) * int(z1)
            d2 = int(m) * int(z2)
            da1 = (int(d1) + (float(m)*2))
            da2 = (int(d2) + (float(m)*2))
            db1 = (int(d1)*math.cos(20))
            db2 = (int(d2)*math.cos(20))
            df1 = (int(d1)-(float(m)*2)-(float(c)*2))
            df2 = (int(d2)-(float(m)*2)-(float(c)*2))
            time.sleep(2)
            print("\nEredmények:\nz2: "+ str(z2) + "\ni: "+ str(i) + "\nd1: "+ str(d1) + "\nd2: "+ str(d2)+ "\nda1: "+ str(da1) + "\nda2: "+ str(da2)+ "\ndb1: "+ str(db1) + "\ndb2: "+ str(db2)+ "\ndf1: "+ str(df1) + "\ndf2: "+ str(df2))
           # print("\nd1:"+ str(d1)) 
           ## print("d2: "+ str(d2))  
        
        

# kompenzált
elif kompActive:
    if int(inputZ1) < 17:
        z1 = inputZ1
        inputZ2 = input("z2: ")
    elif int(inputZ1) > 16:
        print(bcolors.RED + "Hiba z1 nagyobb mint 16" + bcolors.WHITE)
        sys.exit()
    
    if int(inputZ2) > 17:
        z2 = inputZ2
        inputM = input("m: ")
    elif int(inputZ2) < 16:
        print(bcolors.RED + "Hiba z2 kisebb mint 16" + bcolors.WHITE)
        sys.exit()
    
    if int(float(inputM)) > 0:
        m = float(inputM)
        inputCstar = input("c*: ")
    elif int(inputM) < 1:
        print(bcolors.RED + "Hiba: m nem lehet 0" + bcolors.WHITE)
        sys.exit()

    if int(float(inputCstar)) >= 0:
        cstar = float(inputCstar)
        kerekitesInput = input("Kerekítés(2,3,4,5,6): ")

    if int(kerekitesInput) >= 2 and int(kerekitesInput) <= 6:
        kerekites = "{:."+kerekitesInput+"f}"
        datasdone = True

        if datasdone:
            zhat = 17
            kszog = math.radians(20)
            c = float(m) * float(cstar)
            x = (float(zhat) - float(z1)) / float(zhat)
            x12 = (float(x)*float(m))
            d1 = float(m) * float(z1)
            d2 = float(m) * float(z2)
            da1 = (float(d1) + (2*float(m))) + (2*float(str(kerekites).format(x12)))
            da2 = (float(d2) + (2*float(m))) - (2*float(str(kerekites).format(x12)))
            db1 = (float(d1) + (math.cos(kszog))) + (2*float(str(kerekites).format(x12)))
            db2 = (float(d2) + (math.cos(kszog))) - (2*float(str(kerekites).format(x12)))
            df1 = (float(d1) - (2*float(m)) - (2*float(c))) + (2*float(str(kerekites).format(x12)))
            df2 = (float(d2) - (2*float(m)) - (2*float(c))) - (2*float(str(kerekites).format(x12)))
            h1 = (float(m)*2)+float(c)
            h2 = (float(m)*2)+float(c)
            ha1 = float(m) + float(str(kerekites).format(x12))
            ha2 = float(m) - float(str(kerekites).format(x12))
            hf1 = (float(m)+float(c)) - float(str(kerekites).format(x12))
            hf2 = (float(m)+float(c)) + float(str(kerekites).format(x12))
            p = (float(m)*3.14)
            s1veg = 2*float(str(kerekites).format(x12))*(math.tan(kszog))
            s1 = ((float(p)/2))+s1veg
            s2 = ((float(p)/2))-((2*float(str(kerekites).format(x12)))*(math.tan(kszog)))
            hw = (float(m)*2)
            aw = (float(d1)+float(d2))/2

            datas = []
            datas.append("\nAlap adatok:\nz1: " + str(z1) + "\nz2: " + str(z2) + "\nm: " + str(m) + "mm\nc*: " + str(cstar) + "\n-------------")
            datas.append("\nx1,2: "+ str(float(str(kerekites).format(x12)))+"mm")
            datas.append("\nd1: "+ str(float(str(kerekites).format(d1)))+"mm")
            datas.append("d2: "+ str(float(str(kerekites).format(d2)))+"mm")
            datas.append("\nda1: "+ str(float(str(kerekites).format(da1)))+"mm")
            datas.append("da2: "+ str(float(str(kerekites).format(da2)))+"mm")
            datas.append("\ndb1: "+ str(float(str(kerekites).format(db1)))+"mm")
            datas.append("db2: "+ str(float(str(kerekites).format(db2)))+"mm")
            datas.append("\ndf1: "+ str(float(str(kerekites).format(df1)))+"mm")
            datas.append("df2: "+ str(float(str(kerekites).format(df2)))+"mm")
            datas.append("\nh1: "+ str(float(str(kerekites).format(h1)))+"mm")
            datas.append("h2: "+ str(float(str(kerekites).format(h2)))+"mm")
            datas.append("\nha1: "+ str(float(str(kerekites).format(ha1)))+"mm")
            datas.append("ha2: "+ str(float(str(kerekites).format(ha2)))+"mm")
            datas.append("\nhf1: "+ str(float(str(kerekites).format(hf1)))+"mm")
            datas.append("hf2: "+ str(float(str(kerekites).format(hf2)))+"mm")
            datas.append("\nhw: "+ str(float(str(kerekites).format(hw)))+"mm")
            datas.append("aw: "+ str(float(str(kerekites).format(aw)))+"mm")
            datas.append("\nP: "+ str(float(str(kerekites).format(p)))+"mm")
            datas.append("s1: "+ str(float(str(kerekites).format(s1)))+"mm")
            datas.append("s2: "+ str(float(str(kerekites).format(s2)))+"mm")

            for data in datas:
                print(data)