def get_lastword(s):
    i = len(s) - 1
    while i >= 0:
        if s[i] == " ":
            if len(s) - i == 1:
                s = s[:-1]
                i -= 1
                continue
            return len(s) - (i + 1)
        i -= 1
    return len(s) or 0


print get_lastword("Hello world")            
print get_lastword("   ")            
print get_lastword("")            
print get_lastword("abc")            
print get_lastword(" abc   def    xyz  ")            

