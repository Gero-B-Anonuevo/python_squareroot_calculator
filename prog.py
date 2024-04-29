number = input("Please input a number you want to find the squareroot of: ") #Storing inputted data in variable
try:
    result = round(int(number)**0.5, 2) #o.5 exponent for the squareroot, limiting the decimal places
except TypeError:
    print("Please input a number.") #If the inputted data is alphabet
except ValueError:
    print("Please input a valid number.") #If the inputted data is negative
else:
    with open("sqrt_result.txt", "w") as file: #To store the result in another file
        file.write(f"{result}")