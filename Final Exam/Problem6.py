class Container(object):
    """ Holds hashable objects. Objects may occur 0 or more times """
    def __init__(self):
        """ Creates a new container with no objects in it. I.e., any object 
            occurs 0 times in self. """
        self.vals = {}
    def insert(self, e):
        """ assumes e is hashable
            Increases the number times e occurs in self by 1. """
        try:
            self.vals[e] += 1
        except:
            self.vals[e] = 1
    def __str__(self):
        s = ""
        for i in sorted(self.vals.keys()):
            if self.vals[i] != 0:
                s += str(i)+":"+str(self.vals[i])+"\n"
        return s
        
class Bag(Container):
    def remove(self, e):
        """ assumes e is hashable
            If e occurs in self, reduces the number of 
            times it occurs in self by 1. Otherwise does nothing. """
        # write code here
        if e in self.vals.keys():
            self.vals[e] -= 1

    def count(self, e):
        """ assumes e is hashable
            Returns the number of times e occurs in self. """
        # write code here
        if e not in self.vals.keys():
            return 0
        else:
            return self.vals[e]
    
    def __add__(self, other):
        new_dict = other.vals.copy()  # copy required to prevent updating `other.vals`
        for e in self.vals.keys():
            if e in other.vals.keys():
                new_dict[e] += self.vals[e]
            else:
                new_dict[e] = self.vals[e]

        # Create a new instance and populate it with new_dict
        new_instance = Bag()
        new_instance.vals.update(new_dict)
        return new_instance

    def __str__(self):
        # Use self.vals here not sef.new_dict
        s1 = ""
        for i in sorted(self.vals.keys()):
            s1 += str(i)+":"+str(self.vals[i])+"\n"
        return s1
      
      
class ASet(Container):
    def remove(self, e):
        """assumes e is hashable
           removes e from self"""
        # write code here
        return self.vals.pop(e)

    def is_in(self, e):
        """assumes e is hashable
           returns True if e has been inserted in self and
           not subsequently removed, and False otherwise."""
        # write code here
        return e in self.vals
