#Based on the corrected code from Task 1, 
# further enhance your code to recommend additional things like "audio system" or "projector" 



attendees =(int)(input("Enter number of attendees:"))
venue = "large hall" if attendees > 100 else "conference room"
print(venue + " with audio system" if attendees > 50 else venue + " with projector")
      