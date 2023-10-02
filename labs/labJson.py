#Author: Daniel Terreros

#Description: A program to parse json dictionary

import json

with open('astronauts.json') as fInput :
    astros = json.load(fInput)

count = 0
sum_total_duration = 0
sum_age_at_mission = 0


for astronaut in astros :
   count +=1

   sName = astronaut['Profile']['Name']
   print(sName)



