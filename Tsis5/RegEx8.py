import re

def ch(s):
    parts = re.findall('[A-Z][^A-Z]*', s)
    return parts


string = "CanIHaveOneDayOfRest?"
result = ch(string)
print(result)
