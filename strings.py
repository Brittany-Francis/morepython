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