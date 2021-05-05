# Version 1
import ClassDemo
parent1 = ClassDemo.Parent('John 1', 41, 1.71, 100)
parent1.display_verbose_info()

# Version 2
import ClassDemo as cd
parent2 = cd.Parent('John 2', 42, 1.72, 100)
parent2.display_verbose_info()

# Version 3
from ClassDemo import Parent, Child
# from ClassDemo import *
parent3 = Parent('John 3', 43, 1.73, 100)
parent3.display_verbose_info()
child3 = Child('Max 3', 13, 1.13, 30, 'Yoyo')
child3.display_verbose_info()

# Version 4
import faux_package.faux_functions as ff
ff.say_hello()
ff.say_bonjour()