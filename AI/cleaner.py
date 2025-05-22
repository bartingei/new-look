'''import random

def display(room):
    print(room)

room = [
    [1,1,1,1],
    [1,1,1,1],
    [1,1,1,1],
    [1,1,1,1],
]

print("all the rooms are dirty")
display(room)

x = 0
y = 0

while x < 4:
    while y < 4:
        room[x][y] = random.choice([0,1])
        y+=1
        x+=1
        y=0

print("Before i clean the rooms i detect all of these random dirts")
display(room)
x=0
y=0
z=0

while x < 4:
    while y < 4:
        if room[x][y] == 1:
            print("vacuum in this location now, " , x, y)
            room[x][y] = 0
            print("cleaned", x, y)
            z += 1
        y += 1
    x += 1
    y = 0

pro = (100 - ((z/16) * 100))
print("Room is clean now: thanks for using : 371093")
display(room)
print("performance", pro, '&')'''


import random

def display(room):
    for row in room:
        print(row)

# Predefined room layout
room = [
    [0, 1, 0, 1],
    [1, 0, 1, 0],
    [0, 1, 1, 0],
    [1, 0, 0, 1],
]

print("Initial room state (0 = clean, 1 = dirty):")
display(room)

# Vacuum cleaning
cleaned = 0
for i in range(4):
    for j in range(4):
        if room[i][j] == 1:
            print(f"Cleaning location ({i}, {j})")
            room[i][j] = 0
            cleaned += 1

# Performance calculation
performance = 100 - (cleaned / 16 * 100)

print("\nRoom is now clean!")
display(room)
print(f"Performance: {performance}%")
