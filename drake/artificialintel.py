import pyttsx3
import pyaudio
import speech_recognition as sr
import datetime
import pyautogui
import os
import random
import PyPDF2
import wikipedia
from pywikihow import search_wikihow
import pyjokes
import operator
import array
import pyqrcode
import PyDictionary
from win10toast import *
import face_recognition
import cv2
import numpy as np
import pywhatkit
import wikipedia
from pywikihow import RandomHowTo, search_wikihow
import os
import speech_recognition as sr
import webbrowser as web
import bs4
import pyttsx3
from time import sleep
import requests

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)

def speak (audio):
    print(f"F.R.I.D.A.Y : {audio}")
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        print("Recognising.....")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"User said: {query}\n") 
    except Exception as e:
        # print(e)    
        print("Say That Again Please...")  
        return "None"
    return query

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        print("Good Morning! Sir")
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        print("Good Afternoon! Sir")    
        speak("Good Afternoon!")    
    else:
        print("Good Evening! Sir")    
        speak("Good Evening!")

def screenshot():
            img = pyautogui.screenshot()
            path1 = "C:\\Users\\usernam\\Desktop\\Screenshots\\"
            img.save(path1)

def diceroller():
    while True:
        print("Rolling The Dice Sir...")
        speak("Rolling The Dice Sir")
        print(f"Sir, The Number Is => ", random.randint(1,6))
        speak("Do you want to roll the dice again sir")
        repeat = takeCommand()
        if 'yes' in repeat:
            diceroller()
        else:
            break

def pdf_reader():
    speak("yes sir I will read it for you")
    os.startfile("C:\\Users\\username\\Desktop\\F.R.I.D.A.Y (2.8.0)\\F.R.I.D.A.Y_Assets\\short-stories-for-children.pdf")
    engine.setProperty('rate' , 125)
    book = open("C:\\Users\\username\\Desktop\\F.R.I.D.A.Y (2.8.0)\\F.R.I.D.A.Y_Assets\\short-stories-for-children.pdf", 'rb')
    pdfReader = PyPDF2.PdfFileReader(book)
    pages = pdfReader.numPages
    speak(f"sir the Total number of pages are {pages}")
    page = pdfReader.getPage(5)
    text = page.extractText()
    speak(text)

def how_to_():
    how = takeCommand()
    max_results = 1
    how_to_do = search_wikihow(how, max_results)
    assert len(how_to_do) == 1
    how_to_do[0].print()
    speak(how_to_do[0].summary)

def jokes():
    print(pyjokes.get_joke())

def passgenerator():
    MAX_LEN = 100
    DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
    					'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
    					'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
    					'z']
    UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
    					'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',
    					'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
    					'Z']
    SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
    		'*', '(', ')', '<']
    COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS
    rand_digit = random.choice(DIGITS)
    rand_upper = random.choice(UPCASE_CHARACTERS)
    rand_lower = random.choice(LOCASE_CHARACTERS)
    rand_symbol = random.choice(SYMBOLS)
    temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol
    for x in range(MAX_LEN - 4):
    	temp_pass = temp_pass + random.choice(COMBINED_LIST)
    	temp_pass_list = array.array('u', temp_pass)
    	random.shuffle(temp_pass_list)
    password = ""
    for x in temp_pass_list:
    		password = password + x
    print(password)

def calculate():
    calc = input("What you want me to calculate => ")
    print("User Said" , calc)
    def get_operator_fn(op):
        return {
            '+' : operator.add,
            '-' : operator.sub,
            'x' : operator.mul,
            'divided' :operator.__truediv__,
            'Mod' : operator.mod,
            'mod' : operator.mod,
            '^' : operator.xor,
            }[op]
    def eval_binary_expr(op1, oper, op2):
        op1,op2 = int(op1), int(op2)
        return get_operator_fn(oper)(op1, op2)
    print(eval_binary_expr(*(calc.split())))

def dictionary():
    dict = PyDictionary()
    word_search = takeCommand()
    print(dict.meaning(word_search))            

def QRgenerator():
    data = input("Enter the text or link to generate QR code => ")
    qr = pyqrcode.create(data)
    qr.svg('qr_code.svg', scale = 8)

def verifyuser():
    while True:
        print("Please Tell Your Name => ")
        UserName_Password1 = str(input("Please Tell Your Name => "))
        print("Please Tell The Password => ")
        UserPass_Password2 = str(input("Please Tell The Password => "))
        if 'hello' in UserName_Password1 or 'hello' in UserName_Password1:
            if 'hi' in UserPass_Password2 or 'hi' in UserPass_Password2:
                print("Access Granted, Welcome")
                break
        else:
            print("Access Denied")

