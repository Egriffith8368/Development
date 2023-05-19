import random
import time
com=""
co=""
tyr=10
def reset():
    data = open("data.txt","w")
    data.write("1")
    att=0
    re=""
    print("Deleteing saved data...")
    time.sleep(1)
    print("Creating new save data..")
    time.sleep(2)
    print("LOADING.")
    time.sleep(.25)
    print("LOADING..")
    time.sleep(.25)
    print("LOADING...")
    time.sleep(.25)
    print("LOADING.")
    time.sleep(.25)
    print("LOADING..")
    time.sleep(.25)
    print("LOADING...")
    time.sleep(.25)
    print("LOADING.")
    time.sleep(.25)
    print("100%")
    time.sleep(1)



ty=0
att=0
print("Hello and welcome to word guesser.")
time.sleep(1)
print("You progress will be saved as you play this game.")
time.sleep(1)
print("you can continue right where you left off")
time.sleep(1)
print("Loading your data...")
time.sleep(2)



while 0!=100:
    re=input("Too continue press enter, to reset save data type 'RESET'")
    if re=="":
        time.sleep(.2)
        print("LOADING SAVE....")
        time.sleep(1)
        data = open("data.txt","r+")
        lev=data.read()
        co!="com"
        

    
    elif re=="RESET":
        reset()
        data = open("data.txt","r+")
        lev=data.read()
        co!="com"
        print("Your data was succsessfully Reset. Please restart the program and select continue.")
        time.sleep(1000000)

    if lev=="1":
        while ty!=10 and co!="com":
            anw="cat"
            print("LEVEL:1")
            print("CLUE:")
            print("c_t")
            an=input("Enter your guess here:")
            if an==anw:
                print("You passed this level")
                data = open("data.txt","w")
                data.write("2")
                data.close()
                data = open("data.txt","r+")
                lev=data.read()
                co="com"
            else:
                ty=ty+1
                tyr=tyr-ty
                print(f"Sorry thats wrong. You have {tyr} trys left.")
    elif lev=="2":

        while ty!=10:

            anw="house"
            print("LEVEL:2")
            print("CLUE:")
            print("h_u_e")
            an=input("Enter your guess here:")
            if an==anw:
                print("You passed this level")
                data.close()
                data = open("data.txt","w")
                data.write("3")
                data.close()
                data = open("data.txt","r+")
                lev=data.read()
            else:
                ty=ty+1
                print(f"Sorry thats wrong. You have {ty} trys left.")
    elif lev=="3":
        while ty!=10:

            anw="chicken"
            print("LEVEL:3")
            print("CLUE:")
            print("c_i___n")
            an=input("Enter your guess here:")
            if an==anw:
                print("You passed this level")
                data = open("data.txt","w")
                data.write("4")
                data.close
                data = open("data.txt","r+")
                lev=data.read()
            else:
                ty=ty+1
                print(f"Sorry thats wrong. You have {ty} trys left.")
    elif lev=="4":

        while ty!=10:

            anw="computer"
            print("LEVEL:4")
            print("CLUE:")
            print("com_____")
            an=input("Enter your guess here:")
            if an==anw:
                print("You passed this level")
                data = open("data.txt","w")
                data.write("5")
                data.close()
                data = open("data.txt","r+")
                lev=data.read()
            else:
                ty=ty+1
                print(f"Sorry thats wrong. You have {ty} trys left.")
    elif lev=="5":

        while ty!=10:

            anw="building"
            print("LEVEL:5")
            print("CLUE:")
            print("bu__d__g")
            an=input("Enter your guess here:")
            if an==anw:
                print("You passed this level")
                data = open("data.txt","w")
                data.write("6")
                data.close()
                data = open("data.txt","r+")
                lev=data.read()
            else:
                ty=ty+1
                print(f"Sorry thats wrong. You have {ty} trys left.")
    elif lev=="6":

        while ty!=10:

            anw="copyright"
            print("LEVEL:6")
            print("CLUE:")
            print("co_____t")
            an=input("Enter your guess here:")
            if an==anw:
                print("You passed this level")
                data = open("data.txt","w")
                data.write("7")
                data.close()
                data = open("data.txt","r+")
                lev=data.read()
            else:
                ty=ty+1
                print(f"Sorry thats wrong. You have {ty} trys left.")
    elif lev=="7":

        while ty!=10:

            anw="binary"
            print("LEVEL:6")
            print("CLUE:")
            print("b____y")
            an=input("Enter your guess here:")
            if an==anw:
                print("You passed this level")
                data = open("data.txt","w")
                data.write("8")
                data.close()
                data = open("data.txt","r+")
                lev=data.read()
            else:
                ty=ty+1
                print(f"Sorry thats wrong.")
    elif lev=="8":
        ty=0
        while ty!=5:

            anw="dog"
            print("LEVEL:6")
            print("CLUE:")
            print("__g")
            an=input("Enter your guess here:")
            if an==anw:
                print("You passed this level")
                data = open("data.txt","w")
                data.write("9")
                data = open("data.txt","r+")
                lev=data.read()
            else:
                ty=ty+1
                print(f"Sorry thats wrong. You have {ty} trys left.")
    elif lev=="9":

        while ty!=10:

            anw="national"
            print("LEVEL:6")
            print("CLUE:")
            print("___io___")
            an=input("Enter your guess here:")
            if an==anw:
                print("You passed this level")
                data = open("data.txt","w")
                data.write("10")
                data = open("data.txt","r+")
                lev=data.read()
            else:
                ty=ty+1
                print(f"Sorry thats wrong. You have {ty} trys left.")
    elif lev=="10":

        while ty!=10:

            anw="program"
            print("LEVEL:6")
            print("CLUE:")
            print("p______")
            an=input("Enter your guess here:")
            if an==anw:
                print("You passed this level")
                data = open("data.txt","w")
                data.write("11")
                data = open("data.txt","r+")
                lev=data.read()
            else:
                ty=ty+1
                print(f"Sorry thats wrong. You have {ty} trys left.")
    elif lev=="11":

        while ty!=10:

            anw="inhail"
            print("LEVEL:11")
            print("CLUE:")
            print("____i_")
            an=input("Enter your guess here:")
            if an==anw:
                print("You passed this level")
                data = open("data.txt","w")
                data.write("12")
                data = open("data.txt","r+")
                lev=data.read()
            else:
                ty=ty+1
                print(f"Sorry thats wrong. You have {ty} trys left.")
    elif lev=="12":

        while ty!=10:

            anw="pneumonoultramicroscopicsilicovolcanoconiosis"
            print("LEVEL:11")
            print("CLUE:")
            print("______________________i_____ovolcano_______")
            an=input("Enter your guess here:")
            if an==anw:
                print("You passed this level")
                data = open("data.txt","w")
                data.write("13")
                data = open("data.txt","r+")
                lev=data.read()
            else:
                ty=ty+1
                print(f"Sorry thats wrong. You have {ty} trys left.")
    if ty==10:
        print("Sorry the answer was {anw}. Your save is being reset")        
        time.sleep(2)
        reset()    
    else:
        data= open("data.txt","r+")
        lev=data.read()
    
        




print(f"You have succsessfully finished the game. The next time you start the game your saved data will be reset")