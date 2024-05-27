import os
import random
import datetime
import smtplib
import speech_recognition as sr
import pyttsx3
import wikipedia
import webbrowser
import sys
import subprocess

# Initialize the text-to-speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Set voice (index 1 for female voice)

# Set the volume level (0.0 to 1.0)
engine.setProperty('volume', 1.0)  # Set volume to maximum (1.0)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good morning! Akash")
    elif 12 <= hour < 18:
        speak("Good afternoon! Akash")
    else:
        speak("Good evening! Akash")
    speak('I am Siya. Please tell me how may I help you')

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=2)  # Adjust for ambient noise for 2 seconds
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio)
        print(f"User said: {query}")
        return query.lower()
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that. Please repeat.")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return ""

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('pandey4921@gmail.com', 'kmir hviy nxqi auqv')
    
    for recipient_email in to:
        if recipient_email:  # Check if the recipient is not an empty string
            server.sendmail('pandey4921@gmail.com', recipient_email, content)
            print(f"Email sent to {recipient_email}")
    
    server.close()

if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia...")
            print(results)
            speak(results)
        
        elif 'open youtube' in query:
            webbrowser.open('https://youtube.com')

        elif 'open google' in query:
            webbrowser.open('https://google.com')

        elif 'open st' in query:
            webbrowser.open("stackoverflow.com")

        elif 'open chat gpt' in query or 'open chatgpt' in query:
            webbrowser.open('https://chatgpt.com')
        
        elif 'play music' in query:
            music_dir = 'C:\\Users\\akash pandey\\Desktop\\Akash photos\\audio'
            songs = os.listdir(music_dir)
            random_song_index = random.randint(0, len(songs)-1)
            os.startfile(os.path.join(music_dir, songs[random_song_index]))

        elif 'what is the time' in query:
           strtime = datetime.datetime.now().strftime("%I:%M %p")
           speak(f"Akash, the time is {strtime}")
        
        elif 'open vs code' in query:
            codepath = '"C:\\Users\\akash pandey\\AppData\Local\\Programs\\Microsoft VS Code\\Code.exe"'
            os.startfile(codepath)

        elif 'open whatsapp' in query:
            webbrowser.open('https://web.whatsapp.com')

        elif 'open instagram' in query:
            webbrowser.open('https://www.instagram.com')

        elif 'open pyc' in query:
            pycharm_shortcut_path = r"C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\pycharm IDE\\PyCharm Community Edition 2022.3.lnk"
            if os.path.exists(pycharm_shortcut_path):
                os.startfile(pycharm_shortcut_path)
            else:
                speak("I could not find the PyCharm shortcut. Please check the path.")

        elif 'open cmd' in query:
             cmdpath = os.path.join(os.environ["windir"], "system32", "cmd.exe")
             os.startfile(cmdpath)

        elif 'open code' in query:
            codePath = "C:\\Users\\akash pandey\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'sql' in query:
            sqlplus_shortcut_path = r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Oracle - OraDB19Home1\Application Development\SQL Plus.lnk"
            if os.path.exists(sqlplus_shortcut_path):
                os.startfile(sqlplus_shortcut_path)
            else:
                speak("I could not find the SQL*Plus shortcut. Please check the path.")

        elif 'open j note' in query:
            import subprocess
            import os
    
             # Expand the %USERPROFILE% environment variable to get the user's profile directory
            user_profile = os.path.expanduser('~')
    
            notebook_command = [
        r"C:\ProgramData\anaconda3\python.exe",
        r"C:\ProgramData\anaconda3\cwp.py",
        r"C:\ProgramData\anaconda3",
        r"C:\ProgramData\anaconda3\python.exe",
        r"C:\ProgramData\anaconda3\Scripts\jupyter-notebook-script.py",
            user_profile  # Use the expanded user profile directory
    ]
    
            subprocess.run(notebook_command)

        elif 'send mail' in query:
            try:
               speak("Who do you want to send the email to?")
               recipient = takeCommand().strip().lower()  # Get recipient's name from user input

               if "a p" in recipient:
                  to = ['makashpandey@gmail.com']
               elif "abhishek rai" in recipient:
                  to = ['abhishekrai3355@gmail.com']
               else:
                  speak("Sorry, I didn't recognize the recipient.")
                  continue

               speak("What should I write in the email?")
               content = takeCommand()
               sendEmail(to, content)
               speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak('Sorry, I am not able to send this email.')

        elif "exit" in query:
            speak("Goodbye, Akash! If you need anything else, feel free to ask.")
            sys.exit()
