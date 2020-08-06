# imports the play sound library
from playsound import playsound
# imports the python random library
import random
# Robot Chicken program
# Programmer: Jake Stuck
# Date created 8/2/20

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.  
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.




# Function: AppendDolphinSounds
# appends dolphin sounnds to the list that 
# holds references to the audio files.
# Parameter(s): 2, a string list that contains 
# references to audio files and a single String variable 
# that holds in the reference to dolphin noises 
def AppendDolphinSounds( audioList, dolphinSounds ):

    # sets the return variable dolphinizedList equal to python's built in append method, which will append file names 
    # to the parameter audioList.
    dolphinizedList = audioList.append(dolphinSounds)

    
    return dolphinizedList





# Function: robotChicken
# Function is the driver for initiating the sounds.
# Parameter(s): 3, a string list that contains references to audio files, An integer value 
# will hold in a random number, which will be used in deteriming whether or not dolphins/dragons satanically 
# possess this robotic chicken and finally a count value which is also randomly generated and will be used 
# to determine how long the inner loop runs.
def robotChicken( audioList, randomInteger, count ): 


    # list holds in filenames that are excluded from the standard chickenList/audioList
    # items in this collection will be appended to the main playList under certian conditions
    miscSoundsList = ["dolph1.wav", "dolph2.wav, aGiantFuckingDragon.mp3"]

    # holds in a random index which will be 
    # used to determine which sound will be appended to 
    # the audioList/PlayList and what index will be played
    randomIndex = random.randint(0,2)

    # sets audioList equal to the placeholder playList
    playList = audioList

    
    
    print("\n\t Welcome to Robot Chicken, this program will emulate the sound effect side of the robot chicken")

    # prompts the user for input which will allow them to run the inner loop again if desired
    # if the user presses anything other than Y, y or yes the loop will exit and the program will close
    userConformation = input("\n\t Play chicken sounds? (y/n):  ")

    yesFlag = "Y"
    noFlag  = "N"

    # While loop will run as long as the expression below resolves true
    if(userConformation != noFlag.lower() ):

        print("\n\t Chicken noises intensifies!!")

        # plays the sound for however many times the randomized count variable dictates 
        while count > 0:

            # tests if the randomInteger is between the specified values
            # if so, then the function appendDolphinSounds is called in and then there 
            # is a small chance of hearing either a dolphin or a dragon
            if(randomInteger < 15 or randomInteger == 400):

                print("\n\t Dolphins attack!! ")
                playList =  AppendDolphinSounds( audioList, miscSoundsList[randomIndex] )
                playsound(playList[randomIndex])

            else:

                playsound(playList[randomIndex])

    else:

        print("\n\t You have chosen to exit the program! sad:( ")
        print("\n\n")
        

def main():

    #count: will hold in a random value between 69 and 420 that will be used as 
    # a counter variable
    count = random.randint(69,420)

    # randomInteger: a random integer variable which will be used
    # in determining if the chicken mutates into a dolphin or a dragon.
    randomInteger = random.randint(69, 420)
    
   
    # A list of string variables which hold in references to
    # chicken sounds
    chickenList = ["chick1.mp3", "chick2.mp3", "chick3.mp3", "chick4.mp3", "chick5.mp3"]

    # Function call
    robotChicken(chickenList, randomInteger, count)

if __name__ == "__main__":
    main()





