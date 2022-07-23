def aboundant(objects):
    sum_stars = 0
    sum_galaxies = 0
    sum_supernovae = 0
    sum_frbs = 0
    chosen_item = ""
    for o in objects:
        if o['type'] == 'star':
            sum_stars += 1
        elif o['type'] == 'galaxy':
            sum_galaxies += 1
        elif o['type'] == 'supernovae':
            sum_supernovae += 1
        elif o['type'] == 'frb':
            sum_frbs += 1
    
    print("Total Number of stars : " + str(sum_stars))
    print("Total Number of galaxies : " + str(sum_galaxies))
    print("Total Number of supernovae : " + str(sum_supernovae))
    print("Total Number of frbs : " + str(sum_frbs))
    
    info_dict = {"stars": "stars","galaxies": "galaxies","supernovae": "supernovae","frbs": "frbs",
                 "st_g":"stars and galaxies","st_su":"stars and supernovae","st_fr":"stars and frbs",
                 "g_su":"galaxies and supernovae","g_fr":"galaxies and frbs","su_fr":"supernovea and frbs",
                 "st_g_su":"stars,galaxies and supernovae","st_g_fr":"stars,galaxies and frbs","st_su_fr":"stars,supernovae and frbs",
                 "g_su_fr":"galaxies,supernovae and frbs","st_g_su_fr":"stars,galaxies,supernovae and frbs"
                 }
    
    if (sum_stars >= sum_galaxies and sum_stars >= sum_supernovae and sum_stars >= sum_frbs):
        if(sum_stars > sum_galaxies and sum_stars > sum_supernovae and sum_stars > sum_frbs):
            chosen_item = "stars"
        elif(sum_stars == sum_galaxies and sum_stars > sum_supernovae and sum_stars > sum_frbs):
            chosen_item = "st_g"
        elif(sum_stars > sum_galaxies and sum_stars == sum_supernovae and sum_stars > sum_frbs):
            chosen_item = "st_su"
        elif(sum_stars > sum_galaxies and sum_stars > sum_supernovae and sum_stars == sum_frbs):
            chosen_item = "st_fr"
        elif(sum_stars == sum_galaxies and sum_stars == sum_supernovae and sum_stars > sum_frbs):
            chosen_item = "st_g_su"
        elif(sum_stars == sum_galaxies and sum_stars > sum_supernovae and sum_stars == sum_frbs):
            chosen_item = "st_g_fr"
        elif(sum_stars > sum_galaxies and sum_stars == sum_supernovae and sum_stars == sum_frbs):
            chosen_item = "st_su_fr"
        
    elif (sum_galaxies >= sum_stars and sum_galaxies >= sum_supernovae and sum_galaxies >= sum_frbs):
        if(sum_galaxies > sum_stars and sum_galaxies > sum_supernovae and sum_galaxies > sum_frbs):
            chosen_item = "galaxies"
        elif(sum_galaxies == sum_stars and sum_galaxies > sum_supernovae and sum_galaxies > sum_frbs):
            chosen_item = "st_g"
        elif(sum_galaxies > sum_stars and sum_galaxies == sum_supernovae and sum_galaxies > sum_frbs):
            chosen_item = "g_su"
        elif(sum_galaxies > sum_stars and sum_galaxies > sum_supernovae and sum_galaxies == sum_frbs):
            chosen_item = "g_fr"
        elif(sum_galaxies == sum_stars and sum_galaxies == sum_supernovae and sum_galaxies > sum_frbs):
            chosen_item = "st_g_su"
        elif(sum_galaxies == sum_stars and sum_galaxies > sum_supernovae and sum_galaxies == sum_frbs):
            chosen_item = "st_g_fr"
        elif(sum_galaxies > sum_stars and sum_galaxies == sum_supernovae and sum_galaxies == sum_frbs):
            chosen_item = "g_su_fr"
    
    elif(sum_supernovae >= sum_stars and sum_supernovae >= sum_galaxies and sum_supernovae >= sum_frbs):
        if(sum_supernovae > sum_stars and sum_supernovae > sum_galaxies and sum_supernovae > sum_frbs):
            chosen_item = "supernovae"
        elif(sum_supernovae == sum_stars and sum_supernovae > sum_galaxies and sum_supernovae > sum_frbs):
            chosen_item = "st_su"
        elif(sum_supernovae > sum_stars and sum_supernovae == sum_galaxies and sum_supernovae > sum_frbs):
            chosen_item = "g_su"
        elif(sum_supernovae > sum_stars and sum_supernovae > sum_galaxies and sum_supernovae == sum_frbs):
            chosen_item = "su_fr"
        elif(sum_supernovae == sum_stars and sum_supernovae == sum_galaxies and sum_supernovae > sum_frbs):
            chosen_item = "st_g_su"
        elif(sum_supernovae == sum_stars and sum_supernovae > sum_galaxies and sum_supernovae == sum_frbs):
            chosen_item = "st_su_fr"
        elif(sum_supernovae > sum_stars and sum_supernovae == sum_galaxies and sum_supernovae == sum_frbs):
            chosen_item = "g_su_fr"
            
    elif(sum_frbs >= sum_stars and sum_frbs >= sum_galaxies and sum_frbs >= sum_supernovae):
        if(sum_frbs > sum_stars and sum_frbs > sum_galaxies and sum_frbs > sum_supernovae):
            chosen_item = "frbs"
        elif(sum_frbs == sum_stars and sum_frbs > sum_galaxies and sum_frbs > sum_supernovae):
            chosen_item = "st_fr"
        elif(sum_frbs > sum_stars and sum_frbs == sum_galaxies and sum_frbs > sum_supernovae):
            chosen_item = "g_fr"
        elif(sum_frbs > sum_stars and sum_frbs > sum_galaxies and sum_frbs == sum_supernovae):
            chosen_item = "su_fr"
        elif(sum_frbs == sum_stars and sum_frbs == sum_galaxies and sum_frbs > sum_supernovae):
            chosen_item = "st_g_fr"
        elif(sum_frbs == sum_stars and sum_frbs > sum_galaxies and sum_frbs == sum_supernovae):
            chosen_item = "st_su_fr"
        elif(sum_frbs > sum_stars and sum_frbs == sum_galaxies and sum_frbs == sum_supernovae):
            chosen_item = "g_su_fr"
        
    elif(sum_stars == sum_galaxies and sum_stars == sum_supernovae and sum_stars == sum_frbs):
            chosen_item = "st_g_su_fr"
            
    return info_dict.get(chosen_item, "No info available")


def farthest(objects):
    highest_redshift = None
    total = []
    for o in objects:
        if highest_redshift is None or o["redshift"] < highest_redshift:
            highest_redshift = o["redshift"]
            print("highest redshift = " + str(highest_redshift))
            
    for o in objects:
        if o["redshift"] == highest_redshift:
            total.append(o)
            
    
    return total
        
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

print("Data for json input_1")
print("Aboundant = " + str(aboundant(json.loads(input_1))) + "\n")

print("Data for json input_2")
print("Aboundant = " + str(aboundant(json.loads(input_2))) + "\n")

print("Data for json input_3")
print("Aboundant = " + str(aboundant(json.loads(input_3))) + "\n")

print("Data for json input_4")
print("Aboundant = " + str(aboundant(json.loads(input_4))) + "\n")

print("Farthest Data for json input_1")
print("Farthest = " + str(farthest(json.loads(input_1))) + "\n")

print("Farthest Data for json input_2")
print("Farthest = " + str(farthest(json.loads(input_2))) + "\n")

print("Farthest Data for json input_3")
print("Farthest = " + str(farthest(json.loads(input_3))) + "\n")

print("Farthest Data for json input_4")
print("Farthest = " + str(farthest(json.loads(input_4))) + "\n")