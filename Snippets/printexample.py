#string prints
print ("Hey, you!")

print ("Hello!")

print ('Hey ' + 'Ana! ')

ans = 13
solution = "The product is " + str(ans)
print (solution)

#variable prints
variable1 = "hi"
print (variable1)

#printing on same lines
a = "hello"
for i in a:
    print (i, end = " ")


print ('somthing')

#variable string shortcuts
name = "Ana"
age = "14"
color = "blue"
print ("Hello, my name is %s and I am %s years old, my favorite color is %s." % (name,age,color))

#arithmitics or math :) How much money is left in wallet?
money_in_wallet = 20
donut_price = 2.50
sales_tax = .08 * donut_price

donut_price += sales_tax
money_in_wallet -= donut_price
print(money_in_wallet)

#Integers: A whole number with no decimal point
int1 = 1
print (int1)

#Floats: A decimal or number
float1 = 1.0
float2 = -5.5
float3 = 0.35
print(float1 + float2 + float3)

#Scientific Notation: Use 'e' to indicate the power of 10
scientific_float = 1.5e2
print(scientific_float)

#cucumber shopping!
cucumbers = 100
price_per_cucumber = 3.25
total_cost = cucumbers * price_per_cucumber
print(total_cost)
#cucumber sharing!
cucumbers = 100
num_people = 6
whole_cucumbers_per_person = cucumbers / num_people
print(whole_cucumbers_per_person)
float_cucumbers_per_person = float(cucumbers)/num_people
print(float_cucumbers_per_person)

#math commands!
addition = 5 + 5
subtraction = 5 - 5
multiplication = 5 * 5
division = 25 / 5
rounded_quotient_division = 7/2
remainder_division = 12 % 5
to_make_a_float = 7./2
#division exact, to make a float
to_make_a_float2 = float(7)/2
#make the product a float.

#multiline stings, use triple quotes
address_string = """136 whoowhoo street
apt 867
WhooWhooville, WW, 44607"""
haiku = """The old pond,
A frog jumps in:
Plop!"""

# A variable with the value 7 is an integer, 7. is a float, "7" is a string. 
#converting:
age = 14
print("I am " + str(age) + " years old!")

number1 = "100"
number2 = "10"

string_addition = number1 + number2 
#string_addition now has a value of "10010"

int_addition = int(number1) + int(number2)
#int_addition has a value of 110

string_num = "7.5"

float_1 = 0.25
float_2 = 40.0

product = float_1 * float_2
big_string = "The product was " + str(product)

#What to review: 

#Print statements
#How to create, modify, and use variables
#Arithmetic operations like addition, subtraction, division, and multiplication
#How to use comments to make your code easy to understand
#Different data types, including strings, ints, floats, and booleans
#Converting between data types

#Review:

skill_completed = str('Python Syntax')

exercises_completed = 13
points_per_exercise = 5
point_total = 100
#The amount of points for each exercise may change, because points don't exist yet
point_total += exercises_completed * points_per_exercise
print('I got ' + str(point_total) + ' points!')
