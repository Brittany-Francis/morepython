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

#larger sum
def larger_sum(lst1, lst2):
  sum1=0
  sum2=0
  for num in lst1:
    sum1+=num
  for num in lst2:
    sum2+=num
  if sum1>=sum2:
    return lst1
  else:
    return lst2


print(larger_sum([1, 9, 5], [2, 3, 7]))

#larger than 9000
def over_nine_thousand(lst):
  sum=0
  if len(lst)==0:
    return 0
  for num in lst:
    sum+=num
    if sum>9000:
      break
  return sum

print(over_nine_thousand([8000, 900, 120, 5000]))

#max num
def max_num(nums):
  largest=nums[0]
  for num in nums:
    if num>largest:
      largest=num
  return largest

print(max_num([50, -10, 0, 75, 20]))

#same_value
def same_values(lst1, lst2):
  same_value=[]
  for idx in range(len(lst1)):
    if lst1[idx]==lst2[idx]:
      same_value.append(idx)

  return same_value
    

print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))