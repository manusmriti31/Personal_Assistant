import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import time
import webbrowser
import os
import openai
import sys

chatStr = ""
def chat(command):
    global chatStr
    print(chatStr)
    openai.api_key = "API-KEY"
    chatStr += f"Manu: {command}\nJarvis: "
    response = openai.Completion.create(
        model="gpt-3.5-turbo",
        prompt= chatStr,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # todo: Wrap this inside of a  try catch block
    say(response["choices"][0]["text"])
    chatStr += f"{response['choices'][0]['text']}\n"
    return response["choices"][0]["text"]


def say(text):
    engine = pyttsx3.init()
    a = engine.setProperty('rate',250)
    engine.say(text)
    engine.runAndWait()
    
def Wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        say("Good Morning sir")
    elif hour >= 12 and hour < 17:
        say("Good afternoon sir")
    else:
        say("Good Evining sir")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

        try:
            print("Recognizing....")
            query = r.recognize_google(audio, language = 'en-in')
            print(f"The user said: {query}")
        except Exception as e:
            print("Say again Please...")
            return "None"
        return query
    
def wikipedia_fun():
    say("Searching wikipedia.....")
    global command
    command = command.replace("wikipedia", "")
    results = wikipedia.summary(command, sentences = 2)
    say("According to Wikipedia")
    print(results)
    say(results)

def website():
    global command
    #Make it more automated 
    l1 = command.split()
    try:
        index = l1.index("website")
        say(f"opening {l1[index + 1]}")
        print(f"opening {l1[index + 1]}")
        l1[index + 1] = l1[index + 1] + ".com"
        webbrowser.open(l1[index+1])
    except:
        say("Sorry Please try again")
        print("Sorry Please try again")
        
def Open_app():
    global command
    l2 = {'photoshop':r"C:\Program Files\Adobe\Adobe Photoshop 2021\Photoshop.exe",
          'vs code':r"C:\Users\MANU\Desktop\Visual Studio Code.lnk",
          'chrome':r"C:\Users\Public\Desktop\Google Chrome.lnk",
          'study':r"C:\Users\MANU\Desktop\Course"}
    l3 = command.split()
    index = l3.index("app")
    app_name = l3[index + 1]
    app_path = l2[app_name]
    try:
        webbrowser.open(app_path)
        #os.startfile(app_path)
    except:
        say("App not in the directory")
        print("App not in the directory")



if __name__ == "__main__":
    say("Hello I am Jarvis A I")
    Wishme()
    say("How may I assist you today")
    global command
    while True:
        command = takeCommand().lower()

        if "wikipedia" in command:
            wikipedia_fun()
        elif "open website" in command:
            website()
        elif "the time" in command:
            time_now = datetime.datetime.now().strftime("%H:%M:%S")
            say(f"Sir the time is {time_now}")
        elif "play music" in command:
            say("Opening Spotify....")
            os.startfile("spotify")
        elif "app" in command:
            #os.startfile("Photoshop.exe")
            Open_app()
        elif "exit" == command:
            say("Good by sir")
            sys.exit()
        elif "clear chat" in command:
            chatStr = ""
        else:
            chat(command)
        



