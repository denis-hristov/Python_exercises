from math import floor
record = float(input())
distance = float(input())
time = float(input())

distanceTime = distance * time
additionalTime = floor(distance / 15) * 12.5

totalTime = distanceTime + additionalTime

if totalTime < record:
    print(f"Yes, he succeeded! The new world record is {totalTime:.2f} seconds.")
else:
    endTime = totalTime - record
    print(f"No, he failed! He was {endTime:.2f} seconds slower.")
