'''
https://docs.python.org/2/reference/datamodel.html#implementing-descriptors
https://docs.python.org/2/howto/descriptor.html

descriptor can only be used as class property. is T.d = D()
For instance get such as T().d
Priority: 
data descriptors priority
instance variables
non-data descriptors
__getattr__()
'''

class D(object):
    def __get__(self, instance, owner):
        print "get",instance
        return self.ttt
    def __set__(self, instance, val):
        print "set",instance
        self.ttt = val
        

class T(object):
    d = D()

a = T()
# __set__ can only be called by instance
a.d = "wgg"
T.d = "ttt" # No call to __set__, just override
print 'get'
print a.d
print T.d
