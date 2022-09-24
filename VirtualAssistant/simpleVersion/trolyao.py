import speech_recognition
import pyttsx3
from datetime import date, datetime

robot_ear = speech_recognition.Recognizer()
robot_mounth = pyttsx3.init()
robot_brain = ""

while True:
	with speech_recognition.Microphone() as mic: 
		print("Robot: I'm listening")
		audio = robot_ear.listen(mic)

	print("Robot: ...")

	try:
		you = robot_ear.recognize_google(audio)
	except:
		you = ""

	print("You: " + you)

	if you == "":
		robot_brain = "I can't hear you, try again"
	elif "hi" in you:
		robot_brain = "Hello Dung"
	elif "today" in you:
		today = date.today()
		robot_brain = today.strftime("%B %d, %Y")
	elif "time" in you:
		now = datetime.now()
		robot_brain = now.strftime("%H hours %M minutes %S seconds")
	elif "bye" in you:
		robot_brain = "Good bye"
		robot_mounth.say(robot_brain)
		robot_mounth.runAndWait()
		break
	else:
		robot_brain	= "I'm fine thank you and you"

	print("Robot: " + robot_brain)

	robot_mounth.say(robot_brain)
	robot_mounth.runAndWait()

