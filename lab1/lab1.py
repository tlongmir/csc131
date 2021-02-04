# Date:
#This program plans a number trick

originalNumber = int(input('Enter the number of times per week \
you would like to have ice cream (greater than zero): '))

b = originalNumber ** 2
print("Now square that number: ", b)

c = b + originalNumber
print("Add your original number to that result: ", c)

d = c // originalNumber
print("Divide that by your original number: ", d)

e = d + 17
print("Add 17: ", e)

f = e - originalNumber
print("Subtract your original number: ", f)

g = f // 6 
print("Divide by 6. The result is:", g)

print("The result is always 3.")

