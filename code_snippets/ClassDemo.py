'''
Object-oriented programming creates reusable patterns of code to curtail redundancy in development projects.

One way that object-oriented programming achieves recyclable code is through inheritance,
when one subclass can leverage code from another base class.
'''


# create a base class
class Parent:
    'Insert class description (optional)'

    # a class variable (the value is shared among all class instances)
    visibleClassVar = 10
    __hiddenClassVar = 189

    # constructor (note that you cannot overload functions in python)
    def __init__(self, name, age, height, weight, country='GB'):
        self.name = name # public class member variable (accessible outside of class)
        self.__age = age # private class member variable (accessed by class member functions)
        self.height = height
        self.weight = weight
        self.country = country
        self.set_bmi()

    # class member functions (methods)
    def set_bmi(self):
        self.bmi = self.weight / self.height**2

    def display_info(self):
        print('Name:', self.name,
              '\b, Age:', self.__age)

    def display_verbose_info(self):
        print('Name:', self.name,
              '\b, Age:', self.__age,
              '\b, BMI:', self.bmi,
              '\b, Country:', self.country)


# create a derived class which inherits from the base class
class Child(Parent):

    childVisibleClassVar = -1
    __childHiddenClassVar = 300

    # overwrite the inherited constructor (only if required)
    # call the inherited method using the 'super' function
    def __init__(self, name, age, height, weight, toy, country='NA'):
        super().__init__(name, age, height, weight, country)
        self.toy = toy # this derived class has an additional member variable

    # overwrite an inherited method
    def display_verbose_info(self):
        print('Name:', self.name,
              '\b, Age:', self._Parent__age, # access a base class hidden variable (no such thing as a protected member)
              '\b, BMI:', self.bmi,
              '\b, Country:', self.country,
              '\b, Toy:', self.toy)

    # this derived class has an additional method
    def years_until_adult(self):
        return 18 - self._Parent__age


# will NOT run this code if we import the classes
if __name__ == '__main__':

    parent = Parent('John', 40, 1.8, 75) # create a Parent object instance
    print(dir(parent)) # inspect the class
    print()
    parent.display_info()
    parent.display_verbose_info()
    print()
    print()

    child = Child('Max', 11, 1.1, 30, 'Lego') # create a Child object instance
    print(dir(child)) # inspect the class
    print()

    print(child.__dict__) # a useful way to print member variable values
    print()
    child.display_info()
    child.display_verbose_info()
    print(child.years_until_adult())
