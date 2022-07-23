def aboundant(objects):
    sum_stars = 0
    sum_galaxies = 0
    sum_supernovae = 0
    sum_frbs = 0
    for o in objects:
        if o['type'] == 'star':
            sum_stars += 1
    for o in objects:
        if o['type'] == 'galaxy':
            sum_galaxies += 1
    for o in objects:
        if o['type'] == 'supernovae':
            sum_supernovae += 1
    for o in objects:
        if o['type'] == 'frb':
            sum_supernovae += 1
    
    if sum_stars >= sum_galaxies and sum_stars >= sum_supernovae and sum_stars >= sum_frbs:
        return 'stars'
    if sum_galaxies >= sum_stars and sum_galaxies >= sum_supernovae and sum_galaxies >= sum_frbs:
        return 'galaxies'
    if sum_supernovae >= sum_stars and sum_supernovae >= sum_galaxies and sum_supernovae >= sum_frbs:
        return 'supernovae'
    if sum_frbs >= sum_stars and sum_frbs >= sum_galaxies and sum_frbs >= sum_supernovae:
        return 'frbs'

#Retaining the original input
input_1 = """
[
    {
        "type": "star",
        "name": "alpha-centaurus",
        "redshift": 0
    },
    {
        "type": "nebula",
        "name": "crab",
        "redshift": 0
    },
    {
        "type": "galaxy",
        "name": "sombrero",
        "redshift": 0
    }
]
"""
#Removed "type":"stars" alone from the original input
input_2 = """
[
    {
        "type": "nebula",
        "name": "crab",
        "redshift": 3
    },
    {
        "type": "galaxy",
        "name": "sombrero",
        "redshift": 5
    }
]
"""

#Retaining the original input
input_3 = """
[
    {
        "type": "star",
        "name": "alpha-centaurus",
        "redshift": 1
    },
    {
        "type": "nebula",
        "name": "crab",
        "redshift": 3
    },
    {
        "type": "galaxy",
        "name": "sombrero",
        "redshift": 2
    },
    {
        "type": "star",
        "name": "alpha-centaurus_2",
        "redshift": 4
    }
]
"""

#Removed "type":"stars" and "type":"galaxy" from the original input
input_4 = """
[
    {
        "type": "nebula",
        "name": "crab",
        "redshift": 0
    }
]
"""

import json

print(aboundant(json.loads(input_1)))
print(aboundant(json.loads(input_2)))
print(aboundant(json.loads(input_3)))
print(aboundant(json.loads(input_4)))

def farthest(objects):
    highest_redshift = None
    for o in objects:
        if highest_redshift is None or o["redshift"] < highest_redshift:
            highest_redshift = o["redshift"]
    for o in objects:
        if o["redshift"] == highest_redshift:
            return o

print(farthest(json.loads(input_1)))
print(farthest(json.loads(input_2)))
print(farthest(json.loads(input_3)))
print(farthest(json.loads(input_4)))
