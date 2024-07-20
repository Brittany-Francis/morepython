# OOP
class Employee():
  new_id = 1
  def __init__(self, name=None):
    self.id = Employee.new_id
    Employee.new_id += 1
    self._name=name

  def say_id(self):
    print("My id is {}.".format(self.id))

  def get_name(self):
    return self._name

  def set_name(self, new_name):
    self._name=new_name

  def del_name(self):
    del self._name

class Admin(Employee):
  def say_id(self):
    super().say_id()
    print("I am an admin.")


class Manager(Admin):
  def say_id(self):
    super().say_id()
    print("I am in charge")

e1=Employee()
a1=Admin()
m1=Manager()

meeting=[e1, a1, m1]

for e in meeting:
  e.say_id()

class Meeting:
  def __init__(self):
    self.attendees = []
  
  def __add__(self, employee):
    print("ID {} added.".format(employee.id))
    self.attendees.append(employee)
  def __len__(self):
    return len(self.attendees)

  # Write your code
  
    
#e1 = Employee()
e2 = Employee()
e3 = Employee()
m1 = Meeting()
m1+e1
m1+e2
m1+e3

print(len(m1))



e4 = Employee("Maisy")
e5 = Employee()
