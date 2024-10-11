#If the user makes an invalid choice at any point, incorporate a pass statement to handle it. 
# HINT: How can an else statement be of use here?

place = input("Choose a place: forest or cave? ")
if place == "forest":
    action = input("climb a tree or cross a river?")
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
    else:
        pass
    print("self destruct mode initiated!")      
        #i wasnt sure if we could only use a pass statement once or as many times as we wanted

else:
    pass
    print("self destruct mode initiated!")