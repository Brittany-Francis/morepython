my_name= "Brittany"
print("Hello " + my_name)

# Define the release and runtime integer variables below:
release_year=1999
runtime=120


# Define the rating_out_of_10 float variable below: 
rating_out_of_10=2.5

print(25 * 68 + 13/28)

quilt_width=8
quilt_length=12

print(quilt_width * quilt_length)

quilt_length=8

print(quilt_width * quilt_length)

# Calculation of squares for:
# 6x6 quilt
print(6**2)
# 7x7 quilt
print(7**2)
# 8x8 quilt
print(8**2)
# How many squares for 6 people to have 6 quilts each that are 6x6?
print(6**2 *6 *6) 

order_263_r= 263%11
print(order_263_r)

order_263_coupon="no"

order_264_r=264%11
print(order_264_r)
order_264_coupon="yes"

string1 = "The wind, "
string2 = "which had hitherto carried us along with amazing rapidity, "
string3 = "sank at sunset to a light breeze; "
string4 = "the soft air just ruffled the water and "
string5 = "caused a pleasant motion among the trees as we approached the shore, "
string6 = "from which it wafted the most delightful scent of flowers and hay."

# Define message below:
message= string1+ string2+ string3+string4+string5+ string6


#print(message)
print(message)

total_price = 0

new_sneakers = 50.00

total_price += new_sneakers

nice_sweater = 39.00
fun_books = 20.00
# Update total_price here:
total_price+= nice_sweater
total_price+=fun_books

print("The total price is", total_price)

# Assign the string here
to_you= """Stranger, if you passing meet me and desire to speak to me, why
  should you not speak to me?
And why should I not speak to you? """



print(to_you)

#Brittany Francis
#initials in code

print("BBBB     FFFFF")
print("B   B    F    ")
print("B   B    F    ")
print("BBBB     FFF  ")
print("B   B    F    ")
print("B   B    F    ")
print("BBBB     F    ")

lovely_loveseat_description="Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white."

lovely_loveseat_price=254.00

stylish_settee_description="Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black."


stylish_settee_price=180.50

luxurious_lamp_description="Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade."

luxurious_lamp_price=52.15

sales_tax=.088

customer_one_total=0

customer_one_itemization=""

customer_one_itemization+=lovely_loveseat_description

customer_one_total+=lovely_loveseat_price
customer_one_total+=luxurious_lamp_price

customer_one_itemization+=luxurious_lamp_description

customer_one_tax=customer_one_total * sales_tax

customer_one_total+=customer_one_tax

print("Customer One Items")
print(customer_one_itemization)
print("customer 1 total:")
print(customer_one_total)

my_baby_bool = "true"
print(type(my_baby_bool))
my_baby_bool_two=True
print(type(my_baby_bool_two))

# Enter a user name here, make sure to make it a string
user_name = "angela_catlady_87"

if user_name == "Dave":
  print("Get off my computer Dave!")

if user_name=="angela_catlady_87":
  print("I know it is you, Dave! Go away!")

  x = 20
y = 20

# Write the first if statement here:
if x==y:
  print("These numbers are the same")


credits = 120

# Write the second if statement here:
if credits>=120:
  print("You have enough credits to graduate!")

  statement_one = (2 + 2 + 2 >= 6) and (-1 * -1 < 0)

statement_two = (4 * 2 <= 8) and (7 - 1 == 6)

credits = 120
gpa = 3.4

if (credits >= 120) and (gpa>=2.0):
  print("You meet the requirements to graduate!")

  credits = 118
gpa = 2.0
if credits>=120 or gpa>=2.0:
  print("You have met at least one of the requirements.")

  credits = 120
gpa = 1.8

if not credits >=120:
  print("You do not have enough credits to graduate.")

if not gpa>=2.0:
  print("Your GPA is not high enough to graduate.")

if not credits >=120 and not gpa >=2.0:
  print("You do not meet either requirement to graduate!")


credits = 120
gpa = 1.9

if (credits >= 120) and (gpa >= 2.0):
  print("You meet the requirements to graduate!")
else:
  print("You do not meet the requirements to graduate.")

grade = 86

if grade>=90:
  print("A")
elif grade>=80:
  print("B")
elif grade>=70:
  print("C")
elif grade>=60:
  print("D")
else:
  print("F")

weight=41.5
cost=0
premium_shipping_cost=125
#ground shipping
if weight<=2:
  cost=weight*1.5+20
  print(cost)
elif weight>2 and weight <=6:
  cost=weight*3+20
  print(cost)
elif weight>6 and weight<=10:
  cost=weight*4+20
  print(cost)
elif weight>10:
  cost=weight*4.75+20
  print(cost)

print("Premium shipping cost= $" + str(premium_shipping_cost))

#Drone Shipping
if weight<=2:
  cost=weight*4.5
  print(cost)
elif weight>2 and weight <=6:
  cost-weight*9
  print(cost)
elif weight>6 and weight<=10:
  cost=weight*12
  print(cost)
elif weight>10:
  cost=weight*14.25
  print(cost)

# Fortune Cookie Program 🥠

import random

fortune = random.randint(0, 4)

if fortune == 0:
  print("May you one day be carbon neutral")
elif fortune == 1:  
  print("You have rice in your teeth")
elif fortune == 2:
  print("No snowflake feels responsible for an avalanche")
elif fortune == 3:
  print("You can only connect the dots looking backwards")
elif fortune == 4:
  print("The fortune you seek is in another cookie")

# Who Wants To Be A Millionaire 💰 

score = 0

option1 = 'Fresca'
option2 = 'V8'
option3= "Water"
option4 = 'A&W'
  
print("For ordering his favorite beverages on demand, LBJ had four buttons installed in the Oval Office labeled 'Coffee', 'Tea', 'Coke', and what?\n")

print("A.", option1)
print("B.", option2)
print("C.", option3)
print("D.", option4)
  
answer = 'a'

if answer == 'A' or answer == 'a': 
  score += 100
  print("\nCorrect!")
else:
  print("\nNope, sorry!")
# Area Calculator 📏

import math

base = 20
height = 30
area = base * height / 2

print("The triangle area is", area)

length = 2
width = 12
area = length * width

print("The rectangle area is" + str(area))
    
radius = 36
area = math.pi * radius * radius
    
print("The circle area is", area)