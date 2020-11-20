import speech_recognition as sr
from tkinter import *
import pyttsx3
from pyttsx3 import drivers
import pyjokes
import PyPDF2
import requests
from bs4 import BeautifulSoup
import time
from plyer import notification
import datetime
import webbrowser
import wikipedia as wiki
from pytube import YouTube
from tkinter.filedialog import *
from tkinter.messagebox import *
from threading import *
from tkinter.scrolledtext import ScrolledText
import random
import speedtest
import os
import smtplib
from PIL import ImageTk,Image

def pdreader():
    read = Tk()
    read.iconbitmap("./res/vin.ico")
    read.title("PDF Reader by VINAY")
    read.configure(bg= "white")

    book = askopenfilename()
    pdfreader = PyPDF2.PdfFileReader(book)
    pages = pdfreader.numPages

    for num in range(0, pages):
        page = pdfreader.getPage(num)
        texts = page.extractText()
        player = pyttsx3.init()
        player.say(texts)
        player.runAndWait()

def netspeed():
    st = speedtest.Speedtest()
    #servernames=[]
    #st.get_servers(servernames)
    print("your download speed is" +st.download()//10**6,"Mbps") 
    print("and your upload speed is"+ st.upload()//10**6,"Mbps")

def wikiwithVinay():
    wik =Tk()
    wik.title("wikipedia by vinay")
    wik.iconbitmap("./res/vin.ico")
    wik.geometry('320x480')
    wik.minsize(320,480)
    wik.maxsize(320,480)
    wik.configure(bg= "grey")

    def search():
        search_data = search_entry.get()
        data= wiki.summary(search_data)
        #delete current data
        ent.set("")
        text.delete(0.0,END)
        search_lbl['text'] = "Searching for result : {}".format(search_data)
        text.insert(0.0,data)

    def enter_pressed(event):
        search()

    ent = StringVar()
    search_entry = Entry(wik,width=32 , font=("arial",12),bd=2,relief=RIDGE, textvariable=ent)
    search_entry.bind("<Return>",enter_pressed)
    search_entry.place(x=15,y=20)
    search_lbl = Label(wik, text="Searching results for :",bg="black",fg="white", font=("arial",12, "bold"))
    search_lbl.place(x=15,y=70)
    text = ScrolledText(wik,font=('time',13),bg="white",fg="blue",bd=4,relief=SUNKEN,wrap= WORD)
    text.place(x=15,y=100,height=300,width=300)
    search_btn =  Button(wik,text='Search',bg="black",fg="white",font=('arial',12,'bold'),width=10,command=search)
    search_btn.place(x=15,y=420)
    clear_btn = Button(wik,text='Clear', bg="black",fg="white",font=('arial',12,'bold'),width=10,command=lambda :text.delete(0.0,END))
    clear_btn.place(x=205,y=420)


def information():
    new = Toplevel()
    new.iconbitmap("./res/vin.ico")
    new.geometry("360x360")
    new.minsize(360,360)
    new.maxsize(360,360)

    def info ():
        global myname
        myname = name.get()
                                                                        
        global cal                           
        cal = caler.get()
    
        if myname == "" or cal == "":
            Label(new, text = "Fill both fields to proceed." , bg = "red" , fg = "white" , font = 'Verdana 11 bold').place( x =0 , y = 150)
            
        elif myname == "vinay" or myname == "Vinay" or myname == "VINAY" or myname == "VINAY" or myname == "Vinay":
            new.destroy()
            speak("Your name is so sweet. because vinay sir create me by taking very hard efforts.")
        else:
            new.destroy()

    user_name = Label (new, text = 'Enter your name: ' , fg ="blue", font = 'Ariel 15')
    user_name.place(x = 0,y=0)
    name = Entry(new, bg = "white", fg = "blue" , width ='40' , font = 'Ariel 15')
    name.place(x =0 , y = 30)
    name.focus()
    chatbot_name = Label (new, text = 'What should i call you?(sir/mam): ' , fg = "blue" , font = 'Ariel 15')
    chatbot_name.place(x =0 , y = 60)
    caler = Entry(new, bg = "white", fg = "blue" , width ='40' , font = 'Ariel 15')
    caler.place(x =0 , y = 90)
    caler.focus()
    button_1 = Button (new, image =submit , font = 'Vardana 10 bold' , command = info)
    button_1.place(x = 270 , y = 120)


root = Tk()
root.title("AI by Vinay")
root.geometry("360x500")
root.minsize(360,500)
root.maxsize(360,500)
root.configure(bg= "grey")
root.wm_iconbitmap("./res/vin.ico")

image = Image.open("./res/terminal.png")
photo=ImageTk.PhotoImage(image)
lbl=Label(root, image=photo)
lbl.place(x=0,y=0)

logo = PhotoImage(file = './res/welcome1.png')
welc_lbl=Label(root, image = logo)
welc_lbl.place(x=0,y=83)

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak(f"Good Morning!")
    elif hour>=12 and hour<18:
        speak(f"Good Afternoon!")  
    else:
        speak(f"Good Evening")
        
def headtail():
    coin = ["Heads", "Tails"]
    toss = random.choice(coin)
    speak(toss)

reply = ["youtube.com/watch?v=ZyhwHjO7UWQ", "youtube.com/watch?v=VAZxSoKb65o", "youtube.com/watch?v=hoNb6HuNmU0"]
givereply = random.choice(reply)
        
def commands():
    if "hello" in text:
        speak("hi")
        wishMe()
    
    elif "hi" in text:
        speak("hello")
        wishMe()

    elif "who makes you" in text:
        speak("I started as an idea, then vinay sir helped bring me to life!")

    elif "what can you do" in text:
        speak("play music, search wikipedia, show your location, tell some jokes, send email, play games")

    elif "how are you" in text or "how are u" in text:
        speak("I am fine! What about you?")
  
    elif "what are you doing" in text:
        speak("helping some people like you")

    elif "download" in text:
        query = list(text)
        query.remove('download')
        webbrowser.open(query)

    elif "thanks" in text or "thankyou" in text or "bye" in text or "thank you" in text:
        speak(f"its my duty")
        root.destroy()

    elif "your father" in text:
        speak("Vinay sir")

    elif "what is my name" in text:
      speak(f"your name is {myname}")

    elif "call me" in text:
        speak("what should i call you")
        speak("ok!")
     
    elif "mail" in text:
        webbrowser.open("gmail.com")
        speak(f"opening gmail {cal}")

    elif "love u"in text or "love you" in text:
        speak(f"love u too {myname}")

    elif "my location" in text:
        speak("you are in karanjali")

    elif "miss u" in text or "miss you" in text:
        speak(f"I am always be with you please smile {myname}")
 
    elif 'open youtube' in text:
        webbrowser.open("youtube.com")
        speak(f"Opening youtube {cal}")

    elif 'time' in text:
        strTime = datetime.datetime.now().strftime("%I : %M")
        speak(f"{cal} The time is {strTime}")

    elif 'wikipedia' in text:
        wikiwithVinay()

    elif 'rain' in text:
        webbrowser.open(text)
        speak(f'searching ')

    elif "weather" in text:
        search = text
        URL = f"https://www.google.com/search?q={search}"
        req = requests.get(URL)
        sav = BeautifulSoup(req.text,"html.parser")
        update = sav.find("div",class_="BNeawe").text
        #print(update)
        speak(update)

    elif 'good morning' in text or 'Good Morning' in text or 'GOOD MORNING' in text or 'GM' in text or 'gm' in text:
        wishMe()
 
    elif 'good night' in text or 'Good Night' in text or 'GOOD NIGHT' in text or 'GN' in text or 'gn' in text or "Gn" in text:
        wishMe()

    elif 'good afternoon' in text or 'Good Afternoon' in text or 'GOOD AFTERNOON' in text or 'GA' in text or 'ga' in text or "Ga" in text:
        wishMe()

    elif "can i change your name" == text:
        speak("I might be confused if you do that")

    elif "your name" in text:
        speak('my name is jarvin coded by vinay sir')

    elif 'my name is vinay' in text:
        speak("your name is so sweet. because vinay sir create me by taking very hard efforts.")
      
    elif "jarvin" in text:
        speak(f"At your service {cal}")

    elif "jokes" in text or "joke" in text or "boare" in text:
        speak(pyjokes.get_joke())

    elif "translate" in text:
        speak("ok")
    
    elif "roll dice" in text:
        min =1
        max =6
        roll_again ="yes"
        while roll_again =="yes" or roll_again=="y":
	        speak("rolling dice")
	        speak("The value is")
	        speak(random.randint(min, max))
	        roll_again = input("roll dice again y or n- ")

    elif "internet speed" in text or "net speed" in text:
        netspeed()

    elif "year going on" in text:
        hour = datetime.datetime.now()
        speak("it's" + hour.year)

    elif "whats the day" in text or "what's the day" in text or "day is" in text:
        hour = datetime.datetime.now()
        speak("its" + hour.strftime("%A"))

    elif "toss" in text or "toss coin" in text or "coin" in text or "toss a coin" in text:
        headtail()

    elif "play music" in text or "some music" in text or "play music on youtube" in text or "some music on youtube" in text:
        webbrowser.open(givereply)
        speak("Ok! playing music for you")
    
    elif "change my name" in text:
        inform()

    elif "on youtube" in text:
        webbrowser.open("https://www.youtube.com/results?search_query="+text)
        speak("searching...")

    elif "search" in text:
        webbrowser.open(text)
        speak("searching...")

    elif "how do you do" in text:
        speak("fine")

    elif "how" in text or "how to" in text:
        webbrowser.open(text)
        speak("searching...")

    elif "i call you" in text:
        speak("just call me your jarvin Assistant")

    elif "do you have a nickname" in text:
        speak("One day i hope to have a nickname")

    elif "what do you want to call me" in text:
        speak("I'd like to call you a friend")
    
    elif "can i call you alexa" in text:
        speak("But i'm your jarvin assistant")

    elif "please please" in text:
        speak("Sure Sure. What can i do for you?")

    elif "i want to see your face" in text:
        speak("I never know how to describe myself")

    elif "kiss me" in text:
        speak("I'd prefer to keep chatting")

    elif "dance for me" in text:
        speak("one two chaa chaa chaa")
    
    elif "you are funny" in text:
        speak("I was being serious, seriously funny")

    elif "can you laugh" in text:
        speak("Hahaha")

    elif "remimd water" in text or "drink water" in text:
        notify = "yes"
        while notify == "yes":
            speak("Please drink water")
            notification.notify(
                title = "**Please Drink Water Now",
                message="Its important to drink water",
                app_icon= "./res/vin.ico",
                timeout=10
            )
            time.sleep(60*60)

    elif "to take break" in text or "to take a break" in text:
        notify_break = "yes"
        while notify_break == "yes":
            notification.notify(
                title = "**Please Take A Break",
                message="Its important to take a break",
                app_icon= "./res/vin.ico",
                timeout=10
            )
            time.sleep(60*60)

    elif "read the pdf" in text or "read pdf" in text:
        speak("which pdf i read for you?")
        pdreader()

    elif "can you here me" in text or "listen me" in text or "hey jarvin" in text or "jarvin" in text:
        speak("just type anything")

    elif "what should i do now" in text:
        speak("You can say Help me play music")

    elif "alarm" in text:
        speak("Sorry, something went wrong while i was looking for your alarm.")

    elif "who created you" in text:
        speak("Vinay sir made me")

    else:
        speak("i got this from web")
        webbrowser.open(text)

#-----------
microphone = PhotoImage(file = './res/micro.png')
send = PhotoImage(file = './res/send.png')
submit = PhotoImage(file = "./res/submit.PNG")

#--------------------------------
def inform():
    your_info['text']= 'You have entered your name'
    your_info['state'] = 'disabled'
    information()

def giveresponce():
    thread=Thread(target=commands)
    thread.start()

def enter_pressed(event):
    giveresponce()

def start():
    tm = datetime.datetime.now().strftime("%I:%M %p")
    label.config(text=tm)
    label.after(200,start)

label=Label(root, fg="blue", font="Verdana 14")
label.place(x = 210,y=40)
start()
mic_button = Button(root, image = microphone,command = commands)
mic_button.place(x=283, y=390)
your_info = Button(root, text="Enter you name..",fg="blue",relief=RIDGE, command = inform)
your_info.place(x=0, y= 40)
wel=Label(root,text = "WELCOME                                                ", bg="blue", fg="red",width=55, font="Verdana 11 bold")
wel.place(x=2, y=0)
joke_lbl=Label(root, text='"How can i help you?', fg = "red", font = "Verdana 10 bold")
joke_lbl.place(x=0,y=85)
joke_lbl1=Label(root, text='"play music"', fg = "blue", font = "Verdana 10 bold")
joke_lbl1.place(x=0,y=125)
joke_lbl2=Label(root, text='"tell me a joke"', fg = "blue", font = "Verdana 10 bold")
joke_lbl2.place(x=0,y=155)
joke_lbl3=Label(root, text='"search jarvis on youtube"', fg = "blue", font = "Verdana 10 bold")
joke_lbl3.place(x=0,y=185)
joke_lbl4=Label(root, text='"remind me to drink water"', fg = "blue", font = "Verdana 10 bold")
joke_lbl4.place(x=0,y=215)
text = Entry(root, bg ="white", fg ="blue", width ='29', font = 'Ariel 15')
text.bind("<Return>",enter_pressed)
text.place(x=0,y=420)
text.focus()

wishMe()
root.mainloop()