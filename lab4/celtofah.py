# Name: Trevor      
# Date: 2/3/2021
# Description: Simple Cel to Fah Temperature conversion 

def main():

    print('This will convert temperatures (Fahrenheit/Celsius)')

    temp = int(input('Enter temperature to convert Celsius to Fahrenheit: '))

    converted_temp = (9/5 * temp) + 32
    print(temp, 'degrees Celsius equals', format(converted_temp, '.1f'), 'degrees Fahrenheit')

if __name__ == "__main__":
    main()