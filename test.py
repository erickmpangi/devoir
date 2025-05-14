print("Welcome to the Band Name Generator.")
street = input("What's the name of the city you grew up in?\n")
pet = input("What's your pet's name?\n")
print("Your band name could be " + street + " " + pet)

# Language: python
print("Day 1 - Python Print Function\nThe function is declared like this:\nprint('what to print')")
print("Hello " + "Angela")
#fix bug
print("Day 1 - Sting manipulation")
print('String Concatenation is done with the "+" sign.' )
print('e.g. print("Hello " + "world")')
print("New lines can be created with a backslash and n.")
#Print a len input
print( len( input("What is your name?") ) )
#exercice
a=input("A: ")
b=input("B: ")
c=a
a=b
b=c
print("Value A="+ a)
print("Value B=" + b)

#final test
print("Welcome to the Band Name Generator.")
city = input("What's name of the city you grew up in ? \n")
pet = input("What's your pet's name?\n")
print("Your band name could be " + city + " " + pet)

#int, float and str

num_char = len(input("What is your name?"))
new_num_char = str(num_char)
print("Your name has " + new_num_char + " characters.")

a = float(123)
print(type(a))
print(str(70) + str(100))

#Exercice 1

numbers = input("Type a two digit number: ")
print(int(numbers[0]) + int(numbers[1]))

#Exercice 2

height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

bmi = int(weight) / float (height) ** 2

print(int(bmi))

#Exercice 3

age = input("What is your current age? ")
age_as_int = int(age)

year_left = 90 - age_as_int
mouth_left = year_left * 12
week_left = year_left * 52
days_left = year_left * 365
message = f"you have {days_left} days, {week_left} weeks,  {mouth_left} mouths left"

print(message)

#Exercice 4
print("Welcome to the tip calculator")

Total_bill = float(input("What was the total bill ? $"))
Percentage = int (input("What percentage tip would you like to give ? 10, 12, or 15 ?"))
People = int(input("How many people split the bill ?"))

Percentage = Percentage / 100
Percentage_total = float(Percentage + 1)
bill = float(Total_bill * Percentage_total)
Paid = float(bill / People)
Paid_total = round(Paid,2)

print(f"Each person should pay $ {Paid_total}")

#if and else

number = int(input("Witch number do you want to change?"))

if number % 2 == 0:
    print("This is an even number")
else:
    print("This is an odd number")

#Exercice 5

Height = float(input("Enter your height in m: ?"))
Weight = float(input("Enter your weight in kg"))
BMI = float (Weight) / float(Height) ** 2
BMI_round = round(BMI,1)

if BMI_round > 18.5:
    if BMI_round <= 25:
        print(f"Your BIM is {BMI_round} You have a Normal Weight")

    elif BMI_round <= 30:
        print(f"Your BIM is {BMI_round} You are Over Weight")

    elif BMI_round <= 35:
        print(f"Your BIM is {BMI_round} You are Obese")

    else:
        print(f"Your BIM is {BMI_round} You are clinically Obese")

else:
    print(f"Your BIM is {BMI_round} You are underweight")

#Exercice 6

Year = int(input("Which year do you want to check ? "))
if Year % 4 == 0:
    if Year % 100 == 0:
        print("It is 2 Leap Year")
    else: 
        if Year % 400 == 0:
            print("It is a Leap Year")
        else:
            print("It is Not a Leap Year")
else:
    print("It is a Not Leap Year")

# Exercice 7

print("Welcome to Python Pizza Deliveries! ")
size = input("What size pizza do you want? S, M or L : ")
add_pepperoni = input("Do you want pepperoni? Yes or No : ")
extra_cheese = input("Do you want extra cheese? Yes or No : ")
small_price = 15
medium_price = 20
large_price = 25

if size == "S":
    small_price_pepperoni = small_price + 2

    if add_pepperoni == "Yes":
        if extra_cheese == "Yes":
            small_price_pepperoni_cheese = small_price_pepperoni + 1
            print(f"Your final bill is: ${small_price_pepperoni_cheese}.")
        else:
            print(f"Your final bill is : ${small_price_pepperoni}.")

    else:
        if extra_cheese == "Yes":
            small_price_cheese = small_price + 1
            print(f"Your final bill is: ${small_price_cheese}.")
        else:
            print(f"Your final bill is : ${small_price}.")

