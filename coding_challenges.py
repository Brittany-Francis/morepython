letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
# Write your unique_english_letters function here:
def unique_english_letters(word):
  count=0
  unique_letters=[]
  for let in word:
    if let not in unique_letters:
        unique_letters.append(let)
        count+=1
  return count


# Uncomment these function calls to test your function:
print(unique_english_letters("mississippi"))
# should print 4
print(unique_english_letters("Apple"))
# should print 4

# Write your count_char_x function here:
def count_char_x(word, x):
  count=0
  for let in word:
    if let==x:
      count+=1
  return count
# Uncomment these function calls to test your tip function:
print(count_char_x("mississippi", "s"))
# should print 4
print(count_char_x("mississippi", "m"))
# should print 1

# Write your count_multi_char_x function here:
def count_multi_char_x(word, x):
  count=0
  count=word.count(x)
  return count

# Uncomment these function calls to test your function:
print(count_multi_char_x("mississippi", "iss"))
# should print 2
print(count_multi_char_x("apple", "pp"))
# should print 1

# Write your x_length_words function here:
def x_length_words(sentence, x):
  new_list=sentence.split(" ")
  print(new_list)
  for word in new_list:
    if not len(word)  >=x:
      return False
    else: 
      return True

# Uncomment these function calls to test your tip function:
print(x_length_words("i like apples", 2))
# should print False
print(x_length_words("he likes apples", 2))
# should print True

# Write your check_for_name function here:
def check_for_name(sentence, name):
  new_sent=sentence.upper()
  print(new_sent)
  new_name=name.upper()
  print(new_name)
  if new_name in new_sent:
    return True
  else:
    return False
# Uncomment these function calls to test your  function:
print(check_for_name("My name is Jamie", "Jamie"))
# should print True
print(check_for_name("My name is jamie", "Jamie"))
# should print True
print(check_for_name("My name is Samantha", "Jamie"))
# should print False

# Write your every_other_letter function here:
def every_other_letter(word):
  new_string=""
  for idx in range(len(word)):
    if idx%2==0:
      new_string+=word[idx]
      #print(word[idx])
      #print(new_string)
    else: 
      continue
  return new_string
# Uncomment these function calls to test your function:
print(every_other_letter("Codecademy"))
# should print Cdcdm
print(every_other_letter("Hello world!"))
# should print Hlowrd
print(every_other_letter(""))
# should print 

# Write your reverse_string function here:
def reverse_string(word):
  new_word=""
  for idx in range(len(word)-1, -1, -1):
    print(word[idx])
    new_word+=word[idx]
  return new_word
# Uncomment these function calls to test your  function:
print(reverse_string("Codecademy"))
# should print ymedacedoC
print(reverse_string("Hello world!"))
# should print !dlrow olleH
print(reverse_string(""))
# should print

# Write your make_spoonerism function here:
def make_spoonerism(word1, word2):
  first_word_letter_one=word1[0]
  second_word_letter_one=word2[0]
  rest_of_word_one=word1[1:]
  rest_of_word_two=word2[1:]
  new_word1=first_word_letter_one+rest_of_word_two
  new_word2=second_word_letter_one+rest_of_word_one
  new_phrase= new_word2 + " " + new_word1
  return new_phrase
# Uncomment these function calls to test your function:
print(make_spoonerism("Codecademy", "Learn"))
# should print Lodecademy Cearn
print(make_spoonerism("Hello", "world!"))
# should print wello Horld!
print(make_spoonerism("a", "b"))
# should print b a

# Write your add_exclamation function here:
def add_exclamation(word):
  if len(word)>=20:
    return word
  else:
    while len(word)<20:
      word+="!"
    return word
# Uncomment these function calls to test your function:
print(add_exclamation("Codecademy"))
# should print Codecademy!!!!!!!!!!
print(add_exclamation("Codecademy is the best place to learn"))
# should print Codecademy is the best place to learn

# Write your sum_values function here:
def sum_values(my_dictionary):
  sum=0
  for val in my_dictionary.values():
    sum+=val
  return sum

# Uncomment these function calls to test your sum_values function:
print(sum_values({"milk":5, "eggs":2, "flour": 3}))
# should print 10
print(sum_values({10:1, 100:2, 1000:3}))
# should print 6

# Write your sum_even_keys function here:
def sum_even_keys(my_dictionary):
  sum=0
  for key in my_dictionary.keys():
    
    if key%2==0:
     sum+=my_dictionary[key]
  return sum
# Uncomment these function calls to test your  function:
print(sum_even_keys({1:5, 2:2, 3:3}))
# should print 2
print(sum_even_keys({10:1, 100:2, 1000:3}))
# should print 6


# Write your add_ten function here:
def add_ten(my_dictionary):
  for key in my_dictionary.keys():
   value= my_dictionary[key]
   value+=10
   my_dictionary[key]=value
  return my_dictionary
# Uncomment these function calls to test your  function:
print(add_ten({1:5, 2:2, 3:3}))
# should print {1:15, 2:12, 3:13}
print(add_ten({10:1, 100:2, 1000:3}))
# should print {10:11, 100:12, 1000:13}

# Write your values_that_are_keys function here:
def values_that_are_keys(my_dictionary):
  my_list=[]
  key_and_value=[]
  for key in my_dictionary.keys():
    my_list.append(key)
  print(my_list)
  for value in my_dictionary.values():
    if value in my_list:
      key_and_value.append(value)

  return key_and_value
