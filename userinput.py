

def main():
    '''This program demonstrates interaction with the user.'''

    userName = input("What is your name? ")
    userAge = int(input("How old are you? "))
    userWage = float(input("How much do you get paid per hour? "))

    print('hello', userName)
    print('Are you really', userAge, 'years old?')
    print("You don't look a day over 90.")
    print('Your annual salary would be $', format(2000*userWage, ".2f"), "if you work 40 hours per week.")


if __name__ == "__main__":
    main()