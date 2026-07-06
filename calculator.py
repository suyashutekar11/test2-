number=int(input("Enter a integer value: "))
operator=input("Enter an operator (+, -, *, /, %): ")
if operator=="+":
    result=number+number
    print("The result is:", result)
elif operator=="-":
    result=number-number
    print("The result is:", result)
elif operator=="*":
    result=number*number
    print("The result is:", result)
elif operator=="/":
    if number==0:
        print("Error: Division by zero is not allowed.")
    else:
        result=number/number
        print("The result is:", result)
elif operator=="%":
    if number==0:
        print("Error: Modulus by zero is not allowed.")
    else:
        result=number%number
        print("The result is:", result) 
else:
    print("Invalid operator. Please enter a valid operator (+, -, *, /, %).")