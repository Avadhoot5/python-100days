# Regular Expressions 
# Resources for learning 
# https://regexr.com/
# https://www.ibm.com/docs/en/rational-clearquest/9.0.1?topic=tags-meta-characters-in-regular-expressions
import re

# pattern = r"expression"
# pattern = r"ello"
# text = "Hello World!"
# match = re.search(pattern, text)
# print(match)
# if match:
#     print("Match found!")
# else:
#     print("Match not found.")

pattern = r"[A-Z]yclone"
text = '''
a Cyclone is a large air mass Dyclone that rotates around a strong center of low atmospheric pressure, Nyclone counterclockwise in the Northern Hemisphere and clockwise in the Southern Hemisphere as viewed from above (opposite to an anticyclone).[1][2] Cyclones are characterized by inward-spiraling winds that rotate about a zone of low pressure.[3][4] The largest low-pressure systems are polar vortices and extratropical cyclones of the largest scale (the synoptic scale). Warm-core cyclones such as tropical cyclones and subtropical cyclones also lie within the synoptic scale.
'''
# match = re.findall(pattern, text)
matches = re.finditer(pattern, text)
# Span and Match - returns result in form of tuple
# for match in matches:
#     print(match)
for match in matches:
    print(text[match.span()[0]: match.span()[1]])
