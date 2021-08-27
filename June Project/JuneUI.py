import pyttsx3 #using pip install pyttsx3
import datetime
import speech_recognition as sr #using pip install speechRecognition
import wikipedia #using pip install wikipedia
import smtplib
import webbrowser as wb
import os
import os.path
import pyautogui # using pip install pyautogui
import calendar
import subprocess
import psutil #pip install psutil
import pyjokes # using pip install pyjokes
import playsound
import random
from requests import get
import pywhatkit as kit # using pip install pywhatkit
import sys
import requests
import msgpack # using pip install msgpack
import instaloader# using pip install instaloader
import PyPDF2 # using pip install PyPDF2
from bs4 import BeautifulSoup # using pip install bs4
import operator
import pywikihow # using pip install pywikihow
from pywikihow import search_wikihow
import speedtest
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from June import Ui_MainWindow



engine = pyttsx3.init()
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice', voices[2].id)
engine.runAndWait()


def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("the current time is")
    speak(Time)
    print(Time)


def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("the current date is")
    speak(date)
    speak(month)
    speak(year)


def wishme():
    hour = int(datetime.datetime.now().hour)
    tt = datetime.datetime.now().strftime("%I:%M %p")
    if hour >= 6 and hour <12:
        speak("Good Morning sir!")

    elif hour >=12 and hour <18:
        speak("Good Afternoon sir!")

    else:
        speak(f"Good Evening sir! it's {tt}")
    speak("June is at your service, please tell me how can i help you?")


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('rahulpandey04012001@gmail.com', '9992439195')
    server.sendmail('rahulpandey04012001@gmail.com', to, content)
    server.close()


def screenshot():
    img = pyautogui.screenshot()
    img.save("C:/Users/Asus/OneDrive/Desktop/June Picture/ss.png")


def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU is at" + usage)
    battery = psutil.sensors_battery()
    speak("Battery is at")
    speak(battery.percent)


