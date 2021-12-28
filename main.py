import pyttsx3

speaker = pyttsx3.init()
speaker.setProperty('rate', 150)
voice = speaker.getProperty("voices")
speaker.setProperty('voice', voice[1].id)

run = True

speaker.say("Welcome to Text to Speech.")
speaker.runAndWait()
speaker.say("Type the word stop to end the process.")
speaker.runAndWait()

while run:
    a = input("Type/paste the text to dictate : ")
    print()
    print()

    if a.lower() == "stop":
        run = False
    else:
        speaker.say(a)
        speaker.runAndWait()
