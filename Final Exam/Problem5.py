def cipher(map_from, map_to, code):
    """ map_from, map_to: strings where each contain 
                          N unique lowercase letters. 
        code: string (assume it only contains letters also in map_from)
        Returns a tuple of (key_code, decoded).
        key_code is a dictionary with N keys mapping str to str where 
        each key is a letter in map_from at index i and the corresponding 
        value is the letter in map_to at index i. 
        decoded is a string that contains the decoded version 
        of code using the key_code mapping. """
    # Your code here
    
    key_code = {}
    decode = ''
    
    for letter in map_from:
        key_code[letter] = map_to[map_from.index(letter)]

    for e in code:
        de = key_code[e]
        decode += de

    return (key_code, decode)
