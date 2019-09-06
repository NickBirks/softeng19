__all__ = ['Turtle', 'ColossusTurtle']


class Turtle(object):
    def __init__(self, name, mass):
        self.name = name
        self.mass = mass

    def __repr__(self):
        return self.name


class ColossusTurtle(Turtle):
    def __init__(self, name, mass):
        super().__init__(name, mass)
        self.buddy = None

    def carry(self, buddy):
        self.buddy = buddy

    def __repr__(self):
        if self.buddy:
            return '{}, who is carrying {}'.format(self.name, self.buddy.name)
        else:
            return super().__repr__()


def test_turtles():
    t = Turtle('Josh', 59.0)
    s = ColossusTurtle('Sven', 80.0)
    s.carry(t)

    print(t)
    print(s)


if __name__ == '__main__':
    test_turtles()
