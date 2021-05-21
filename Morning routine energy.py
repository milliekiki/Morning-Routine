import random

Low_energy = ["meditate for 10 minute","drink water","sit on the balcony for 5 mins","journal"]
Medium_energy = ["light stretch","clean room","clean kitchen","gratitude journal"]
High_energy = ["work out","dance","yoga","read non-fiction"]

energy_level = int(input("What is your energy level today?1 to 3"))
print("This is something you should do")

if energy_level == 1:
    print(random.choice(Low_energy))
if energy_level == 2:
    print (random.choice(Medium_energy))
if energy_level == 3:
    print (random.choice(High_energy))