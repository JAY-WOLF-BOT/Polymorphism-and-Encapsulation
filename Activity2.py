class Cat:
  def _init_(self,name,age):
    self.name = name
    self.age = age

def info(self):
  print(f"I am a cat. My name is {self.name}. I am {self.age} years old.") 

def make_sound(self):
  print("Meow")

class Dog:
  def _init_(self,name,age):
    self.name = name
    self.age = age

def info(self):
  print(f"I am a dog. My name is {self.name}. I am {self.age} years old.") 

def make_sound(self):
  print("Bark")

  cat1 = Cat("Dodo", 2.5)
  dog1 = Dog("Tyson", 8)

  for animal in (cat1,dog1):
    animal.make_sound()
    animal.info()

