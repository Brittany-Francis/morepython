# Write your code below: 

def calculate_expenses(plane_ticket_price, car_rental_rate, hotel_rate, trip_time):
  car_rental_total=car_rental_rate * trip_time
  hotel_total=(hotel_rate * trip_time)-10
  trip_total=car_rental_total+hotel_total+ plane_ticket_price

  return trip_total

print(calculate_expenses(200, 100, 100, 5))


def trip_planner(first_destination, second_destination, final_destination="Codecademy HQ"):
  print("Here is what your trip will look like!")
  print("First, we will stop in " + first_destination + ", then " + second_destination + ", and lastly " + final_destination)

trip_planner("Brooklyn", "Queens")

tshirt_price = 9.75
shorts_price = 15.50
mug_price = 5.99
poster_price = 2.00

# Write your code below:
max_price=max(tshirt_price, shorts_price, mug_price, poster_price)

print(max_price)

min_price=min(tshirt_price, shorts_price, mug_price, poster_price)

print(min_price)

rounded_price=round(tshirt_price, 1)

print(rounded_price)

current_budget = 3500.75

def print_remaining_budget(budget):
  print("Your remaining budget is: $" + str(budget))

print_remaining_budget(current_budget)

# Write your code below: 
def deduct_expense(budget, expense):
 return budget-expense

shirt_expense=9
new_budget_after_shirt=deduct_expense(current_budget, shirt_expense)

print_remaining_budget(new_budget_after_shirt)

#multiple returns

def top_tourist_locations_italy():
  first = "Rome"
  second = "Venice"
  third = "Florence"
  return first, second, third

most_popular1, most_popular2, most_popular3= top_tourist_locations_italy()

print(most_popular1)
print(most_popular2)
print(most_popular3)

#physics formulas in functions

train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1

def get_force(mass, acceleration):
  return mass*acceleration

train_force=get_force(train_mass, train_acceleration)  
print(train_force)

print("The GE train supplies " + str(train_force) + " Newtons of force.")


def get_energy(mass, c=3*10**8):
  return mass*c**2

bomb_energy=get_energy(bomb_mass)
print(bomb_energy)

print("A 1kg bomb supplies " + str(bomb_energy)+ " Joules.")

# Write your code below: 
def f_to_c(f_temp):
  c_temp=(f_temp-32)*5/9
  return c_temp

f100_in_celsius=f_to_c(100)
print(f100_in_celsius)

def c_to_f(c_temp):
  f_temp=c_temp*(9/5)+32
  return f_temp

c0_in_fahrenheit=c_to_f(0)
print(c0_in_fahrenheit)

def get_work(mass, acceleration, distance):
  force=get_force(mass, acceleration)* distance
  return force

train_work=get_work(train_mass, train_acceleration, train_distance)

print(train_work)
print("The GE train does " + str(train_work) + " Joules of work over " +str(train_distance)+ " meters.")