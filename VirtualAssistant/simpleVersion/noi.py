print("noi")

'''text to speech'''

robot_brain	= "Hello"

import pyttsx3
robot_mounth = pyttsx3.init()
robot_mounth.say(robot_brain)
robot_mounth.runAndWait()

