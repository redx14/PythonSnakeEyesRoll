#Andrey Ilkiv Assignment 4 problem 2 section 01 10/12/2020

#imports random function for RNG
import random

#initial user input and variables
#gets number of sides on both dice from input
sides = int(input("How many sides on your dice (4, 6, 8, 10, 12, 14, 16, 18, 20)? "))
roll = 0
dice1 = 0
dice2 = 0
doubles = 0
sum1 = 0
sum2 = 0
snakeeyes = False

#checks if input is valid
#if it is program runs
while sides not in range(4 , 22 , 2):
    print("Sorry, that's not a valid size.")
    sides = int(input("How many sides on your dice (4, 6, 8, 10, 12, 14, 16, 18, 20)? "))
print("" , "Thanks! Here we go ..." , "" , sep='\n')

#loop of min range 1 and max range 999
for i in range(1, 999):
    #checks if both dice equaled 1 at the same time
    #if not roll is incremented, obtained random roll for dice 1 and 2, sum of dice 1 and sum of dice 2
    #prints each roll
    if(snakeeyes == False):
        roll = roll + 1
        dice1 = random.randrange(1 , sides+1)
        dice2 = random.randrange(1 , sides+1)
        sum1 = sum1 + dice1
        sum2 = sum2 + dice2
        print(i , ". " , "Die number 1 is " , dice1 , " and die number 2 is " , dice2 , "." , sep="")
        #Checks if a double is rolled and if dice 1 and dice 2 = 1
        #if a double is rolled 1 is added to the doubles var
        #if both dice = 1 snakeeyes = true
        #loop ends
        if(dice1 == dice2):
            doubles = doubles + 1
        if(dice1 == 1 and dice2 == 1):
            snakeeyes = True
#calculates the averages for the sum of dice 1 rolls and dice 2 rolls
#calculates percentage of doubles rolled over total amount of rolls
#prints results
avg1 = format(sum1/roll, '.2f')
avg2 = format(sum2/roll, '.2f')
percentage = format((doubles/roll)*100, '.2f')
print("" , "You got snake eyes! Finally! On try number " + str(roll) + "!" , sep='\n')
print("Along the way you rolled doubles " + str(doubles) + " times (" + str(percentage) + "% of all rolls were doubles)")
print("The average roll for die #1 was " + str(avg1))
print("The average roll for die #2 was " + str(avg2))
      
