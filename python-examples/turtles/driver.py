from turtles import *

t = Turtle('Josh', 59.0)
s = ColossusTurtle('Sven', 80.0)
s.carry(t)

print(t)
print(s)

# We shouldn't be able to use this any more since
# it is not exposed through __all__ in turtles.py.
#
# test_turtles()
