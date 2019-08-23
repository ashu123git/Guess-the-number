#it's Ashutosh Choubey
print("\t\t\t\t\t\t\t\tCOME LET'S PLAY A GAME")
print("-->Guess the number taken by me\n-->You have only 10 guesses")
a=53
c=10
while(c>0):
    b=int(input("Enter any number = "))
    if(b<a):
        print("Your number is less than my number")
        c=c-1
        print("Number of guesses left = ",c)
        continue
    elif(b>a):
        print("Your number is greater than my number")
        c=c-1
        print("Number of guesses left = ",c)
        continue
    else:
        print("Congrats, you have won the game in ",10-c+1,"guesses.")
        print("")
        exit()
print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tGame over")