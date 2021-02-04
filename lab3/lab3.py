#I know...I need to work on my column editing skills..
current_col = 1
column_width = 10
blank_char = '    '
blank_column = format(blank_char, str(column_width))

#main
def main():
    print('This program will display the monthly car payments for a given\nloan amount and loan period for interest rates from 3%-18%\n')

    principal = int(input('Enter loan amount: '))
    years = int(input('Enter number of years of loan: '))
    print('Loan Amount: ','${:.2f}'.format(principal), 'Term: ', years, 'years\n')

    rate = 3
    n = 0
    print('Interest rate', blank_char, 'Monthly Payment')

    while rate <= 18:
        num_payments = years * 12
        decimal_rate = (rate/100) / 12
        monthly_payment = (principal * decimal_rate * (1 + decimal_rate) ** num_payments) / ((1+decimal_rate) ** num_payments - 1)
        print(blank_char, rate, '%', blank_column,'${:.2f}'.format(monthly_payment))
        rate = rate + 1



if __name__ == "__main__":
    main()





#print(blank_char, rate, '%', (format(monthly_payment, '.2f')))