#Assignment 3 Rachel Weller
# some parts of this 
import random
import time

print("\U0001F33A Its time to grow your own meadow! \U0001F33A")

flower_options = ["\U0001F338", "\U0001F33C", "\U0001F33B", "\U0001F339", "\U0001F33A", "\U0001FABB"]
print("Choose what flowers you want to grow! (Lavender, Rose, Sunflower, Hibiscus, Blossom, Cherry Blossom)")
for idx, flower in enumerate(flower_options, 1):
    print(f"{idx}: {flower}")

time.sleep(2)

width = int(input("How wide should your meadow be (5-50)? "))
height = int(input("How high should your meadow be (3-20)? "))

if width < 5:
    width = 5
if width > 50:
    width = 50
if height < 3:
    height = 3
if height > 20:
    height = 20

flower_number = int(input("Choose what flower you want to plant: (1.Cherry Blossom, 2. Blossom, 3. Sunflower, 4. Rose, 5. Hibiscus, 6. Lavender) "))
if 1 <= flower_number <= len(flower_options):
    chosen_flower = flower_options[flower_number - 1]
else:
    print("Invalid choice! We'll use a \U0001F33A as your flower!")
    chosen_flower = "\U0001F33A"

extra_flowers = random.sample(flower_options, 2)

print("Growing your meadow...")
time.sleep(2)

for i in range(height):
    for j in range(width):
        if random.random() > 0.3:  
            flower_to_print = random.choice([chosen_flower] + extra_flowers)
            print(flower_to_print, end="")
        else:
            print(" ", end="")
    print() 

print("\U0001F338 Your beautiful meadow is ready! \U0001F33A")
