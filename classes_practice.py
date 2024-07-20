class School:
  def __init__(self, name, level, numberOfStudents):
    self.name=name
    self.level=level
    self.numberOfStudents=numberOfStudents

  def get_name(self):
    return self.name

  def get_level(self):
    return self.level

  def get_student_num(self):
    return self.numberOfStudents

  def set_num_students(self, newStudentNum):
    self.numberOfStudents=newStudentNum
    return self.numberOfStudents

  def __repr__(self):
    return f"{self.name} is a {self.level} school with {self.numberOfStudents} students."

class Primary(School):
  
  def __init__(self, name, numberOfStudents, pickupPolicy):
    super().__init__(name, "primary", numberOfStudents)
    self.pickupPolicy=pickupPolicy

  def get_pickup_policy(self):
    return self.pickupPolicy

  def __repr__(self):
    original=super().__repr__()
    return original + f" Our pick up policy is {self.pickupPolicy}"

class Middle(School):
  def __init__(self, name, numberOfStudents):
    super().__init__(name, "middle", numberOfStudents)

class High(School):
  def __init__(self, name, numberOfStudents, sportsTeams):
    super().__init__(name, "high", numberOfStudents)
    self.sportsTeams=sportsTeams
  
  def get_teams(self):
    return self.sportsTeams

  def __repr__(self):
    teams=""
    for team in self.sportsTeams:
      teams+= f"{team} " 
    return "Our sports teams are " + teams

newSchool1=School("Dickinson Ave", "Primary", 627)
print(newSchool1)
print(newSchool1.get_name())
print(newSchool1.get_student_num())
newSchool1.set_num_students(321)
print(newSchool1.get_student_num())

school2=Primary("Bellrose", 100, "Must be picked up at 3.")

print(school2)

school3=High("Northport", 500, ["baseball", "basketball", "soccer"])
print(school3)

school4=Middle("East Northport", 600)
print(school4)


