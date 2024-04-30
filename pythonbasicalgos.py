#Budget
# Monthly budget
budget = 2000

# Monthly expenses
food_bill = 200
electricity_bill = 100
internet_bill = 60
rent = 1500

# Calculate the total amount of expenses
total=food_bill+electricity_bill+internet_bill+rent


# Check if the total is greater than the budget and store the result in over_budget
if total>budget:
  over_budget=True
else: 
  over_budget=False

# Uncomment the below lines to see the results

print("Total: " + str(total))
print("Is it over budget? " + str(over_budget))


# Exponents
# Write your large_power function here:
def large_power(base, exponent):
  if base**exponent>5000:
    return True
  else: 
    return False

# Uncomment these function calls to test your large_power function:
print(large_power(2, 13))
# should print True
print(large_power(2, 12))
# should print False

# Twice as large
# Write your twice_as_large function here:
def twice_as_large(num1, num2):
  if num1>num2*2:
    return True
  else:
    return False

# Uncomment these function calls to test your twice_as_large function:
print(twice_as_large(10, 5))
# should print False
print(twice_as_large(11, 5))
# should print True

#Divisible by ten
# Write your divisible_by_ten() function here:
def divisible_by_ten(num):
  if num%10==0:
    return True
  else:
    return False



# Uncomment these print() function calls to test your divisible_by_ten() function:

print(divisible_by_ten(20))
# should print True
print(divisible_by_ten(25))
# should print False

#In range
def in_range(num, lower, upper):
  if num>=lower and num<=upper:
    return True
  else:
    return False
# Uncomment these function calls to test your in_range function:
print(in_range(10, 10, 10))
# should print True
print(in_range(5, 10, 20))
# should print False

#same name
def same_name(your_name, my_name):
  if your_name==my_name:
    return True
  else:
    return False
# Uncomment these function calls to test your same_name function:
print(same_name("Colby", "Colby"))
# should print True
print(same_name("Tina", "Amber"))
# should print False

#Always false
def always_false(num):
  if num>0:
    return False
  elif num==0:
    return False
  else:
    return False
# Uncomment these function calls to test your always_false function:
print(always_false(0))
# should print False
print(always_false(-1))
# should print False
print(always_false(1))
# should print False

#movie review
# Write your movie_review function here:
def movie_review(rating):
  if rating<=5:
    return "Avoid at all costs!"
  elif rating>5 and rating <9:
    return "This one was fun."
  else:
    return "Outstanding!"
# Uncomment these function calls to test your movie_review function:
print(movie_review(9))
# should print "Outstanding!"
print(movie_review(4))
# should print "Avoid at all costs!"
print(movie_review(6))
# should print "This one was fun."

#max number
def max_num(num1, num2, num3):
  if num1>num2 and num1>num3:
    return num1
  elif num2>num1 and num2>num3:
    return num2
  elif num3>num1 and num3>num2:
    return num3
  elif num1>num2 and num1==num3:
    return "It's a tie!"
  elif num2>num1 and num2==num3:
    return "It's a tie!"
  elif num1>num3 and num1==num2:
    return "It's a tie!"
  elif num2>num3 and num2==num1:
    return "It's a tie!"
  
# Uncomment these function calls to test your max_num function:
print(max_num(-10, 0, 10))
# should print 10
print(max_num(-10, 5, -30))
# should print 5
print(max_num(-5, -10, -10))
# should print -5
print(max_num(2, 3, 3))
# should print "It's a tie!"


#Append size
def append_size(my_list):
  x=len(my_list)
  my_list.append(x)
  return my_list


print(append_size([23, 42, 108]))

#Append Sum

def append_sum(my_list):
  for num in range(0, 3):
    x=my_list[-1]
    y=my_list[-2]
    last=x+y
    my_list.append(last)
    print(my_list)
  return my_list


print(append_sum([1, 1, 2]))

#largerlist
def larger_list(my_list1,my_list2):
  if len(my_list1)>=len(my_list2):
    return my_list1[-1]
  else:
    return my_list2[-1]

print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10]))

#more than n
def more_than_n(my_list, item, n):
  x=my_list.count(item)
  if x>n:
    return True
  else:
    return False

print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3))

#larger list
def combine_sort(my_list1, my_list2):
  new_list=my_list1+my_list2
  new_list.sort()
  return new_list

print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))

#every three numbers
def every_three_nums(start):
  listy=[]
  for num in range(start, 101, 3):
    listy.append(num)
  return listy

print(every_three_nums(91))

#remove middle
def remove_middle(my_list, start, end):
  new_list=my_list[0:start]+my_list[end+1:]
  return new_list


print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))

#return larger count
def more_frequent_item(my_list, item1, item2):
  item1_count=my_list.count(item1)
  item2_count=my_list.count(item2)
  if item1_count>=item2_count:
    return item1
  else:
    return item2

print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))

#double index
def double_index(my_list, index):
  if index>len(my_list)-1:
    return my_list
  else:
    my_list[index]=my_list[index]*2
    return my_list


print(double_index([3, 8, -10, 12], 2))

#middle
#Write your function here
import math

def middle_element(my_list):
  if len(my_list)%2==0:
    num1=my_list[int(len(my_list)/2)]
    num2=my_list[int(len(my_list)/2)-1]
    return (num1+num2)/2
  else:
    middle=my_list[int(len(my_list)/2)]
    return middle


print(middle_element([5, 2, -10, -4, 4, 5]))