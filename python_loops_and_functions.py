#divisible by ten
def divisible_by_ten(nums):
  count=0
  for num in nums:
    if num%10==0:
      count+=1
    else:
      continue
  return count

print(divisible_by_ten([20, 25, 30, 35, 40]))

#greetings
def add_greetings(names):
  name_list=[]
  for name in names:
    name_greeting="Hello, " + name
    name_list.append(name_greeting)
  return name_list

print(add_greetings(["Owen", "Max", "Sophie"]))


#Delete Starting Even Numbers
def delete_starting_evens(my_list):
  while len(my_list)>0 and my_list[0]%2==0:
    my_list.pop(0)

  return my_list


print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))

#odd indices
def odd_indices(my_list):
  new_list = []
  for index in range(1, len(my_list), 2):
    new_list.append(my_list[index])
  return new_list

#exponents
def exponents(bases, powers):
  new_list=[]
  for base in bases:
    for power in powers:
      new_list.append(base**power)

  return new_list
print(exponents([2, 3, 4], [1, 2, 3]))