#Ask the user if they want "vegetarian" food. 
# Recommend "Veggie Delight Caterers" if yes, 
# otherwise recommend "Gourmet Meals Caterers".



attendees =(int)(input("Enter number of attendees:"))
venue = "large hall" if attendees > 100 else "conference room"
print(venue + " with audio system" if attendees > 50 else venue + " with projector")
food_prep =input("do want vegetarian food? (yes/no)")
print("Veggie Delight Caterers" if food_prep == 'yes' else "Gourmet Meals Caterers")