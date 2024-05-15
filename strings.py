def username_generator(first_name, last_name):
  if len(first_name)>=3 and len(last_name)>=4:
    user_name=first_name[0:3] + last_name[0:4]
  elif len(first_name)<3:
    user_name=first_name+ last_name[0:4]
  elif len(last_name)<4:
    user_name=first_name[0:3]+ last_name
  else:
    user_name= first_name+last_name
  return user_name

def password_generator(user_name):
  password=""
  for idx in range(0, len(user_name)):
    password+=user_name[idx-1]
    print(password)
  return password


password_generator("Brittany")

# def password_generator(user_name):
#   password=""
#   last=user_name[-1]
#   first=user_name[:-1]
#   print(last)
#   print(first)
#   return last+first