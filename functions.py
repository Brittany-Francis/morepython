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