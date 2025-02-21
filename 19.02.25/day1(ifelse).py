'''Write a program to check if a given number is positive,
negative, or zero'''

# number = float(input("Enter a number : "))
# if number > 0 :
#     print("given number is positive")
# elif number == 0 :
#     print("given number is zero")
# else:
#     print("given number is negative")

''' Determine if a number is odd or even.'''


# num = int(input("Enter a number : "))
# if num == 0 :
#     print("given number is zero")
# elif num % 2 == 0 :
#     print("given number is even")
# else:
#     print("given number is odd")

''' Check if a person is eligible to vote (age >= 18).'''

# age = float(input("Enter your age : "))
# if age >= 18 :
#     print("you are eligible")  
# else:
#     print("not eligible")

# print("you are eligible") if age >=18 else print("not eligible")

'''Write a program to find the greatest of two numbers.'''

# num1 = float(input("Enter a number for num1 : "))
# num2 = float(input("Enter a number for num2 : "))
# print('num1 is greatest') if num1 > num2 else print('both are equal') if num1 == num2 else print ('num2 is greater')

'''Print "Pass" if a student scores more than 40 marks;
otherwise, print "Fail."'''

# marks = int(input("marks obtaine : "))
# print("pass") if marks > 40 else print("fail") 

''' Write a program to display the day of the week based on a
number input (1 for Monday, 2 for Tuesday, etc.).
'''

# day = int(input("Enter a number for day : "))

# if day == 1 :
#     print('Monday')
# elif day == 2 :
#     print('Tuesday')
# elif day == 3 :
#     print('Wednesday')
# elif day == 4 :
#     print('Thursday')
# elif day == 5 :
#     print('Friday')
# elif day == 6 :
#     print('Saturday')
# elif day == 7 :
#     print('Sunday')
# else:
#     print('invalid day')

'''Implement a simple calculator to perform addition,
subtraction, multiplication, and division.
'''

# numb1 = float(input("Enter a number for numb1 : "))
# numb2 = float(input("Enter a number for numb1 : "))
# operation = input("Enter an operation : ").lower()

# if operation == 'add' or operation == '+' :
#     print('addition of two numbers is : ',numb1+numb2)
# elif operation == 'sub' or operation == '-':
#     print('subtraction of two numbers is : ',numb1-numb2)
# elif operation == 'mul' or operation == '*':
#     print('multiplication of two numbers is : ',numb1*numb2)
# elif operation == 'div' or operation == '/':
#     if numb2 == 0:
#         print("division by zero is not possible")
#     else:
#         print('division of two numbers is : ',numb1/numb2)
# else:
#     print('invalid input')

'''Write a program to display the name of a month based on
the month number (1 for January, 2 for February, etc.).
'''

# month = int(input("Enter a number for month : "))

# if month == 1 :
#     print('January')
# elif month == 2 :
#     print('February')
# elif month == 3 :
#     print('March')
# elif month == 4 :
#     print('April')
# elif month == 5 :
#     print('May')
# elif month == 6 :
#     print('June')
# elif month == 7 :
#     print('July')
# elif month == 8 :
#     print('August')
# elif month == 9 :
#     print('September')
# elif month == 10 :
#     print('October')
# elif month == 11 :
#     print('November')
# elif month == 12 :
#     print('December')
# else:
#     print('invalid month')


'''Write a program to find the greatest of three numbers.
'''


# num1 = float(input("Enter a number for num1 : "))
# num2 = float(input("Enter a number for num2 : "))
# num3 = float(input("Enter a number for num3 : "))

# if num1>=num2 and num1>num3:
#     print(num1, "is greatest")
# elif num2>=num3 and num2>num1:
#     print(num2 ,"is greatest")
# elif num3>=num1 and num3>num2:
#     print(num3, "is greatest")
# else:
#     print("all numbers are equal so nothing is greater")


'''Check if a year is a leap year.'''

# year = int(input("Enter a year : "))
# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     print (year,"is a leap year")
# else:
#     print(year,"is not a leap year")


'''Write a program to classify a character entered by the user
as a vowel, consonant, or neither.'''

# alphabet=input("Enter a single Character :").lower()
# if len(alphabet)!=1:
#     print("Invalid")
# else:
#     if alphabet in['a','e','i','o','u']:
#         print("Vowels")
#     elif alphabet.isalpha():
#         print("consonant")
#     else:
#         print("Special characters")

'''Calculate the grade of a student based on the marks they
score:
1. 90-100: Grade A
2. 80-89: Grade B
3. 70-79: Grade C
4. <70: Fail.
'''

# marks = float(input("Enter your marks to know your grade : "))

# if marks>=90 and marks<=100:
#     print("Your grade is A")
# elif marks>=80 and marks<=89:
#     print("Your grade is B")
# elif marks>=70 and marks<=79:
#     print("Your grade is C")
# elif marks>=0 and marks<=70:
#     print('You are Failed')
# else:
#     print("Invalid input,enter marks from 0 to 100")

'''Write a program to check if three sides length form a valid
triangle.'''

# side1= float((input("Enter 1st side of triangle : ")))
# side2= float((input("Enter 2nd side of triangle : ")))
# side3= float((input("Enter 3rd side of triangle : ")))

# if side1 + side2 > side3 and side2 + side3 > side1 and side3 + side1 > side2 :
#     print ("Given sides form a valid triangle")
# else: 
#     print("Given sides dosen't form a triangle")
    



    




