# Voice-assistant    :microphone:

#### A program which takes a request from a user and responds through speech or performs the task.
### Technology Used:
This project was created using Python. 

To run this program, I had to install multiple Python libraries:
- pttsx3 (text-to-speech)
- speech_recognition
- pywhatkit (internet search)
- pyjokes (tells jokes)
- webbrowser (opens web browsers)
- datetime (provides current date and time)
- wikipedia (wikipedia search)
- pyaudio (microphone access)
- python_weather (provides current weather)
- asyncio (needed for python_weather)
- os (needed for python-weather)

### Process: 
I followed a tutorial from a Udemy Python course to create this project. I started by installing the libraries to my laptop using Terminal. Next, I used the tutorial to help me set up the main structure of the program. When I was able to sucessfully run the program, I went back and added some changes, personal touches, and extra features. I changed how the day of the week was displayed, and some other small technical features. I also added the weather and date feature after doing some research on those libraries. I had some trouble setting up the pyaudio and pttsx3 libraries. Pyaudio was supposed to be imported as a part of the speech_recognition library but it did not work so I had to import it separately. I wasn't able to import it using just "pip3 install pyaudio" so I had to do some research and found that I needed to download it using homebrew which worked for me. I also had an error with pttsx3 importing incorrectly on my mac. I tried different solutions to fix the issue but I still was not able to. I beleive the issue was with the version of python on my Mac being uncompatible with the versions the library was made for. Pttsx3 is an older library which hasn't been updated since 2020. As a solution, I decided to complete the rest of the project on my backup windows laptop and was able to sucessfully finish. Overall, this was my favorite Python project so far even with all of the issues I faced. 
