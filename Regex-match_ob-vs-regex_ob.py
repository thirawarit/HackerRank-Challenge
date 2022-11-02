import re
#___a match object___ vs ___a regular expression object___
#a match object is from "re.search()" that scan through string looking for the first pos., and return it.
#a reg ex object is from "re.compile()" that can be used for matching using its method.
#especially, matching using its search() with _arguement_ -> (string[, pos[, endpos]])

string = input()
m_string = input()
pattern = r"%s" % (m_string)
# re.search(pattern, string) -> return _a match object_
mo = re.search(pattern, string)
if mo:
    while mo:
        print((mo.start(), mo.end()-1))
        # re.compile() -> return _a regular expression object_
        regexo = re.compile(pattern)
        # re.compile = pattern -> pattern.search(string[, pos[, endpos]]) 
        #              -> return _a match object_
        mo = regexo.search(string, mo.start() + 1)
else:
    print((-1, -1))
