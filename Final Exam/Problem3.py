def sum_digits(s):
    """ assumes s a string
        Returns an int that is the sum of all of the digits in s.
          If there are no digits in s it raises a ValueError exception. """
    # Your code here
    num_list = '1234567890'
    n = 0
    digit_flag = False
    for e in s:
        if e in num_list:
            n += int(e)
            digit_flag = True
    if digit_flag ==  False:
        raise ValueError('no digits in s')
    else:
        return n