def recognize_face():
    video_capture = cv2.VideoCapture(2)
    
    # Load a sample picture and learn how to recognize it.
    Vipul_image = face_recognition.load_image_file("hi1.jpg")
    Vipul_face_encoding = face_recognition.face_encodings(Vipul_image)[0]
    
    # Load a second sample picture and learn how to recognize it.
    SKMishra_image = face_recognition.load_image_file("hi2.jpg")
    SKMishra_face_encoding = face_recognition.face_encodings(SKMishra_image)[0]
    
    # Load a second sample picture and learn how to recognize it.
    Rashmi_image = face_recognition.load_image_file("hi3.jpg")
    Rashmi_face_encoding = face_recognition.face_encodings(Rashmi_image)[0]
    
    # Create arrays of known face encodings and their names
    known_face_encodings = [
        Vipul_face_encoding,
        SKMishra_face_encoding,
        Rashmi_face_encoding
    ]
    known_face_names = [
        "Hello1",
        "Hello2",
        "Hello3"
    ]
    
    # Initialize some variables
    face_locations = []
    face_encodings = []
    face_names = []
    process_this_frame = True
    
    while True:
        # Grab a single frame of video
        ret, frame = video_capture.read()
    
        # Resize frame of video to 1/4 size for faster face recognition processing
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    
        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_small_frame = small_frame[:, :, ::-1]
    
        # Only process every other frame of video to save time
        if process_this_frame:
            # Find all the faces and face encodings in the current frame of video
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
    
            face_names = []
            for face_encoding in face_encodings:
                # See if the face is a match for the known face(s)
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                name = "Unknown"
    
                # # If a match was found in known_face_encodings, just use the first one.
                # if True in matches:
                #     first_match_index = matches.index(True)
                #     name = known_face_names[first_match_index]
    
                # Or instead, use the known face with the smallest distance to the new face
                face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = known_face_names[best_match_index]
    
                face_names.append(name)
    
        process_this_frame = not process_this_frame
    
    
        # Display the results
        for (top, right, bottom, left), name in zip(face_locations, face_names):
            # Scale back up face locations since the frame we detected in was scaled to 1/4 size
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4
    
            # Draw a box around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
    
            # Draw a label with a name below the face
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 255, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (220, 20, 60), 1)
    
        # Display the resulting image
        cv2.imshow('Face Recognition Made By Drake Parker', frame)
    
        # Hit 'q' on the keyboard to quit!
        if cv2.waitKey(1) & 0xFF == ord('v'):
            break
        video_capture.release()
        cv2.destroyAllWindows()

def notify():
    n = ToastNotifier()
    n.show_toast("F.R.I.D.A.Y", "Enjoy Your Day Sir", duration = 20,
    icon_path ="C:\\Users\\Dell\\Desktop\\F.R.I.D.A.Y (2.8.0)\\F.R.I.D.A.Y_Assets\\icon_8.ico")

def YouTubeSearch(term):
    result = "https://www.youtube.com/results?search_query=" + term
    web.open(result)
    pywhatkit.playonyt(term)

def Alarm(query):

    TimeHere=  open('E:\\Y O U T U B E\\J A R V I S  S E R I E S\\H O W  T O  M A K E  J A R V I S\\Data.txt','a')
    TimeHere.write(query)
    TimeHere.close()
    os.startfile("E:\\Y O U T U B E\\J A R V I S  S E R I E S\\H O W  T O  M A K E  J A R V I S\\DataBase\\ExtraPro\\Alarm.py")

def DownloadYouTube():
    from pytube import YouTube
    from pyautogui import click
    from pyautogui import hotkey
    import pyperclip
    from time import sleep

    sleep(2)
    click(x=942,y=59)
    hotkey('ctrl','c')
    value = pyperclip.paste()
    Link = str(value) # Important 

    def Download(link):


        url = YouTube(link)


        video = url.streams.first()


        video.download('E:\\YouTube Channel\\YouTube - Jarvis\\How To Make Jarvis In Python\\DataBase\\YouTube\\')


    Download(Link)

    os.startfile('E:\\Y O U T U B E\\J A R V I S  S E R I E S\\H O W  T O  M A K E  J A R V I S\\DataBase\\YouTube\\')

def SpeedTest():

    os.startfile("E:\\Y O U T U B E\\J A R V I S  S E R I E S\\H O W  T O  M A K E  J A R V I S\\DataBase\\Gui Programs\\SpeedTestGui.py")

def DateConverter(Query):

    Date = Query.replace(" and ","-")
    Date = Date.replace(" and ","-")
    Date = Date.replace("and","-")
    Date = Date.replace("and","-")
    Date = Date.replace(" ","")

    return str(Date)

def My_Location():
    ip_add = requests.get('https://api.ipify.org').text

    url = 'https://get.geojs.io/v1/ip/geo/' + ip_add + '.json'

    geo_q = requests.get(url)

    geo_d = geo_q.json()

    state = geo_d['city']

    country = geo_d['country']

def CoronaVirus(Country):

    countries = str(Country).replace(" ","")

    url = f"https://www.worldometers.info/coronavirus/country/{countries}/"

    result = requests.get(url)

    soups = bs4.BeautifulSoup(result.text,'lxml')

    corona = soups.find_all('div',class_ = 'maincounter-number')

    Data = []

    for case in corona:

        span = case.find('span')

        Data.append(span.string)

    cases , Death , recovored = Data