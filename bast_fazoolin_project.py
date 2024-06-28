class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name=name
    self.items=items
    self.start_time=start_time
    self.end_time=end_time
  def __repr__(self):
    return "This is the " + self.name + " menu and is available from " + str(self.start_time) + " to " + str(self.end_time)
  def calculate_bill(self, purchased_items):
    total=0
    for item in purchased_items:
      total+=self.items[item]
    return total



brunch = Menu("Brunch", {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}, 11, 4)

early_bird = Menu("Early Bird", {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}, 3, 6)

dinner=Menu("Dinner", {
  'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}, 5, 11)

kids=Menu("Kids", {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}, 11, 9)

print(repr(brunch))
print(brunch)

print(brunch.calculate_bill(["pancakes", "home fries", "coffee"]))

print(early_bird.calculate_bill(["salumeria plate", "mushroom ravioli (vegan)"]))

class Franchise:
  def __init__(self, address, menus):
    self.address=address
    self.menus=menus
  def __repr__(self):
    return "The location of this restaurant is " + self.address
  def available_menus(self, time):
    what_menu=[]
    for menu in menus:
      if time >= menu.start_time or time<= menu.end_time:
        what_menu.append(menu.name)
    return what_menu



menus=[brunch, early_bird, dinner, kids]
flagship_store=Franchise("1232 West End Road", menus)
new_installment = Franchise("12 East Mulberry Street", menus)
print(new_installment)

print(new_installment.available_menus(5))

class Business:
  def __init__(self, name, franchises):
    self.name=name
    self.franchises=franchises

franchises_1=[flagship_store, new_installment]
business_1=Business("Basta Fazoolin' with my Heart", franchises_1)

arepas_menu=Menu("Take a' Arepa", {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}, 10, 8)

arepas_place=Franchise("189 Fitzgerald Avenue", arepas_menu)

business_2=Business("Take a' Arepa", arepas_place)




