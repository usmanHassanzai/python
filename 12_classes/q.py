#Understanding the concpet of self

class Person:
    #default constructor automatically call when object is created
    def __init__(self , name , age):
        self.name = name
        self.age = age
    def greet(self):
        print(f"Hello my name is {self.name} and i am {self.age} years old.")

person_object = Person("Usman" , 24)
person_object.greet()

"""1.self must always be the first parameter of instance methods.
2.It is not a keyword, so technically you could name it anything, but by convention, it is always named self.
3.self allows each instance of the class to have its own attributes, separate from other instances."""
