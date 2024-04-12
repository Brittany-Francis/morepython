#lists

my_empty_list =[]

ints_and_strings = [1, 2, 3, "four", "five", "cats"]

sam_height_and_testscore =["Sam", 67, 85.5, True]
heights = [61, 70, 67, 64]

broken_heights = [65, 71, 59, 62]
heights = [61, 70,67, 64, 65]

example_list = [1, 2, 3, 4]

#Using Append
example_list.append(5)
# print(example_list)

#Using Remove
example_list.remove(5)
# print(example_list)

orders = ["daisies", "periwinkle"]
print(orders)
orders.append('tulips')
orders.append('roses')
print(orders)

orders = ["daisy", "buttercup", "snapdragon", "gardenia", "lily"]

# Create new orders here:

new_orders=  ["lilac", "iris"]
orders_combined = orders + new_orders

broken_prices = [5, 3, 4, 5, 4] + [4]

employees = ["Michael", "Dwight", "Jim", "Pam", "Ryan", "Andy", "Robert"]

print(employees[3])
employee_four= employees[3]
print(employees[1])

shopping_list = ["eggs", "butter", "milk", "cucumbers", "juice", "cereal"]

last_element= shopping_list[-1]
index5_element=shopping_list[5]
print(last_element)
print(index5_element)

# Your code below:
garden_waitlist=["Jiho", "Adam", "Sonny", "Alisha"]

garden_waitlist[1]="Calla"
print(garden_waitlist)

garden_waitlist[-1]="Alex"
print(garden_waitlist)

# Your code below: 
order_list=["Celery", "Orange Juice", "Orange", "Flatbread"]
print(order_list)
order_list.remove("Flatbread")
print(order_list)
new_store_order_list=["Orange", "Apple", "Mango", "Broccoli", "Mango"]
print(new_store_order_list)
new_store_order_list.remove("Mango")
print(new_store_order_list)

#2D lists
heights = [["Jenny", 61], ["Alexus", 70], ["Sam", 67], ["Grace", 64]]
heights.append(["Vik", 68])

ages=[["Aaron", 15], ["Dhruti", 16]]

#Your code below:
class_name_test=[["Jenny", 90], ["Alexus", 85.5], ["Sam", 83], ["Ellie", 101.5]]

print(class_name_test)
sams_score=class_name_test[2][1]
print(sams_score)
ellies_score=class_name_test[-1][-1]
print(ellies_score)

#Your code below:
incoming_class=[["Kenny", "American", 9], ["Tanya", "Ukrainian", 9], ["Madison", "Indian", 7]]
print (incoming_class)

incoming_class[2][2]=8
print(incoming_class)

incoming_class[-3][-3]="Ken"
print(incoming_class)

# Your code below: 
first_names= ["Ainsley", "Ben", "Chani", "Depak"]

preferred_size= ["Small", "Large", "Medium"]

preferred_size.append("Medium")
print(preferred_size)

customer_data=[["Ainsley", "Small", True], ["Ben", "Large", False], ["Chani", "Medium", True], ["Depak", 
"Medium", False]]

print(customer_data)
customer_data[2][2]=False

customer_data[1].remove(False)
customer_data_final= customer_data +[["Amit", "Large", True], ["Karim", "X-Large", False]]

print(customer_data_final)