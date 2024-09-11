import time
while (1):
        question = input("your question :\n ").lower()
        if question == "horn":
            print("give side")
        elif question == "braking light":
            print("stoping car")
        elif question == "object":
            print("slowinhg car") 
        elif question == "none":
            print("moving") 
        time.sleep(5)