#Problem 8
#20.0/20.0 points (graded)

"""
Write a function called general_poly, that meets the specifications below. For example, 
general_poly([1, 2, 3, 4])(10) should evaluate to 1234 because 1∗10^3+2∗10^2+3∗10^1+4∗10^0.
"""

def general_poly (L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value 
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """
    #YOUR CODE HERE
    def to_apply (x):
        i = 0
        for n in L:
            i = x*i + n
        return i
    return to_apply
