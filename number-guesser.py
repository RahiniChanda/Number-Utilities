"""
This program lets the user play three different number guessing games.
"""

print("Hello. This program will give you the choice of playing three number guessing games.")
print("")

first_num = 8.7
print("Guess the first number.")
print("")
print("It has one decimal point (in the tenths place), however if your guess rounds the same integer as the mystery number, you win.")
print("")

while True:
    user_first_guess = float(input("Your guess (between 1-10): "))

    if round(user_first_guess) == round(first_num):
        print("You win! The number was " + str(first_num) + ".")
        print("")
        break
    elif round(user_first_guess) < round(first_num):
        print("Your guess is too low. Try again!")
    elif round(user_first_guess) > round(first_num):
        print("Your guess is too high. Try again!")
    
print("Do you want to play the second game?")
print("It is the same as the previous one, except the mystery number has two decimal points (to the hundredths place).")
print("Enter 'yes' if you want to play or 'no' if you don't want to.")
user_choice_one = input("Your answer: ")
print("")

second_num = 6.98
if user_choice_one == "yes":
    print("Great choice! Guess the number.")
    
    while True:
        user_second_guess = float(input("Your guess (between 1-10): "))
        
        if round(user_second_guess) == round(second_num):
            print("You win! The number was " + str(second_num) + ".")
            print("")
            break
        elif round(user_second_guess) < round(second_num):
            print("Your guess is too low. Try again!")
        elif round(user_second_guess) > round(second_num):
            print("Your guess is too high! Try again!")
else:
    print("Have a good day. We hope you enjoyed your experience.")
    
print("Do you want to play the third game?")
print("It is the same as the previous one, except the mystery number has three decimal points (to the thousandths place).")
print("Enter 'yes' if you want to play or 'no' if you don't want to.")
user_choice_two = input("Your answer: ")
print("")

third_num = 4.791
if user_choice_two == "yes":
    print("Great choice! Guess the number.")
    
    while True:
        user_third_guess = float(input("Your guess (between 1-10): "))
        
        if round(user_third_guess) == round(third_num):
            print("You win! The number was " + str(third_num) + ".")
            print("Thank you for playing all three games.")
            break
        elif round(user_third_guess) < round(third_num):
            print("Your guess is too low. Try again!")
        elif round(user_third_guess) > round(third_num):
            print("Your guess is too high! Try again!")
else:
    print("Have a good day. We hope you enjoyed your experience.")
