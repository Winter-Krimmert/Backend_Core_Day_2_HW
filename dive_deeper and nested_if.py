#  Lesson 1 Dive_Deeper
# Decisions at the Crossroad

number = int(input("Enter a number: "))

if number > 0:
    print("The number is positive.")
elif number == 0:
    print("The number is zero.")
else:
    print("The number is negative.")


# The Greatest Showdown
print("Please input 3 numbers.")
num_1 = int(input("please input a number (from 1 to 10). "))
num_2 = int(input("please input a number (from 1 to 10). "))
num_3 = int(input("please input a number (from 1 to 10). "))

if num_3 > num_1 < num_2:
    print(f"{num_1} is the smallest.")

elif num_3 >= num_2 <= num_1:
        print(f"{num_2} is the smallest.")
else:
    print(f"{num_3} is the smallest.")

if num_3 <= num_1 >= num_2:
    print(f"{num_1} is the largest.")

elif num_3 <= num_2 >= num_1:
    print(f"{num_2} is the largest.")
else:
    print(f"{num_3} is the largest.")

    # Lesson 2 Nested_If

    # The Adventure Game

place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river? ")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == ("cross a river"):
        print("You found a boat!")
elif place == "cave":
    print("You find a hidden treasure!")


    # task 2 and task 3
place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river? ")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == ("cross a river"):
        print("You found a boat!")
    else:
        pass
elif place == "cave":
    action = input("Light a torch or proceed in the dark? ")
    if action == "Light a torch":
        print("May you find your way.")
    elif action == ("proceed in the dark"):
        print("it might be slightly harder to see in a dark cave.")
    else:
        pass


# The Event Planner

attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
print(venue)

# Task 2

attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
if attendees > 100:
    
    additional_facilities = input("Would you like a sound system or projector? ")
    
    if additional_facilities == "sound system":
        print(f" {venue} with sound system.")
    elif additional_facilities ==" projector":
        print(f"{venue} with a projector.")
    elif additional_facilities == "sound system and projector":
        print(f"{venue} with a sound system and prjector.")
    elif additional_facilities == "both":
        print(f"{venue} with a sound system and projector.")
    else:
        pass
elif attendees < 100:
    additional_facilities = input("Would you like a sound system or projector? ")
        
    if additional_facilities == "sound system":
        print(f" {venue} with sound system.")
    elif additional_facilities =="projector":
        print(f"{venue} with a projector.")
    elif additional_facilities == "sound system and projector":
        print(f"{venue} with a sound system and projector.")
    elif additional_facilities == "no":
        print(f"{venue} without additional facilities.")
    elif additional_facilities == "both":
        print(f"{venue} with a sound system and projector.")
    else:
        pass

else:
    pass

# Catering Choices
print("Catering Choices")
vegeterian_food = input("Would you like vegetarian food? ")
if vegeterian_food == "yes":
    print("We recommend Veggie Delight Caterers.")
elif vegeterian_food == "no":
    print("We recommend Gourmet Meals Caterers.")
else:
    pass