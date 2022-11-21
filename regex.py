import re

allApes =  re.findall('ape.', 'the ape was at the apex')

for i in allApes:
    print(i)
