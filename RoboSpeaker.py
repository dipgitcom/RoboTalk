import pyttsx3



if __name__=="__main__" :
    print("Welcome to RoboSpeaker , created by Professor ")
    engine = pyttsx3.init()
    while True :
        enter = input("What would you like me to speak : ")
        if enter == "exit" :
            engine.say("Goodbye my dear Friend")
            engine.runAndWait()
            break
        engine.say(enter)
        engine.runAndWait()    