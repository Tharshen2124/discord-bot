import random

def welcomeMessage():
    message = [
        "It seems that you aren't coming tonight, thats a bummer. Hope you can make it for the next meet!",
        "Damnnn, it would have been more fun if you were coming. Welp, its alright. Hope you can join us next time!",
    ]
    
    num = random.randint(0,1)
    return message[num]
    
def startMessage():
    message = [
        "Yoooo ",
        "Heyyy ",
        "Wassup ",
        "HALLOO ",
    ]
    
    num = random.randint(0,3)
    return message[num]