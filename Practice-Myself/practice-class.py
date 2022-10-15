#python class
# Classes are created by keyword 'class'
class Person:
    
    # vvvvvv --attributes
    # Class Variables
    attr1 = "Human"
    attr2 = "Earth planet"
    name = "Adam"
    
    # vvvvvv --methods
    # 'class methods' must have an extra first parameter in the method definition
    # init method or constructor
    def __init__(self, name: str):
        # Instance Variables
        self.name = name
    
    # 'sample method'
    def say_hi(self):
        print('Hello, my name is', self.name)

#Driver code
#Object instantiation
# when you create a 'declaring object', it consists of identity[name], state[attr], behaviour[method]

# identity + state
# we do not give a value for this parameter when we call the method, Python provides it
p = Person('Nikhil')
# behaviour
p.say_hi()
#accessing class attributes
print(p.name)
