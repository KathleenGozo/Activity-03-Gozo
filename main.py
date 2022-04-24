import k_stat as ks
import k_ev as ke

counter = 1
while counter == 1:
    print ("\n[1] Stat Calculator")
    print ("[2] EV Calculator")
    num0 = int(input("Choose number:"))

    bas = int (input("\nBase Stats:"))
    LVL = int (input("Level:"))
    ev = int (input("EVHP:"))
    iv = int (input("IVHP:"))
    stat = int(input("Desired increase in stat:"))

    if num0 == 1:
        print ("\nHP = ", ks.lei.hpcal(bas,iv,ev,LVL))
        print ("Attack = ", ks.lei.otherstat(bas,iv,ev,LVL))
        print ("Def = ", ks.lei.otherstat(bas,iv,ev,LVL))
        print ("Sp. Attack = ", ks.lei.otherstat(bas,iv,ev,LVL))
        print ("Sp. Def = ", ks.lei.otherstat(bas,iv,ev,LVL))
        print ("Speed = ", ks.lei.otherstat(bas,iv,ev,LVL))
        print ("\nThe needed EVs to increase stat is ", ke.kath.evneed(stat,bas,iv,ev,LVL))


    elif num0 == 2:
        print ("\n[1] Single Stat")
        print ("[2] All Stats")
        num1 = int(input("Choose a number:"))

        if num1 == 1:
            print ("\n[1] Attak")
            print ("[2] Def")
            print ("[3] SP. Attack")
            print ("[4] SP. Def")
            print ("[5] Speed")
            print ("[6] HP")
            num20= int(input ("Choose Stat: "))

            if num20 == 1 or 2 or 3 or 4 or 5:
                print ("\nThe Stat is  ", ks.lei.otherstat(bas,iv,ev,LVL))
            elif num20 == 6:
                print ("\nHP = ", ks.lei.hpcal(bas,iv,ev,LVL))


        elif num1 == 2:
            print ("\nHP = ", ks.lei.hpcal(bas,iv,ev,LVL))
            print ("Attack = ", ks.lei.otherstat(bas,iv,ev,LVL))
            print ("Def = ", ks.lei.otherstat(bas,iv,ev,LVL))
            print ("Sp. Attack = ", ks.lei.otherstat(bas,iv,ev,LVL))
            print ("Sp. Def = ", ks.lei.otherstat(bas,iv,ev,LVL))
            print ("Speed = ", ks.lei.otherstat(bas,iv,ev,LVL))

    print ("\n[1] Perform another calculation")
    print ("[2] End the program")
    num3 = int(input("Choose a number:"))
    if num3 == 2:
        break
    elif num3 == 1:
        continue
