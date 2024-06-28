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