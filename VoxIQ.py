import speech_recognition as sr
import os
import wikipedia
import pyttsx3
import random
from datetime import datetime
import time
import webbrowser as wb
import pywhatkit as pykt
from tqdm import tqdm


engine = pyttsx3.init("sapi5") # Microsoft Speech API (SAPI5) is the technology for voice recognition and
                               # synthesis provided by Microsoft.

voice = engine.getProperty('voices') # Gets the current value of a property.
engine.setProperty("voice", voice[1].id) # Adds a property value to set to the event queue.

rate = engine.getProperty("rate") # Gets the current value of a property.
engine.setProperty("rate", 140) # Adds a property value to set to the event queue.

rec = sr.Recognizer()


def speak(audio):
    engine.say(audio) #  say - Adds an utterance to speak to the event queue.
    engine.runAndWait()


def pbar():
    bar = tqdm(total =  100)
    for i in range(10):
        time.sleep(0.08)
        bar.update(10)
    bar.close()
    time.sleep(1)


def wish():
    time = int(datetime.now().hour)
    if time >=0 and time <=12 :
        print("->Hey! Good Morning,I'm VoxIQ, How May I Help You")
        speak("Hey! Good Morning!,I'm VoxIQ, How May I Help You")
    elif time >12 and time<=18:
        print("->Hey! Good Afternoon!,I'm VoxIQ, How May I Help You")
        speak("hey! Good Afternoon!,I'm VoxIQ, how may i help you")
    elif time >18 and time <24:
        print("->Hey! Good Evening!,I'm VoxIQ, How May I Help You")
        speak("hey! Good Evening!,I'm VoxIQ, How May I Help You")


def command_input():
    with sr.Microphone() as source:
        print("listening.....")
        rec.pause_threshold = 3
        audio = rec.listen(source, timeout=5, phrase_time_limit=5)
    try:
        query = rec.recognize_google(audio, language="en-IN").lower()
        if not query.strip():  # Check if the recognized query is empty after stripping whitespace
            print("->Say that again please")
            speak("Say that again please")
            return command_input()  # Ask the user to repeat themselves
        else:
            print("\t\t\t\t" + query.title() + "<--\n")
            return query
    except sr.UnknownValueError:
        print("->Say that again please")
        speak("Say that again please")
        return command_input()  # Ask the user to repeat themselves
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        speak("There was an error with the speech recognition service. Please try again later.")
        return None


def gettym():
    curtym = datetime.now()
    tym_now = curtym.strftime("%H:%M")

    ln = len(tym_now)
    tym = ""
    for i in range(ln):
        if i != 2:
            tym = tym + tym_now[i]
    global h
    h = tym[0:2]
    global m
    m = tym[2:4]


