import pyttsx3
engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
engine.setProperty("rate",150)
engine.say("I will speak this text")
engine.runAndWait()