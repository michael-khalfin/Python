def rot(c, n):
    """ returns a new letter which has been "rotated" by n characters forward
        in the alphabet
        
        input c is a string
        input n is a number
    """
    # check to ensure that c is a single character
    assert(type(c) == str and len(c) == 1)

    # lowercase letters 97 to 122
    # uppercase letters 65 to 90
    c = ord(c)

    if n <= 25 and (97 <= c <= 122 - n or 65 <= c <= 90 - n):
        c = chr(c + n)
    elif n <= 25 and 122 - n <= c <= 122:
        c -= 97
        c += n
        c %= 26
        c += 97
        c = chr(c)
    elif n <= 25 and 90 - n <= c <= 90:
        c -= 65
        c += n
        c %= 26
        c += 65
        c = chr(c)
    elif n >= 26 and (97 <= c <= 122 or 65 <= c <= 90):
        return rot(chr(c), n - 26)
    else:
        c = chr(c)
    return c

def encipher(s, n):
    """ returns a new string in which the letters in s have been "rotated" by n
        characters forward in the alphabet, wrapping around as needed
        
        input s is a string
        input n is a number
    """
    new = "".join([rot(c,n) for c in s])
    return new

def letter_probability(c):
    """ if c is the space character (' ') or an alphabetic character,
        returns c's monogram probability (for English);
        returns 1.0 for any other character.
        adapted from:
        http://www.cs.chalmers.se/Cs/Grundutb/Kurser/krypto/en_stat.html
    """
    # check to ensure that c is a single character
    assert(type(c) == str and len(c) == 1)

    if c == ' ': return 0.1904
    if c == 'e' or c == 'E': return 0.1017
    if c == 't' or c == 'T': return 0.0737
    if c == 'a' or c == 'A': return 0.0661
    if c == 'o' or c == 'O': return 0.0610
    if c == 'i' or c == 'I': return 0.0562
    if c == 'n' or c == 'N': return 0.0557
    if c == 'h' or c == 'H': return 0.0542
    if c == 's' or c == 'S': return 0.0508
    if c == 'r' or c == 'R': return 0.0458
    if c == 'd' or c == 'D': return 0.0369
    if c == 'l' or c == 'L': return 0.0325
    if c == 'u' or c == 'U': return 0.0228
    if c == 'm' or c == 'M': return 0.0205
    if c == 'c' or c == 'C': return 0.0192
    if c == 'w' or c == 'W': return 0.0190
    if c == 'f' or c == 'F': return 0.0175
    if c == 'y' or c == 'Y': return 0.0165
    if c == 'g' or c == 'G': return 0.0161
    if c == 'p' or c == 'P': return 0.0131
    if c == 'b' or c == 'B': return 0.0115
    if c == 'v' or c == 'V': return 0.0088
    if c == 'k' or c == 'K': return 0.0066
    if c == 'x' or c == 'X': return 0.0014
    if c == 'j' or c == 'J': return 0.0008
    if c == 'q' or c == 'Q': return 0.0008
    if c == 'z' or c == 'Z': return 0.0005
    return 1.0

def decipher(s):
    """ returns the original English string to the best of its ability
        input s is a string
    """
    possibilities = [encipher(s, n) for n in range(26)]
    possibilitieslist = []
    problist = []
    for i in range(len(possibilities)):
        possibilitieslist.append([poss for poss in possibilities[i]])
        problist.append([letter_probability(c) for c in possibilitieslist[i]])
    prob = [sum(add) for add in problist]
    
    best = 0
    for p in range(len(prob)):
        if prob[p] > best:
            best = p
    return possibilities[best]
