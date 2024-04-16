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