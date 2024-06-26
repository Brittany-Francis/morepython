print(type(5))

my_dict={}

print(type(my_dict))

my_list=[]

print(type(my_list))

class Facade:
  pass

facade_1=Facade()

class Rules:
  def washing_brushes(self):
    return "Point bristles towards the basin while washing your brushes."

class Circle:
  def __init__(self, diameter):
    print("New circle with diameter: " +  str(diameter))
  pi = 3.14
  
  # Add constructor here:
teaching_table=Circle(36)

class Circle:
  pi = 3.14
  def __init__(self, diameter):
    print("Creating circle with diameter {d}".format(d=diameter))
    # Add assignment for self.radius here:
    self.radius = diameter/2
  def circumference(self):
    circumference = 2 * self.pi * self.radius
    return circumference

medium_pizza=Circle(12)

teaching_table=Circle(36)

round_room=Circle(11460)

print(medium_pizza.circumference())
print(teaching_table.circumference())
print(round_room.circumference())

class Circle:
  pi = 3.14
  
  def __init__(self, diameter):
    self.radius = diameter / 2
  
  def area(self):
    return self.pi * self.radius ** 2
  
  def circumference(self):
    return self.pi * 2 * self.radius
  def __repr__(self):
    return "Circle with radius "+ str(self.radius)
  
  
medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

print(medium_pizza)
print(teaching_table)
print(round_room)

class Student:
  def __init__(self, name, year):
    self.name=name
    self.year=year
    self.grades=[]
  def add_grade(self, grade):
    if type(grade) is Grade:
      self.grades.append(grade)
  def get_average(self):
    if len(self.grades)==0:
      return "No grades yet"
    elif len(self.grades)==1:
      return self.grades[0].score
    else:
      count=0
      for grade in self.grades:
        count += grade.score
        print(count)
        print(len(self.grades))
      return count/len(self.grades)


roger=Student("Roger van der Weyden", 10)
sandro=Student("Sandro Botticelli", 12)
pieter=Student("Pieter Bruegel the Elder", 8)

class Grade:
  minimum_passing=65
  def __init__(self, score):
    self.score=score
  def is_passing(self):
    if self.score >= self.minimum_passing:
      return "You are passing"
    else:
      return "Not passing"
grade_1= Grade(100)
grade_2= Grade(75)
grade_3= Grade(80)
pieter.add_grade(grade_1)
pieter.add_grade(grade_2)
pieter.add_grade(grade_3)
print(grade_1.is_passing())

print(pieter.get_average())
