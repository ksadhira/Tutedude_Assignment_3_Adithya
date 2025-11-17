''' Write a Python program that:
1.   Defines a function named factorial that takes a number as an argument and calculates its factorial using a loop or recursion.
2.   Returns the calculated factorial.
3.   Calls the function with a sample number and prints the output.'''


def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)

Enter_num = int(input("Enter the Number to check the Factorial: "))
print("The Factorial of the Given Number is: ",factorial(Enter_num))
