import time

tiles = ""
while True:
    print("In which tiles is the agent want to move?")
    new_tiles = str(input())
    if tiles==new_tiles:
        print("The agent is already in tiles " + str(new_tiles))
    tiles = new_tiles
    print("Is the tiles dirty?")
    ans = str(input())
    if ans=="yes":
        print("The agent is cleaning the tiles")
    else:
        print("The tiles is already clean. No need for further cleaning.")
    time.sleep(5)