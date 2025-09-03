"""
f_name = input("Enter your name: ")
age = input("Enter your age: ")
print(f"Your name is {f_name} and your age is {age}")
"""

# Write a program that takes 2 numbers from user and display the sum of both numbers
# Note: anything from input is a string
#num1 = int(input("What is your first number: "))
#num2 = int(input("What is your second number: "))
#sum = num1 + num2
#print(f"The sum is {sum}")

# Write a code to help your client with money transfer
# It should ask for user total amount to send in USD
# Then it should tell how much the receiver will get in Cameroon ==> CFA
# sending fees should be 0.02 added to the total amount
# Exchange rate should be 655
sending_fees = 0.02
exchange_rate = 655
user_amount = int(input("Enter the amount: "))
fee_amount = sending_fees * user_amount
amount_plus_fees = user_amount + fee_amount
receiving_amount = exchange_rate * user_amount
print(f"The toatal amount plu fees is ${amount_plus_fees:,} and your family will receive {receiving_amount:,} CFA")


user_answer = input("Do you want to proceed (yes/no)?")
if user_answer == 'yes':
    print("Proceed with payment")
else:
    print("Thank you for stopping by")
