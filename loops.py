promise = "I will finish the python loops module!"

for num in range(5):
  print(promise)

# While Loop Walkthrough
count = 0
print("Starting While Loop")
while count <= 3:
  # Loop Body
  # Print if the condition is still true
  print("Loop Iteration - count <= 3 is still true")
  # Print the current value of count 
  print("Count is currently " + str(count))
  # Increment count
  count += 1
  print(" ----- ")
print("While Loop ended")


countdown=10
while countdown>=0:
  print(countdown)
  countdown-=1

print("We have Liftoff!")

python_topics = ["variables", "control flow", "loops", "modules", "classes"]

#Your code below: 
length=len(python_topics)
index=0

while index<length:
  print("I am learning about " + python_topics[index])
  index+=1

students_period_A = ["Alex", "Briana", "Cheri", "Daniele"]
students_period_B = ["Dora", "Minerva", "Alexa", "Obie"]

for student in students_period_A:
  students_period_B.append(student)
  print(student)

print(students_period_B)

#break
dog_breeds_available_for_adoption = ["french_bulldog", "dalmatian", "shihtzu", "poodle", "collie"]
dog_breed_I_want = "dalmatian"

for dog_breed in dog_breeds_available_for_adoption:
  print(dog_breed)
  if dog_breed == dog_breed_I_want:
    print("They have the dog I want!")
    break
  
#continue
ages = [12, 38, 34, 26, 21, 19, 67, 41, 17]

for age in ages:
  if age<21:
    continue
  else:
    print(age)

#nested loops
sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]

scoops_sold=0

for location in sales_data:
  for num in location:
    scoops_sold+=num

print(scoops_sold)
#list comprehension
# Your code below:
single_digits=range(0, 10)
for num in single_digits:
  print(num)

squares=[]
for num in single_digits:
  squares.append(num**2)

print(squares)
cubes=[num**3 for num in single_digits]
print(cubes)