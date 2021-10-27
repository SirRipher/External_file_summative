#--------
#External_Files_Summative
#Graden_Rusk
#Oct_22_2021
#--------

#----Info----#
#external files are good for my code because it allows you to be able to have your character be read off even if you made the character
#way earlier, and you can make as many files as you want and then have the code read them all out for you.
#and then you don't have to worry about it being deleted when the code is done. In my code it helps you so that you can keep the information
#you get and let the computer read it off at a different time. Good examples for using external files is if you use a resume website it will
#make a new file for you to use when you download it so that you can keep it forever, and another example is you could be playing minecraft,
#and your world will be saved onto your computer so that even if you delete minecraft you can still load into older worlds.
#lastly it will save all of the data placed in them until you delete them yourself so you can keep it forever.
#Data that could be stored, could be photos, lists, names, links, whole word files, minecraft maps, really anything.(almost)

#----Lists\Dictionaries----#
import random#imports random for me
#----Functions----#

def random(x):
    import random
    math = random.randint(x * 1, x * 20)
    return random.randint(x * 1, x * 20)#makes my random function, picks a number between 0 and 21 for a power level.

def start(new_file):#start of new function taking the information form new_file
    writing = open(new_file, 'w')#opens the new_file and writes to it
    print("Let's start off by getting some details about your new character.")
    gender = input("Are you male or female?\n>>>" )
    if gender == 'male':
        writing.write("Male")#writes male to the file
    else:
        writing.write("Female")#writes female to the file
    print("We can save this character so that you can use it at a later date.")
    print("We have three options: golem, knight, and ninja.")
    type_1 = input("What are you?\n>>>" )
    if type_1 == 'golem':
        print("You have chosen to be a golem.")
        writing.write("\nGolem")#writes golem to the file
    elif type_1 == 'knight':
        print("You have chosen to be a Knight")
        writing.write("\nKnight")#writes knight to the file
    else:
        print("You have chosen to be a ninja.")
        writing.write("\nNinja")#writes ninja to the file
    writing.close()#closes the file for me so it doesn't stay open and cause me problems
    middle(new_file)#stats the next function still with the file name
    
def middle(new_file):#middle file with the file name
    try:
        writing = open(new_file, 'a')#opens new_file and appends to it.
        print("Now CHOSE YOUR  WEAPON!")
        print("You have full freedom of choice for this one.")
        print("ALthough I reccomend a katana, fists, or a spear.")
        weapon = input("What is your weapon of choice?\n>>>" )
        if weapon == 'katana':
            print("You have chosen to weild a katana!")
            writing.write("\nKatana")#adds katana to the file
        elif weapon == 'fists':
            print("You have chosen to use your fists!")
            writing.write("\nFists")#adds fists to the file
        else:
            print("You have chosen to weild a spear!")
            writing.write("\nSpear")#or it can add the spear to the file
        print("Next let's add a special power for your characters to have.")
        print("""You now have two options.
1.freeze time.
2.'The Force'""")
        try:
            power = int(input(">>>" ))
            if power == 1:
                print("Your character now has the power of freezing time.")
                writing.write("\nFreeze Time")#finally it adds freeze time to the file
        
            else:
                print("Your character now has the ability to use 'The Force'.")
                writing.write("\nThe Force")#adds the force to the file
        except:
            print("You were obviously supposed to pick a number.")
            print("You get 'The Force'.")
            writing.write("\nThe Force")#writes foce to the file
        power_level = random(1)#uses the power level function and gives us a power level
        writing.write(f"\n{power_level}")#adds power level to the list
        print(f"The power level of it is {power_level}.")
        writing.close()#closes the file for us
    except:
        print("That file does not exist, would you like to make a new file?")
        print("Please select a file")
        print("What will the file name be?")
        file_name = input(">>>" )
        new_file = file_name + '.txt'#makes a new text file using the awnser from file_name
        start(new_file)#starts start funct
    read(new_file)#starts read funct
    
