import time
count=0
i=0
while i<=10:

        print("At first the agent is in tiles A ")
        print("In which tiles is the agent want to move? (A/B)")
        state = input("the agent want to move tiles ")
        state = count
        count=count+1
        if state == "A":
            print("The agent is already in tiles A ")
        elif (state!=1):
            print("The agent is already in tiles B ")
        print("is the tiles is dirty? ")
        answer = input("Enter yes or no : ") 
        if answer == "yes":
              print("The agent is cleaning the tiles.") 
        elif answer == "no": 
            print("The tiles is already clean. No need for further cleaning.") 
        time.sleep(5)