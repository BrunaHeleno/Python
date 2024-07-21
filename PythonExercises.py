#Exercises from "Python for Evrybody by Dr. Charles R. Severance"
#Solved by Bruna Heleno
from decimal import *;

### Chapter 2 ### 
#Program to get user name and print
inputName = input("What's your name?");
print("Hello " + inputName.title()); #capitalize first letter of each word

#Program that asks for hour and rate to compute gross pay
inputHours = input("Enter Hours:");
inputRate = input("Enter Rate:");
pay = Decimal(inputHours) * Decimal(inputRate); #casting string to decimal
pay = pay.quantize(Decimal('0.00'), rounding=ROUND_HALF_UP); #2 decimals, round up, ex 0.456 is gonna be 0.46
print("Pay: " + str(pay));

#Program to get Celsius and convert to Fahrenheit
inputCelsius = input("Celsius Degree:");
fahrenheit = float(inputCelsius) * 1.8 + 32;
print(fahrenheit);