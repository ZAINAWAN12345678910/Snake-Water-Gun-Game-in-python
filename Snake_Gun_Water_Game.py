import random
print("\t\t\t******Welcome to Snake-Water_Gun Game******")
def SWG():
    print("Choose One from the Following Options")
    print("S = Snake \nW = Water \nG = Gun")
    choice = input("Enter you choice = ")
    list = ["S" , "W" , "G"]
    random_choice = random.choice(list)
    print("Computer Choice = ",random_choice)
    #Snake combination
    if choice==("S" or "s") and random_choice==("S" or "s"):
        print(" ******* Your game is Draw ******* ")
    elif choice==("S" or "s") and random_choice==("W" or "w"):
        print(" ******* you are win ******* ")
    elif choice==("S" or "s") and random_choice==("G" or "g"):
        print(" ******* you are loss ******* ")
    #Water Combination
    elif choice==("W" or "w") and random_choice==("S" or "s"):
        print(" ******* you are loss ******* ")
    elif choice==("W" or "w") and random_choice==("W" or "w"):
        print(" ******* Your Game is Draw ******* ")
    elif choice==("W" or "w") and random_choice==("G" or "g"):
        print(" ******* You are win ******* ")

    #Gun Combination
    elif choice==("G" or "g") and random_choice==("S" or "s"):
        print(" ******* You are win ******* ")
    elif choice==("G" or "g") and random_choice==("W" or "w"):
        print(" ******* You are loss ******* ")
    elif choice==("G" or "g") and random_choice==("G" or "g"):
        print(" ******* Your game is draw ******* ")

    #Otherwise for wrong input
    else:
        print(" ******* Your input is wrong ******* ")
        SWG()

SWG()