def read(new_file):#opens read funct and the file
    reading = open(new_file, 'r')#opens the file to read mode
    working = reading.readlines()#adds each line to their own part of a list
    print(working)
    if 'Male\n' in working:#this will do the check for everything in the list and print out the only acceptable option.
        if 'Golem\n' in working:
            if 'Katana\n' in working:
                if 'Freeze Time\n' in working:
                    print("You are a Male golem who weilds a Katana and can freeze time.")
                else:
                    print("you are a male golem who weilds a Katana and can use the force.")
            elif 'Fists\n' in working:
                if 'Freeze Time\n' in working:
                    print("You are a Male golem who fights with their fists and can freeze time.")
                else:
                    print("you are a male golem who fights with their fists and can use the force.")
            else:
                if 'Freeze Time\n' in working:
                    print("You are a Male golem who fights with their spear and can freeze time.")
                else:
                    print("you are a male golem who fights with their spear and can use the force.")
        elif 'Knight\n' in working:
            if 'Katana\n' in working:
                if 'Freeze Time\n' in working:
                    print("You are a Male knight who weilds a Katana and can freeze time.")
                else:
                    print("you are a male knight who weilds a Katana and can use the force.")
            elif 'Fists\n' in working:
                if 'Freeze Time\n' in working:
                    print("You are a Male knight who fights with their fists and can freeze time.")
                else:
                    print("you are a male knight who fights with their fists and can use the force.")
            else:
                if 'Freeze Time\n' in working:
                    print("You are a Male knight who fights with their spear and can freeze time.")
                else:
                    print("you are a male knight who fights with their spear and can use the force.")
        else:
            if 'Katana\n' in working:
                if 'Freeze Time\n' in working:#Congrats on making it this far.
                    print("You are a Male ninja who weilds a Katana and can freeze time.")
                else:
                    print("you are a male ninja who weilds a Katana and can use the force.")
            elif 'Fists\n' in working:
                if 'Freeze Time\n' in working:
                    print("You are a Male ninja who fights with their fists and can freeze time.")
                else:
                    print("you are a male ninja who fights with their fists and can use the force.")
            else:
                if 'Freeze Time\n' in working:
                    print("You are a Male ninja who fights with their spear and can freeze time.")
                else:
                    print("you are a male ninja who fights with their spear and can use the force.")
    else:
        if 'Golem\n' in working:
            if 'Katana\n' in working:
                if 'Freeze Time\n' in working:
                    print("You are a female golem who weilds a Katana and can freeze time.")
                else:
                    print("you are a female golem who weilds a Katana and can use the force.")
            elif 'Fists\n' in working:
                if 'Freeze Time\n' in working:
                    print("You are a female golem who fights with their fists and can freeze time.")
                else:
                    print("you are a female golem who fights with their fists and can use the force.")
            else:
                if 'Freeze Time\n' in working:
                    print("You are a female golem who fights with their spear and can freeze time.")
                else:
                    print("you are a female golem who fights with their spear and can use the force.")
        elif 'Knight\n' in working:
            if 'Katana\n' in working:
                if 'Freeze Time\n' in working:
                    print("You are a female knight who weilds a Katana and can freeze time.")
                else:
                    print("you are a female knight who weilds a Katana and can use the force.")
            elif 'Fists\n' in working:
                if 'Freeze Time\n' in working:#almost done
                    print("You are a female knight who fights with their fists and can freeze time.")
                else:
                    print("you are a female knight who fights with their fists and can use the force.")
            else:
                if 'Freeze Time\n' in working:
                    print("You are a female knight who fights with their spear and can freeze time.")
                else:
                    print("you are a female knight who fights with their spear and can use the force.")
        else:
            if 'Katana\n' in working:
                if 'Freeze Time\n' in working:
                    print("You are a female ninja who weilds a Katana and can freeze time.")
                else:
                    print("you are a female ninja who weilds a Katana and can use the force.")
            elif 'Fists\n' in working:
                if 'Freeze Time\n' in working:
                    print("You are a female ninja who fights with their fists and can freeze time.")
                else:
                    print("you are a female ninja who fights with their fists and can use the force.")
            else:
                if 'Freeze Time\n' in working:
                    print("You are a female ninja who fights with their spear and can freeze time.")
                else:
                    print("you are a female ninja who fights with their spear and can use the force.")
                #I added all of those lines just to show that it reads everything and works properly.
                    #and that it can actually read it.
    power = working[4]#finds the fourth thing in the list
    print(f"With a power level of {power}.")#prints off the fourth thing in the list

#----Main Code----#
if __name__ == '__main__':#checks to see if it's the main file, if it is it plays anything below it.
    print("welcome to Castles and Peasants character creater.")
    choice = int(input("""What are you doing today?
1. Read file
2. Make + Read file.
>>> """))
    try:#tries these.
        if choice == 1:
                 print("What will the file name be?")
                 print("(Don't add the .txt),")
                 file_name = input(">>>" )
                 new_file = file_name + '.txt'#checks for file
                 read(new_file)#opens the read function
        else:
                 print("What will the file name be?")
                 file_name = input(">>>" )
                 new_file = file_name + '.txt'
                 start(new_file)#starts the start function with the file name.
    except:#this happens when it don't work.
        print("Either you can't read or you typed in a file that isn't there.")
        print("figure it out.")
        print("Why do you think there are numbers there?")