elif size == "M":
    medium_price_pepperoni = medium_price + 3

    if add_pepperoni == "Yes":
        if extra_cheese == "Yes":
            medium_price_pepperoni_cheese = medium_price_pepperoni + 1
            print(f"Your final bill is: ${medium_price_pepperoni_cheese}.")
        else:
            print(f"Your final bill is : ${medium_price_pepperoni}.")

    else:
        if extra_cheese == "Yes":
            medium_price_cheese = medium_price + 1
            print(f"Your final bill is : ${medium_price_cheese}.")
        else:
            print(f"Your final bill is : ${medium_price}.")


elif size == "L":
    large_price_pepperoni = large_price + 3

    if add_pepperoni == "Yes":
        if extra_cheese == "Yes":
            large_price_pepperoni_cheese = large_price_pepperoni + 1
            print(f"Your final bill is: ${large_price_pepperoni_cheese}.")
        else:
            print(f"Your final bill is : ${large_price_pepperoni}.")
    else:
        if extra_cheese == "Yes":
            large_price_cheese = large_price + 1
            print(f"Your final bill is : ${large_price_cheese}.")
        else:
            print(f"Your final bill is : ${large_price}.")
else:

    print("Sorry, enter a valid size please")

#EXERCICE 8

print("WELCOME TO THE LOVE CALCULATOR")

name1 = input("What is your name ? \n")
name2 = input("What is their name ?\n")

name = str((name1 + name2).lower())

T_name = name.count("t")
R_name = name.count("r")
U_name = name.count("u")
E_name = name.count("e")

True_name = T_name + R_name + U_name + E_name

L_name = name.count("l")
O_name = name.count("o")
V_name = name.count("v")

Love_name = L_name + O_name + V_name + E_name

X= int(f"{True_name}"+f"{Love_name}")

if X < 10 or X >  90 :
    print(f"Your score is {X}, you go together like coke and mentos.")
elif  40 <= X <= 50 :
    print(f"Your score is {X}, you alright together.")
else:
    print(f"Your score is {X}.")

#EXERCICE 9

print("WELCOME TO TREASURE ISLAND\n"
      "YOUR MISSION IS TO FIND THE TREASURE")

decision1 = input("Left or Right ? ").lower()
if decision1 == "left" :
    decision2 = input("swim or wait ? ").lower()
    if decision2 == "wait" :
        decision3 = input("which dor ? : Red, Blue or Yellow ? ").lower()
        if decision3 == "yellow" :
            print('''           
                                                        /\ /|
                                                       /  \---._
                                                      / / `     `\|
                                                      \ \   `'<@)@)      
                                                      /`         ~ ~._ 
                                                     /                `() 
                                                    /    \   (` ,_.:.  /
                                                   / ~    `\   (vVvvvvV
                                                  /       |`\_ `^^^/
                                              ___/________|_  `---'
                                             (_____R_E_X____) _
                                             _/~          | `(_)
                                           _/~             \  
                                         _/~               |
                                       _/~                 |
                                     _/~                   |
                                   _/~         ~.          |
                                 _/~             \        /\|
                             __/~               /`\     `||
                           _/~      ~~-._     /~   \     ||
                           /~             ~./~'      \    |)
                         /                 ~.        \   )|
                         /                    :       |   ||
                    jgs  |                    :       |   ||
                         |                   .'       |   ||
                    __.-`                __.'--.      |   |`---. 
                 .-~  ___.         __.--~`--.))))     |   `---.)))
                `---~~     `-...--.________)))))      \_____)))))
                ''')

        elif decision3 == "blue" or "red" :
            print("GAME OVER")
        else :
            print("GAME OVER")
    else :
        print("GAME OVER")
else :
    print("GAME OVER")


 #EXERICICE 10

import random

C = random.randint(0,1)
if C == 0 :
    print("Tails")
else:
    print("Heads")

f = random.random() * 5
print(f)

#EXERCICE 11

import random

names_string = input("Give me everybody's names, separated by a coma : ")
names = names_string.split(",")
num_random = random.randint(0,len(names) - 1)
names_random = names[num_random]

print(f"{names_random} is going to buy the meal today !")

#EXERCICES 12

