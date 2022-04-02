# Programmers:  Amanda Carrico and Hillary Nguyen
# Course:  CS151, Dr. Olsen
# Due Date: 3/29/22
# Lab Assignment: 7
# Problem Statement:  Create a program to display the distribution of rolls of two dice.
# Data In: number of times the user wants to roll the two dice
# Data Out: histogram displaying the distribution of the sums of the values rolled by the two dice
# Credits: Class notes and videos

# import module to use the function to get a random number between two values
import random

# function for obtaining the two values for the two dice using the random module and randint function
def roll():
    result = random.randint(1, 6)
    result2 = random.randint(1, 6)
    # sum the two values
    sum = result + result2
    # return the sum (variable) to number_list function to use later in the program
    return sum

# function for printing out the "histogram"
def print_results(numbers):
    # print the list that contains the number of times each sum is rolled (list goes from 0 to 12) for user
    print(numbers)
    # print "Sum of" index:" for each index (each sum is at the corresponding index), from index 2 to the end (since
    # the range for sums is 2 to 12
    for i in range(2, len(numbers)):
        j = str(i)
        print("Sum of", j + ":", "*"*(numbers[i]))


for i in range(2, len(numbers)):
    print("Sum of ", end='')
    print(i, end='')
    print(": ", end='')
    # for each index print one "*" for each number at the index (ex: sum of 2 at index 2 is "Sum of 2:" "**")
    for i in range(0, numbers[i]):
        print('*', end='')
    print()

# function for adding a number (+1) to the corresponding index each time a roll results in the two dice summing to that number
# (ex: one die rolls a 2 and the other rolls a 3, sum = 5 so at index 5 we add 1)
def numbers_list(rolls):
    # store the list in numbers
    numbers = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    # add one to index when dice rolled sum to index
    for i in range(0, rolls):
        sum = roll()
        numbers[sum] = numbers[sum] + 1
    # return number (list) to main function to use later in program
    return numbers

# function for user input and error checking
def rolls_input():
    # ask user for input
    rolls = input("how many rolls do you want to do?").strip()
    # when the user does not input a positive integer, ask to input a different number
    while not rolls.isdigit():
        print("This input is invalid. Please enter a positive integer value.")
        rolls = input("how many rolls do you want to do?").strip()
    # typecast to an integer
    rolls = int(rolls)
    # return rolls (variable) to the main function to use later
    return rolls

# function to print statements to user and call other functions of program
def main():
    # output to user description of program
    print("This program will display the distribution of rolls of two dice.")
    # call all other functions in program
    rolls = rolls_input()
    numbers = numbers_list(rolls)
    print_results(numbers)
    # thank user for using program
    print("Thank you for using this program!")

# call the main function which will call all other functions
main()