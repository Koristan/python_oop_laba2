class User :
  name = None
  position = None
  department = None

  def __init__(self,name, position, department):
    self.name = name
    self.position = position
    self.department = department

class Position:
  pass

class Departament:
  pass

pos = Position()
dep = Departament()

user = User("Shiskail", pos, dep)