raw1 = ["◻️", "◻️", "◻️"]
raw2 = ["◻️", "◻️", "◻️"]
raw3 = ["◻️", "◻️", "◻️"]
Map = [raw1, raw2, raw3]
print(f"{raw1}\n{raw2}\n{raw3}")
position = input("where do you want to put the treasure ? ")
horizontal = int(position[0])
vertical = int(position[1])

col = (Map[vertical - 1])
col[horizontal - 1] = "X"

print(f"{raw1}\n{raw2}\n{raw3}")


#EXERCICES 13

import random
numbers_rand = random.randint (1,3)

numbers = (int(input("What do you chose? Type 1 for Rock, 2 for Paper or 3 for Scissor : ")))
# numbers = input()
# Rock_number = 1
# Paper_number = 2
# Scissor_number = 3
Rock = '''
    ________
___'   _____)
      (_____)
      (_____)
      (____)
---,__(___)
'''
Paper = '''
    _________
___'    _____)___
           ______)
         ________)
       _________)
---,___________)
'''
Scissor = '''
    _________
___'    _____)_____
           ________)
         __________)
       (_____)
---,___(___)
'''
if  numbers == 1 and numbers_rand == 3 :
    print(f"Your choice : {Rock}\n and The computer choice : {Scissor}\n YOU WIN")
elif numbers == 1 and numbers_rand == 2 :
    print(f"Your choice : {Rock}\n and The computer choice : {Paper}\n YOU LOSE")
elif numbers == 1 and numbers_rand == 1 :
    print(f"Your choice : {Rock}\n and The computer choice : {Rock}\n START AGAIN")
elif numbers == 2 and numbers_rand == 1 :
    print(f"Your choice : {Paper}\n and The computer choice : {Rock}\n YOU WIN")
elif numbers == 2 and numbers_rand == 2 :
    print(f"Your choice : {Paper}\n and The computer choice : {Paper}\n START AGAIN")
elif numbers == 2 and numbers_rand == 3 :
    print(f"Your choice : {Paper}\n and The computer choice : {Rock}\n YOU LOSE")
elif numbers == 3 and numbers_rand == 1 :
    print(f"Your choice : {Scissor}\n and The computer choice : {Rock}\n YOU LOSE")
elif numbers == 3 and numbers_rand == 2 :
    print(f"Your choice : {Scissor}\n and The computer choice : {Paper}\n YOU WIN")
elif numbers == 3 and numbers_rand == 3 :
    print(f"Your choice : {Scissor}\n and The computer choice : {Scissor}\n START AGAIN")
else:
    print("START AGAIN")

#EXERCICE 1 DAY 5 forloop (boucle)

# fruits = ["Apple", "Peach", "Pear"]
# for fruit in fruits:
#     # print(fruit)
#     print(fruit + "pie")
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)
total_height = 0
total_student = 0
for height in student_heights:
    total_height += height
# print(total_height)
for student in student_heights:
    total_student += 1
# print(total_student)
average_height = round(total_height / total_student)
print(average_height)

#EXERCICE 2 DAY 5 forloop (boucle)

student_scores = input("Input a list of student heights ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)
highest_score = 0
lowermost_score = 0
for score in student_scores:
    if score > highest_score:
        highest_score = score
print(f" Te highest_score in the class is : {highest_score}")
#EXERCICES 3 DAY 5
total_even_number = 0
for number in (range(2, 101, 2)):
    total_even_number += number
print(total_even_number)

#EXRCICES 4 DAY 5
for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0 :
        print("FizzBuzz")
    elif number % 3 == 0 :
        print("Fizz")
    elif number % 5 == 0 :
        print("Buzz")
    else:
        print(number)

#EXRCICES 5 DAY 5

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '+']

print("WELCOME TO THE PASSWORD GENERATOR")

number_letters = int(input("How many letters would you like in your password ? :\n"))
number_symbols = int(input("How many symbols would you want in your password ? : \n"))
number_numbers = int(input("How many numbers would you want in your password ? : \n"))

letter = 0
number = 0
symbol = 0
password_list = []
password = ""
for l in range(0, number_letters):
    password_list.append(random.choice(letters))
    # print(letters[letter])
for s in range(0,number_symbols):
    password_list += random.choice(symbols)
    # print(symbols[symbol])
for n in range(0,number_numbers):
    password_list += random.choice(numbers)
    # print(password_list)
random.shuffle(password_list)
for p in password_list:
    password += p
print(f'Your password is {password}')



