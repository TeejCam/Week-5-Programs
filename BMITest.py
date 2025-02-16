import BMI

# Here i am testing 120 pounds and 65 inches, a pretty common input. The expected outcome is 20
def testCalculateBMI():
    assert BMI.calculateBMI(120, 65) == 20.0

# I am testing 200 pounds and 74 inches in a similar fashion
def testCalculateBMI2():
    assert BMI.calculateBMI(200, 74) == 25.7

# Once again, I am testing for this combination of pounds and inches
def testCalculateBMI3():
    assert BMI.calculateBMI(150, 71) == 20.9

# This test is designed to fail. I made the result two decimal places, when the function actually rounds to one
def testCalculateBMI4():
    assert BMI.calculateBMI(203, 75) == 25.37

# This is also designed to fail. I need to see if the function is actually rounding to one decimal place
# And if the program will recognize when the rounding is off
def testCalculateBMI5():
    assert BMI.calculateBMI(85, 53) == 21.27