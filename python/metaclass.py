'''
https://blog.ionelmc.ro/2015/02/09/understanding-python-metaclasses/
instance is instance of class
class is instance of metaclass
default metaclass is type

in new style classes: https://docs.python.org/release/2.5.2/ref/node33.html
__new__ static method to create a new instance
__new__ will call __init__ for the new created instance
'''

MyClass = type.__new__(type, 'MyClass',(),{})
# equivalent to type('MyClass',(),{})
# argument for type: __name__, __base__, __dict__
MyClass1 = type('MyClass',(),{})
print MyClass
print MyClass1

class MetaClass(object):
    def __new__(cls, name, parents, dct):
        print "newwgg"
        print dct
        # init will not be called since we pass type,
        # so type's init will be called
        return type.__new__(type, name, parents, dct)
    def __init__(self,name, parents, dct):
        print "init"+name

class Hello(object):
    __metaclass__ = MetaClass
    p1 = 'ppp'
    @staticmethod
    def b():
        print 'b'
    def p(self):
        print 'p'

# Or
BB = MetaClass.__new__(MetaClass,"BB",(),{})


print Hello().p()
