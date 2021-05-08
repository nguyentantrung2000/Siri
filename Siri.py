import speech_recognition
import gtts  # noi
import os  # doc ghi file
import pyttsx3
from datetime import date, datetime  # ngaygio


# Listening
robot_ear = speech_recognition.Recognizer()
robot_mouth = pyttsx3.init()
robot_brain = ""
with speech_recognition.Microphone() as mic:
        print("AI Listening:")
        audio =robot_ear.record(mic, duration=3)  # sau 5s sẽ tự động đóng mic
print("\n AI:.... ")
try:
        you = robot_ear.recognize_google(audio, language=" ")
        print("\n User: " + you)
except:
        you = ""
print("You " + you)

    # Understand
if you == "":
        robot_brain = "Try again please ..."
elif you == "hello":
        robot_brain = "Hi Trung"
elif you == "how" in you:
        robot_brain = "You look so good today"
elif "today" in you:
        today = date.today()
        robot_brain = today.strftime("%B %d, %Y")
elif "time" in you:
        now = datetime.now()
        robot_brain = today.strftime("%H Hours %M minutes %S Seconds")
elif "bye" in you:
        robot_brain = "Bye Trung"
        robot_mouth = pyttsx3.init()
        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()
else:
        robot_brain = "Thanks!"
print("\n AI:" + robot_brain)

# Talking
print("AI: " +robot_brain)
robot_mouth.say(robot_brain)
robot_mouth.runAndWait()
