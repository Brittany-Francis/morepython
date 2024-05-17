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

poem_title = "spring storm"
poem_author = "William Carlos Williams"

poem_title_fixed=poem_title.title()
print(poem_title)
print(poem_title_fixed)

poem_author_fixed=poem_author.upper()
print(poem_author)
print(poem_author_fixed)

line_one = "The sky has given over"

line_one_words=line_one.split()

authors = "Audre Lorde,Gabriela Mistral,Jean Toomer,An Qi,Walt Whitman,Shel Silverstein,Carmen Boullosa,Kamala Suraiyya,Langston Hughes,Adrienne Rich,Nikki Giovanni"

author_names=authors.split(',')

print(author_names)
names_list=[]
for name in author_names:
  new_name=name.split(" ")
  names_list.append(new_name)

print(names_list)
author_last_names=[]
for name in names_list:
  author_last_names.append(name[1])

print(author_last_names)

reapers_line_one_words = ["Black", "reapers", "with", "the", "sound", "of", "steel", "on", "stones"]

reapers_line_one=" ".join(reapers_line_one_words)
love_maybe_lines = ['Always    ', '     in the middle of our bloodiest battles  ', 'you lay down your arms', '           like flowering mines    ','\n' ,'   to conquer me home.    ']

love_maybe_lines_stripped=[]
for line in love_maybe_lines:
  this_line=line.strip()
  love_maybe_lines_stripped.append(this_line)

love_maybe_full="\n".join(love_maybe_lines_stripped)
print(love_maybe_full)

def poem_title_card(title, poet):
  return 'The poem "{}" is written by {}.'.format(title, poet)

highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"

# print(highlighted_poems)

highlighted_poems_list = highlighted_poems.split(',')

# print(highlighted_poems_list)

highlighted_poems_stripped = []

for poem in highlighted_poems_list:
  highlighted_poems_stripped.append(poem.strip())
  
# print(highlighted_poems_stripped)

highlighted_poems_details = []

for poem in highlighted_poems_stripped:
  highlighted_poems_details.append(poem.split(':'))
  
titles = []
poets = []
dates = []

for poem in highlighted_poems_details:
  titles.append(poem[0])
  poets.append(poem[1])
  dates.append(poem[2])
  
for i in range(0,len(highlighted_poems_details)):
    print('The poem {} was published by {} in {}'.format(titles[i], poets[i], dates[i]))
