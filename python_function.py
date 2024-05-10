#tenth power
def tenth_power(num):
  return num**10

print(tenth_power(1))
# 1 to the 10th power is 1
print(tenth_power(0))
# 0 to the 10th power is 0
print(tenth_power(2))
# 2 to the 10th power is 1024

#square root
def square_root(num):
  return num**.5
# Uncomment these function calls to test your square_root function:
print(square_root(16))
# should print 4
print(square_root(100))
# should print 10

#win rate
def win_percentage(wins, losses):
  total=wins+losses
  win_rate=wins/total
  return win_rate*100
# Uncomment these function calls to test your win_percentage function:
print(win_percentage(5, 5))
# should print 50
print(win_percentage(10, 0))
# should print 100

#avg
def average(num1, num2):
  avg=(num1+num2)/2
  return avg
print(average(1, 100))
# The average of 1 and 100 is 50.5
print(average(1, -1))
# The average of 1 and -1 is 0

#remainder
def remainder(num1, num2):
  return(num1*2)%(num2/2)

  
# Uncomment these function calls to test your remainder function:
print(remainder(15, 14))
# should print 2
print(remainder(9, 6))
# should print 0

def first_three_multiples(num):
  print(num*1)
  print(num*2)
  print(num*3)
  return num*3

# Uncomment these function calls to test your first_three_multiples function:
first_three_multiples(10)
# should print 10, 20, 30, and return 30
first_three_multiples(0)
# should print 0, 0, 0, and return 0

#tip
def tip(total, percentage):
  return total*percentage/100
# Uncomment these function calls to test your tip function:
print(tip(10, 25))
# should print 2.5
print(tip(0, 100))
# should print 0.0

#name
def introduction(first_name, last_name):
  bond_intro= last_name + ", " + first_name + " " + last_name
  return bond_intro
# Uncomment these function calls to test your introduction function:
print(introduction("James", "Bond"))
# should print Bond, James Bond
print(introduction("Maya", "Angelou"))
# should print Angelou, Maya Angelou

#age in dog years
def dog_years(name, age):
  new_age=age*7
  age_sentence= name +" you are " + str(new_age) + " years old in dog years"
  return age_sentence
# Uncomment these function calls to test your dog_years function:
print(dog_years("Lola", 16))
# should print "Lola, you are 112 years old in dog years"
print(dog_years("Baby", 0))
# should print "Baby, you are 0 years old in dog years"

#math
def lots_of_math(a, b, c, d):
  print(a+b)
  num1=a+b
  print(c-d)
  num2=c-d
  print(num1*num2)
  num3=num1*num2
  return num3%a
# Uncomment these function calls to test your lots_of_math function:
print(lots_of_math(1, 2, 3, 4))
# should print 3, -1, -3, 0
print(lots_of_math(1, 1, 1, 1))
# should print 2, 0, 0, 0