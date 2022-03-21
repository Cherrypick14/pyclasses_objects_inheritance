# Using inheritance in python
class Pet:
    def __init__(self, name, age):
        self.name =name
        self.age=age
    def speak(self):
        print(f"Hey there, I am {self.name} and I am {self.age}")
class Cat(Pet):

    def speak(self):
        print("Meow")

class Dog(Pet):
     def __init__(self,name, age,color):
         super().__init__(name,age)
         self.color=color
     def speak(self):
        print("Bark")
     def show(self):
        print(f"Hey there, I am {self.name} and I am {self.age} my color is {self.color}")
p1 = Pet("hoho",12)
p1.speak()
c1 =Cat("hooli",40)
c1.speak()
d1 =Dog("jido",33,"black")
d1.show()