def tym_to_wrds(h,m):
    tymdict = {1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine",10:"ten",11:"eleven",12:"twelve",13:"thirteen",14:"fourteen",15:"fifteen",16:"sixteen",17:"seventeen",18:"eighteen",19:"nineteen",20:"twenty",21:"twenty one",22:"twenty two",23:"twenty three",24:"twenty four",25:"twenty five",26:"twenty six",27:"twenty seven",28:"twenty eight",29:"twenty nine"}

    if h > 12:
        h = h - 12
    if m == 0:
        print("It's "+tymdict[h]+" o'clock")
        speak("It's "+tymdict[h]+" o'clock")

    elif m == 30:
        print("->It's half past "+tymdict[h])
        speak("It's half past "+tymdict[h])
    elif m == 1:
        print("->It's one minutes past "+tymdict[h])
        speak("It's one minutes past "+tymdict[h])
    elif 1 < m < 30:
        print("->It's "+tymdict[m]+" minutes past "+tymdict[h])
        speak("It's "+tymdict[m]+" minutes past "+tymdict[h])
    else:
        h += 1
        m = 60 -m
        print("->It's "+tymdict[m]+" minutes to "+tymdict[h])
        speak("It's "+tymdict[m]+" minutes to "+tymdict[h])

def timer(duratn):
    if "hours" in query or "hour" in query:
        tym_sec = duratn*60*60
        for i in range(0,tym_sec,1):
            time.sleep(1)
            if i//60==1:
                print(str(i//60)+"Hour\n")
            elif i//60>1:
                print(str(i//60)+"hours\n")
            elif i == tym_sec:
                print("->Time Up!")
                speak("Time Up!")
            else:
                continue
    elif "minutes" in query or "minute" in query:
        tym_sec = duratn*60
        for i in range(0,tym_sec+1,1):
            time.sleep(1)
            if duratn == 1:
                if tym_sec == 1:
                    print(str(i), end=" ")
                else:
                    print(str(i), end=" ")
                if i == 30:
                    print("Half Time!")
                elif i == 60:
                    speak("Time Up!")
                    print("Time Up!")
            else:
                if i == tym_sec//2:
                    print("Half TIme Left!")
                if i//60==1:
                    print(str(i)+"minute")
                elif i//60>1:
                    print(str(i)+"minutes")
                elif i == tym_sec:
                    print("Time Up!")

    elif "seconds" in query:
        for i in range(duratn,0,-1):
            time.sleep(1)
            print(i)
            if i == duratn // 2:
                print("->Time Left : " + str(i) + " Seconds")
            elif i == 0:
                print("->Time Up!")
                speak("->Time Up!")
            else:
                continue

def get_directions(query):
    destination = query  # You can update this variable based on user input
    destination = destination.replace(" ", "+")  # Replace spaces with plus signs for URL
    url = f"https://www.google.com/maps/dir/?api=1&destination={destination}"
    wb.open(url, new=2)


def play_music():
    path = r"C:\Users\suyas\Desktop\Everything\Files And Floders\CODING\VoxIQ\songs"
    songlst = os.listdir(path)
    song = random.choice(songlst)
    speak("playing music")
    print("->Playing Now : " + song)
    os.startfile("C:\\Users\\suyas\\Desktop\\Everything\\Files And Floders\\CODING\\VoxIQ\\songs\\" + song)  # change the path according to your pc


def opentxt():
    txtnme = query.lstrip("open")
    txtnm = txtnme.lstrip(" ")
    txt = txtnm.rstrip("text file")
    fle = txt + ".txt"

    path = "C:\\Users\\suyas\\Desktop\\Everything\\Files And Floders\\CODING\\VoxIQ\\" + txt + ".txt"
    path_ = "C:\\Users\\suyas\\Desktop\\Everything\\Files And Floders\\CODING\\VoxIQ\\"
    files = os.listdir(path_)

    if fle in files:
        with open(path,"r") as file:
            red = file.readlines()
            print(fle + " Reads :-")
            speak(fle + " Reads :-")
            for i in red:
                print(i)
                speak(i)
    else:
        print(fle + " Dosen't Exists")
        speak(fle + " Dosen't Exists")

def joinclass():
    link_zoom_eng="https://zoom.us/j/96655371661?pwd=UTR5Vk5YR09OSTZHUlVsZlp1bFE3dz09"
    link_zoom_maths="https://zoom.us/j/96655371661?pwd=UTR5Vk5YR09OSTZHUlVsZlp1bFE3dz09"
    link_zoom_chem="https://zoom.us/j/96655371661?pwd=UTR5Vk5YR09OSTZHUlVsZlp1bFE3dz09" 
    link_zoom_phy="https://zoom.us/j/96655371661?pwd=UTR5Vk5YR09OSTZHUlVsZlp1bFE3dz09"
    link_zoom_cs="https://zoom.us/j/96655371661?pwd=UTR5Vk5YR09OSTZHUlVsZlp1bFE3dz09"
    link_meet_cs="https://meet.google.com/fns-vnqj-hch?authuser=2&hs=179"
    link_meet_phy="https://meet.google.com/fns-vnqj-hch?authuser=2&hs=179"
    link_meet_chem="https://meet.google.com/fns-vnqj-hch?authuser=2&hs=179"
    link_meet_maths="https://meet.google.com/fns-vnqj-hch?authuser=2&hs=179"
    link_meet_eng="https://meet.google.com/fns-vnqj-hch?authuser=2&hs=179"
    
    if "english" in query:
        if "zoom" in query:
            lnk = link_zoom_eng 
            speak("Opening Zoom!")
            print("Opening Zoom!")
            wb.open(lnk, new=2)

        elif "google meet" in query or "meet" in query:
            lnk = link_meet_eng
            speak("Opening Google Meet!")
            print("Opening Google Meet!")
            wb.open(lnk, new=2)

    elif "maths" in query:
        if "zoom" in query:
            lnk = link_zoom_maths  
            speak("Opening Zoom!")
            print("Opening Zoom!")
            wb.open(lnk, new=2)

        elif "google meet" in query or "meet" in query:
            lnk = link_meet_maths 
            speak("Opening Google Meet!")
            print("Opening Google Meet!")
            wb.open(lnk, new=2)

    elif "chemistry" in query:
        if "zoom" in query:
            lnk = link_zoom_chem  
            speak("Opening Zoom!")
            print("Opening Zoom!")
            wb.open(lnk, new=2)

        elif "google meet" in query or "meet" in query:
            lnk = link_meet_chem 
            speak("Opening Google Meet!")
            print("Opening Google Meet!")
            wb.open(lnk, new=2)

    elif "physics" in query:
        if "zoom" in query:
            lnk = link_zoom_phy 
            speak("Opening Zoom!")
            print("Opening Zoom!")
            wb.open(lnk, new=2)

        elif "google meet" in query or "meet" in query:
            lnk =  link_meet_phy 
            speak("Opening Google Meet!")
            print("Opening Google Meet!")
            wb.open(lnk, new=2)

    elif "cs" in query or "computer science" in query:
        if "zoom" in query:
            lnk =  link_zoom_cs
            speak("Opening Zoom!")
            print("Opening Zoom!")
            wb.open(lnk, new=2)

        elif "google meet" in query or "meet" in query:
            lnk =  link_meet_cs
            speak("Opening Google Meet!")
            print("Opening Google Meet!")
            wb.open(lnk, new=2)

print("\t\t\t\t\t\tWELCOME! This is VoxIQ.\n\t\t\t\t\t Your Virtual Desktop Assistant")
time.sleep(1)
ch = input("Press Enter To Start : ")

print("Starting........")
time.sleep(0.7)
print("Getting VoxIQ ready.....")
time.sleep(2)
pbar()
wish()

flag = False

while True:
    if not flag:    
        query = command_input()

    if "navigate to" in query:
        flag = True
        print("->Opening Google Maps")
        speak("Opening Google Maps")
        destination = query.replace("navigate to", "").strip()
        get_directions(destination)
        input("Press Enter to continue after you close the Browser Window...")
        flag = False
        continue

    elif "hi" in query or "hello" in query:
        hi_output = ["Hi!", "Hey There!", "Hello", "Hi there! How are you?"]
        choice = random.choice(hi_output)
        print("->",choice)
        speak(choice)
        if choice == "Hi there! How are you?":
            answr = command_input()
            positive_reply = ["i am good", "i am fine", "i am great", "good", "fine", "great"]
            if answr in positive_reply:
                print("->Good To Hear That")
                speak("good to hear that")

            else:
                print("->Sorry To Hear That!")
                speak("Sorry To Hear That!")
        continue

    elif 'wikipedia' in query:
        print("->Searching Wikipedia.....")
        speak('Searching Wikipedia')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2, auto_suggest=True)
        speak("->According to Wikipedia")
        print(results)
        speak(results)
        continue

    elif "text file" in query:
        opentxt()
        continue

    elif "open" in query:
        flag = True
        subject = query.strip("open")
        pykt.search(subject)
        input("Press Enter to continue after you close the Browser Window...")
        flag = False
        continue

    elif "youtube" in query:
        flag = True
        print("->Searching Youtube!")
        speak("searching youtube")
        subjectlst = query.split(" ")
        subject = ""
        for i in subjectlst:
            if i == "search":
                continue
            elif i == "youtube":
                continue
            elif i == "for":
                continue
            else:
                subject += str(i)
                subject += " "

        link = "https://www.youtube.com/results?search_query=" + subject
        wb.open(link, new=2, autoraise=True)
        input("Press Enter to continue after you close the Browser Window...")
        flag = False
        continue

    elif "timer" in query:
        subjectlst = query.split(" ")
        subjectstr = str(subjectlst)
        digit = ""

        for i in subjectstr:
            if i.isdigit():
                digit += i
            else:
                continue
        digit = int(digit)
        if "seconds" in query:
            print("->Setting Timer For " + str(digit) + " seconds")
            speak("Setting Timer For " + str(digit) + " seconds")
        elif "hour" in query or "hours" in query:
            if digit == 1:
                print("->Setting Timer For " + str(digit) + " hour")
                speak("Setting Timer For " + str(digit) + " hour")
            else:
                print("->Setting Timer For " + str(digit) + " hours")
                speak("Setting Timer For " + str(digit) + " hours")
        elif "Minute" in query or "Minutes" in query:
            if digit == 1:
                print("->Setting Timer For " + str(digit) + " Minute")
                speak("Setting Timer For " + str(digit) + " Minute")
            else:
                print("->Setting Timer For " + str(digit) + " Minutes")
                speak("Setting Timer For " + str(digit) + " Minutes")
        timer(digit)
        continue

    elif "time" in query:
        gettym()
        tym_to_wrds(int(h), int(m))
        continue

    elif "class" in query:
        flag = True
        joinclass()
        input("Press Enter to continue after you close the Browser Window...")
        flag = False
        continue

    elif "what" in query or "how" in query or "tell me about" in query:
        flag = True
        if "tell me about" in query:
            subjectlst = query.split(" ")
            print(subjectlst)
            subject = ""
            for i in subjectlst:
                if i == "tell":
                    continue
                elif i == "me":
                    continue
                elif i == "about":
                    continue
                else:
                    subject += str(i)
                    subject += " "
            speak("searching for " + subject + " ......")
            time.sleep(1)
            pykt.search(subject)

        else:
            speak("searching for " + query + " ......")
            time.sleep(1)
            pykt.search(query)
        input("Press Enter to continue after you close the Browser Window...")
        flag = False
        continue

    elif "bye" in query or "exit" in query or "quit" in query:
        print("->Bye!, Have A Good Day")
        speak("Bye!, Have A Good Day")
        break

    elif "play music" in query or "play songs" in query or "play song":
        flag = True
        play_music()
        input("Press Enter to continue after you close the music player...")
        flag = False
        continue

    else:
        flag = True
        print("Searching For " + query)
        speak("Searching For " + query)
        pykt.search(query)
        input("Press Enter to continue after you close the Browser Window...")
        flag = False
        
