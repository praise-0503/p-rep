# MY PROJECT

#introduction
print("\n                                          WELCOME TO \n ")
print("                                      GUESS THE NUMBER\n")
print("                        ************************************************\n")
x=int(input("# To start game enter : 1 \n# To read instruction enter : 2 \n"))


# to ask the user whether to start the game or to give instruction
for i in range(5):
    if x==2:
        print("________________________________________________________________________________________________________________")
        print("|             INSTRUCTIONS                                                                                      |")
        print("| 1.The admin should enter the secret code                                                                      |")
        print("| 2.The user have to guess the value behind it(will be a number between 1 to 15)                                |")
        print("| 3.If the number is guessed in first chance score will be 20 or else 5 points will be reduced for each try     |")
        print("| 4.If the guess is wrong then hints will be provided                                                           |")
        print("| 5.You will have a total of 4 chances                                                                          |")
        print(" ________________________________________________________________________________________________________________")
        x=int(input("\n# To start game enter : 1 \n# To read instruction enter : 2\n"))
    elif x==1:
        break
    elif x!=1 and x!=2:
            print("           !!!!!!! ERORR !!!!!!!")
            x=int(input("# To start game enter : 1 \n# To read instruction enter : 2\n"))


#defining functions used in program

#1.function to find the value behind the code
def secretcode(listcode,listvalue,p):
    q=0
    for i in range(len(listcode)):
        if p==listcode[i]: #checking whether the given code is in my codelist
            q=listvalue[i] #substituting value of that code into a varable
            break
        else:
            continue
    return q

#2.function to find the score
def point(s):
    if s==1:
        score=20
    elif s==2:
        score=15
    elif s==3:
        score=10
    elif s==4:
        score=5
    return score


#main program of game
list1=["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15"]
list2=[13,2,14,7,10,8,4,1,5,12,15,6,11,9,3]
a=input("   Enter the secret code : ")
val=secretcode(list1,list2,a)      #calling function to return the value behind the code

if val==0:    #admin gave an invalid secret code
    print("   not in my list\n Invalid Code \n    !!!!ERORR!!!!")
else:
    for i in range(4):
        print("\n   CHANCE ",i+1)
        gval=int(input("   GUESS the number::"))
        if gval==val:
            print("\n\n           EXCELLENT \n        YOUR GUESS IS RIGHT\n             YOU WON\n  *******congratulations******** \n " )
            print("   Your Score Is :: ",point(i+1))
            break
        elif gval>val:
            if i==3:
                print("\n\n   ###### GAME OVER ######\n   You Have All Your Chances\n   Your Score Is : 0\n     You LOST This Game")
            else:
                print("   Try Again \n   HINT::: Guessed value is greater than the actual number!!!")
                continue
        elif gval<val:
            if i==3:
                print("\n\n   ###### GAME OVER ######\n   You Have All Your Chances\n   Your Score Is : 0\n     You LOST This Game")
            else:
                print("   Try Again \n   HINT::: Guessed value is smaller than the actual number!!!")
                continue
