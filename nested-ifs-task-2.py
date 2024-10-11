#Task 2: Setting the Scene
#Based on your corrected code from Task 1, expand the game. 
# If the user chooses "cave", ask them if they want to "light a torch" or "proceed in the dark",
# and provide outcomes for each decision.

place = input("Choose a place: forest or cave? ")
action = input("climb a tree or cross a river?")

if place == "forest":
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
         print("You found a boat!")
if place == "cave":
    nite_lite =input("light a torch or proceed in darkness? ")
    if nite_lite == "light a torch":
        print("see the path! ")
    elif nite_lite == "proceed in darkness":
        print("watch your step! ")
        
        