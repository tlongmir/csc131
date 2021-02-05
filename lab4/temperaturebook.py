# Name: Trevor      
# Date: 2/3/2021
# Description: Temperature conversion from book


def main():

    print('This will convert temperatures (Fahrenheit/Celsius)')
    print('Enter (F) to convert Fahrenheit to Celsius')
    print('Enter (C) to convert Celsius to Fahrenheit')

    #get temp to convert
    which = input('Enter selection: ')
    while which != 'F' and which != 'C':  #input error check
        which = input("Please enter 'F' or 'C': ") #input error check
    temp = int(input('Enter temperature to convert: '))

    #determine temperature conversion needed and display results
    if which == 'F':
        converted_temp = (temp - 32) * 5/9
        print(temp, 'degrees Fahrenheit equals', format(converted_temp, '.1f'), 'degrees Celsius')

    else:
        converted_temp = (9/5 * temp) + 32
        print(temp, 'degrees Celsius equals', converted_temp, 'degrees Fahrenheit')

    

if __name__ == "__main__":
    main()