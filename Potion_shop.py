import random
Ingredients = [
    ["Coffee Bean", "Students seek me before battles with textbooks." ],
    ["Honey", "When wounds complain, I often get invited." ],
    ["Magic Glitter", "Nobody knows what I do, yet everyone throws me into the cauldron."],
    ["Unlabeled Powder", "Every great disaster starts with curiosity."],
    ["Moon Flower", "I whisper only to dreamers."],
    ['Frog Slime', "Touch me if you enjoy unexpected transformations."],
    ["Dragon Scale", "Once belonged to a creature that never skipped arm day."],
    ["Unicorn Fur", "Luck tends to follow wherever I wander"],
    ["Dew Drops", "I am the first thing flowers drink."],
    ["Star Dust", "Ancient secrets cling to me like glitter"]
]

Requests = [
    "I need help focusing on my exam.",
    "My bullies keep picking on me.",
    "I need to sneak past the guards today",
    "I keep forgetting.",
    "I am tired everyday.",
    "I need to learn fire magic.",
    "I am being chased by the goblins.",
    "I just survived the dragon attack."
    " I need to complete my art project.",
    "I am so unlucky."
]

Recipes = [
    ["Coffee Bean", "Star Dust", "Memory"],
    ["Coffee Bean", "Honey", "Energy"],
    ["Dragon Scale", "Unlabeled Powder", "Concentration"],
    ["Star Dust", "Magic Gitter", "Fire Magic"],
    ["Unicorn Fur", "Unlabeled Powder", "Teleportation"],
    ["Honey", "Dew Drops", "Healing"],
    ["Frog Slime", "Unicorn Fur", "Luck"],
    ["Magic Glitter", "Frog Slime", "Invisibility"],
    ["Moon Flower", "Magic Glitter", "Creativity"],
    ["Dragon Scale", "Moon Flower", "Superhuman Strength"]
]

Failed_Outcomes =[
    "Turned to Giant",
    "turned to Frog",
    "grew a tail",
    "Smells like trash",
    "Starts laughing uncontrollably",
    "Grew Horns",
    "Shrunk to the size of a Mouse",
    "started dancing",
    "Started floating",
    "starts crying uncontrollably"
]

customer = random.choice(Requests)
print("=============================================")
print("||           THE POTION SHOP               ||")
print("=============================================")
print("--------------------------------------------")
print("       A customer enters the shop")
print("--------------------------------------------")
print()
print()
print("The Customer says:")
print(f'"{customer}"')
Potions = []
while len(Potions) < 2:
    print("===============================================")
    print("         THE INGREDIENTS SHELF")
    print("===============================================")

    for i in range(10):
        print(f"{i+1}.{Ingredients[i][0]}")
    print()
    Choice = int(input("Choose an ingredient to inspect: "))
    index = Choice - 1
    print()
    print(Ingredients[index][0]) 
    print(Ingredients[index][1])
    print()

    ans1 = input("Use the ingredient? (y/n) ")
    if ans1 == "y":
        Potions.append(Ingredients[index][0])
    print()
    print("----------------------------------------")
    print("         SELECTED INGREDIENTS")
    print("----------------------------------------")
    for i in range(len(Potions)):
        print(f"{i+1}.{Potions[i]}")
    print()
for Recipe in Recipes:
    if Potions[0] == Recipe[0] and Potions[1]== Recipe[1]:
        Created_potion = Recipe[2]
        print(Created_potion)
        break
    