# Uncomment these function calls to test your  function:
print(values_that_are_keys({1:100, 2:1, 3:4, 4:10}))
# should print [1, 4]
print(values_that_are_keys({"a":"apple", "b":"a", "c":100}))
# should print ["a"]


# Write your word_length_dictionary function here:
def word_length_dictionary(words):
  my_dictionary={}
  for word in words:
    my_dictionary[word]=len(word)
  return my_dictionary

# Uncomment these function calls to test your  function:
print(word_length_dictionary(["apple", "dog", "cat"]))
# should print {"apple":5, "dog": 3, "cat":3}
print(word_length_dictionary(["a", ""]))
# should print {"a": 1, "": 0}

# Write your frequency_dictionary function here:
def frequency_dictionary(words):
  my_dictionary={}
  for word in words:
    if not word in my_dictionary:
      num=words.count(word) 
      my_dictionary[word]=num
  return my_dictionary
# Uncomment these function calls to test your  function:
print(frequency_dictionary(["apple", "apple", "cat", 1]))
# should print {"apple":2, "cat":1, 1:1}
print(frequency_dictionary([0,0,0,0,0]))
# should print {0:5}


# Write your unique_values function here:
def unique_values(my_dictionary):
  
  listy=[]
  for val in my_dictionary.values():
    if not val in listy:
      listy.append(val)
  return len(listy)
# Uncomment these function calls to test your  function:
print(unique_values({0:3, 1:1, 4:1, 5:3}))
# should print 2
print(unique_values({0:3, 1:3, 4:3, 5:3}))
# should print 1

# Write your count_first_letter function here:
def count_first_letter(names):
  new_dict={}
  for key in names.keys():
    first_let=key[0]
    print(first_let)
    if not first_let in new_dict:
      count=0
      for name in names[key]:
        count+=1
        print("The count is " + str(count))
        new_dict[first_let]=count
    else:
      count=new_dict[first_let]
      print("This is the count " + str(count))
      for name in names[key]:
        count+=1
        print("The count is " + str(count))
        new_dict[first_let]=count
  return new_dict

  #     count=0
  #     for name in names:
  #       count+=1
  #       new_dict[key]=count
  #   else:
  #     count=new_dict[key]
  #     for name in names:
  #       count+=1
  #       new_dict[key]=count
  # return new_dict

# Uncomment these function calls to test your  function:
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 4, "L": 3}
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Sannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 7}

# Define the DriveBot class here!
class DriveBot:
  motor_speed=0
  sensor_range=0
  direction=0
  # def __init__(self, motor_speed, sensor_range, direction):
  #   self.motor_speed=motor_speed
  #   self.sensor_range=sensor_range
  #   self.direction=direction
robot_1=DriveBot()
robot_1.motor_speed=5
robot_1.direction=90
robot_1.sensor_range=10
print(robot_1.motor_speed)
print(robot_1.direction)
print(robot_1.sensor_range)



class DriveBot:
    # Update this constructor!
    def __init__(self, motor_speed=0, direction=180, sensor_range=10):
        self.motor_speed = motor_speed
        self.direction = direction
        self.sensor_range = sensor_range
    
    def control_bot(self, new_speed, new_direction):
        self.motor_speed = new_speed
        self.direction = new_direction

    def adjust_sensor(self, new_sensor_range):
        self.sensor_range = new_sensor_range

robot_1 = DriveBot()
robot_1.motor_speed = 5
robot_1.direction = 90
robot_1.sensor_range = 10

# Create robot_2 here!
robot_2=DriveBot(35,75,25)
print(robot_2.motor_speed)
print(robot_2.direction)
print(robot_2.sensor_range)

class DriveBot:
  # Create the class variables!
  all_disabled=False
  latitude=-999999
  longitude=-999999
  def __init__(self, motor_speed = 0, direction = 180, sensor_range = 10):
    self.motor_speed = motor_speed
    self.direction = direction
    self.sensor_range = sensor_range
    
    def control_bot(self, new_speed, new_direction):
        self.motor_speed = new_speed
        self.direction = new_direction

    def adjust_sensor(self, new_sensor_range):
        self.sensor_range = new_sensor_range

robot_1 = DriveBot()
robot_1.motor_speed = 5
robot_1.direction = 90
robot_1.sensor_range = 10

robot_2 = DriveBot(35, 75, 25)
robot_3 = DriveBot(20, 60, 10)

# Change the latitude, longitude, and all_disabled values for all three robots using only three lines of code!
DriveBot.latitude=-50
DriveBot.longitude=50
DriveBot.all_disabled=True

print(robot_1.latitude)
print(robot_2.longitude)
print(robot_3.all_disabled)

class DriveBot:
  # Create a counter to keep track of how many robots were created
    all_disabled = False
    latitude = -999999
    longitude = -999999
    robot_count=0

    def __init__(self, motor_speed = 0, direction = 180, sensor_range = 10):
        self.motor_speed = motor_speed
        self.direction = direction
        self.sensor_range = sensor_range
        DriveBot.robot_count += 1
        self.id=DriveBot.robot_count
        # Assign an `id` to the robot when it is constructed by incrementing the counter and assigning the value to `id`
    
    def control_bot(self, new_speed, new_direction):
        self.motor_speed = new_speed
        self.direction = new_direction

    def adjust_sensor(self, new_sensor_range):
        self.sensor_range = new_sensor_range

robot_1 = DriveBot()
robot_1.motor_speed = 5
robot_1.direction = 90
robot_1.sensor_range = 10

robot_2 = DriveBot(35, 75, 25)
robot_3 = DriveBot(20, 60, 10)

print(robot_1.id)
print(robot_2.id)
print(robot_3.id)

