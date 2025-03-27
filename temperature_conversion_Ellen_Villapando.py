# asks user to enter a Celsius temperature
temp_c = float(
    input(
        'Enter temperature in degree Celsius you would like to convert to Fahrenheit: '
    ))
temp_c_divide = float(temp_c) * 9
temp_c_add = float(temp_c_divide) / 5
#this is the final conversion
temp_c_final = float(temp_c) + 32
#prints the final conversion
print(str(temp_c_final) + ' Fahrenheit')
