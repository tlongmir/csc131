#I know...I need to work on my column editing skills..
current_col = 1
column_width = 10
blank_char = '    '
blank_column = format(blank_char, str(column_width))

#main
def main():
    print('This program will display your monthly car payment for a given\nloan amount and loan period for your interest rate.\n')

    principal = int(input('Enter loan amount: '))
    years = int(input('Enter number of years of loan: '))
    interest = float(input('Enter interest rate: '))
    print('Loan Amount: ','${:.2f}'.format(principal), 'Term: ', years, 'years\n')

    print('Interest rate', blank_char, 'Monthly Payment')

  
    num_payments = years * 12
    decimal_rate = (interest/100) / 12
    monthly_payment = (principal * decimal_rate * (1 + decimal_rate) ** num_payments) / ((1+decimal_rate) ** num_payments - 1)
    print(blank_char, interest, '%', blank_column,'${:.2f}'.format(monthly_payment))
    print()
    print('Make your monthly payment of ''${:.2f}'.format(monthly_payment), 'and you will pay off your loan in exactly',num_payments, 'months\n')
    # print('and you will pay off your\nloan in exactly ',num_payments, 'months.')
    



if __name__ == "__main__":
    main()
