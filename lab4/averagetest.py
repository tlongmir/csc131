# Name: Trevor      
# Date: 2/4/2021
# Description: Test averages
def main():

    num1 = float(input("Enter your first grade : "))
    num2 = float(input("Enter second grade: "))
    num3 = float(input("Enter your third grade: "))

    add = num1 + num2 + num3

    avg = add/3

    print("average : ", '{:.2f}'.format(avg))    

if __name__ == "__main__":
    main()