def news():
    main_url = 'https://newsapi.org/v2/top-headlines?sources=techcrunch&apikey=7237502f4a7f4d7c97f77f6879fd3f9e'

    main_page = requests.get(main_url).json()
    articles = main_page["articles"]
    head = []
    day = ["first","second","third","fourth","fifth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range(len(day)):
        speak(f"todays {day[i]} news is: {head[i]}")


def pdf_reader():
    book = open('E:/Hacking Courses/Ashutosh Pratap Singh (Joker) - Hacking_ The Unlocking of Transparency Security is a myth… (2020).pdf', 'rb')
    pdfReader = PyPDF2.PdfFileReader(book)#using pip install PyPDF2
    pages = pdfReader.numPages
    speak(f"Total num pages in this book are {pages}")
    speak("sir please enter the page number you want me to read")
    pg = int(input("Please enter the page number: "))
    page = pdfReader.getPage(pg)
    text = page.extractText()
    speak(text)


def jokes():
    speak(pyjokes.get_joke())


class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()
    
    def run(self):
        # self.TaskExecution()
        speak("Please say wake up to continue...")
        while True:
            self.query = self.takeCommand()
            if "wake up" in self.query:
                self.TaskExecution()

    def TaskExecution(self):
        wishme()
        while True:
            self.query = self.takeCommand().lower()

            if 'time' in self.query:
                time()
            elif 'date' in self.query:
                date()


            #wikipedia searches
            elif 'wikipedia' in self.query:
                speak("Searching wikipedia")
                self.query = self.query.replace("wikipedia", "")
                result = wikipedia.summary(self.self.query, sentences=2)
                print(result)
                speak(result)

            #sending emails
            elif 'send email' in self.query:
                try:
                    speak("What Should i say sir?")
                    content = takeCommand()
                    speak("Whom should i send")
                    to = input("Enter the email address: ")
                    sendEmail(to, content)
                    speak("Email has been sent sir!")
                except Exception as e:
                    print(e)
                    speak("Unable to send the email sir...")
            #Whatsapp messages
            elif'send message' in self.query:
                    kit.sendwhatmsg("+919255473806","Hello dad",2,9)

            #opening chrome and Searching
            elif 'chrome' in self.query:
                speak("What should i search sir?")
                chromepath = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
                search = takeCommand().lower()
                speak(" opening chrome browser" + search)
                wb.get(chromepath).open_new_tab(search+'.com')

            elif 'search' in self.query:
                speak("What should i search sir?")
                search = takeCommand().lower()
                wb.open("https://www.google.com/search?q=" + search)
                speak(" opening chrome browser" + search)

            elif 'youtube' in self.query:
                wb.open("www.youtube.com")

            elif 'stack overflow' in self.query:
                    wb.open("www.stackoverflow.com")

            elif 'facebook' in self.query:
                wb.open("www.facebook.com")

            elif 'open instagram' in self.query:
                wb.open("www.instagram.com")

            elif 'gmail' in self.query:
                wb.open("www.gmail.com")

            elif 'bb' in self.query:
                wb.open("https://cuchd.blackboard.com/")

            elif 'cuims' in self.query:
                wb.open("https://uims.cuchd.in/uims/")

            elif 'amazon' in self.query:
                wb.open("https://www.primevideo.com/")

            

            #logout shutdown Restart
            elif 'logout' in self.query:
                speak("logging out...")
                time.sleep(5)
                subprocess.call(["shutdown", "/l"])
            elif 'shutdown' in self.query:
                speak("shutting down the system...")
                subprocess.call("shutdown /s /t 5")
            elif 'restart' in self.query:
                speak("Restarting the system...")
                subprocess.call(["shutdown", "/r"])
            # elif "hibernate" in self.query:
            #     speak("Hibernating")
            #     subprocess.call("shutdown / h")
            elif 'sleep' in self.query:
                os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

            #playing songs
            elif 'play song' in self.query or 'play music' in self.query:
                speak("Playing song")
                songs_dir = 'C:/Users/Asus/Music/June Songs'
                songs = os.listdir(songs_dir)
                d = random.choice(songs)
                random = os.startfile(os.path.join(songs_dir, d))

            #remember stuff for me
            elif 'remember' in self.query:
                speak("What should i remember?")
                data = takeCommand()
                speak("You want me to remember that" + data)
                remember = open('data.txt','w')
                remember.write(data)
                speak("I will remind you whenever you ask me!")
                remember.close()
            elif 'do you know anything' in self.query:
                remember = open('data.txt','r')
                speak("Yes Sir! you asked me to remember that" + remember.read())

            #screenshot
            elif 'screenshot' in self.query:
                screenshot()
                speak("Done sir!")

            # general stuff
            elif 'who are you' in self.query:
                speak("Hello there! i am your virtual assistant sir. I do what you ask me to")
            elif 'what is your name' in self.query:
                speak("My name is June")
            elif 'what is your name june' in self.query:
                speak("You already said my name sir")
            elif 'who am i' in self.query:
                speak("You are a Human and my control sir!")
            elif 'created' in self.query:
                speak("I was created by Mr. Rahul Pandey on february,15 2021")
            elif 'exist' in self.query:
                speak("Now thats the secret only my creator knows")
            elif 'how are you' in self.query:
                speak("I am good sir how are you?")
            elif 'fine' in self.query or 'good' in self.query:
                speak("Its good to know that you are good sir")
            elif "will you be my gf" in self.query or "will you be my bf" in self.query:
                speak("I'm not sure about, may be you should give me some time")
            elif 'i love you' in self.query:
                speak("It's hard to understand love for me!!!")

            #set alarm
            elif 'alarm' in self.query:
                nn = int(datetime.datetime.now().hour)
                if nn ==22:
                    songs_dir = 'C:/Users/Asus/Music/June Songs'
                    songs = os.listdir(songs_dir)
                    os.startfile(os.path.join(songs_dir, songs[0]))
                else:
                    speak("sorry")
            #jokes
            elif 'joke' in self.query:
                jokes()
            elif 'good one' in self.query:
                speak("i am glad to make you laugh!!!")

            # battery and cpu info
            elif 'cpu' in self.query:
                cpu()

            # opening system applications
            elif 'open word' in self.query:
                speak("opening microsoft word")
                os.startfile(r"C:/Program Files (x86)/Microsoft Office/Office12/WINWORD.EXE")

            elif 'open excel' in self.query:
                speak("opening microsoft excel")
                os.startfile(r"C:/Program Files (x86)/Microsoft Office/Office12/EXCEL.EXE")

            elif 'open powerpoint' in self.query:
                speak("opening microsoft powerpoint")
                os.startfile(r"C:/Program Files (x86)/Microsoft Office/Office12/POWERPNT.exe")
            
            elif 'open pycharm' in self.query:
                speak("opening pycharm")
                os.startfile(r"C:/Program Files (x86)/JetBrainsPyCharm Community Edition 2020.3.3/PyCharm Community Edition 2020.3.3/bin/pycharm64.exe")
            
            elif 'open chrome' in self.query:
                speak("opening chrmoe browser")
                os.startfile(r"C:/Program Files/Google/Chrome/Application/chrome.exe")

            elif 'open notepad' in self.query:
                speak("opening notepad")
                os.startfile(r"C:/Windows/System32/notepad.exe")

            elif 'open vs code' in self.query:
                speak("opening visual code")
                os.startfile(r"C:/Program Files/Microsoft VS Code/Code.exe")

            elif 'open command prompt' in self.query:
                speak("opening command prompt")
                os.system("start cmd")


            #closing application
            elif 'close word' in self.query:
                speak("okay sir! closing microsoft word")
                os.system("taskkill /f /im WINWORD.exe")
            elif 'close excel' in self.query:
                speak("okay sir! closing microsoft excel")
                os.system("taskkill /f /im EXCEL.exe")

            # switching windows
            elif 'switch windows' in self.query:
                pyautogui.keyDown("alt")
                pyautogui.press("tab")
                pyautogui.press("enter")
                time.sleep(1)
                pyautogui.keyUp("alt")

            #location
            # elif 'where is' in self.query or 'where' in self.query:
            #    ind = self.takeCommand().lower().split().index("is")
            #    location = self.takeCommand().split()[ind + 1:]
            #    url =  "https://www.google.com/maps/place/" + "".join(location)
            #    speak("This is where" + str(location) + " is")
            #    wb.open(url)
            

            # elif 'where i am' in self.query or 'where we are' in self.query:
            #     speak("Wait sir, let me check")
            #     try:
            #         ipAdd = requests.get('https://api.ipify.org').text
            #         print(ipAdd)
            #         url = 'https://get.geojson.io/v1/ip/geo/'+ipAdd+'.json'
            #         geo_requests = requests.get(url)
            #         geo_data = geo_requests.json()
            #         city = geo_data['city']
            #         state = geo_data['state']
            #         country = geo_data['country']
            #         speak(f"sir i am not sure, but i think we are in {city} of {country} country")
            #     except Exception as e:
            #         speak("sorry sir! due to bad network connection i am unable to search the current location")
            #         pass
            #news
            elif 'news' in self.query:
                speak("okay sir please wait fetching the latest news")
                news()

            # instagram profile check
            elif 'instagram profile' in self.query:
                speak("sir please enter the user name")
                name = input("Enter username here: ")
                wb.open(f"www.instagram.com/{name}")
                speak(f"sir here is the profile you asked me for {name}")
                speak("sir would you like to download the profile picture?")
                condition = takeCommand().lower()
                if 'yes' in condition:
                    mod = instaloader.Instaloader()#using pip install instaloader
                    mod.download_profile(name, profile_pic_only=True)
                    img.save("C:/Users/Asus/OneDrive/Desktop/June Picture/s1.png")
                    speak("I am done sir, you can have a look of the picture in my folder")
                else:
                    pass

            #----------------------Hide files and folders-----------------#
            elif 'hide files' in self.query or 'hide folders' in self.query or 'visible for everyone' in self.query:
                speak("Sir please tell me you want to hide or make it visible")
                condition = takeCommand().lower()
                if "hide" in condition:
                    os.system("attrib +h /s /d") #os module
                    speak("Sir, all the files in the folder are now hidden")

                elif "visible" in condition:
                    os.system("attrib -h /s /d")
                    speak("Sir, all the files in the folder are now visible to everyone")

                elif "leave it" in condition or "leave for now" in condition:
                    speak("Ok sir!!!")

            # reading pdf file
            elif 'read pdf' in self.query:
                pdf_reader()
                
            #temperature
            elif 'temperature' in self.query:
                search = f"temperature in sirsa"
                url = f"http://www.google.com/search?q={search}"
                r = requests.get(url)
                data = BeautifulSoup(r.text, "html.parser")
                temp = data.find("div",class_="BNeawe").text
                speak(f"current {search} is {temp}")

            # search anything
            elif 'activate how to do mod' in self.query:
                speak("How to do mod is activated please tell me what you want me to do")
                how = takeCommand()
                max_results = 1
                how_to = search_wikihow(how, max_results)
                assert len(how_to) == 1
                how_to[0].print()
                speak(how_to[0].summary)
            
            #speed test
            elif 'internet speed' in self.query:
                st = speedtest.Speedtest()
                dl = st.download()
                up = st.upload()
                speak(f"sir we have {dl} bit per second downloading speed and {up} bit per second uploading speed")
            # calculate
            elif 'calculate' in self.query:
                r =sr.Recognizer()
                with sr.Microphone() as source:
                    speak("Say what you want me to calculate, example: 2 plus 2")
                    print("Listening...")
                    r.adjust_for_ambient_noise(source)
                    audio = r.listen(source)
                my_string = r.recognize_google(audio)
                print(my_string)
                def get_operator_fn(op):
                    return {
                        '+' : operator.add, #plus
                        '-' : operator.sub, #minus
                        '*' : operator.mul, #multiply
                        'divided' : operator.__truediv__, #divide
                    }[op]
                def eval_binary_expr(op1, oper, op2): #5 plus 8
                    op1,op2 = int(op1), int(op2)
                    return get_operator_fn(oper)(op1, op2)
                speak("your result is")
                speak(eval_binary_expr(*(my_string.split())))


            #shutting the application
            elif 'call' in self.query:
                speak("okay sir goodnight i will wake you up")
                break
            elif 'shut up' in self.query:
                speak("I am sorry sir if i made a mistake")
                quit()
            elif 'offline' in self.query:
                speak("OKay! as you say, Going offline!")
                quit()

    
    def takeCommand(self):
        r =sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"user said: {query}")
        except Exception as e:
            print(e)
            speak("Can you speak again please...")
            return "None"
        return query


startExecution = MainThread()
class Main(QMainWindow):
    def __init__(self): 
        super(). __init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask) 
        self.ui.pushButton_2.clicked.connect(self.close)

    def startTask(self):
        self.ui.movie = QtGui.QMovie("C:/Users/Asus/OneDrive/Desktop/pics/giphy (1).gif") 
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        startExecution.start()


app = QApplication(sys.argv)
JuneUI = Main()
JuneUI.show()
exit(app.exec_())