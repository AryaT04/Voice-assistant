# A program that takes a request from a user and responds
# through speech and/or performs a task. 

import pyttsx3
import speech_recognition as sr
import pywhatkit
import pyjokes
import webbrowser
import datetime
import wikipedia
import pyaudio
import python_weather
import asyncio
import os

# a function that listens from the microphone and returns the audio as a test

def audioToText():

    # store recognizer in variable

    r = sr.Recognizer()

    #set microphone 

    with sr.Microphone() as source:

        # wait some time before starting to listen 
        
        r.pause_threshold = 0.8

        # notify user that recording has begun

        print("Listening...")

        # save what was heard as audio

        audio = r.listen(source)

        try:
            # search on goole 

            request = r.recognize_google(audio, language = "en-US")

            # test in text 

            print("You said: " + request)

            #return request 

            return request
        
        # program can't understand audio

        except sr.UnknownValueError:
            print("I do not understand the audio.")

            #return error

            return("")
        
        # program can't resolve request 

        except sr.RequestError:
            print("I cannot resove this request.")

            #return error

            return("")

        # unexpected error

        except:
            print("Something went wrong.")

            #return error

            return("")
        
# a function for the assistant to speak

def speak(message):

    # start engine of pyttsx3

    engine = pyttsx3.init()

    # choose voice

    voiceId='HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'
    engine.setProperty('voice',voiceId)

    # deliver message 

    engine.say(message)
    engine.runAndWait()
    
# a function that returns today's weather
    
async def getweather(city):
    async with python_weather.Client(unit=python_weather.IMPERIAL) as client:
        weather = await client.get(str(city))
        speak(f"It is {weather.temperature} degrees Farenheit and {weather.description} today.")


# a function that returns today's date 

def askDate():

    # today's date

    dateVal = str(datetime.date.today())
    

    dateList = dateVal.split("-")
    year = dateList[0]
    monthNum = int(dateList[1].replace('0', ''))
    day = dateList[2].replace('0', '')
    months = {1: "January",
              2: "February",
              3: "March",
              4: "April",
              5: "May",
              6: "June",
              7: "July",
              8: "August",
              9: "September",
              10: "October",
              11: "November",
              12: "December"
              }
    
    speak(f"It is {months[monthNum]} {day} {year}")


# a function that returns the day of the week

def askDay():

    # today's date

    day = datetime.date.today()
    

    # today's day of the week 

    weekDay = day.weekday()
    

    # Names of days 

    calendar = {0: 'Monday',
                1: 'Tuesday',
                2: 'Wednesday',
                3: 'Thursday',
                4: 'Friday',
                5: 'Saturday',
                6: 'Sunday'}
    
    # say the day of thw week

    speak(f"Today is {calendar[weekDay]}")

# a function that return the current time 
    
def askTime():
   
    # time info
    
    time = datetime.datetime.now()
    if time.hour >= 12:
        hour = time.hour - 12
        realTime = f"It is {hour} {time.minute} p.m."
        
    else:
        realTime = f"It is {hour} {time.minute} a.m."
    
    # say time 
    speak(realTime)

# greeeting

def greeting():

    speak("Hello I am Nexus, your personal voice assistant. How may I help you?")

def mainLoop():

    # greet User
    
    greeting()

    # loop break variable

    goAgain = True

    #main loop
    

    while goAgain:

        # listen to user and save request

        request = audioToText().lower()

        if 'open youtube' in request:
            speak('Sure. Opening youtube.')
            webbrowser.open('https://www.youtube.com')
            continue
        elif 'open google' in request:
            speak('On it!')
            webbrowser.open('https://www.google.com')
            continue
        elif 'what day of the week is it today' in request:
            askDay()
            continue
        elif "what is today's date" in request:
            askDate()
            continue
        elif 'time' in request:
            askTime()
            continue
        elif 'weather' in request:
            request = request.replace("what is the weather today in", '')
            asyncio.run(getweather(request))
            continue

        elif 'play' and "on youtube" in request:
            request = request.replace("can you play", '')
            request = request.replace("on youtube", '')
            speak(f"playing {request} on youtube.")
            pywhatkit.playonyt(request)
            continue
        elif "do a wikipedia search" in request:
            speak("I am looking...")
            request = request.replace('can you do a wikipedia search for', '')
            answer = wikipedia.summary(request, sentences = 1)
            speak("According to wikipedia.com, ")
            speak(answer)
            continue
        elif "search the internet" in request:
            speak("searching...")
            request = request.replace('can you search the internet for', '')
            pywhatkit.search(request)
            speak("here is what I found")
            continue
        elif "joke" in request:
            speak(pyjokes.get_joke())
            continue
        elif 'goodbye' in request:
            speak("Goodbye!   ")
            break
    
       

# needed for weather library
if __name__ == '__main__':
    if os.name == 'nt':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())



mainLoop()



