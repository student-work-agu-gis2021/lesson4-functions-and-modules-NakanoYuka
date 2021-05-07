def fahr_to_celsius(temp_fahrenheit):
 """
 Purpose: converts the input temperature from degrees Fahrenheit to degrees Celsius. 
 Parameters: temp_fahrenheit.
 returned values : converted_temp.
 """
 converted_temp = (temp_fahrenheit-32)/1.8
 return converted_temp

def temp_classifier(temp_celsius):
  """
  purpose: reclassified into integer numbers 0-3.
  parameter: temp_celsius
  returned values: 0 to 3
  """
  if temp_celsius<-2:
    return 0
  elif (temp_celsius>=-2)and(temp_celsius<2):
    return 1
  elif (temp_celsius>=2)and(temp_celsius<15):
    return 2
  elif temp_celsius>=15:
    return 3

    """
    Purpose: To take advantage of your new functions and sort a dataset of temperatures in Fahrenheit into four different classes.
    parameters: temp_fahrenheit and temp_celsius
    returned values: converted_temp and 0 to 3
    """