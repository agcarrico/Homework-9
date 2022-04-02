# Programmers: Amanda Carrico
# Course: CS151, Dr. Olsen
# Due Date: 4/1/2022
# Homework Assignment: 9
# Problem Statement: Active Learning Task
# Data In: length of list, start value for range, end value for range
# Data Out: list of random numbers generated, certain number of "+" or "-" signs based on value in list
# Credits: In class notes, textbook


# import module to get random numbers later in program
import random
# output description to user
print ("This program will print out a certain number of '+' signs or '-' signs based on a random number in a range chosen by "
       "the user.")
print("These numbers are values in a list. The length of the list of random numbers can also be decided by you, the user.")
# get input from user
list_length = input("How long would you like your list to be? Enter a positive integer value:").strip()
# error checking input
while not list_length.isdigit():
    print ("Sorry that's not a positive integer.")
    list_length = input("How long would you like your list to be? Enter a positive integer value:").strip()
list_length = int(list_length)
start = input("What would you like the range of values that could be randomly generated to start with? Enter a positive "
              "or negative integer:").strip()
if "-" in start:
    checking_start = start[1:]
    while not checking_start.isdigit():
        print("You have chosen a negative number but it is not an integer or you have entered a negative sign when the "
              "program told you not.")
        checking_start = input("What would you like the range of values that could be randomly generated to start with? "
                               "Enter a positive integer (we will add the negative later):").strip()
    checking_start = int(checking_start)
    start = checking_start * -1
else:
    while not start.isdigit():
        print("Sorry that's not an integer.")
        checking_start = input("What would you like the range of values that could be randomly generated to start with? Enter a positive "
                           "integer:").strip()
    start = int(start)
# get input from user
end = input("What would you like the range of values that could be randomly generated to end with? Enter a positive "
              "or negative integer that is greater than the start value:").strip()
# error checking input
if "-" in end:
    checking_end = end[1:]
    while not checking_end.isdigit():
        print("Sorry that's not an integer.")
        print("What would you like the range of values that could be randomly generated to end with? ")
        checking_end = input("Enter a positive integer that is greater than the start value (we will add the negative later):").strip()
    checking_end = int(checking_end)
    end = checking_end * -1
    while end < start:
        print("That that value is not greater than the start value or you added a negative when asked not to.")
        print("What would you like the range of values that could be randomly generated to end with? ")
        checking_end = input("Enter a positive integer that is greater than the start value (we will add the negative later):").strip()
        while not checking_end.isdigit():
            print("You have chosen a negative number but it is not an integer or you have added a negative sign when "
                  "the program told you not to.")
            print("What would you like the range of values that could be randomly generated to end with?")
            checking_end = input("Enter a positive integer that is greater than the start value (we will add the negative later):").strip()
        checking_end = int(checking_end)
        end = checking_end * -1
else:
    while not end.isdigit():
        print("Sorry that's not an integer or you entered a negative when prompted not to.")
        end = input("What would you like the range of values that could be randomly generated to end with? Enter a positive "
                           "integer that is greater than the start value:").strip()
    end = int (end)
    while end < start:
        print("That that value is not more than the start value.")
        while not end.isdigit():
            print("Sorry that's not an integer.")
            end = input("What would you like the range of values that could be randomly generated to start with? Enter a positive "
                "integer that is greater than the start value:").strip()
        checking_end = int(checking_end)
        end = checking_end * -1
def print_results(numbers):
    # print the list that contains the number of times each sum is rolled (list goes from 0 to 12) for user
    print(numbers)
    # print "Sum of" index ":" for each index (each sum is at the corresponding index), from index 2 to the end (since
    # the range for sums is 2 to 12
# while loop to form list with randomly generated numbers using range user provided with input
q = 0
list = []
while q < list_length:
    a = random.randint(start,end)
    list.append(a)
    q+=1
# print list for user to see
print(list)

list2 = list
count_list = []
number_list = []
for i in range(len(list2)):
    if list2[i] != "0":
        count = list2.count(list2[i])
        count_list.append(count)
        number_list.append(list2[i])
        print("The number", list2[i], "is in this list", count, "times.")
        for n in range(i+1, len(list2)):
            if list2[n] == list2[i]:
                list2[n] = "0"
            print(list2)
print("This is a list of all of the different numbers that were randomly generated:", number_list)
print("This is a list of all of the times each number from the original list showed up, index corresponds to above printed list:", count_list)

for i

# for loop to print the "+" and "-" signs for user
for i in range(len(list)):
    value = list[i]
    var = str (value)
    j = str(i)
    print("Random number", j + ":", end=" ")
    if "-" in var:
        print("-"*-value)
    else:
        print("+"*value)
# thank user for using program
print("Thank you for using this program. Goodbye!")
