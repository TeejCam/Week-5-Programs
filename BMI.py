print("Hello! I will ask you to enter your weight in pounds and height in feet and inches.")

def userWeightAndHeight():
    #let user try again, don't terminate program
    while True:
        weight = input("Enter your weight in pounds: ")
        try:
            weight = float(weight)
            if weight <= 0:
                print("Error: value must be greater than zero")
                continue
            break
        except ValueError:
            print("Error: input must be a number")

    while True:
        heightFt = input("Please enter your height in feet: ")
        try:
            heightFt = float(heightFt)
            if heightFt <= 0:
                print("Error: value must be greater than zero")
                continue
            break
        except ValueError:
            print("Error: input must be a number")

    while True:
        heightIn = input("Please enter your height in inches: ")
        try:
            heightIn = float(heightIn)
            if heightIn <= 0 or heightIn>= 12:
                print("Error: value must be greater than zero and less than 12")
                continue
            break
        except ValueError:
            print("Error: input must be a number")

    heightTotal = (heightFt * 12) + heightIn
    return weight, heightTotal

def calculateBMI(pounds, inches):
    #modified function to satisfy parameter validation requirement
    try:
        pounds = float(pounds)
        if pounds <= 0:
            raise ValueError("Input was either negative, zero, or invalid data type")

        inches = float(inches)
        if inches <= 0:
            raise ValueError("Input was either negative, zero, or invalid data type")
        BMI = (pounds / (inches*inches)) * 703
        return round(BMI, 1)

    except ValueError as e:
        print(e)
        exit()

def display():
    while True:
        weight, heightTotal = userWeightAndHeight()

        BMI = calculateBMI(weight, heightTotal)
        print("BMI: ", f"{BMI:.1f}")

        #reprompt user
        choice = input("Would you like to calculate another BMI? Type 'yes' or 'no': ").strip().lower()
        #this allows user to terminate the program
        if choice == 'no':
            print("Thank you for using the BMI calculator.")
            break

    print("Underweight: < 18.4")
    print("Normal: 18.5-24.9")
    print("Overweight: 25.0-29.9")


def displayTable():
    #function that displays a BMI table with the increments mentioned in the activity requirement
    print("BMI Table (Height in inches from 58 to 76 and Weight in pounds from 100 to 250)")

    #print labels for the columns
    print(f"\n{'Weight (lbs)':<15}", end="")
    for height in range(58, 78, 2):  # Heights from 58 to 76 in 2-inch increments
        print(f"{height:<10}", end="")
    print()

    # Print BMI values for each weight
    for weight in range(100, 260, 10):  # Weights from 100 to 250 in 10-pound increments
        print(f"{weight:<15}", end="")

        for height in range(58, 78, 2):  # Heights from 58 to 76 in 2-inch increments
            BMI = calculateBMI(weight, height)  # Calculate the BMI
            print(f"{BMI:<10.1f}", end="")  # Print BMI value for current weight and height
        print()  # This will make each row have a separation



display()
displayTable()