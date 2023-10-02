#Author: Daniel Terreros

#Description: A program to parse json dictionary

import json

with open('astronauts.json') as fInput :
    astros = json.load(fInput)

count = 0
dSumTotalDuration = 0
iSumAgeAtMission = 0


for astronaut in astros :
   count +=1

   sName = astronaut['Profile']['Name']
   iMissionYear = astronaut['Mission']['Year']
   iBirthYear  = astronaut['Profile']['Birth Year']
   dMissionDuration = astronaut['Mission']['Durations']['Mission duration']
   dSumTotalDuration += dMissionDuration
   iAgeAtMission = iMissionYear - iBirthYear
   iSumAgeAtMission += iAgeAtMission
   



   print(f"Record number: {count}")
   print(f"Name: {sName}")
   print(f"Mission Year: {iMissionYear}")
   print(f"Birth Year: {iBirthYear}\n")

#  print(f"Age at mission: {iAgeAtMission}")
#  print(f"Duration: {dMissionDuration}")

dAverageMissionDuration = dSumTotalDuration / count
dAverageAgeAtMission = round(iSumAgeAtMission / count)
print(f"The average age of an astronaut at the time of their mission is {dAverageAgeAtMission} years old")
print(f"The average mission duration is: {dAverageMissionDuration:.2f}")







