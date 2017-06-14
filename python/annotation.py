def helloSolarSystem(original_function):
    def new_function(*args, **kwargs):
        original_function(*args, **kwargs)
        print("Hello, solar system!")
    return new_function
 
def helloGalaxy(original_function):
    def new_function(*args, **kwargs):
        original_function(*args, **kwargs)
        print("Hello, galaxy!")
    return new_function
 
@helloGalaxy
@helloSolarSystem
def hello(targetName=None):
    if targetName:
        print("Hello, " +  targetName +"!")
    else:
        print("Hello, world!")
 
# Here is where we actually *do* something!
hello("wgg")

''' equivalent to this
def hello():
    print ("Hello, world!")
hello = helloSolarSystem(hello)
hello = helloGalaxy(hello)
'''
