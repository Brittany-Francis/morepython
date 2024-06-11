#what dictionaries look like

sensors =  {"living room": 21, "kitchen": 23, "bedroom": 20, "pantry": 22}
num_cameras = {"backyard": 6,  "garage": 2, "driveway": 1}

print(sensors)
translations={
"mountain": "orod", 
"bread": "bass",
"friend": "mellon",
"horse": "roch"
}

children = {"von Trapp":["Johannes", "Rosmarie", "Eleonore"] ,"Corleone": ["Sonny", "Fredo", "Michael"] }

#keys cannot be lists b/c they are mutable
#to add a key value pair

#dictionary[key] = value

animals_in_zoo={}
animals_in_zoo["zebras"]=8
animals_in_zoo["monkeys"]=12
animals_in_zoo["dinosaurs"]=0
print(animals_in_zoo)

user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}

#use.update() to add multiple things to dictionary at once

user_ids.update({"theLooper":138475, "stringQueen":85739})

print(user_ids)

#overwrite value of existing key
oscar_winners = {"Best Picture": "La La Land", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}

oscar_winners["Supporting Actress"]= "Viola Davis"

oscar_winners["Best Picture"]="Moonlight"

#can zip 2 lists into a dictionary
songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]

plays={key:value for key,value in zip(songs,playcounts)}

print(plays)

plays["Purple Haze"]=1
plays["Respect"]=94

library={"The Best Songs": plays, "Sunday Feelings": {}}
print(library)

#find values at a certain key
zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]}

print(zodiac_elements["earth"])
print(zodiac_elements["fire"])

# unsustainable way to check for key
zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]}


zodiac_elements["energy"]="Not a Zodiac element"

if "energy" in zodiac_elements:
  print(zodiac_elements["energy"])

# better way to check for key, and also add a default value if its not there
user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}

tc_id=user_ids.get("teraCoder", 100000)
print(tc_id)
stack_id=user_ids.get("superStackSmash", 100000)
print(stack_id)

#remove item from dictionary and give default value
available_items = {"health potion": 10, "cake of the cure": 5, "green elixir": 20, "strength sandwich": 25, "stamina grains": 15, "power stew": 30}
health_points = 20

health_points+=available_items.pop("stamina grains", 0)

health_points+=available_items.pop("power stew", 0)
health_points+=available_items.pop("mystic bread", 0)

print(available_items)
print(health_points)

#.keys() and .values() grabs all the keys or values from a dictionary and you can assign them to a variable
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}

total_exercises=0

for ex in num_exercises.values():
  total_exercises+= ex

print(total_exercises)
#grab and loop through both keys and values in a dictionary
pct_women_in_occupation = {"CEO": 28, "Engineering Manager": 9, "Pharmacist": 58, "Physician": 40, "Lawyer": 37, "Aerospace Engineer": 9}

for job, num in pct_women_in_occupation.items():
  print("Women make up "+ str(num) + " percent of " + job)

  tarot = { 1:	"The Magician", 2:	"The High Priestess", 3:	"The Empress", 4:	"The Emperor", 5:	"The Hierophant", 6:	"The Lovers", 7:	"The Chariot", 8:	"Strength", 9:	"The Hermit", 10:	"Wheel of Fortune", 11:	"Justice", 12:	"The Hanged Man", 13:	"Death", 14:	"Temperance", 15:	"The Devil", 16:	"The Tower", 17:	"The Star", 18:	"The Moon", 19:	"The Sun", 20:	"Judgement", 21:	"The World", 22: "The Fool"}

spread={}
spread["past"]=tarot.pop(13)
spread["present"]=tarot.pop(22)
spread["future"]=tarot.pop(10)

for time, card in spread.items():
  print("Your "+ time + " is the "+ str(card) +" card.")


