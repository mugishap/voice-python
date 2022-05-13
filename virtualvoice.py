import pyttsx3 

friend = pyttsx3.init()
voices =friend.getProperty('voices')
friend.setProperty('rate',150)
friend.setProperty('voice',voices[2].id)
friend.say("Hello Kevin. Have you sent the file" )
friend.runAndWait()
friend.stop()