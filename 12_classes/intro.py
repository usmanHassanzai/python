class Animal:
    legs = False    #class variable/class member
    name = " "
    
    def sound(self):    #member function
        return '*silence*'
    def move(self):     #self is used to access variables and methods that belongs to class instance.
        return True

class Dog(Animal):  #dog is a type of animal
    def sound(self):
        return "bark"

class Cat(Animal):
    def sound(self):
        return "meow"

d = Dog()
d.sound()
d.move()    #it will take from animal class which is a parent class 
d.run() #now it is not present it will give attribute error

c = Cat()
c.sound()


    

a = Animal() #Instance of class / object of a class
a.legs
a.sound()