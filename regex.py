import re

theStr =  re.findall('ape.', 'the ape was at the apex')

for i in re.finditer('ape.', theStr):

    locTuple = i.span()

    print(locTuple)
    print(theStr[locTuple[0]:locTuple[i]])
