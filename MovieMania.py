from tkinter import *           #importing all modules needed so they can be accessed and used by the program
from tkinter import ttk
from tkinter import Listbox
from tkinter import messagebox
from functools import partial
import os
import uuid
import hashlib
import webbrowser
from datetime import datetime
import datetime as dt
import json
import smtplib, ssl
import re
import string
import random
import ctypes
import fileinput


def home_screen(canvas):            #function for the first screen of the system
    canvas.destroy()                #destroys the previous canvas so a new one can replace it
    user32 = ctypes.windll.user32
    w = str(user32.GetSystemMetrics(0))         #gets the dimensions of the screen of the device being used
    h = str(user32.GetSystemMetrics(1))
    home_screen_canvas = Tk()           #creates a tkinter window
    home_screen_canvas.geometry(w+"x"+h)        #sets the size of the window to the size of the screen
    home_screen_canvas.configure(background='dark grey')        #sets the colour of the window to dark grey
    home_screen_canvas.title("Welcome to MovieMania")           #sets the title of the window
    Label(home_screen_canvas, font=("Arial", 30), text="Welcome to MovieMania", fg="purple", anchor='center').grid(row=0, column=1)         #adds a label to the canvas
    Button(home_screen_canvas, text='Log In', width=15, height=3, command=lambda: loginHomeScreen(home_screen_canvas)).grid(row=1, column=2, padx=(0, 100), sticky=E)     #adds a button to the canvas
    Button(home_screen_canvas, text='Exit', width=15, height=3, command=quit).grid(row=1, column=0, padx=(100,0), sticky=W)
    #font sets the text type, text sets what writing will be on the button, width and height set the size of the button, command sets what will happen when the button is clicked and parameters are passed to the function for them to be used within in
    #grid sets where on the canvas it will be, sticky sets which side of the column it will be, pady/padx moves it within the row/column
    home_screen_canvas.grid_rowconfigure(0, weight=1)           #makes sure the whole canvas is filled and distributed
    home_screen_canvas.grid_rowconfigure(2, weight=1)
    home_screen_canvas.grid_columnconfigure(0, weight=1)
    home_screen_canvas.grid_columnconfigure(2, weight=1)


    films = ["Avengers 4", "Glass", "Dumbo", "It 2", "Toy Story 4", "Lego Movie 2"]     #the default film selection

    if os.path.isfile(os.getcwd() + "\\films\\films.txt"):          #checking the folder and file path exists on the device
        print()

    else:
        os.makedirs(os.getcwd() + "\\films")            #makes the folder and file if it isn't already there
        file = open(os.getcwd() + "\\films\\films.txt", "w")
        for film in films:                              #writes the default films to the text file
            file.write(film + "\n")
        file.close()

    dateToday = dt.datetime.today().strftime('%Y-%m-%d')            #gets todays date
    if os.path.isdir(os.getcwd() + "\\food"):
        if os.path.isfile(os.getcwd() + "\\food\\" + dateToday + ".txt"):           #checks if the file already exists
            print()
    else:
        os.makedirs(os.getcwd() + "\\food")
        with open(os.getcwd() + "\\food\\" + dateToday + '.txt', "w") as f:
            f.write(dateToday)
            f.close()



    q = open(os.getcwd() + "\\films\\films.txt", "r")               #opens the films text file for reading - this sets up all of the film folders so they are ready to use
    currentFilms = []                                               #defines a new list
    for line in q.readlines():                                      #reads all of the lines and does the same thing for each line in the opened file
        currentFilms.append(line.strip())                           #appends to the file
    for film in currentFilms:
        if os.path.isdir(os.getcwd() + "\\films\\" + film):         #checks if the file exists
            print()

        else:
            print()
            os.makedirs(os.getcwd() + "\\films\\" + film)           #creates the file if not
    q.close()                                                       #closes the opened file

    if os.path.isfile(os.getcwd() + "\\films\\seats.txt"):          #this removes any existing seat text file so it is available to re create later
        path = os.getcwd() + "\\films\\seats.txt"
        os.remove(path)

    films = ["Avengers 4", "Glass", "Dumbo", "It 2", "Toy Story 4", "Lego Movie 2"]                 #default films
    AvengersScreening = ["10-3-19 "+"\n"+"19-30 "+"\n"+"Screen 4 "+"\n"+"2D", "24-3-19 "+"\n"+"14-45 "+"\n"+"Screen 5 "+"\n"+"3D"]
    GlassScreening = ["10-3-19 "+"\n"+"19-30 "+"\n"+"Screen 4 "+"\n"+"2D", "24-3-19 "+"\n"+"14-45 "+"\n"+"Screen 5 "+"\n"+"3D"]
    DumboScreening = ["10-3-19 "+"\n"+"19-30 "+"\n"+"Screen 4 "+"\n"+"2D", "24-3-19 "+"\n"+"14-45 "+"\n"+"Screen 5 "+"\n"+"3D"]
    It2Screening = ["10-3-19 "+"\n"+"19-30 "+"\n"+"Screen 4 "+"\n"+"2D", "24-3-19 "+"\n"+"14-45 "+"\n"+"Screen 5 "+"\n"+"3D"]
    ToystoryScreening = ["10-3-19 "+"\n"+"19-30 "+"\n"+"Screen 4 "+"\n"+"2D", "24-3-19 "+"\n"+"14-45 "+"\n"+"Screen 5 "+"\n"+"3D"]
    LegomovieScreening = ["10-3-19 "+"\n"+"19-30 "+"\n"+"Screen 4 "+"\n"+"2D", "24-3-19 "+"\n"+"14-45 "+"\n"+"Screen 5 "+"\n"+"3D"]

    Screenings = [AvengersScreening,GlassScreening,DumboScreening,It2Screening,ToystoryScreening,LegomovieScreening]

    if os.path.isfile(os.getcwd()+"\\films\\films.txt"):
        print()

    else:
        os.makedirs(os.getcwd()+"\\films")
        file = open(os.getcwd()+"\\films\\films.txt", "w")
        for film in films:
            file.write(film+"\n")
            file.close()

    q = open(os.getcwd() + "\\films\\films.txt", "r")
    currentFilms = []
    for line in q.readlines():
        currentFilms.append(line.strip())
    for film in currentFilms:                   #creating text files for each default screening
        if os.path.isdir(os.getcwd() + "\\films\\"+film):
            print()
            for Screening in Screenings: #This is getting a list from a tuple
                for screen in Screening: #So we get each element of the screening list
                    if os.path.isfile(os.getcwd() + "\\films\\" + film.strip() + "\\" + screen.replace("\n", "") + ".txt"): #Removing the \n's as they would be in the file path otherwise
                        print()
                    else:
                        print()
                        a = open(os.getcwd() + "\\films\\" + film.strip() + "\\" + screen.replace("\n", "") + ".txt", "w")
                        a.write(screen)
                        a.close()

        else:
            print()
            os.makedirs(os.getcwd()+"\\films\\"+film)
            for Screening in Screenings:
                for screen in Screening:
                    if os.path.isfile(os.getcwd() + "\\films\\" + film + "\\" + screen.replace("\n", "") + ".txt"):
                        print()

                    else:
                        print()
                        a = open(os.getcwd() + "\\films\\" + film +"\\" + screen.replace("\n", "") +".txt", "w")
                        a.write(screen)
                        a.close()

    q.close()

    container1 = Canvas(home_screen_canvas, width=280, height=130)              #sets up a box for the image to go in
    imgLogoOG = PhotoImage(file="logo.png")                                     #assigns a variable the image
    imgLogoDisplay = imgLogoOG.subsample(2,2)                                   #makes sure the whole of the image is displayed
    container1.grid(row=1, column=1)                                            #puts it in the right place on the canvas
    container1.create_image(1, 1, anchor=NW, image=imgLogoDisplay)              #puts the image in the container and displays it

    avengersp = Button(home_screen_canvas)
    photo1 = PhotoImage(file="avengers4.png")
    avengersp.config(image=photo1, width="130", height="200", activebackground="black", bg="black", bd=0, command=lambda: avengers4(home_screen_canvas))    #assigns the button an image
    avengersp.grid(row=2, column=0)

    glassp = Button(home_screen_canvas)
    photo2 = PhotoImage(file="glass.png")
    glassp.config(image=photo2, width="130", height="200", activebackground="black", bg="black", bd=0, command=lambda: glass(home_screen_canvas))
    glassp.grid(row=2, column=1)

    dumbop = Button(home_screen_canvas)
    photo3 = PhotoImage(file="dumbo.png")
    dumbop.config(image=photo3, width="130", height="200", activebackground="black", bg="black", bd=0, command=lambda: dumbo(home_screen_canvas))
    dumbop.grid(row=2, column=2)

    itp = Button(home_screen_canvas)
    photo4 = PhotoImage(file="it2.png")
    itp.config(image=photo4, width="130", height="200", activebackground="black", bg="black", bd=0, command=lambda: it2(home_screen_canvas))
    itp.grid(row=3, column=0, pady=5)

    toystoryp = Button(home_screen_canvas)
    photo5 = PhotoImage(file="toystory4.png")
    toystoryp.config(image=photo5, width="130", height="200", activebackground="black", bg="black", bd=0, command=lambda: toystory(home_screen_canvas))
    toystoryp.grid(row=3, column=1, pady=5)

    legomoviep = Button(home_screen_canvas)
    photo6 = PhotoImage(file="legomovie2.png")
    legomoviep.config(image=photo6, width="130", height="200", activebackground="black", bg="black", bd=0, command=lambda: legomovie(home_screen_canvas))
    legomoviep.grid(row=3, column=2, pady=5)

    mainloop()                                  #allows the images to be displayed properly


def avengers4(canvas):          #function that is ran when the avengers 4 film poster button is clicked
    canvas.destroy()
    user32 = ctypes.windll.user32
    w = str(user32.GetSystemMetrics(0))
    h = str(user32.GetSystemMetrics(1))
    trailername = "AV"              #variable to be used when wanting to view a trailer
    avengers_canvas = Tk()
    avengers_canvas.geometry(w+'x'+h)
    avengers_canvas.configure(background='dark grey')
    avengers_canvas.title("Avengers 4 (2019)")
    avengers_canvas.grid_rowconfigure(0, weight=1)
    avengers_canvas.grid_rowconfigure(2, weight=1)
    avengers_canvas.grid_columnconfigure(0, weight=1)
    avengers_canvas.grid_columnconfigure(2, weight=1)

    container2 = Canvas(avengers_canvas, width=270, height=400)
    imgAvengersOG = PhotoImage(file="avengers4.png")
    imgAvengersDisplay = imgAvengersOG.zoom(2,2)
    container2.grid(row=1, column=0)
    container2.create_image(1, 1, anchor=NW, image=imgAvengersDisplay)

    avengerstext = Text(avengers_canvas, height=15, width=60)           #creates a text box to display a message
    avengerstext.insert(END, "Title: Avengers 4 - Endgame \nRunning length: 180 mins \nRating: 12 \nScreen type: 2D and 3D \n\nSynopsis: Adrift in space with no food or water, Tony Stark sends a message to Pepper Potts as his oxygen supply starts to dwindle. Meanwhile, the remaining Avengers -- Thor, Black Widow, Captain America and Bruce Banner -- must figure out a way to bring back their vanquished allies for an epic showdown with Thanos -- the evil demigod who decimated the planet and the universe.")
    avengerstext.grid(row=1, column=0, columnspan=3, padx=(100, 0))
    Button(avengers_canvas, text='Trailer', width=10, height=3, command=lambda: video(trailername)).grid(row=2,column=0,sticky=E, pady=(0, 150),padx=50)
    Button(avengers_canvas, text='Book Now', width=20, height=3, command=lambda: loginHomeScreen(avengers_canvas)).grid(row=2,column=1,sticky=W, pady=(0, 150),padx=50)
    Button(avengers_canvas, text='Back', width=10, height=3, command=lambda: home_screen(avengers_canvas)).grid(row=2, column=2, sticky=W, pady=(0, 150), padx=50)
    mainloop()

def glass(canvas):
    canvas.destroy()
    user32 = ctypes.windll.user32
    w = str(user32.GetSystemMetrics(0))
    h = str(user32.GetSystemMetrics(1))
    trailername = "GL"
    glass_canvas = Tk()
    glass_canvas.geometry(w+'x'+h)
    glass_canvas.configure(background='dark grey')
    glass_canvas.title("Glass (2019)")
    glass_canvas.grid_rowconfigure(0, weight=1)
    glass_canvas.grid_rowconfigure(2, weight=1)
    glass_canvas.grid_columnconfigure(0, weight=1)
    glass_canvas.grid_columnconfigure(2, weight=1)

    container3 = Canvas(glass_canvas, width=250, height=400)
    imgGlassOG = PhotoImage(file="glass.png")
    imgGlassDisplay = imgGlassOG.zoom(2, 2)
    container3.grid(row=1, column=0)
    container3.create_image(1, 1, anchor=NW, image=imgGlassDisplay)

    glasstext = Text(glass_canvas, height=15, width=60)
    glasstext.insert(END,
                        "Title: Glass \nRunning length: 129 mins \nRating: 15 \nScreen type: 2D \n\nSynopsis: Following the conclusion of Split, Glass finds Dunn pursuing Crumb’s superhuman figure of The Beast in a series of escalating encounters, while the shadowy presence of Price emerges as an orchestrator who holds secrets critical to both men.")
    glasstext.grid(row=1, column=0, columnspan=3, padx=(100,0))
    Button(glass_canvas, text='Trailer', width=10, height=3,
           command=lambda: video(trailername)).grid(row=2, column=0, sticky=E,pady=(0,150), padx=50)
    Button(glass_canvas, text='Book Now', width=20, height=3, command=lambda: loginHomeScreen(glass_canvas)).grid(row=2, column=1,sticky=W, pady=(0,150),padx=50)
    Button(glass_canvas, text='Back', width=10, height=3, command=lambda: home_screen(glass_canvas)).grid(row=2, column=2, sticky=W, pady=(0,150), padx=50)
    mainloop()

def dumbo(canvas):
    canvas.destroy()
    user32 = ctypes.windll.user32
    w = str(user32.GetSystemMetrics(0))
    h = str(user32.GetSystemMetrics(1))
    trailername = "DU"
    dumbo_canvas = Tk()
    dumbo_canvas.geometry(w+'x'+h)
    dumbo_canvas.configure(background='dark grey')
    dumbo_canvas.title("Dumbo (2019)")
    dumbo_canvas.grid_rowconfigure(0, weight=1)
    dumbo_canvas.grid_rowconfigure(2, weight=1)
    dumbo_canvas.grid_columnconfigure(0, weight=1)
    dumbo_canvas.grid_columnconfigure(2, weight=1)

    container4 = Canvas(dumbo_canvas, width=270, height=400)
    imgDumboOG = PhotoImage(file="dumbo.png")
    imgDumboDisplay = imgDumboOG.zoom(2,2)
    container4.grid(row=1, column=0)
    container4.create_image(1, 1, anchor=NW, image=imgDumboDisplay)

    dumbotext = Text(dumbo_canvas, height=15, width=60)
    dumbotext.insert(END,
                     "Title: Dumbo \nRunning length: 130 mins \nRating: PG \nScreen type: 2D \n\nSynopsis: The owner of a struggling circus enlists a man and his two children to care for a newborn elephant that can fly.")
    dumbotext.grid(row=1, column=0, columnspan=3, padx=(100,0))
    Button(dumbo_canvas, text='Trailer', width=10, height=3,
           command=lambda: video(trailername)).grid(row=2, column=0, sticky=E,pady=(0,150), padx=50)
    Button(dumbo_canvas, text='Book Now', width=20, height=3, command=lambda: loginHomeScreen(dumbo_canvas)).grid(row=2, column=1, sticky=W,pady=(0,150), padx=50)
    Button(dumbo_canvas, text='Back', width=10, height=3, command=lambda: home_screen(dumbo_canvas)).grid(row=2, column=2, sticky=W, pady=(0,150), padx=50)
    mainloop()



def it2(canvas):
    canvas.destroy()
    user32 = ctypes.windll.user32
    w = str(user32.GetSystemMetrics(0))
    h = str(user32.GetSystemMetrics(1))
    trailername = "IT"
    it2_canvas = Tk()
    it2_canvas.geometry(w+'x'+h)
    it2_canvas.configure(background='dark grey')
    it2_canvas.title("It - Chapter 2 (2019)")
    it2_canvas.grid_rowconfigure(0, weight=1)
    it2_canvas.grid_rowconfigure(2, weight=1)
    it2_canvas.grid_columnconfigure(0, weight=1)
    it2_canvas.grid_columnconfigure(2, weight=1)

    container5 = Canvas(it2_canvas, width=270, height=400)
    imgItOG = PhotoImage(file="it2.png")
    imgItDisplay = imgItOG.zoom(2, 2)
    container5.grid(row=1, column=0, pady=10)
    container5.create_image(1, 1, anchor=NW, image=imgItDisplay)

    it2text = Text(it2_canvas, height=15, width=60)
    it2text.insert(END,
                     "Title: It - Chapter 2 \nRunning length: Currently unknown \nRating: 15 \n\nScreen type: 2D \nSynopsis: The evil clown Pennywise returns 27 years later to torment the grown-up members of the Losers' Club.")
    it2text.grid(row=1, column=0, columnspan=3, padx=(100,0))
    Button(it2_canvas, text='Trailer', width=10, height=3,
           command=lambda: video(trailername)).grid(row=2, column=0, sticky=E, pady=(0, 150), padx=50)
    Button(it2_canvas, text='Book Now', width=20, height=3, command=lambda: loginHomeScreen(it2_canvas)).grid(row=2, column=1, sticky=W, pady=(0, 150), padx=50)
    Button(it2_canvas, text='Back', width=10, height=3, command=lambda: home_screen(it2_canvas)).grid(row=2, column=2, sticky=W, pady=(0, 150), padx=50)
    mainloop()


def toystory(canvas):
    canvas.destroy()
    user32 = ctypes.windll.user32
    w = str(user32.GetSystemMetrics(0))
    h = str(user32.GetSystemMetrics(1))
    trailername = "TS"
    toystory_canvas = Tk()
    toystory_canvas.geometry(w+'x'+h)
    toystory_canvas.configure(background='dark grey')
    toystory_canvas.title("Toy Story 4 (2019)")
    toystory_canvas.grid_rowconfigure(0, weight=1)
    toystory_canvas.grid_rowconfigure(2, weight=1)
    toystory_canvas.grid_columnconfigure(0, weight=1)
    toystory_canvas.grid_columnconfigure(2, weight=1)

    container6 = Canvas(toystory_canvas, width=270, height=400)
    imgToystoryOG = PhotoImage(file="toystory4.png")
    imgToystoryDisplay = imgToystoryOG.zoom(2, 2)
    container6.grid(row=1, column=0, pady=10)
    container6.create_image(1, 1, anchor=NW, image=imgToystoryDisplay)

    toystorytext = Text(toystory_canvas, height=15, width=60)
    toystorytext.insert(END,
                   "Title: Toy Story 4 \nRunning length: 114 mins \nRating: U \nScreen type: 2D \n\nSynopsis: Sheriff Woody and Buzz Lightyear, among their other toy friends, have found new appreciation after being given by Andy to Bonnie. They are introduced to Forky, a spork that has been made into a toy, and they soon embark on a road trip adventure alongside old and new friends.")
    toystorytext.grid(row=1, column=0, columnspan=3, padx=(100,0))
    Button(toystory_canvas, text='Trailer', width=10, height=3, command=lambda: video(trailername)).grid(row=2, column=0, sticky=E,pady=(0, 150), padx=50)
    Button(toystory_canvas, text='Book Now', width=20, height=3, command=lambda: loginHomeScreen(toystory_canvas)).grid(row=2, column=1, sticky=W,pady=(0, 150), padx=50)
    Button(toystory_canvas, text='Back', width=10, height=3, command=lambda: home_screen(toystory_canvas)).grid(row=2, column=2, sticky=W, pady=(0, 150), padx=50)
    mainloop()


def legomovie(canvas):
    canvas.destroy()
    user32 = ctypes.windll.user32
    w = str(user32.GetSystemMetrics(0))
    h = str(user32.GetSystemMetrics(1))
    trailername = "LM"
    legomovie_canvas = Tk()
    legomovie_canvas.geometry(w+'x'+h)
    legomovie_canvas.configure(background='dark grey')
    legomovie_canvas.title("The LEGO Movie 2 (2019)")
    legomovie_canvas.grid_rowconfigure(0, weight=1)
    legomovie_canvas.grid_rowconfigure(2, weight=1)
    legomovie_canvas.grid_columnconfigure(0, weight=1)
    legomovie_canvas.grid_columnconfigure(2, weight=1)

    container7 = Canvas(legomovie_canvas, width=270, height=400)
    imgLegomovieOG = PhotoImage(file="legomovie2.png")
    imgLegomovieDisplay = imgLegomovieOG.zoom(2,2)
    container7.grid(row=1, column=0, pady=10)
    container7.create_image(1, 1, anchor=NW, image=imgLegomovieDisplay)

    legomovietext = Text(legomovie_canvas, height=15, width=60)
    legomovietext.insert(END,
                        "Title: The LEGO Movie 2 \nRunning length: 90 mins \nRating: U \nScreen type: 2D \n\nSynopsis: The citizens of Bricksburg face a dangerous new threat when LEGO DUPLO invaders from outer space start to wreck everything in their path. The battle to defeat the enemy and restore harmony to the LEGO universe takes Emmet, Lucy, Batman and the rest of their friends to faraway, unexplored worlds that test their courage and creativity.")
    legomovietext.grid(row=1, column=0, columnspan=3, padx=(100,0))
    Button(legomovie_canvas, text='Trailer', width=10, height=3,
           command=lambda: video(trailername)).grid(row=2, column=0, sticky=E, pady=(0, 150), padx=50)
    Button(legomovie_canvas, text='Book Now', width=20, height=3, command=lambda: loginHomeScreen(legomovie_canvas)).grid(row=2, column=1,sticky=W, pady=(0, 150),padx=50)
    Button(legomovie_canvas, text='Back', width=10, height=3, command=lambda: home_screen(legomovie_canvas)).grid(row=2, column=2, sticky=W, pady=(0, 150), padx=50)
    mainloop()

def video(trailername):         #determines which link is opened in the web browser depending which film is being viewed
    if trailername == "TS":
        webbrowser.open("https://www.youtube.com/watch?v=LDXYRzerjzU")
    if trailername == "LM":
        webbrowser.open("https://www.youtube.com/watch?v=11K013qpRR4")
    if trailername == "IT":
        webbrowser.open("https://www.youtube.com/watch?v=OvfCQ2g4s0s")
    if trailername == "DU":
        webbrowser.open("https://www.youtube.com/watch?v=7NiYVoqBt-8")
    if trailername == "GL":
        webbrowser.open("https://www.youtube.com/watch?v=95ghQs5AmNk")
    if trailername == "AV":
        webbrowser.open("https://www.youtube.com/watch?v=hA6hldpSTF8")


def loginHomeScreen(canvas):            #screen to log in from
    canvas.destroy()
    user32 = ctypes.windll.user32
    w = str(user32.GetSystemMetrics(0))
    h = str(user32.GetSystemMetrics(1))
    loginHomeScreen_canvas = Tk()
    loginHomeScreen_canvas.geometry(w+'x'+h)
    loginHomeScreen_canvas.configure(background='dark grey')
    loginHomeScreen_canvas.title("Login")
    loginHomeScreen_canvas.grid_rowconfigure(0, weight=1)
    loginHomeScreen_canvas.grid_rowconfigure(2, weight=1)
    loginHomeScreen_canvas.grid_columnconfigure(0, weight=1)
    loginHomeScreen_canvas.grid_columnconfigure(2, weight=1)

    container = Canvas(loginHomeScreen_canvas, width=280, height=130)
    imgLogoOG = PhotoImage(file="logo.png")
    imgLogoDisplay = imgLogoOG.subsample(2,2)
    container.grid(row=1, column=1, pady=(0, 100))
    container.create_image(1, 1, anchor=NW, image=imgLogoDisplay)

    Label(loginHomeScreen_canvas, font=("Arial", 30), text="Login To Your MovieMania Account", fg="purple", anchor='center').grid(row=0,
                                                                                                column=1, sticky=W)
    Button(loginHomeScreen_canvas, text='Customer', width=20, height=5, command=lambda: customerLogin(loginHomeScreen_canvas)).grid(row=2, column=0,
                                                                                                      sticky=E, pady=(0, 200),
                                                                                                      padx=50)
    Button(loginHomeScreen_canvas, text='Staff', width=20, height=5, command=lambda: staffLogin(loginHomeScreen_canvas)).grid(row=2, column=1, pady=(0,200),
                                                                                                padx=50)
    Button(loginHomeScreen_canvas, text='Manager', width=20, height=5, command=lambda: managerLogin(loginHomeScreen_canvas)).grid(row=2, column=2,
                                                                                                    sticky=W, pady=(0, 200),
                                                                                                    padx=50)
    Button(loginHomeScreen_canvas, text='Exit', width=5, height=2, command=quit).grid(row=3, column=0, sticky=W, padx=50, pady=(0,100))     #quit stops the program running
    Button(loginHomeScreen_canvas, text='Back', width=5, height=2, command=lambda: home_screen(loginHomeScreen_canvas)).grid(row=3, column=2, sticky=E, padx=50, pady=(0,100))
    mainloop()

def customerLogin(canvas):          #screen for the customers to log in at
    canvas.destroy()
    user32 = ctypes.windll.user32
    w = str(user32.GetSystemMetrics(0))
    h = str(user32.GetSystemMetrics(1))
    customerLogin_canvas = Tk()
    customerLogin_canvas.geometry(w+"x"+h)
    customerLogin_canvas.configure(background='dark grey')
    customerLogin_canvas.title("Customer's Login")
    customerLogin_canvas.grid_rowconfigure(0, weight=1)
    customerLogin_canvas.grid_rowconfigure(2, weight=1)
    customerLogin_canvas.grid_columnconfigure(0, weight=1)
    customerLogin_canvas.grid_columnconfigure(2, weight=1)


    Label(customerLogin_canvas, font=("Arial", 25), text="Customer's Login", fg="purple").grid(row=0, column=0, columnspan=3)
    Label(customerLogin_canvas, font=("Arial", 12), text="Username", width=20, height=2).grid(row=1, column=0, sticky=E, pady=(0,5), padx=10)
    username_entry = Entry(customerLogin_canvas, width=30, font=("Arial", 15))          #entry gives a box the user can type in
    username_entry.grid(row=1, column=1, sticky=E)
    Label(customerLogin_canvas, font=("Arial", 12), text="Password", width=20, height=2).grid(row=2, column=0, sticky=E, pady=(10, 0), padx=10)
    password_entry = Entry(customerLogin_canvas, show="*", width=30, font=("Arial", 15))        #show is used to hide the letters of the password
    password_entry.grid(row=2, column=1, sticky=E)

    Button(customerLogin_canvas, text='Log In', width=20, height=3,
           command=lambda: passwordChecker(customerLogin_canvas, username_entry.get(), password_entry.get())).grid(row=3, column=1, sticky=W, padx=10)      #.get() gets the data that was inputted by the user in the entry box
    Button(customerLogin_canvas, text='Forgot Password', width=20, height=3, command=lambda: forgotPassword(customerLogin_canvas)).grid(row=4, column=1, sticky=W, padx=10)
    Button(customerLogin_canvas, text='Sign Up', width=20, height=3, command=lambda: signUpUsername(customerLogin_canvas)).grid(row=5, column=1,
                                                                                                    sticky=W, padx=10)
    Button(customerLogin_canvas, text='Back', width=20, height=3, command=lambda: home_screen(customerLogin_canvas)).grid(row=6, column=1,
                                                                                                      sticky=W, padx=10, pady=(0,70))

def forgotPassword(canvas):         #if the user has forgotten their password
    canvas.destroy()
    user32 = ctypes.windll.user32
    w = str(user32.GetSystemMetrics(0))
    h = str(user32.GetSystemMetrics(1))
    forgotPassword_canvas = Tk()
    forgotPassword_canvas.geometry(w+"x"+h)
    forgotPassword_canvas.configure(background='dark grey')
    forgotPassword_canvas.title("Forgotten Your Password")
    forgotPassword_canvas.grid_rowconfigure(0, weight=1)
    forgotPassword_canvas.grid_rowconfigure(2, weight=1)
    forgotPassword_canvas.grid_columnconfigure(0, weight=1)
    forgotPassword_canvas.grid_columnconfigure(2, weight=1)

    newPassword = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=10))        #creates a random string of 10 characters that can include uppercase, lowercase and numbers
    Label(forgotPassword_canvas, font=("Arial", 30), text="Forgotten Password", fg="purple").grid(row=0, column=0,
                                                                                               columnspan=3)
    Label(forgotPassword_canvas, text="Username", font=("Arial", 12), width=20, height=2).grid(row=1, column=0, padx=10, pady=(10,0), sticky=E)
    username_entry = Entry(forgotPassword_canvas, width=30, font=("Arial", 15) )
    username_entry.grid(row=1, column=1, sticky=E)

    Button(forgotPassword_canvas, text="Get new password", width=20, height=3, command=lambda: tempPassword(forgotPassword_canvas, newPassword, username_entry.get())).grid(row=2, column=1, sticky=W, padx=10, pady=(5, 0))
    Button(forgotPassword_canvas, text="Back", width=20, height=3, command=lambda: customerLogin(forgotPassword_canvas)).grid(row=3, column=1, sticky=W, padx=10, pady=(0, 150))

def tempPassword(canvas, newPassword, name):            #once the new password has been requested
    canvas.destroy()
    user32 = ctypes.windll.user32
    w = str(user32.GetSystemMetrics(0))
    h = str(user32.GetSystemMetrics(1))
    tempPassword_canvas = Tk()
    tempPassword_canvas.geometry(w+"x"+h)
    tempPassword_canvas.configure(background='dark grey')
    tempPassword_canvas.title("New Temporary Password")
    tempPassword_canvas.grid_rowconfigure(0, weight=1)
    tempPassword_canvas.grid_rowconfigure(2, weight=1)
    tempPassword_canvas.grid_columnconfigure(0, weight=1)
    tempPassword_canvas.grid_columnconfigure(2, weight=1)

    if os.path.isfile(os.getcwd() + "\\customeraccounts\\" + name + ".txt"):
        if name == "":
            messagebox.showinfo("Invalid", "Enter a valid username")        #if the username entered doesnt exist
            forgotPassword(tempPassword_canvas)
        else:                                                               #if it does exist
            userEmail = ""
            file = open(os.getcwd() + "\\customeraccounts\\" + name + ".txt", "r")      #opens the user's text file
            lines = file.readlines()                                                    #reads the lines in the file
            infoLine = lines[1]                                                         #selects line 1
            howmanylines = len(lines)                                                   #sees how many different lines there are in the file
            splitline = infoLine.split(";")                                             #splits the line up so every time ';' appears, it separates
            for split in splitline:                                                     #loop for each of the parts in the line
                if "@" in split:                                                        #looks for the @ symbol
                    userEmail = str(split)                                              #that part of the line is the email
            file.close()
            newPasswordHashed = hasher(newPassword)                                     #sends the password to be hashed
            lines[0] = newPasswordHashed                                                #updates the password line so it has the new one instead
            writingstuff = []
            writingstuff.append(lines[0]+"\n")
            i = 1
            while i < howmanylines:                                                     #gets what is in the file
                writingstuff.append(lines[i])
                i=i+1

            with open(os.getcwd() + "\\customeraccounts\\" + name + ".txt", "w") as file:
                for line in writingstuff:
                    file.write(line)                                                    #writes the same stuff back to the file but this time is has the new password
            file.close()

            port = 587
            smtp_server = "smtp.gmail.com"
            sender_email = "bookings.moviemania@gmail.com"                                  #the company email
            receiver_email = userEmail                                                      #the email found in the usernames file
            password = "QDD87kNV55P#8BC"
            subject = "Forgotton Passsword"
            message = (str(name) + ", here is your new temporary password: \n" + str(newPassword) + "\n You can now log into your account using this password and reset it from within 'My Account'.")

            context = ssl.create_default_context()
            with smtplib.SMTP(smtp_server, port) as server:
                server.ehlo()
                server.starttls(context=context)
                server.ehlo()
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, 'Subject: {}\n\n{}'.format(subject, message))         #contents of the email

            Label(tempPassword_canvas, width=60, height=10, font=("Arial", 12), text="An email has been sent with a new temporary password. \nUse this to logon to your account. \nYou can reset your password from within 'My Account'.").grid(row=1, column=1, sticky=W, padx=150)
            Button(tempPassword_canvas, text="Ok", width=20, height=3, command=lambda: customerLogin(tempPassword_canvas)).grid(row=12, column=1, sticky=W, padx=(350, 0), pady=(0, 100))
    else:
        messagebox.showinfo("Invalid", "Enter a valid username")            #message box to provide information to the user and so an error doesn't make the whole thing crash
        forgotPassword(tempPassword_canvas)

def signUpUsername(canvas):             #registering for a new account
    canvas.destroy()
    user32 = ctypes.windll.user32
    w = str(user32.GetSystemMetrics(0))
    h = str(user32.GetSystemMetrics(1))
    signUpUsername_canvas = Tk()
    signUpUsername_canvas.geometry(w+"x"+h)
    signUpUsername_canvas.configure(background='dark grey')
    signUpUsername_canvas.title("Sign Up")
    signUpUsername_canvas.grid_rowconfigure(0, weight=1)
    signUpUsername_canvas.grid_rowconfigure(2, weight=1)
    signUpUsername_canvas.grid_columnconfigure(0, weight=1)
    signUpUsername_canvas.grid_columnconfigure(2, weight=1)

    Label(signUpUsername_canvas, font=("Arial", 30), text="Create a MovieMania Account", fg="purple", anchor='center').grid(row=0, column=0, columnspan=3)
    Label(signUpUsername_canvas, text="Username", font=("Arial", 12), width=20, height=2).grid(row=1, column=0, sticky=E, padx=10)
    username_entry = Entry(signUpUsername_canvas, width=30, font=("Arial", 15))
    username_entry.grid(row=1, column=1, sticky=E)
    Label(signUpUsername_canvas, text="Password",  font=("Arial", 12), width=20, height=2).grid(row=2, column=0, sticky=E, padx=10)
    password1_entry = Entry(signUpUsername_canvas,  show="*",  width=30, font=("Arial", 15))
    password1_entry.grid(row=2, column=1, sticky=E)
    Label(signUpUsername_canvas, text="Confirm Password",  font=("Arial", 12), width=20, height=2).grid(row=3, column=0, sticky=E, padx=10)
    password2_entry = Entry(signUpUsername_canvas,  show="*", width=30, font=("Arial", 15))
    password2_entry.grid(row=3, column=1, sticky=E)

    Button(signUpUsername_canvas, text='Back', width=20, height=3, command=lambda: customerLogin(signUpUsername_canvas)).grid(row=5, column=1,
                                                                                                   sticky=W, padx=10, pady=(0, 100))
    Button(signUpUsername_canvas, text='Next', width=20, height=3, command=lambda: signUpCheck(signUpUsername_canvas, username_entry.get(), password1_entry.get(), password2_entry.get())).grid(row=4,
                                                                                                          column=1,
                                                                                                          sticky=W,
                                                                                                          padx=10, pady=(50, 10))

def signUpCheck(canvas,username, password1, password2):                 #checking the new account is valid to be made

    if username == "" or password1 == "" or password2 == "":            #checks if the boxes were left empty
        messagebox.showinfo("Invalid", "Enter a valid username/password")
    else:
        if re.match("^[a-zA-Z0-9_.-]+$", username):                     #checks that the username doesn't include special keys (upper, lower, digits only)
            if password1 == password2:                                  #checks the two passwords entered match each other
                if os.path.isfile(os.getcwd()+"\\customeraccounts\\"+username+".txt"):
                    messagebox.showinfo("Username unavailable", "Username is already taken")
                else:
                    if not os.path.isdir(os.getcwd()+"\\customeraccounts"):
                        os.makedirs(os.getcwd()+"\\customeraccounts")
                    file = open(os.getcwd()+"\\customeraccounts\\"+username+".txt", "w")            #creates a new text file for the username
                    file.write(hasher(password1))                                                   #sends the password to get hashed and writes this result to the file
                    file.close()
                    signUpDetails(canvas, username)

            else:
                messagebox.showinfo("Incorrect Password", "Passwords do not match")
        else:
            messagebox.showinfo("Invalid", "Only use letters and numbers in the username")



def signUpDetails(canvas, username):            #entering personal details to sign up for an account
    canvas.destroy()
    user32 = ctypes.windll.user32
    w = str(user32.GetSystemMetrics(0))
    h = str(user32.GetSystemMetrics(1))
    signUpDetails_canvas = Tk()
    signUpDetails_canvas.geometry(w+'x'+h)
    signUpDetails_canvas.configure(background='dark grey')
    signUpDetails_canvas.title("Sign Up")
    signUpDetails_canvas.grid_rowconfigure(0, weight=1)
    signUpDetails_canvas.grid_rowconfigure(11, weight=1)
    signUpDetails_canvas.grid_columnconfigure(0, weight=1)
    signUpDetails_canvas.grid_columnconfigure(2, weight=1)

    Label(signUpDetails_canvas, font=("Arial", 20), text="Create a MovieMania Account \n Enter Personal Details",
          fg="purple", anchor='center').grid(
        row=0, column=0, columnspan=8)              #columnspan makes it spread across multiple columns
    Label(signUpDetails_canvas, width=20, height=2, font=("Arial", 12), text="Title").grid(row=1, column=0, sticky=E,
                                                                                           pady=0, padx=10)
    titleMenu = ttk.Combobox(signUpDetails_canvas, font=("Arial", 12), width=28, values=("Mr", "Mrs", "Miss", "Ms"))            #drop down box with prepopulated selections
    titleMenu.grid(row=1, column=1, columnspan=5, sticky=W)
    titleMenu.current(0)            #sets what the default drop down menu box selection is
    Label(signUpDetails_canvas, width=20, height=2, font=("Arial", 12), text="Name").grid(row=2, column=0, sticky=E,
                                                                                          pady=0, padx=10)
    Name_entry = Entry(signUpDetails_canvas, width=30, font=("Arial", 12))
    Name_entry.grid(row=2, column=1, columnspan=5, sticky=W)
    Label(signUpDetails_canvas, width=20, height=2, font=("Arial", 12), text="Surname").grid(row=3, column=0, sticky=E,
                                                                                             pady=0, padx=10)
    Surname_entry = Entry(signUpDetails_canvas, width=30, font=("Arial", 12))
    Surname_entry.grid(row=3, column=1, columnspan=5, sticky=W)
    Label(signUpDetails_canvas, width=20, height=2, font=("Arial", 12), text="Date of birth").grid(row=4, column=0,
                                                                                                   sticky=E, pady=0,
                                                                                                   padx=10)
    Label(signUpDetails_canvas, text="/").grid(row=4, column=2, sticky=W)
    Label(signUpDetails_canvas, text="/").grid(row=4, column=4, sticky=W)
    day_entry = Entry(signUpDetails_canvas, width=5, font=("Arial", 12))
    day_entry.grid(row=4, column=1, sticky=W)
    month_entry = Entry(signUpDetails_canvas, width=5, font=("Arial", 12))
    month_entry.grid(row=4, column=3, sticky=W)
    year_entry = Entry(signUpDetails_canvas, width=10, font=("Arial", 12))
    year_entry.grid(row=4, column=5, sticky=W)
    Label(signUpDetails_canvas, width=20, height=2, font=("Arial", 12), text="Address line 1").grid(row=5, column=0,
                                                                                                    sticky=E, pady=0,
                                                                                                    padx=10)
    Address1_entry = Entry(signUpDetails_canvas, width=30, font=("Arial", 12))
    Address1_entry.grid(row=5, column=1, columnspan=5, sticky=W)
    Label(signUpDetails_canvas, width=20, height=2, font=("Arial", 12), text="Address line 2").grid(row=6, column=0,
                                                                                                    sticky=E, pady=0,
                                                                                                    padx=10)
    Address2_entry = Entry(signUpDetails_canvas, width=30, font=("Arial", 12))
    Address2_entry.grid(row=6, column=1, columnspan=5, sticky=W)
    Label(signUpDetails_canvas, width=20, height=2, font=("Arial", 12), text="Postcode").grid(row=7, column=0, sticky=E,
                                                                                              pady=0, padx=10)
    Postcode_entry = Entry(signUpDetails_canvas, width=30, font=("Arial", 12))
    Postcode_entry.grid(row=7, column=1, columnspan=5, sticky=W)
    Label(signUpDetails_canvas, width=20, height=2, font=("Arial", 12), text="Email address").grid(row=8, column=0,
                                                                                                   sticky=E, pady=0,
                                                                                                   padx=10)
    Email_entry = Entry(signUpDetails_canvas, width=30, font=("Arial", 12))
    Email_entry.grid(row=8, column=1, columnspan=5, sticky=W)
    Label(signUpDetails_canvas, width=20, height=2, font=("Arial", 12), text="Mobile number").grid(row=9, column=0,
                                                                                                   sticky=E, pady=0,
                                                                                                   padx=10)
    Mobile_entry = Entry(signUpDetails_canvas, width=30, font=("Arial", 12))
    Mobile_entry.grid(row=9, column=1, columnspan=5, sticky=W)

    Button(signUpDetails_canvas, width=20, height=3, text='Submit',
           command=lambda: addinfo(username, signUpDetails_canvas, titleMenu.get(), Name_entry.get(),
                                   Surname_entry.get(),
                                   day_entry.get(), month_entry.get(), year_entry.get(), Address1_entry.get(),
                                   Address2_entry.get(), Postcode_entry.get(),
                                   Email_entry.get(), Mobile_entry.get())).grid(row=10, column=2, sticky=W, pady=(10, 10))
    Button(signUpDetails_canvas, width=20, height=3, text='Back',
           command=lambda: signUpBack(signUpDetails_canvas, username)).grid(row=11, column=2,
                                                                   sticky=W,
                                                                   pady=(0, 100))

def signUpBack(canvas, username):           #if the user backs out of creating an account
    file = os.getcwd() + "\\customeraccounts\\" + username + ".txt"
    os.remove(file)                         #the file is removed from the system
    loginHomeScreen(canvas)

def addinfo(username, canvas, title, Name, Surname, day, month, year, Address1, Address2, Postcode, Email, Mobile):        #checking the details are valid
    nameValid = False
    if not Name.isalpha():            #checkings it only letters
        messagebox.showinfo("Invalid", "'First name' entered is not valid.")
    else:
        nameValid = True

    surnameValid = False
    if not Surname.isalpha():
        messagebox.showinfo("Invalid", "'Surname' entered is not valid.")
    else:
        surnameValid = True

    yearValid = False
    monthValid = False
    dayValid = False
    if year.isdigit():             #checkings its numbers
        year = int(year)           #turning the variable into an integer so it can be compared to other numbers using > and <
        if year < 1910 or year > 2018:
            messagebox.showinfo("Invalid", "'DOB' entered is not valid.")
        else:
            yearValid = True
            if month.isdigit():
                month = int(month)
                if month < 1 or month > 12:
                    messagebox.showinfo("Invalid", "'DOB' entered is not valid.")
                else:
                    monthValid = True
                    if day.isdigit():
                        day = int(day)
                        if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:            #days available depends which month it is
                            if day < 1 or day > 31:
                                messagebox.showinfo("Invalid", "'DOB' entered is not valid.")
                            else:
                                dayValid = True
                        if month == 2:
                            if day < 1 or day > 28:
                                messagebox.showinfo("Invalid", "'DOB' entered is not valid.")
                            else:
                                dayValid = True
                        if month == 4 or month == 6 or month == 9 or month == 11:
                            if day < 1 or day > 30:
                                messagebox.showinfo("Invalid", "'DOB' entered is not valid.")
                            else:
                                dayValid = True
                    else:
                        messagebox.showinfo("Invalid", "'DOB' entered is not valid.")
            else:
                messagebox.showinfo("Invalid", "'DOB' entered is not valid.")
    else:
        messagebox.showinfo("Invalid", "'DOB' entered is not valid.")

    address1Valid = False
    if len(Address1) > 20 or len(Address1) < 1:
        messagebox.showinfo("Invalid", "'Address 1' entered is not valid.")
    else:
        address1Valid = True

    address2Valid = False
    if len(Address2) > 20 or len(Address2) < 1:
        messagebox.showinfo("Invalid", "'Address 2' entered is not valid.")
    else:
        address2Valid = True

    postcodeValid = False
    postcode = Postcode.upper()
    if len(postcode) == 6 or len(postcode) == 7 or len(postcode) == 8:
        postcodeValid = True
    else:
        messagebox.showinfo("Invalid", "'Postcode' entered is not valid.")

    emailValid = False
    email = Email.replace(" ", "")
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):           #checks its in the correct format for an email, including @ and .
        messagebox.showinfo("Invalid", "'Email' entered is not valid.")
    else:
        emailValid = True

    mobileValid = False
    if Mobile.isdigit():
        if len(Mobile) != 11:
            messagebox.showinfo("Invalid", "'Mobile' entered is not valid.")
        else:
            mobileValid = True
    else:
        messagebox.showinfo("Invalid", "'Mobile' entered is not valid.")

    if nameValid==True and surnameValid==True and dayValid==True and monthValid==True and yearValid==True and address1Valid==True and address2Valid==True and postcodeValid==True and emailValid==True and mobileValid==True:
        DOB = str(day) + "/" + str(month) + "/" + str(year)         #puts the dob in the usual format

        o = open(os.getcwd()+"\\customeraccounts\\"+username+".txt", "a")         #adds the information to the user's file if everythng is valid
        o.write("\n" + title + ";" + Name + ";" + Surname + ";" + DOB + ";" + Address1 + ";" + Address2 + ";" + postcode + ";" + Email + ";" + Mobile + "\n")
        o.close()
        customerLogin(canvas)
    else:
        messagebox.showinfo("Invalid", "Enter valid details")


def customerHomeScreen(name, canvas):            #customer home screen once logged in
    canvas.destroy()
    user32 = ctypes.windll.user32
    w = str(user32.GetSystemMetrics(0))
    h = str(user32.GetSystemMetrics(1))
    customerHome_canvas = Tk()
    customerHome_canvas.geometry(w+'x'+h)
    customerHome_canvas.configure(background='dark grey')
    customerHome_canvas.title("Customer Home")
    customerHome_canvas.grid_rowconfigure(0, weight=1)
    customerHome_canvas.grid_rowconfigure(2, weight=1)
    customerHome_canvas.grid_columnconfigure(0, weight=1)
    customerHome_canvas.grid_columnconfigure(2, weight=1)

    Label(customerHome_canvas, font=("Arial", 30), text="Welcome To Your MovieMania Account", fg="purple", anchor='center').grid(row=0,
                                                                                                column=0,  columnspan=5)
    Button(customerHome_canvas, text='Book Tickets', width=20, height=3, command=lambda: bookTicket(name, customerHome_canvas)).grid(row=1, column=0, pady=10,
                                                                                                      padx=10)
    Button(customerHome_canvas, text='Refreshments', width=20, height=3, command=lambda: foodHome(customerHome_canvas, name, upcomingScreeningsList)).grid(row=1, column=1, pady=10,
                                                                                                padx=10)
    Button(customerHome_canvas, text='My Orders', width=20, height=3, command=lambda: viewMyOrders(name, customerHome_canvas)).grid(row=1,
                                                                                                           column=2,
                                                                                                           pady=10,
                                                                                                           padx=10)
    Button(customerHome_canvas, text='My Account', width=20, height=3, command=lambda: viewMyAccount(name, customerHome_canvas)).grid(row=1, column=3, pady=10,
                                                                                                    padx=10)

    Button(customerHome_canvas, text='Exit', width=15, height=2, command=quit).grid(row=3, column=0, sticky=W, padx=(100, 0))
    Button(customerHome_canvas, text='Logout', width=15, height=2, command=lambda: home_screen(customerHome_canvas)).grid(row=3, column=4, sticky=E, padx=(0, 100))

    file = open(os.getcwd() + "\\customeraccounts\\" + name + ".txt", "r")
    lines = file.readlines()
    howmanylines = len(lines)
    hasBeenDate = True
    hasBeenTime = True
    upcomingScreeningsList = []                                                    #list of orders that havent been yet
    upcomingScreenings = Listbox(customerHome_canvas, width=40, height=10)         #box that items can be added to
    i = 2
    while i < howmanylines:
        orderLine = lines[i]
        splitline = orderLine.split(";")
        order = i - 1
        film = splitline[1]+" "
        date = splitline[2]
        time = splitline[3]
        if datetime.strptime(date.strip(), '%d/%m/%y') < dt.datetime.today():       #checks if the date has already passed
            hasBeenDate = False
        if datetime.strptime(time.strip(), '%H:%M') < dt.datetime.now():            #checks if the time has already passed
            hasBeenTime = False
        if hasBeenDate == False and hasBeenTime == False:
            screening = film + date + time
            upcomingScreeningsList.append(screening)                                #adds to the list
            upcomingScreenings.insert(END, screening)                               #adds to the list box
        i =i+1
    file.close()

    if not upcomingScreeningsList:
        upcomingScreenings.insert(END, "You have no upcoming screenings,")           #adds text to list box
        upcomingScreenings.insert(END, "click above to BOOK NOW")

    Label(customerHome_canvas, font=("Arial", 20), text=("Upcoming Bookings")).grid(row=2, column=0, columnspan=3, padx=(300, 0))
    upcomingScreenings.grid(row=3, column=0, columnspan=3, padx=(300,0), pady=(0,150))

    mainloop()


def get_usernames():           #gets a list of all of the usernames on the system
    usernames = []
    files = os.listdir(os.getcwd()+"\\customeraccounts")
    for file in files:
        file = os.path.splitext(file)[0]
        usernames.append(file)
    return usernames           #sends the resulting list

def get_usernamesStaff():      #same but for staff employee numbers
    usernames = []
    files = os.listdir(os.getcwd()+"\\staffaccounts")
    for file in files:
        file = os.path.splitext(file)[0]
        usernames.append(file)
    return usernames


def hasher(password):           #applies a hash to the password given
    salt = uuid.uuid4().hex     #uuid is used to generate a random number
    return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt               #adds the salt to the password hashed using sha256 and sends it back


def checker(hashed_password, user_password):            #checks if the password matches that in the file, the hashed versions are compared
    password, salt = hashed_password.split(':')
    return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()


def passwordChecker(canvas, username, password):        #checks if the login details are correct
    pchecker = os.getcwd()+"\\customeraccounts\\"+username+".txt"
    if os.path.isfile(os.getcwd()+"\\customeraccounts\\"+username+".txt"):      #checks the username exists
        f = open(os.getcwd()+"\\customeraccounts\\"+username+".txt")
        lines = f.readlines()
        passwordtocheck = lines[0].strip()                                      #gets the saved hashed password from the file
        if checker(passwordtocheck, password):                                  #calls the function to check the password matches
            customerHomeScreen(username, canvas)

        else:
            messagebox._show("Incorrect Password", "Password is incorrect")
        f.close()
    else:
        messagebox._show("Incorrect Username", "Username doesn't exist")


def bookTicket(name, canvas):            #booking a ticket
    canvas.destroy()
    user32 = ctypes.windll.user32
    w = str(user32.GetSystemMetrics(0))
    h = str(user32.GetSystemMetrics(1))
    bookTicket_canvas = Tk()
    bookTicket_canvas.geometry(w+'x'+h)
    bookTicket_canvas.configure(background='dark grey')
    bookTicket_canvas.title("Book Tickets")
    bookTicket_canvas.grid_rowconfigure(0, weight=1)
    bookTicket_canvas.grid_rowconfigure(2, weight=1)
    bookTicket_canvas.grid_columnconfigure(0, weight=1)
    bookTicket_canvas.grid_columnconfigure(2, weight=1)

    Label(bookTicket_canvas, font=("Arial", 30), fg="purple", text="Book Tickets \nSelect Film").grid(row=0, column=0,
                                                                                                       columnspan=3)

    avengersp = Button(bookTicket_canvas)
    photo1 = PhotoImage(file="avengers4.png")
    avengersp.config(image=photo1, width="130", height="200", activebackground="black", bg="black", bd=0,
                     command=lambda: bookAvengers4(name, bookTicket_canvas))
    avengersp.grid(row=1, column=0, padx=10, pady=10)

    glassp = Button(bookTicket_canvas)
    photo2 = PhotoImage(file="glass.png")
    glassp.config(image=photo2, width="130", height="200", activebackground="black", bg="black", bd=0,
                  command=lambda: bookGlass(name, bookTicket_canvas))
    glassp.grid(row=1, column=1, padx=(50,0), pady=10)

    dumbop = Button(bookTicket_canvas)
    photo3 = PhotoImage(file="dumbo.png")
    dumbop.config(image=photo3, width="130", height="200", activebackground="black", bg="black", bd=0,
                  command=lambda: bookDumbo(name, bookTicket_canvas))
    dumbop.grid(row=1, column=2, padx=10, pady=10)

    itp = Button(bookTicket_canvas)
    photo4 = PhotoImage(file="it2.png")
    itp.config(image=photo4, width="130", height="200", activebackground="black", bg="black", bd=0,
               command=lambda: bookIt2(name, bookTicket_canvas))
    itp.grid(row=2, column=0, padx=10, pady=10)

    toystoryp = Button(bookTicket_canvas)
    photo5 = PhotoImage(file="toystory4.png")
    toystoryp.config(image=photo5, width="130", height="200", activebackground="black", bg="black", bd=0,
                     command=lambda: bookToystory(name, bookTicket_canvas))
    toystoryp.grid(row=2, column=1, padx=(50, 0), pady=10)

    legomoviep = Button(bookTicket_canvas)
    photo6 = PhotoImage(file="legomovie2.png")
    legomoviep.config(image=photo6, width="130", height="200", activebackground="black", bg="black", bd=0,
                      command=lambda: bookLegomovie(name, bookTicket_canvas))
    legomoviep.grid(row=2, column=2, padx=10, pady=10)

    Button(bookTicket_canvas, width=15, height=2, text='Back', command=lambda: customerHomeScreen(name, bookTicket_canvas)).grid(row=3,
                                                                                                             column=2, pady=(10,100), padx=(0,100), sticky=E)

    mainloop()

def bookAvengers4(name, canvas):        #booking an avengers screening
    canvas.destroy()
    dateList = []
    film = 'Avengers 4'
    path = os.getcwd()+"\\Films\\Avengers 4"
    for file in os.listdir(path):           #looks for all text files within the film's folder
        with open(path+"\\"+file,"r") as f: #opens each for reading
            lines = f.readlines()
            dateList.append(lines[0].replace("-","/").strip()+" "+lines[1].replace("-", ":").strip()+" "+lines[2].strip()+" "+lines[3].strip()) #changes the format so it looks better then appends to the list
            f.close()
    trailername = "AV"
    user32 = ctypes.windll.user32
    w = str(user32.GetSystemMetrics(0))
    h = str(user32.GetSystemMetrics(1))
    bookAvengers_canvas = Tk()
    bookAvengers_canvas.geometry(w + 'x' + h)
    bookAvengers_canvas.configure(background='dark grey')
    bookAvengers_canvas.title("Avengers 4 (2019)")
    bookAvengers_canvas.grid_rowconfigure(0, weight=1)
    bookAvengers_canvas.grid_rowconfigure(2, weight=1)
    bookAvengers_canvas.grid_columnconfigure(0, weight=1)
    bookAvengers_canvas.grid_columnconfigure(2, weight=1)

    container2 = Canvas(bookAvengers_canvas, width=130, height=200)
    imgAvengersOG = PhotoImage(file="avengers4.png")
    imgAvengersDisplay = imgAvengersOG.zoom(1, 1)
    container2.grid(row=1, column=0, rowspan=4, sticky=W, padx=(150, 0), pady=(0, 50))
    container2.create_image(1, 1, anchor=NW, image=imgAvengersDisplay)

    avengerstext = Text(bookAvengers_canvas, height=7, width=30, font=("Arial", 12))
    avengerstext.insert(END,
                        "Title: Avengers 4 - Endgame \n\nRunning length: 180 mins \n\nRating: 12 \n\nScreen type: 2D and 3D")
    avengerstext.grid(row=3, column=0, rowspan=4, padx=(100, 0), sticky=W, pady=(50, 0))

    Label(bookAvengers_canvas, font=("Arial", 30), fg="purple", text="Book Tickets").grid(row=0, column=0, columnspan=3,
                                                                                          pady=(10, 10))
    Label(bookAvengers_canvas, font=("Arial", 14), text="Film").grid(row=1, column=1, sticky=W, pady=10, padx=10)
    Label(bookAvengers_canvas, font=("Arial", 14), text="Avengers 4").grid(row=1, column=2, sticky=W, padx=(40, 10))

    Label(bookAvengers_canvas, font=("Arial", 14), text="Date").grid(row=2, column=1, sticky=W, pady=(0, 10), padx=10)
    screeningMenu = ttk.Combobox(bookAvengers_canvas, width=30, height=5, font=("Arial", 14))
    screeningMenu["values"] = dateList      #from the text files in the folder
    screeningMenu.grid(row=2, column=2, sticky=W, padx=(40, 10))
    screeningMenu.current(0)

    Label(bookAvengers_canvas, font=("Arial", 14), text="Child Ticket").grid(row=3, column=1, sticky=W, pady=(0, 10),
                                                                             padx=10)
    ticChildMenu = ttk.Combobox(bookAvengers_canvas, font=("Arial", 14), width=30,
                                values=("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"))
    ticChildMenu.grid(row=3, column=2, sticky=W, padx=(40, 10), pady=(0, 10))
    ticChildMenu.current(0)

    Label(bookAvengers_canvas, font=("Arial", 14), text="Student Ticket").grid(row=4, column=1, sticky=W, pady=(0, 10),
                                                                               padx=10)
    ticStudentMenu = ttk.Combobox(bookAvengers_canvas, font=("Arial", 14), width=30,
                                  values=("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"))
    ticStudentMenu.grid(row=4, column=2, sticky=W, padx=(40, 10), pady=(0, 10))
    ticStudentMenu.current(0)

    Label(bookAvengers_canvas, font=("Arial", 14), text="Adult Ticket").grid(row=5, column=1, sticky=W, pady=(0, 10),
                                                                             padx=10)
    ticAdultMenu = ttk.Combobox(bookAvengers_canvas, font=("Arial", 14), width=30,
                                values=("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"))
    ticAdultMenu.grid(row=5, column=2, sticky=W, padx=(40, 10), pady=(0, 10))
    ticAdultMenu.current(0)

    Label(bookAvengers_canvas, font=("Arial", 14), text="Senior Ticket").grid(row=6, column=1, sticky=W, pady=(10, 10),
                                                                              padx=10)
    ticSeniorMenu = ttk.Combobox(bookAvengers_canvas, font=("Arial", 14), width=30,
                                 values=("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"))
    ticSeniorMenu.grid(row=6, column=2, sticky=W, padx=(40, 10), pady=(10, 10))
    ticSeniorMenu.current(0)

    counter = 0

    Button(bookAvengers_canvas, width=13, height=3, font=("Arial", 12), text='Trailer',
           command=lambda: video(trailername)).grid(row=7, column=0, pady=(50, 100), padx=(50, 0))
    Button(bookAvengers_canvas, width=13, height=3, font=("Arial", 12), text='Back',
           command=lambda: bookTicket(name, bookAvengers_canvas)).grid(row=7, column=1, pady=(50, 100))
    Button(bookAvengers_canvas, width=13, height=3, font=("Arial", 12), text='Book',
           command=lambda: addSeat(name, counter, bookAvengers_canvas, film, screeningMenu.get(), ticChildMenu.get(),
                                   ticStudentMenu.get(), ticAdultMenu.get(), ticSeniorMenu.get())).grid(row=7, column=2,
                                                                                                        pady=(50, 100),
                                                                                                        padx=(0, 50))
    mainloop()


def bookGlass(name, canvas):             #booking an avengers screening
    canvas.destroy()
    dateList = []
    film = 'Glass'
    path = os.getcwd()+ "\\Films\\Glass"
    for file in os.listdir(path):
        with open(path + "\\" + file, "r") as f:
            lines = f.readlines()
            dateList.append(lines[0].replace("-", "/").strip() + " " + lines[1].replace("-", ":").strip() + " " + lines[
                2].strip() + " " + lines[3].strip())
            f.close()
    trailername = "GL"
    bookGlass_canvas = Tk()
    user32 = ctypes.windll.user32
    w = str(user32.GetSystemMetrics(0))
    h = str(user32.GetSystemMetrics(1))
    bookGlass_canvas.geometry(w+'x'+h)
    bookGlass_canvas.configure(background='dark grey')
    bookGlass_canvas.title("Glass (2019)")
    bookGlass_canvas.grid_rowconfigure(0, weight=1)
    bookGlass_canvas.grid_rowconfigure(2, weight=1)
    bookGlass_canvas.grid_columnconfigure(0, weight=1)
    bookGlass_canvas.grid_columnconfigure(2, weight=1)

    container2 = Canvas(bookGlass_canvas, width=130, height=200)
    imgGlassOG = PhotoImage(file="glass.png")
    imgGlassDisplay = imgGlassOG.zoom(1, 1)
    container2.grid(row=1, column=0, rowspan=4, sticky=W, padx=(150,0), pady=(0,50))
    container2.create_image(1, 1, anchor=NW, image=imgGlassDisplay)

    glasstext = Text(bookGlass_canvas, height=7, width=30, font=("Arial", 12))
    glasstext.insert(END,
                        "Title: Glass \n\nRunning length: 129 mins \n\nRating: 15 \n\nScreen type: 2D")
    glasstext.grid(row=3, column=0, rowspan=4, padx=(100,0), sticky=W, pady=(50,0))
    Label(bookGlass_canvas, font=("Arial", 30), fg="purple", text="Book Tickets").grid(row=0, column=0, columnspan=3,
                                                                                          pady=(10, 10))

    Label(bookGlass_canvas, font=("Arial", 14), text="Film").grid(row=1, column=1, sticky=W, pady=10, padx=10)
    Label(bookGlass_canvas, font=("Arial", 14), text="Glass").grid(row=1, column=2, sticky=W, padx=(40,10))

    Label(bookGlass_canvas, font=("Arial", 14), text="Date").grid(row=2, column=1, sticky=W, pady=(0,10), padx=10)
    screeningMenu = ttk.Combobox(bookGlass_canvas, width=30, height=5, font=("Arial", 14))
    screeningMenu["values"] = dateList
    screeningMenu.grid(row=2, column=2, sticky=W, padx=(40,10))
    screeningMenu.current(0)

    Label(bookGlass_canvas, font=("Arial", 14), text="Child Ticket").grid(row=3, column=1, sticky=W, pady=(0,10), padx=10)
    ticChildMenu = ttk.Combobox(bookGlass_canvas, font=("Arial", 14), width=30,
                                values=("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"))
    ticChildMenu.grid(row=3, column=2, sticky=W, padx=(40,10), pady=(0,10))
    ticChildMenu.current(0)

    Label(bookGlass_canvas, font=("Arial", 14), text="Student Ticket").grid(row=4, column=1, sticky=W, pady=(0, 10),
                                                                               padx=10)
    ticStudentMenu = ttk.Combobox(bookGlass_canvas, font=("Arial", 14), width=30,
                                  values=("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"))
    ticStudentMenu.grid(row=4, column=2, sticky=W, padx=(40, 10), pady=(0, 10))
    ticStudentMenu.current(0)

    Label(bookGlass_canvas, font=("Arial", 14), text="Adult Ticket").grid(row=5, column=1, sticky=W, pady=(0, 10),
                                                                             padx=10)
    ticAdultMenu = ttk.Combobox(bookGlass_canvas, font=("Arial", 14), width=30,
                                values=("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"))
    ticAdultMenu.grid(row=5, column=2, sticky=W, padx=(40, 10), pady=(0, 10))
    ticAdultMenu.current(0)

    Label(bookGlass_canvas, font=("Arial", 14), text="Senior Ticket").grid(row=6, column=1, sticky=W, pady=(10, 10),
                                                                              padx=10)
    ticSeniorMenu = ttk.Combobox(bookGlass_canvas, font=("Arial", 14), width=30,
                                 values=("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"))
    ticSeniorMenu.grid(row=6, column=2, sticky=W, padx=(40, 10), pady=(10, 10))
    ticSeniorMenu.current(0)

    counter = 0

    Button(bookGlass_canvas, width=13, height=3, font=("Arial", 12), text='Trailer',
           command=lambda: video(trailername)).grid(row=7, column=0, pady=(50, 100), padx=(50, 0))
    Button(bookGlass_canvas, width=13, height=3, font=("Arial", 12), text='Back',
           command=lambda: bookTicket(name, bookGlass_canvas)).grid(row=7, column=1, pady=(50, 100))
    Button(bookGlass_canvas, width=13, height=3, font=("Arial", 12), text='Book',
           command=lambda: addSeat(name, counter, bookGlass_canvas, film, screeningMenu.get(), ticChildMenu.get(),
                                   ticStudentMenu.get(), ticAdultMenu.get(), ticSeniorMenu.get())).grid(row=7, column=2,
                                                                                                        pady=(50, 100),
                                                                                                        padx=(0, 50))

    mainloop()

def bookDumbo(name, canvas):                 #booking a dumbo screening
    canvas.destroy()
    dateList = []
    film = 'Dumbo'
    path = os.getcwd() + "\\Films\\Dumbo"
    for file in os.listdir(path):
        with open(path + "\\" + file, "r") as f:
            lines = f.readlines()
            dateList.append(lines[0].replace("-", "/").strip() + " " + lines[1].replace("-", ":").strip() + " " + lines[
                2].strip() + " " + lines[3].strip())
            f.close()
    trailername = "DU"
    bookDumbo_canvas = Tk()
    user32 = ctypes.windll.user32
    w = str(user32.GetSystemMetrics(0))
    h = str(user32.GetSystemMetrics(1))
    bookDumbo_canvas.geometry(w+'x'+h)
    bookDumbo_canvas.configure(background='dark grey')
    bookDumbo_canvas.title("Dumbo (2019)")
    bookDumbo_canvas.grid_rowconfigure(0, weight=1)
    bookDumbo_canvas.grid_rowconfigure(2, weight=1)
    bookDumbo_canvas.grid_columnconfigure(0, weight=1)
    bookDumbo_canvas.grid_columnconfigure(2, weight=1)

    container2 = Canvas(bookDumbo_canvas, width=130, height=200)
    imgDumboOG = PhotoImage(file="dumbo.png")
    imgDumboDisplay = imgDumboOG.zoom(1, 1)
    container2.grid(row=1, column=0, rowspan=4, sticky=W, padx=(150,0), pady=(0,50))
    container2.create_image(1, 1, anchor=NW, image=imgDumboDisplay)

    dumbotext = Text(bookDumbo_canvas, height=7, width=30, font=("Arial", 12))
    dumbotext.insert(END,
                        "Title: Dumbo \n\nRunning length: 130 mins \n\nRating: PG \n\nScreen type: 2D")
    dumbotext.grid(row=3, column=0, rowspan=4, padx=(100,0), sticky=W, pady=(50,0))
    Label(bookDumbo_canvas, font=("Arial", 30), fg="purple", text="Book Tickets").grid(row=0, column=0, columnspan=3,
                                                                                          pady=(10, 10))
    Label(bookDumbo_canvas, font=("Arial", 14), text="Film").grid(row=1, column=1, sticky=W, pady=10, padx=10)
    Label(bookDumbo_canvas, font=("Arial", 14), text="Dumbo").grid(row=1, column=2, sticky=W, padx=(40, 10))

    Label(bookDumbo_canvas, font=("Arial", 14), text="Date").grid(row=2, column=1, sticky=W, pady=(0, 10), padx=10)
    screeningMenu = ttk.Combobox(bookDumbo_canvas, width=30, height=5, font=("Arial", 14))
    screeningMenu["values"] = dateList
    screeningMenu.grid(row=2, column=2, sticky=W, padx=(40, 10))
    screeningMenu.current(0)

    Label(bookDumbo_canvas, font=("Arial", 14), text="Child Ticket").grid(row=3, column=1, sticky=W, pady=(0, 10),
                                                                             padx=10)
    ticChildMenu = ttk.Combobox(bookDumbo_canvas, font=("Arial", 14), width=30,
                                values=("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"))
    ticChildMenu.grid(row=3, column=2, sticky=W, padx=(40, 10), pady=(0, 10))
    ticChildMenu.current(0)

    Label(bookDumbo_canvas, font=("Arial", 14), text="Student Ticket").grid(row=4, column=1, sticky=W, pady=(0, 10),
                                                                               padx=10)
    ticStudentMenu = ttk.Combobox(bookDumbo_canvas, font=("Arial", 14), width=30,
                                  values=("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"))
    ticStudentMenu.grid(row=4, column=2, sticky=W, padx=(40, 10), pady=(0, 10))
    ticStudentMenu.current(0)

    Label(bookDumbo_canvas, font=("Arial", 14), text="Adult Ticket").grid(row=5, column=1, sticky=W, pady=(0, 10),
                                                                             padx=10)
    ticAdultMenu = ttk.Combobox(bookDumbo_canvas, font=("Arial", 14), width=30,
                                values=("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"))
    ticAdultMenu.grid(row=5, column=2, sticky=W, padx=(40, 10), pady=(0, 10))
    ticAdultMenu.current(0)

    Label(bookDumbo_canvas, font=("Arial", 14), text="Senior Ticket").grid(row=6, column=1, sticky=W, pady=(10, 10),
                                                                              padx=10)
    ticSeniorMenu = ttk.Combobox(bookDumbo_canvas, font=("Arial", 14), width=30,
                                 values=("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"))
    ticSeniorMenu.grid(row=6, column=2, sticky=W, padx=(40, 10), pady=(10, 10))
    ticSeniorMenu.current(0)

    counter = 0

    Button(bookDumbo_canvas, width=13, height=3, font=("Arial", 12), text='Trailer',
           command=lambda: video(trailername)).grid(row=7, column=0, pady=(50, 100), padx=(50, 0))
    Button(bookDumbo_canvas, width=13, height=3, font=("Arial", 12), text='Back',
           command=lambda: bookTicket(name, bookDumbo_canvas)).grid(row=7, column=1, pady=(50, 100))
    Button(bookDumbo_canvas, width=13, height=3, font=("Arial", 12), text='Book',
           command=lambda: addSeat(name, counter, bookDumbo_canvas, film, screeningMenu.get(), ticChildMenu.get(),
                                   ticStudentMenu.get(), ticAdultMenu.get(), ticSeniorMenu.get())).grid(row=7, column=2,
                                                                                                        pady=(50, 100),
                                                                                                        padx=(0, 50))

    mainloop()

def bookIt2(name, canvas):           #booking an it screening
    canvas.destroy()
    dateList = []
    film = 'It 2'
    path = os.getcwd() + "\\Films\\It 2"
    for file in os.listdir(path):
        with open(path + "\\" + file, "r") as f:
            lines = f.readlines()
            dateList.append(lines[0].replace("-", "/").strip() + " " + lines[1].replace("-", ":").strip() + " " + lines[
                2].strip() + " " + lines[3].strip())
            f.close()
    trailername = "IT"
    bookIt2_canvas = Tk()
    user32 = ctypes.windll.user32
    w = str(user32.GetSystemMetrics(0))
    h = str(user32.GetSystemMetrics(1))
    bookIt2_canvas.geometry(w+'x'+h)
    bookIt2_canvas.configure(background='dark grey')
    bookIt2_canvas.title("It - Chapter 2 (2019)")
    bookIt2_canvas.grid_rowconfigure(0, weight=1)
    bookIt2_canvas.grid_rowconfigure(2, weight=1)
    bookIt2_canvas.grid_columnconfigure(0, weight=1)
    bookIt2_canvas.grid_columnconfigure(2, weight=1)

    container2 = Canvas(bookIt2_canvas, width=130, height=200)
    imgItOG = PhotoImage(file="it2.png")
    imgItDisplay = imgItOG.zoom(1, 1)
    container2.grid(row=1, column=0, rowspan=4, sticky=W, padx=(150,0), pady=(0,50))
    container2.create_image(1, 1, anchor=NW, image=imgItDisplay)

    it2text = Text(bookIt2_canvas, height=7, width=30, font=("Arial", 12))
    it2text.insert(END,
                        "Title: It - Chapter 2 \n\nRunning length: 125 mins \n\nRating: 15 \n\nScreen type: 2D")
    it2text.grid(row=3, column=0, rowspan=4, padx=(100,0), sticky=W, pady=(50,0))

    Label(bookIt2_canvas, font=("Arial", 30), fg="purple", text="Book Tickets").grid(row=0, column=0, columnspan=3,
                                                                                          pady=(10, 10))
    Label(bookIt2_canvas, font=("Arial", 14), text="Film").grid(row=1, column=1, sticky=W, pady=10, padx=10)
    Label(bookIt2_canvas, font=("Arial", 14), text="It - Chapter 2").grid(row=1, column=2, sticky=W, padx=(40, 10))

    Label(bookIt2_canvas, font=("Arial", 14), text="Date").grid(row=2, column=1, sticky=W, pady=(0, 10), padx=10)
    screeningMenu = ttk.Combobox(bookIt2_canvas, width=30, height=5, font=("Arial", 14))
    screeningMenu["values"] = dateList
    screeningMenu.grid(row=2, column=2, sticky=W, padx=(40, 10))
    screeningMenu.current(0)

    Label(bookIt2_canvas, font=("Arial", 14), text="Child Ticket").grid(row=3, column=1, sticky=W, pady=(0, 10),
                                                                             padx=10)
    ticChildMenu = ttk.Combobox(bookIt2_canvas, font=("Arial", 14), width=30,
                                values=("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"))
    ticChildMenu.grid(row=3, column=2, sticky=W, padx=(40, 10), pady=(0, 10))
    ticChildMenu.current(0)

    Label(bookIt2_canvas, font=("Arial", 14), text="Student Ticket").grid(row=4, column=1, sticky=W, pady=(0, 10),
                                                                               padx=10)
    ticStudentMenu = ttk.Combobox(bookIt2_canvas, font=("Arial", 14), width=30,
                                  values=("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"))
    ticStudentMenu.grid(row=4, column=2, sticky=W, padx=(40, 10), pady=(0, 10))
    ticStudentMenu.current(0)

    Label(bookIt2_canvas, font=("Arial", 14), text="Adult Ticket").grid(row=5, column=1, sticky=W, pady=(0, 10),
                                                                             padx=10)
    ticAdultMenu = ttk.Combobox(bookIt2_canvas, font=("Arial", 14), width=30,
                                values=("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"))
    ticAdultMenu.grid(row=5, column=2, sticky=W, padx=(40, 10), pady=(0, 10))
    ticAdultMenu.current(0)

    Label(bookIt2_canvas, font=("Arial", 14), text="Senior Ticket").grid(row=6, column=1, sticky=W, pady=(10, 10),
                                                                              padx=10)
    ticSeniorMenu = ttk.Combobox(bookIt2_canvas, font=("Arial", 14), width=30,
                                 values=("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"))
    ticSeniorMenu.grid(row=6, column=2, sticky=W, padx=(40, 10), pady=(10, 10))
    ticSeniorMenu.current(0)

    counter = 0

    Button(bookIt2_canvas, width=13, height=3, font=("Arial", 12), text='Trailer',
           command=lambda: video(trailername)).grid(row=7, column=0, pady=(50, 100), padx=(50, 0))
    Button(bookIt2_canvas, width=13, height=3, font=("Arial", 12), text='Back',
           command=lambda: bookTicket(name, bookIt2_canvas)).grid(row=7, column=1, pady=(50, 100))
    Button(bookIt2_canvas, width=13, height=3, font=("Arial", 12), text='Book',
           command=lambda: addSeat(name, counter, bookIt2_canvas, film, screeningMenu.get(), ticChildMenu.get(),
                                   ticStudentMenu.get(), ticAdultMenu.get(), ticSeniorMenu.get())).grid(row=7, column=2,
                                                                                                        pady=(50, 100),
                                                                                                        padx=(0, 50))
    mainloop()

def bookToystory(name, canvas):                   #booking a toy story screening
    canvas.destroy()
    dateList = []
    film = 'Toy Story 4'
    path = os.getcwd() + "\\Films\\Toy Story 4"
    for file in os.listdir(path):
        with open(path + "\\" + file, "r") as f:
            lines = f.readlines()
            dateList.append(lines[0].replace("-", "/").strip() + " " + lines[1].replace("-", ":").strip() + " " + lines[
                2].strip() + " " + lines[3].strip())
            f.close()
    trailername = "TS"
    bookToystory_canvas = Tk()
    user32 = ctypes.windll.user32
    w = str(user32.GetSystemMetrics(0))
    h = str(user32.GetSystemMetrics(1))
    bookToystory_canvas.geometry(w+'x'+h)
    bookToystory_canvas.configure(background='dark grey')
    bookToystory_canvas.title("Toy Story 4")
    bookToystory_canvas.grid_rowconfigure(0, weight=1)
    bookToystory_canvas.grid_rowconfigure(2, weight=1)
    bookToystory_canvas.grid_columnconfigure(0, weight=1)
    bookToystory_canvas.grid_columnconfigure(2, weight=1)

    container2 = Canvas(bookToystory_canvas, width=130, height=200)
    imgToystoryOG = PhotoImage(file="toystory4.png")
    imgToystoryDisplay = imgToystoryOG.zoom(1, 1)
    container2.grid(row=1, column=0, rowspan=4, sticky=W, padx=(150,0), pady=(0,50))
    container2.create_image(1, 1, anchor=NW, image=imgToystoryDisplay)

    toystorytext = Text(bookToystory_canvas, height=7, width=30, font=("Arial", 12))
    toystorytext.insert(END,
                        "Title: Toy Story 4 \n\nRunning length: 114 mins \n\nRating: U \n\nScreen type: 2D")
    toystorytext.grid(row=3, column=0, rowspan=4, padx=(100,0), sticky=W, pady=(50,0))

    Label(bookToystory_canvas, font=("Arial", 30), fg="purple", text="Book Tickets").grid(row=0, column=0, columnspan=3,
                                                                                          pady=(10, 10))
    Label(bookToystory_canvas, font=("Arial", 14), text="Film").grid(row=1, column=1, sticky=W, pady=10, padx=10)
    Label(bookToystory_canvas, font=("Arial", 14), text="Toy Story 4").grid(row=1, column=2, sticky=W, padx=(40, 10))

    Label(bookToystory_canvas, font=("Arial", 14), text="Date").grid(row=2, column=1, sticky=W, pady=(0, 10), padx=10)
    screeningMenu = ttk.Combobox(bookToystory_canvas, width=30, height=5, font=("Arial", 14))
    screeningMenu["values"] = dateList
    screeningMenu.grid(row=2, column=2, sticky=W, padx=(40, 10))
    screeningMenu.current(0)

    Label(bookToystory_canvas, font=("Arial", 14), text="Child Ticket").grid(row=3, column=1, sticky=W, pady=(0, 10),
                                                                             padx=10)
    ticChildMenu = ttk.Combobox(bookToystory_canvas, font=("Arial", 14), width=30,
                                values=("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"))
    ticChildMenu.grid(row=3, column=2, sticky=W, padx=(40, 10), pady=(0, 10))
    ticChildMenu.current(0)

    Label(bookToystory_canvas, font=("Arial", 14), text="Student Ticket").grid(row=4, column=1, sticky=W, pady=(0, 10),
                                                                               padx=10)
    ticStudentMenu = ttk.Combobox(bookToystory_canvas, font=("Arial", 14), width=30,
                                  values=("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"))
    ticStudentMenu.grid(row=4, column=2, sticky=W, padx=(40, 10), pady=(0, 10))
    ticStudentMenu.current(0)

    Label(bookToystory_canvas, font=("Arial", 14), text="Adult Ticket").grid(row=5, column=1, sticky=W, pady=(0, 10),
                                                                             padx=10)
    ticAdultMenu = ttk.Combobox(bookToystory_canvas, font=("Arial", 14), width=30,
                                values=("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"))
    ticAdultMenu.grid(row=5, column=2, sticky=W, padx=(40, 10), pady=(0, 10))
    ticAdultMenu.current(0)

    Label(bookToystory_canvas, font=("Arial", 14), text="Senior Ticket").grid(row=6, column=1, sticky=W, pady=(10, 10),
                                                                              padx=10)
    ticSeniorMenu = ttk.Combobox(bookToystory_canvas, font=("Arial", 14), width=30,
                                 values=("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"))
    ticSeniorMenu.grid(row=6, column=2, sticky=W, padx=(40, 10), pady=(10, 10))
    ticSeniorMenu.current(0)

    counter = 0

    Button(bookToystory_canvas, width=13, height=3, font=("Arial", 12), text='Trailer',
           command=lambda: video(trailername)).grid(row=7, column=0, pady=(50, 100), padx=(50, 0))
    Button(bookToystory_canvas, width=13, height=3, font=("Arial", 12), text='Back',
           command=lambda: bookTicket(name, bookToystory_canvas)).grid(row=7, column=1, pady=(50, 100))
    Button(bookToystory_canvas, width=13, height=3, font=("Arial", 12), text='Book',
           command=lambda: addSeat(name, counter, bookToystory_canvas, film, screeningMenu.get(), ticChildMenu.get(),
                                   ticStudentMenu.get(), ticAdultMenu.get(), ticSeniorMenu.get())).grid(row=7, column=2,
                                                                                                        pady=(50, 100),
                                                                                                        padx=(0, 50))


    mainloop()

def bookLegomovie(name, canvas):          #booking a lego movie screening
    canvas.destroy()
    dateList = []
    film = 'Lego Movie 2'
    path = os.getcwd() + "\\Films\\Lego Movie 2"
    for file in os.listdir(path):
        with open(path + "\\" + file, "r") as f:
            lines = f.readlines()
            dateList.append(lines[0].replace("-", "/").strip() + " " + lines[1].replace("-", ":").strip() + " " + lines[
                2].strip() + " " + lines[3].strip())
            f.close()
    trailername = "LM"
    bookLegomovie_canvas = Tk()
    user32 = ctypes.windll.user32
    w = str(user32.GetSystemMetrics(0))
    h = str(user32.GetSystemMetrics(1))
    bookLegomovie_canvas.geometry(w+'x'+h)
    bookLegomovie_canvas.configure(background='dark grey')
    bookLegomovie_canvas.title("The LEGO Movie 2 (2019)")
    bookLegomovie_canvas.grid_rowconfigure(0, weight=1)
    bookLegomovie_canvas.grid_rowconfigure(2, weight=1)
    bookLegomovie_canvas.grid_columnconfigure(0, weight=1)
    bookLegomovie_canvas.grid_columnconfigure(2, weight=1)

    container2 = Canvas(bookLegomovie_canvas, width=130, height=200)
    imgLegomovieOG = PhotoImage(file="avengers4.png")
    imgLegomovieDisplay = imgLegomovieOG.zoom(1, 1)
    container2.grid(row=1, column=0, rowspan=4, sticky=W, padx=(150,0), pady=(0,50))
    container2.create_image(1, 1, anchor=NW, image=imgLegomovieDisplay)

    legomovietext = Text(bookLegomovie_canvas, height=7, width=30, font=("Arial", 12))
    legomovietext.insert(END,
                        "Title: The LEGO Movie 2 \n\nRunning length: 90 mins \n\nRating: U \n\nScreen type: 2D")
    legomovietext.grid(row=3, column=0, rowspan=4, padx=(100,0), sticky=W, pady=(50,0))

    Label(bookLegomovie_canvas, font=("Arial", 30), fg="purple", text="Book Tickets").grid(row=0, column=0, columnspan=3,
                                                                                          pady=(10, 10))
    Label(bookLegomovie_canvas, font=("Arial", 14), text="Film").grid(row=1, column=1, sticky=W, pady=10, padx=10)
    Label(bookLegomovie_canvas, font=("Arial", 14), text="The LEGO Movie 2").grid(row=1, column=2, sticky=W, padx=(40, 10))

    Label(bookLegomovie_canvas, font=("Arial", 14), text="Date").grid(row=2, column=1, sticky=W, pady=(0, 10), padx=10)
    screeningMenu = ttk.Combobox(bookLegomovie_canvas, width=30, height=5, font=("Arial", 14))
    screeningMenu["values"] = dateList
    screeningMenu.grid(row=2, column=2, sticky=W, padx=(40, 10))
    screeningMenu.current(0)

    Label(bookLegomovie_canvas, font=("Arial", 14), text="Child Ticket").grid(row=3, column=1, sticky=W, pady=(0, 10),
                                                                             padx=10)
    ticChildMenu = ttk.Combobox(bookLegomovie_canvas, font=("Arial", 14), width=30,
                                values=("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"))
    ticChildMenu.grid(row=3, column=2, sticky=W, padx=(40, 10), pady=(0, 10))
    ticChildMenu.current(0)

    Label(bookLegomovie_canvas, font=("Arial", 14), text="Student Ticket").grid(row=4, column=1, sticky=W, pady=(0, 10),
                                                                               padx=10)
    ticStudentMenu = ttk.Combobox(bookLegomovie_canvas, font=("Arial", 14), width=30,
                                  values=("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"))
    ticStudentMenu.grid(row=4, column=2, sticky=W, padx=(40, 10), pady=(0, 10))
    ticStudentMenu.current(0)

    Label(bookLegomovie_canvas, font=("Arial", 14), text="Adult Ticket").grid(row=5, column=1, sticky=W, pady=(0, 10),
                                                                             padx=10)
    ticAdultMenu = ttk.Combobox(bookLegomovie_canvas, font=("Arial", 14), width=30,
                                values=("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"))
    ticAdultMenu.grid(row=5, column=2, sticky=W, padx=(40, 10), pady=(0, 10))
    ticAdultMenu.current(0)

    Label(bookLegomovie_canvas, font=("Arial", 14), text="Senior Ticket").grid(row=6, column=1, sticky=W, pady=(10, 10),
                                                                              padx=10)
    ticSeniorMenu = ttk.Combobox(bookLegomovie_canvas, font=("Arial", 14), width=30,
                                 values=("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"))
    ticSeniorMenu.grid(row=6, column=2, sticky=W, padx=(40, 10), pady=(10, 10))
    ticSeniorMenu.current(0)

    counter = 0

    Button(bookLegomovie_canvas, width=13, height=3, font=("Arial", 12), text='Trailer',
           command=lambda: video(trailername)).grid(row=7, column=0, pady=(50, 100), padx=(50, 0))
    Button(bookLegomovie_canvas, width=13, height=3, font=("Arial", 12), text='Back',
           command=lambda: bookTicket(name, bookLegomovie_canvas)).grid(row=7, column=1, pady=(50, 100))
    Button(bookLegomovie_canvas, width=13, height=3, font=("Arial", 12), text='Book',
           command=lambda: addSeat(name, counter, bookLegomovie_canvas, film, screeningMenu.get(), ticChildMenu.get(),
                                   ticStudentMenu.get(), ticAdultMenu.get(), ticSeniorMenu.get())).grid(row=7, column=2,
                                                                                                        pady=(50, 100),
                                                                                                        padx=(0, 50))


    mainloop()

def addSeat(name, counter, canvas, film, screening, child, student, adult, senior):           #seating plan
    canvas.destroy()
    addSeat_canvas = Tk()
    user32 = ctypes.windll.user32
    w = str(user32.GetSystemMetrics(0))
    h = str(user32.GetSystemMetrics(1))
    addSeat_canvas.geometry(w+'x'+h)
    addSeat_canvas.configure(background='dark grey')
    addSeat_canvas.title("Choose your seat(s)")
    addSeat_canvas.grid_rowconfigure(0, weight=1)
    addSeat_canvas.grid_rowconfigure(2, weight=1)
    addSeat_canvas.grid_columnconfigure(0, weight=1)
    addSeat_canvas.grid_columnconfigure(2, weight=1)

    bookingFilmsDic = {"Avengers 4": bookAvengers4, "Glass": bookGlass, "Dumbo": bookDumbo, "It 2": bookIt2,
                       "Toy Story 4": bookToystory, "Lego Movie 2": bookLegomovie}                      #dictionary of the films and their functions

    child=int(child)
    student=int(student)
    adult=int(adult)
    senior=int(senior)
    quantity = child+student+adult+senior
    if quantity == 0:           #checks there at least one ticket
        messagebox.showinfo("Invalid", "Select a number of tickets")
        bookingFilmsDic[film](name, addSeat_canvas)         #if not, goes back to the selection page
    else:

        Label(addSeat_canvas, text="SCREEN", fg="white", bg="black", height=4, width=100).grid(row=1, column=0, columnspan=8, pady=(50, 10), padx=(100,10))
        Label(addSeat_canvas, font=("Arial", 15), text="Select "+str(quantity)+" seats", fg="white", bg="black", height=5, width=15).grid(row=1, column=0, columnspan=1, pady=(50,50))
        foundseat=[]
        seatp = PhotoImage(file="seat.png")     #image for a regular seat
        seatSelected = PhotoImage(file="seat selected2.gif")      #image for a seat once the button has been clicked to show its been selected
        seatTaken = PhotoImage(file="seat taken.png")        #image if the seat is unavailable
        counter = IntVar()            #creates a counter to track how many buttons have been clicked/seats have been selected

        seat0A = Button(addSeat_canvas)         #button for each seat
        seat0A.config(image=seatp, width="35", height="35", activebackground="black", bg="black", bd=0, command=lambda: command(0, "0A", name, addSeat_canvas, seatp, seatSelected, seatNum, foundseat, film, screening, child, student, adult, senior, quantity, counter, seat0A))
        seat0A.grid(row=3, column=1, pady=10, padx=(50, 30))

        seatNum = seat0A.config('image')[4]
        seat0B = Button(addSeat_canvas)
        seat0B.config(image=seatp, width="35", height="35", activebackground="black", bg="black", bd=0,
                      command=lambda: command(0, "0B", name, addSeat_canvas, seatp, seatSelected, seatNum, foundseat, film, screening, child, student, adult, senior,
                                              quantity, counter, seat0B))
        seat0B.grid(row=3, column=2, pady=10, padx=(0, 40))

        seat0C = Button(addSeat_canvas)
        seat0C.config(image=seatp, width="35", height="35", activebackground="black", bg="black", bd=0,
                      command=lambda: command(0, "0C", name, addSeat_canvas, seatp, seatSelected, seatNum, foundseat, film, screening, child, student, adult, senior,
                                              quantity, counter, seat0C))
        seat0C.grid(row=3, column=3, pady=10, padx=(0, 120))

        seat0D = Button(addSeat_canvas)
        seat0D.config(image=seatp, width="35", height="35", activebackground="black", bg="black", bd=0,
                      command=lambda: command(0, "0D", name, addSeat_canvas, seatp, seatSelected, seatNum, foundseat, film, screening, child, student, adult, senior,
                                              quantity, counter, seat0D))
        seat0D.grid(row=3, column=4, pady=10, padx=(0, 120))

        seat0E = Button(addSeat_canvas)
        seat0E.config(image=seatp, width="35", height="35", activebackground="black", bg="black", bd=0,
                      command=lambda: command(0, "0E", name, addSeat_canvas, seatp, seatSelected, seatNum, foundseat, film, screening, child, student, adult, senior,
                                              quantity, counter, seat0E))
        seat0E.grid(row=3, column=5, pady=10, padx=(0, 300))

        seat1A = Button(addSeat_canvas)
        seat1A.config(image=seatp, width="35", height="35", activebackground="black", bg="black", bd=0,
                      command=lambda: command(1, "1A", name, addSeat_canvas, seatp, seatSelected, seatNum, foundseat, film, screening, child, student, adult, senior,
                                              quantity, counter, seat1A))
        seat1A.grid(row=4, column=1, pady=10, padx=(50, 30))

        seat1B = Button(addSeat_canvas)
        seat1B.config(image=seatp, width="35", height="35", activebackground="black", bg="black", bd=0,
                      command=lambda: command(1, "1B", name, addSeat_canvas, seatp, seatSelected, seatNum, foundseat, film, screening, child, student, adult, senior,
                                              quantity, counter, seat1B))
        seat1B.grid(row=4, column=2, pady=10, padx=(0, 40))

        seat1C = Button(addSeat_canvas)
        seat1C.config(image=seatp, width="35", height="35", activebackground="black", bg="black", bd=0,
                      command=lambda: command(1, "1C", name, addSeat_canvas, seatp, seatSelected, seatNum, foundseat, film, screening, child, student, adult, senior,
                                              quantity, counter, seat1C))
        seat1C.grid(row=4, column=3, pady=10, padx=(0, 120))

        seat1D = Button(addSeat_canvas)
        seat1D.config(image=seatp, width="35", height="35", activebackground="black", bg="black", bd=0,
                      command=lambda: command(1, "1D", name, addSeat_canvas, seatp, seatSelected, seatNum, foundseat, film, screening, child, student, adult, senior,
                                              quantity, counter, seat1D))
        seat1D.grid(row=4, column=4, pady=10, padx=(0, 120))

        seat1E = Button(addSeat_canvas)
        seat1E.config(image=seatp, width="35", height="35", activebackground="black", bg="black", bd=0,
                      command=lambda: command(1, "1E", name, addSeat_canvas, seatp, seatSelected, seatNum, foundseat, film, screening, child, student, adult, senior,
                                              quantity, counter, seat1E))
        seat1E.grid(row=4, column=5, pady=10, padx=(0, 300))

        seat2A = Button(addSeat_canvas)
        seat2A.config(image=seatp, width="35", height="35", activebackground="black", bg="black", bd=0,
                      command=lambda: command(2, "2A", name, addSeat_canvas, seatp, seatSelected, seatNum, foundseat, film, screening, child, student, adult, senior,
                                              quantity, counter, seat2A))
        seat2A.grid(row=5, column=1, pady=10, padx=(50, 30))

        seat2B = Button(addSeat_canvas)
        seat2B.config(image=seatp, width="35", height="35", activebackground="black", bg="black", bd=0,
                      command=lambda: command(2, "2B", name, addSeat_canvas, seatp, seatSelected, seatNum, foundseat, film, screening, child, student, adult, senior,
                                              quantity, counter, seat2B))
        seat2B.grid(row=5, column=2, pady=10, padx=(0, 40))

        seat2C = Button(addSeat_canvas)
        seat2C.config(image=seatp, width="35", height="35", activebackground="black", bg="black", bd=0,
                      command=lambda: command(2, "2C", name, addSeat_canvas, seatp, seatSelected, seatNum, foundseat, film, screening, child, student, adult, senior,
                                              quantity, counter, seat2C))
        seat2C.grid(row=5, column=3, pady=10, padx=(0, 120))

        seat2D = Button(addSeat_canvas)
        seat2D.config(image=seatp, width="35", height="35", activebackground="black", bg="black", bd=0,
                      command=lambda: command(2, "2D", name, addSeat_canvas, seatp, seatSelected, seatNum, foundseat, film, screening, child, student, adult, senior,
                                              quantity, counter, seat2D))
        seat2D.grid(row=5, column=4, pady=10, padx=(0, 120))

        seat2E = Button(addSeat_canvas)
        seat2E.config(image=seatp, width="35", height="35", activebackground="black", bg="black", bd=0,
                      command=lambda: command(2, "2E", name, addSeat_canvas, seatp, seatSelected, seatNum, foundseat, film, screening, child, student, adult, senior,
                                              quantity, counter, seat2E))
        seat2E.grid(row=5, column=5, pady=10, padx=(0, 300))

        seat3A = Button(addSeat_canvas)
        seat3A.config(image=seatp, width="35", height="35", activebackground="black", bg="black", bd=0,
                      command=lambda: command(3, "3A", name, addSeat_canvas, seatp, seatSelected, seatNum, foundseat, film, screening, child, student, adult, senior,
                                              quantity, counter, seat3A))
        seat3A.grid(row=6, column=1, pady=10, padx=(50, 30))

        seat3B = Button(addSeat_canvas)
        seat3B.config(image=seatp, width="35", height="35", activebackground="black", bg="black", bd=0,
                      command=lambda: command(3, "3B", name, addSeat_canvas, seatp, seatSelected, seatNum, foundseat, film, screening, child, student, adult, senior,
                                              quantity, counter, seat3B))
        seat3B.grid(row=6, column=2, pady=10, padx=(0, 40))

        seat3C = Button(addSeat_canvas)
        seat3C.config(image=seatp, width="35", height="35", activebackground="black", bg="black", bd=0,
                      command=lambda: command(3, "3C", name, addSeat_canvas, seatp, seatSelected, seatNum, foundseat, film, screening, child, student, adult, senior,
                                              quantity, counter, seat3C))
        seat3C.grid(row=6, column=3, pady=10, padx=(0, 120))

        seat3D = Button(addSeat_canvas)
        seat3D.config(image=seatp, width="35", height="35", activebackground="black", bg="black", bd=0,
                      command=lambda: command(3, "3D", name, addSeat_canvas, seatp, seatSelected, seatNum, foundseat, film, screening, child, student, adult, senior,
                                              quantity, counter, seat3D))
        seat3D.grid(row=6, column=4, pady=10, padx=(0, 120))

        seat3E = Button(addSeat_canvas)
        seat3E.config(image=seatp, width="35", height="35", activebackground="black", bg="black", bd=0,
                      command=lambda: command(3, "3E", name, addSeat_canvas, seatp, seatSelected, seatNum, foundseat, film, screening, child, student, adult, senior,
                                              quantity, counter, seat3E))
        seat3E.grid(row=6, column=5, pady=10, padx=(0, 300))

        seat4A = Button(addSeat_canvas)
        seat4A.config(image=seatp, width="35", height="35", activebackground="black", bg="black", bd=0,
                      command=lambda: command(4, "4A", name, addSeat_canvas, seatp, seatSelected, seatNum, foundseat, film, screening, child, student, adult, senior,
                                              quantity, counter, seat4A))
        seat4A.grid(row=7, column=1, pady=10, padx=(50, 30))

        seat4B = Button(addSeat_canvas)
        seat4B.config(image=seatp, width="35", height="35", activebackground="black", bg="black", bd=0,
                      command=lambda: command(4, "4B", name, addSeat_canvas, seatp, seatSelected, seatNum, foundseat, film, screening, child, student, adult, senior,
                                              quantity, counter, seat4B))
        seat4B.grid(row=7, column=2, pady=10, padx=(0, 40))

        seat4C = Button(addSeat_canvas)
        seat4C.config(image=seatp, width="35", height="35", activebackground="black", bg="black", bd=0,
                      command=lambda: command(4, "4C", name, addSeat_canvas, seatp, seatSelected, seatNum, foundseat, film, screening, child, student, adult, senior,
                                              quantity, counter, seat4C))
        seat4C.grid(row=7, column=3, pady=10, padx=(0, 120))

        seat4D = Button(addSeat_canvas)
        seat4D.config(image=seatp, width="35", height="35", activebackground="black", bg="black", bd=0,
                      command=lambda: command(4, "4D", name, addSeat_canvas, seatp, seatSelected, seatNum, foundseat, film, screening, child, student, adult, senior,
                                              quantity, counter, seat4D))
        seat4D.grid(row=7, column=4, pady=10, padx=(0, 120))

        seat4E = Button(addSeat_canvas)
        seat4E.config(image=seatp, width="35", height="35", activebackground="black", bg="black", bd=0,
                      command=lambda: command(4, "4E", name, addSeat_canvas, seatp, seatSelected, seatNum, foundseat, film, screening, child, student, adult, senior,
                                              quantity, counter, seat4E))
        seat4E.grid(row=7, column=5, pady=10, padx=(0, 300))

        seat5A = Button(addSeat_canvas)
        seat5A.config(image=seatp, width="35", height="35", activebackground="black", bg="black", bd=0,
                      command=lambda: command(5, "5A", name, addSeat_canvas, seatp, seatSelected, seatNum, foundseat, film, screening, child, student, adult, senior,
                                              quantity, counter, seat5A))
        seat5A.grid(row=8, column=1, pady=10, padx=(50, 30))

        seat5B = Button(addSeat_canvas)
        seat5B.config(image=seatp, width="35", height="35", activebackground="black", bg="black", bd=0,
                      command=lambda: command(5, "5B", name, addSeat_canvas, seatp, seatSelected, seatNum, foundseat, film, screening, child, student, adult, senior,
                                              quantity, counter, seat5B))
        seat5B.grid(row=8, column=2, pady=10, padx=(0, 40))

        seat5C = Button(addSeat_canvas)
        seat5C.config(image=seatp, width="35", height="35", activebackground="black", bg="black", bd=0,
                      command=lambda: command(5, "5C", name, addSeat_canvas, seatp, seatSelected, seatNum, foundseat, film, screening, child, student, adult, senior,
                                              quantity, counter, seat5C))
        seat5C.grid(row=8, column=3, pady=10, padx=(0, 120))

        seat5D = Button(addSeat_canvas)
        seat5D.config(image=seatp, width="35", height="35", activebackground="black", bg="black", bd=0,
                      command=lambda: command(5, "5D", name, addSeat_canvas, seatp, seatSelected, seatNum, foundseat, film, screening, child, student, adult, senior,
                                              quantity, counter, seat5D))
        seat5D.grid(row=8, column=4, pady=10, padx=(0, 120))

        seat5E = Button(addSeat_canvas)
        seat5E.config(image=seatp, width="35", height="35", activebackground="black", bg="black", bd=0,
                      command=lambda: command(5, "5E", name, addSeat_canvas, seatp, seatSelected, seatNum, foundseat, film, screening, child, student, adult, senior,
                                              quantity, counter, seat5E))
        seat5E.grid(row=8, column=5, pady=10, padx=(0, 300))

        seatsDic = {"seat0A": seat0A, "seat0B": seat0B, "seat0C": seat0C, "seat0D": seat0D, "seat0E": seat0E,
                 "seat1A": seat1A, "seat1B": seat1B, "seat1C": seat1C, "seat1D": seat1D, "seat1E": seat1E,
                 "seat2A": seat2A, "seat2B": seat2B, "seat2C": seat2C, "seat2D": seat2D, "seat2E": seat2E,
                 "seat3A": seat3A, "seat3B": seat3B, "seat3C": seat3C, "seat3D": seat3D, "seat3E": seat3E,
                 "seat4A": seat4A, "seat4B": seat4B, "seat4C": seat4C, "seat4D": seat4D, "seat4E": seat4E,
                 "seat5A": seat5A, "seat5B": seat5B, "seat5C": seat5C, "seat5D": seat5D, "seat5E": seat5E}      #dictionary for each seat and their button variables

        screening = screening.replace("/", "-")
        screening = screening.replace(":", "-")     #format of the file name

        file = open(os.getcwd() + "\\films\\" + film + "\\" + screening + ".txt", "r")    #text file for the selected screening
        lines = file.readlines()
        howmanylines = len(lines)
        i = 4
        while i < howmanylines:
            orderLine = lines[i]
            splitline = orderLine.split(";")
            seats = splitline[2]    #where info about the seats are stored
            splitseats = seats.split(", ")      #splits wherever there is a comma so the seats are separated
            for seat in splitseats:             #loop for each seat
                takenSeat = "seat" + seat
                takenSeat = str(takenSeat)      #changed to string so it can be called and referenced in the seat dictionary
                seatsDic[takenSeat].config(image=seatTaken, command=lambda: messagebox.showinfo("Unavailable", "Seat has already been taken"))  #changes the seat image and if it is clicked, displays the message instead of calling the usual function
            i = i + 1       #increments until each line has been through the loop
        file.close()

        Button(addSeat_canvas, width=10, height=3, text="Back", command=lambda: bookingFilmsDic[film](name, addSeat_canvas)).grid(row=9, column=4, padx=10, pady=(50, 250))

    mainloop()

def command(row, column, name, addSeat_canvas, seatp, seatSelected, seatNum, foundseat, film, screening, child, student, adult, senior, quantity, counter, button):  #selected seats

    if button.config('image')[4] == seatNum:    #gets the current image of the button
        button.config(image=seatSelected)   #if the image is the seat, then its changed to a tick
        counter.set(counter.get() + 1)      #counter is incremented
    else:
        button.config(image=seatp)          #if the image is the ticket, then its changed back to a seat
        counter.set(counter.get() - 1)      #the counter is set back

    path = os.getcwd()+"\\films\\seats.txt"     #creates a temporary text file to store the seats selected
    if not os.path.isdir(os.getcwd()+"\\films"):
        os.mkdir(os.getcwd()+"\\films")
    if not os.path.isfile(path):
        f = open(path, "w")
        f.close()
    count = 0
    listlen = 0
    if os.path.isfile(path):
        with open(path, "r") as f:      #opens file
            curLines = f.readlines()    #reads lines in file
            newLines = []
            f.close()
        for line in curLines:           #repeats for each line
            listlen = len(curLines)     #sees how many lines there are
            if column not in line:
                count = count + 1
        if count < listlen:
            for line in curLines:
                if column not in line:
                    newLines.append(line)
            with open(path, "w") as f:
                for newLine in newLines:
                    f.write(newLine + "\n")
                f.close()
        else:
            with open(path, "a") as f:
                f.write(column + "\n")
                f.close()
    p = open(os.getcwd() + "\\films\\seats.txt", "r")       #opens that seat file that was just create
    lines = p.readlines()
    for line in lines:
        foundseat.append(line)      #adds the seats to the list
        p.close()

    if counter.get() == quantity:     #condition is met to continue
        Button(addSeat_canvas, width=10, height=3, text="Book",command=lambda: addBooking(name, foundseat, addSeat_canvas, film, screening, child, student, adult, senior, counter)).grid(row=9, column=5, pady=(50, 250), padx=10)
    if counter.get() > quantity:
        messagebox.showinfo("Too many seats selected", "Please select only " + str(quantity) + " seats.")
    if counter.get() < quantity:
        messagebox.showinfo("Not enough seats selected", "Please select " + str(quantity) + " seats.")

    mainloop()

def addBooking(name, foundseat, canvas, film, screening, child, student, adult, senior, counter):    #summary of the booking
    canvas.destroy()
    user32 = ctypes.windll.user32
    w = str(user32.GetSystemMetrics(0))
    h = str(user32.GetSystemMetrics(1))
    addBooking_canvas = Tk()
    addBooking_canvas.geometry(w+'x'+h)
    addBooking_canvas.configure(background='dark grey')
    addBooking_canvas.title("Booking Summary")
    addBooking_canvas.grid_rowconfigure(0, weight=1)
    addBooking_canvas.grid_rowconfigure(2, weight=1)
    addBooking_canvas.grid_columnconfigure(0, weight=1)
    addBooking_canvas.grid_columnconfigure(2, weight=1)

    screening = screening.replace("/", "-")
    screening = screening.replace(":", "-")

    b = open(os.getcwd()+"\\films\\"+film+"\\"+screening+".txt", "r")
    lines = b.readlines()
    date = lines[0].replace("-", "/").replace("\n", "")
    time = lines[1].replace("-", ":").replace("\n", "")
    screen = lines[2].replace("\n", "")
    screentype = lines[3].replace("\n", "")
    b.close()

    p = open(os.getcwd() + "\\films\\seats.txt", "r")
    seats = p.read()
    seats = seats.replace("\n", ", ")
    seats = str(seats)
    seats = seats[:-2]      #takes off the comma from after the last seat in the string
    p.close()
    childPrice = 0
    studentPrice = 0
    adultPrice = 0
    seniorPrice = 0

    if screentype == "2D":          #defines the prices of the tickets
        childPrice = 7.00
        studentPrice = 8.20
        adultPrice = 9.50
        seniorPrice = 8.80

    if screentype == "3D":
        childPrice = 8.00
        studentPrice = 9.20
        adultPrice = 10.50
        seniorPrice = 9.80

    totalCost = (child*childPrice) + (student*studentPrice) + (adult*adultPrice) + (senior*seniorPrice)         #calculates the total cost
    totalCost = ("%.2f" % totalCost)    #sets the cost to two decimal places

    Label(addBooking_canvas, fg="purple", font=("Arial", 20), text="Booking Summary").grid(row=0, column=0,
                                                                                           columnspan=3)

    Label(addBooking_canvas, font=("Arial", 13), text="Username: "+name).grid(row=1, column=0, padx=10, pady=(10, 10))
    Label(addBooking_canvas, font=("Arial", 13), text="Film: " + film).grid(row=2, column=0, padx=10, pady=10)
    Label(addBooking_canvas, font=("Arial", 13), text="Date: " + date).grid(row=3, column=0, padx=10, pady=10)
    Label(addBooking_canvas, font=("Arial", 13), text="Time: " + time).grid(row=4, column=0, padx=10, pady=10)
    Label(addBooking_canvas, font=("Arial", 13), text="Screen: " + screen).grid(row=5, column=0, padx=10, pady=10)
    Label(addBooking_canvas, font=("Arial", 13), text="Screen Type: " + screentype).grid(row=6, column=0, padx=10, pady=10)
    Label(addBooking_canvas, font=("Arial", 13), text="Tickets: "+str(child)+" Child, "+str(student)+" Student, "+str(adult)+" Adult, "+str(senior)+" Senior").grid(row=7, column=0, padx=10, pady=10)
    Label(addBooking_canvas, font=("Arial", 13), text="Seats: " + seats).grid(row=8, column=0, padx=10, pady=10)
    Label(addBooking_canvas, font=("Arial", 13), text="Total cost: £" + str(totalCost)).grid(row=9, column=0, padx=10, pady=(10, 150))

    Button(addBooking_canvas, width=15, height=3, text="Proceed to Payment", command=lambda: payment(name, counter, foundseat, addBooking_canvas, film, screening, child, student, adult, senior, totalCost, date, time, screen, screentype, seats)).grid(row=6, column=2, padx=10, pady=(0, 10))
    Button(addBooking_canvas, width=15, height=3, text="Back", command=lambda: addSeat(name, counter, addBooking_canvas, film, screening, child, student, adult, senior)).grid(row=7, column=2, padx=10, pady=(0, 10))
    Button(addBooking_canvas, width=15, height=3, text="Cancel Order", command=lambda: customerHomeScreen(name, addBooking_canvas)).grid(row=8, column=2, padx=10, pady=(0, 10))

def payment(name, counter, foundseat, canvas, film, screening, child, student, adult, senior, cost, date, time, screen, screentype, seats):   #paying for the order
    canvas.destroy()
    user32 = ctypes.windll.user32
    w = str(user32.GetSystemMetrics(0))
    h = str(user32.GetSystemMetrics(1))
    payment_canvas = Tk()
    payment_canvas.geometry(w+'x'+h)
    payment_canvas.configure(background='dark grey')
    payment_canvas.title("Payment")
    payment_canvas.grid_rowconfigure(0, weight=1)
    payment_canvas.grid_rowconfigure(2, weight=1)
    payment_canvas.grid_columnconfigure(0, weight=1)
    payment_canvas.grid_columnconfigure(2, weight=1)

    Label(payment_canvas, text="Payment", fg="purple", font=("Arial", 20)).grid(row=0, column=0, columnspan=4)

    Label(payment_canvas, font=("Arial", 14), text="Total cost: £" + str(cost)).grid(row=1, column=0, padx=10, pady=10)
    Label(payment_canvas, font=("Arial", 14), text="Card name").grid(row=2, column=0, padx=10, pady=10)
    cardName_entry = Entry(payment_canvas, width=20, font=("Arial", 14))
    cardName_entry.grid(row=2, column=1, sticky=W, columnspan=4)
    Label(payment_canvas, font=("Arial", 14), text="Card number").grid(row=3, column=0, padx=10, pady=10)
    cardNumber_entry = Entry(payment_canvas, width=20, font=("Arial", 14))
    cardNumber_entry.grid(row=3, column=1, sticky=W, columnspan=4)
    Label(payment_canvas, font=("Arial", 14), text="Expiry date").grid(row=4, column=0, padx=10, pady=10)
    cardDateMonth_entry = Entry(payment_canvas, width=10, font=("Arial", 14))
    cardDateMonth_entry.grid(row=4, column=1, sticky=W)
    Label(payment_canvas, font=("Arial", 14), text="/").grid(row=4, column=2, sticky=W)
    cardDateYear_entry = Entry(payment_canvas, width=10, font=("Arial", 14))
    cardDateYear_entry.grid(row=4, column=3, sticky=W, padx=(0,50))
    Label(payment_canvas, font=("Arial", 14), text="CCV").grid(row=5, column=0, padx=10, pady=10)
    cardCCV_entry = Entry(payment_canvas, width=20, font=("Arial", 14))
    cardCCV_entry.grid(row=5, column=1, sticky=W, columnspan=4)

    Button(payment_canvas, width=12, height=4, text="Confirm", command=lambda: validPayment(name, foundseat, payment_canvas, film, screening, child, student, adult, senior, cost, date, time, screen, screentype, seats, cardName_entry.get(), cardNumber_entry.get(), cardDateMonth_entry.get(), cardDateYear_entry.get(), cardCCV_entry.get())).grid(row=6, column=2, padx=10, pady=(50, 200))
    Button(payment_canvas, width=12, height=4, text="Back", command=lambda: addBooking(name, foundseat, payment_canvas, film, screening, child, student, adult, senior, counter)).grid(row=6, column=0, padx=(10,0), pady=(50, 200))


def validPayment(name, foundseat, canvas, film, screening, child, student, adult, senior, cost, date, time, screen, screentype, seats, cardName, cardNumber, cardDateMonth, cardDateYear, cardCCV):     #checks the payment details are valid
    validCardName = False
    validCardNum = False
    validCardDateMonth = False
    validCardDateYear = False
    validCardCCV = False

    def luhn_checksum(card_number):     #luhn's algorithm
        def digits_of(n):
            return [int(d) for d in str(n)]

        digits = digits_of(card_number)
        odd_digits = digits[-1::-2]
        even_digits = digits[-2::-2]
        checksum = 0
        checksum += sum(odd_digits)
        for d in even_digits:
            checksum += sum(digits_of(d * 2))
        return checksum % 10

    def is_luhn_valid(card_number):
        return luhn_checksum(card_number) == 0

    result = is_luhn_valid(cardNumber)      #sends the card number to be checked by the algorithm
    if str(result) == 'True':       #determines the result from the algorithm
        validCardNum = True
    else:
        messagebox.showinfo("Invalid card number", "Enter valid card details")

    cardName = cardName.replace(" ", "")
    if cardName.isalpha()==False:
        messagebox.showinfo("Invalid card name", "Enter valid card details")
    else:
        validCardName = True

    if cardDateMonth.isdigit():
        cardDateMonth = int(cardDateMonth)
        if cardDateMonth < 1 or cardDateMonth > 12:
            messagebox.showinfo("Invalid card date", "Enter valid card details")
        else:
            validCardDateMonth = True

    if cardDateYear.isdigit():
        cardDateYear = int(cardDateYear)
        if cardDateYear < 19 or cardDateYear > 23:
            messagebox.showinfo("Invalid card date", "Enter valid card details")
        else:
            validCardDateYear = True

    if cardCCV.isdigit():
        if len(cardCCV) == 3:
            validCardCCV = True
        else:
            messagebox.showinfo("Invalid CCV number", "Enter valid card details")

    if validCardName == True and validCardNum == True and validCardDateMonth == True and validCardDateYear == True and validCardCCV == True:    #if all conditions are met
        completeBooking(name, foundseat, canvas, film, screening, child, student, adult, senior, cost, date, time, screen, screentype, seats, cardNumber, cardDateMonth, cardDateYear, cardCCV)
    else:
        print()


def completeBooking(name, foundseat, canvas, film, screening, child, student, adult, senior, cost, date, time, screen, screentype, seats, cardNumber, cardDateMonth, cardDateYear, cardCCV):        #completing the booking as all details are valid
    canvas.destroy()
    user32 = ctypes.windll.user32
    w = str(user32.GetSystemMetrics(0))
    h = str(user32.GetSystemMetrics(1))
    completeBooking_canvas = Tk()
    completeBooking_canvas.geometry(w+'x'+h)
    completeBooking_canvas.configure(background='dark grey')
    completeBooking_canvas.title("Booking Complete")
    completeBooking_canvas.grid_rowconfigure(0, weight=1)
    completeBooking_canvas.grid_rowconfigure(2, weight=1)
    completeBooking_canvas.grid_columnconfigure(0, weight=1)
    completeBooking_canvas.grid_columnconfigure(2, weight=1)

    orderIDs = []
    for filename in os.listdir(os.getcwd() + "\\customeraccounts"):
        with open(os.getcwd() + "\\customeraccounts\\" + filename, "r") as f:
            lines = f.readlines()[2:]
            for line in lines:
                order = line.split(";")[0]
                orderIDs.append(order)          #gets all of the existing order numbers
        f.close()
    for filename in os.listdir(os.getcwd() + "\\staffaccounts"):
        with open(os.getcwd() + "\\staffaccounts\\" + filename, "r") as f:
            lines = f.readlines()[3:]
            for line in lines:
                order = line.split(";")[0]
                orderIDs.append(order)
        f.close()

    orderNum = orderNumGenerator(orderIDs)      #calls the function to generate a new, unique order number

    userEmail =""
    file = open(os.getcwd() + "\\customeraccounts\\" + name + ".txt", "r")
    lines = file.readlines()
    infoLine = lines[1]
    splitline = infoLine.split(";")
    for split in splitline:
        if "@" in split:
            userEmail = str(split)
    file.close()

    port = 587
    smtp_server = "smtp.gmail.com"
    sender_email = "bookings.moviemania@gmail.com"
    receiver_email = userEmail
    password = "QDD87kNV55P#8BC"
    subject = "Order Confirmation"
    message = ("Thank you " + str(name) + ". Here is your order summary: \n" + "Order Number: " + str(orderNum) + "\nUsername: " + str(name) + "\nFilm: " + str(film) + "\nDate: " + str(date) +"\nTime: " + str(time) + "\nScreen: " + str(screen) + "\nScreen Type: " + str(screentype) + "\nTickets: " + str(child) + " Child, " + str(student) + " Student, " + str(adult) + " Adult, " + str(senior) + " Senior" + "\nSeats: " + str(seats) + "\nTotal cost: " + str(cost) + " GBP \nPayment: Card " + str(cardNumber[-4:].rjust(len(cardNumber), "*")))

    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, 'Subject: {}\n\n{}'.format(subject, message))     #emails the booking summary

    o = open(os.getcwd() + "\\customeraccounts\\" + name + ".txt", "a")     #appends to the username text file
    o.write("\n" + str(orderNum) + ";" + str(film) + ";" + str(date) + ";" + str(time) + ";" + str(screen) + ";" + str(screentype) + ";" +
            str(child) + ";" + str(student) + ";" + str(adult) + ";" + str(senior) + ";" + str(seats) + ";" + str(cost) +
            ";" + str((cardNumber[-4:].rjust(len(cardNumber), "*"))))           #blanks out part of the card number
    o.close()

    b = open(os.getcwd() + "\\films\\" + film + "\\" + screening + ".txt", "a")         #appends to the screening text file
    b.write("\n" + str(orderNum) + ";" + str(name) + ";" + str(seats) + ";" + str(cost))
    b.close()

    h = str(film + " " + date + "" + time)      #the screening of the order
    screeningList = [h]
    Label(completeBooking_canvas, font=("Arial", 20), text="Booking Summary", fg="purple").grid(row=0, column=0,
                                                                                                columnspan=3)
    Label(completeBooking_canvas, font=("Arial", 15), text=(
        "Thank you for choosing MovieMania. \n\n A confirmation email will be sent shortly. \n\n Present your order confirmation upon arrival.")).grid(
        row=1, column=0, padx=50, pady=20, columnspan=3)

    Button(completeBooking_canvas, font=("Arial", 12), width=15, height=4, text='Exit', command=quit).grid(row=2, column=0, padx=50, pady=(0, 50))
    Button(completeBooking_canvas, font=("Arial", 12), width=15, height=4, text='Home', command=lambda: home_screen(completeBooking_canvas)).grid(row=2, column=2, padx=50, pady=(0, 50))
    Button(completeBooking_canvas, font=("Arial", 12), width=15, height=4, text='Add refreshments', command=lambda: foodToExistingOrder(name, completeBooking_canvas, screeningList)).grid(row=2, column=1, padx=50, pady=(0, 50))

def orderNumGenerator(orderIDs):        #generates random order number
    orderNum = ""
    for i in range(0, 6):               #makes it six digits long
        digit = random.randint(0, 9)    #chooses random digits from 0 to 9
        orderNum = orderNum + str(digit)

    if orderNum in orderIDs:            #checks the number doesn't already exist by seeing if it is in the list
        return "ded"
    return orderNum                     #sends the order number back to the function


def viewMyOrders(name, canvas):         #viewing purchased orders
    canvas.destroy()
    user32 = ctypes.windll.user32
    w = str(user32.GetSystemMetrics(0))
    h = str(user32.GetSystemMetrics(1))
    viewMyOrders_canvas = Tk()
    viewMyOrders_canvas.geometry(w+'x'+h)
    viewMyOrders_canvas.configure(background='dark grey')
    viewMyOrders_canvas.title("Purchased Orders")
    viewMyOrders_canvas.grid_rowconfigure(0, weight=1)
    viewMyOrders_canvas.grid_rowconfigure(2, weight=1)
    viewMyOrders_canvas.grid_columnconfigure(0, weight=1)
    viewMyOrders_canvas.grid_columnconfigure(2, weight=1)

    Label(viewMyOrders_canvas, font=("Arial", 20), fg="purple", text=" Purchased Orders").grid(row=0, column=0, columnspan=3)


    file = open(os.getcwd() + "\\customeraccounts\\" + name + ".txt", "r")
    lines = file.readlines()
    text_frame = Frame(viewMyOrders_canvas, borderwidth=1, relief="flat")
    text_entry = Text(text_frame, wrap=WORD, height=15, width=60, borderwidth=1)
    vertical_scroll = Scrollbar(text_frame, orient=VERTICAL, command=text_entry.yview)      #makes a text box with a scroll bar
    text_entry["yscroll"] = vertical_scroll.set
    vertical_scroll.pack(side="right", fill="y")
    text_entry.pack(side="left", fill="both", expand=True)
    text_frame.grid(row=1, column=0, rowspan=5)
    howmanylines = len(lines)
    i=2     #orders start at line 2 has the first two are the password and personal details
    while i < howmanylines:
        orderLine = lines[i]        #gets the details of each order
        splitline = orderLine.split(";")
        order = i-1
        orderNum = splitline[0]
        film = splitline[1]
        date = splitline[2]
        time = splitline[3]
        screen = splitline[4]
        screentype = splitline[5]
        child = splitline[6]
        student = splitline[7]
        adult = splitline[8]
        senior = splitline[9]
        seats = splitline[10]
        cost = splitline[11]
        card = splitline[12]
        food = splitline[13] + "\n" + splitline[14] + "\n" + splitline[15]
        text = ("Order " + str(order) + "\n Order Number: " + str(orderNum) + "\n Film: " + str(film) + "\n Date: " + str(date) + "\n Time: " + str(time) + "\n Screen: " + str(screen) + "\n Screen type: " + str(screentype) +"\n Child tickets: " + str(child) + "\n Student tickets: " + str(student) + "\n Adult tickets: " + str(adult) + "\n Senior tickets: " + str(senior) + "\n Seats: " + str(seats) + "\n Cost: " + str(cost) + "\n Card used to pay: " + str(card) + "\n Food: " + str(food) +"\n")
        text_entry.insert(END, text)        #inserts the information into the text box
        i=i+1
    file.close()

    Button(viewMyOrders_canvas, width=15, height=4, text='Back', command=lambda: customerHomeScreen(name, viewMyOrders_canvas)).grid(row=21, column=1, sticky=E, padx=10, pady=(50, 200))
    Button(viewMyOrders_canvas, width=15, height=4, text='Delete an order', command=lambda: deleteOrderRequest(name, viewMyOrders_canvas, film, date, time, screen, screentype)).grid(row=20,
                                                                                                                 column=1,
                                                                                                                 sticky=W, padx=10, pady=10)
def deleteOrderRequest(name, canvas, film, date, time, screen, screentype):     #choosing which order to delete
    canvas.destroy()
    user32 = ctypes.windll.user32
    w = str(user32.GetSystemMetrics(0))
    h = str(user32.GetSystemMetrics(1))
    deleteOrderRequest_canvas = Tk()
    deleteOrderRequest_canvas.geometry(w+'x'+h)
    deleteOrderRequest_canvas.configure(background='dark grey')
    deleteOrderRequest_canvas.title("Delete an Order")
    deleteOrderRequest_canvas.grid_rowconfigure(0, weight=1)
    deleteOrderRequest_canvas.grid_rowconfigure(2, weight=1)
    deleteOrderRequest_canvas.grid_columnconfigure(0, weight=1)
    deleteOrderRequest_canvas.grid_columnconfigure(2, weight=1)

    orderList = []
    file = open(os.getcwd()+"\\customeraccounts\\" + name + ".txt", "r")
    lines = file.readlines()
    howmanylines = len(lines)
    i = 2
    while i < howmanylines:
        orderLine = lines[i]
        splitline = orderLine.split(";")
        film = splitline[1]
        date = splitline[2]
        time = splitline[3]
        orderList.append(film+"  "+date+"  "+time)      #appends each screening that exists in the username text file to a list so it can be used in a drop down menu box
        i=i+1
    file.close()

    Label(deleteOrderRequest_canvas, text="Delete an Order", font=("Arial", 20), fg="purple").grid(row=0, column=0,
                                                                                                   columnspan=3,
                                                                                                   padx=10)

    Label(deleteOrderRequest_canvas, font=("Arial", 14), text="Orders").grid(row=1, column=0, sticky=E)
    listOfOrders = ttk.Combobox(deleteOrderRequest_canvas, width=30, font=("Arial", 14))
    listOfOrders["values"] = orderList      #existing orders to choose from
    listOfOrders.grid(row=1, column=1, sticky=W, padx=10)
    listOfOrders.current(0)

    Button(deleteOrderRequest_canvas, width=15, height=4, text='Back', command=lambda: viewMyOrders(name, deleteOrderRequest_canvas).grid(row=3, column=1, padx=10, pady=(10, 200)))
    Button(deleteOrderRequest_canvas, width=15, height=4, text='Delete this order', command=lambda: deleteOrder(name, deleteOrderRequest_canvas, listOfOrders.get(), film, date, time, screen, screentype)).grid(row=2, column=1, padx=10, pady=10)


def deleteOrder(name, canvas, order, film, date, time, screen, screentype):         #deleting an order
    canvas.destroy()
    user32 = ctypes.windll.user32
    w = str(user32.GetSystemMetrics(0))
    h = str(user32.GetSystemMetrics(1))
    deleteOrder_canvas = Tk()
    deleteOrder_canvas.geometry(w+'x'+h)
    deleteOrder_canvas.configure(background='dark grey')
    deleteOrder_canvas.title("Delete an Order")
    deleteOrder_canvas.grid_rowconfigure(0, weight=1)
    deleteOrder_canvas.grid_rowconfigure(2, weight=1)
    deleteOrder_canvas.grid_columnconfigure(0, weight=1)
    deleteOrder_canvas.grid_columnconfigure(2, weight=1)

    order = order.replace("  ", ";").replace("; ", " ;")
    file = open(os.getcwd() + "\\customeraccounts\\" + name + ".txt", "r")
    lines = file.readlines()                                                    #gets the contents of the username text file
    file.close()
    file = open(os.getcwd() + "\\customeraccounts\\" + name + ".txt", "w")      #opens the file for writing
    for line in lines:
        if order.strip() not in line.strip():       #re-writes each line back to the file, leaving out the one that has been selected to be deleted
            print()
            file.write(line)
        else:
            print()
    file.close()

    date = date.replace("/", "-")
    time = time.replace(":", "-")
    screening = date + time + screen + screentype

    o = open(os.getcwd() + "\\films\\" + film + "\\" + screening + ".txt", "r")             #does the same for the screening text file
    lines = o.readlines()
    o.close()
    o = open(os.getcwd() + "\\films\\" + film + "\\" + screening + ".txt", "w")
    for line in lines:
        if name.strip() not in line.strip():
            print()
            o.write(line)
        else:
            print()
    o.close()

    Label(deleteOrder_canvas, font=("Arial", 20), text="Delete an Order", fg="purple").grid(row=0, column=0,
                                                                                            columnspan=3)

    Label(deleteOrder_canvas, font=("Arial", 14), text="This order has now been deleted. \n ").grid(row=1, column=1, padx=(150, 0), pady=10)
    Button(deleteOrder_canvas, width=15, height=4, text="Ok", command=lambda: customerHomeScreen(name, deleteOrder_canvas)).grid(row=2, column=2, padx=20, pady=(10, 200))


def viewMyAccount(name, canvas):        #viewing stored details on the account
    canvas.destroy()
    user32 = ctypes.windll.user32
    w = str(user32.GetSystemMetrics(0))
    h = str(user32.GetSystemMetrics(1))
    viewMyAccount_canvas = Tk()
    viewMyAccount_canvas.geometry(w+'x'+h)
    viewMyAccount_canvas.configure(background='dark grey')
    viewMyAccount_canvas.title("My Account")
    viewMyAccount_canvas.grid_rowconfigure(0, weight=1)
    viewMyAccount_canvas.grid_rowconfigure(2, weight=1)
    viewMyAccount_canvas.grid_columnconfigure(0, weight=1)
    viewMyAccount_canvas.grid_columnconfigure(2, weight=1)

    Label(viewMyAccount_canvas, font=("Arial", 20), fg="purple", text="My Account").grid(row=0, column=0, columnspan=3)

    Button(viewMyAccount_canvas, width=15, height=4, text='Reset Password', command=lambda: resetPasswordRequest(viewMyAccount_canvas, name)).grid(row=1, column=2)
    Button(viewMyAccount_canvas, width=18, height=4, text='View personal details', command=lambda: viewMyDetails(viewMyAccount_canvas, name)).grid(row=1, column=1)
    Button(viewMyAccount_canvas, width=15, height=4, text='Back', command=lambda: customerHomeScreen(name, viewMyAccount_canvas)).grid(row=1, column=0)


def resetPasswordRequest(canvas, name):     #resetting a password
    canvas.destroy()
    user32 = ctypes.windll.user32
    w = str(user32.GetSystemMetrics(0))
    h = str(user32.GetSystemMetrics(1))
    resetPasswordRequest_canvas = Tk()
    resetPasswordRequest_canvas.geometry(w+'x'+h)
    resetPasswordRequest_canvas.configure(background='dark grey')
    resetPasswordRequest_canvas.title("Reset Your Password")
    resetPasswordRequest_canvas.grid_rowconfigure(0, weight=1)
    resetPasswordRequest_canvas.grid_rowconfigure(2, weight=1)
    resetPasswordRequest_canvas.grid_columnconfigure(0, weight=1)
    resetPasswordRequest_canvas.grid_columnconfigure(2, weight=1)

    Label(resetPasswordRequest_canvas, font=("Arial", 20), text="Reset Your MovieMania Account Password", fg="purple", anchor='center').grid(row=0, column=0, columnspan=3, padx=(0, 50))
    Label(resetPasswordRequest_canvas, font=("Arial", 14), text="Current Password").grid(row=1, column=0, sticky=E, pady=10, padx=20)
    currentPassword_entry = Entry(resetPasswordRequest_canvas, width=20, font=("Arial", 14))        #asks for the current password
    currentPassword_entry.grid(row=1, column=1, sticky=W)
    Label(resetPasswordRequest_canvas, font=("Arial", 14), text="New Password").grid(row=2, column=0, sticky=E, pady=10, padx=20)
    password1_entry = Entry(resetPasswordRequest_canvas, show="*", width=20, font=("Arial", 14))
    password1_entry.grid(row=2, column=1, sticky=W)                                                 #asks for a new password
    Label(resetPasswordRequest_canvas, font=("Arial", 14), text="Confirm New Password").grid(row=3, column=0, sticky=E, pady=10, padx=20)
    password2_entry = Entry(resetPasswordRequest_canvas, show="*", width=20, font=("Arial", 14))
    password2_entry.grid(row=3, column=1, sticky=W)

    Button(resetPasswordRequest_canvas, width=15, height=3, text="Reset", command=lambda: resetPassword(resetPasswordRequest_canvas, name, currentPassword_entry.get(), password1_entry.get(), password2_entry.get())).grid(row=4, column=1, pady=(50, 200), padx=(250, 0), sticky=E)
    Button(resetPasswordRequest_canvas, width=15, height=3, text="Back", command=lambda: viewMyAccount(name, resetPasswordRequest_canvas)).grid(row=4, column=0, pady=(50, 200))


def resetPassword(canvas, name, currentPassword, newPassword1, newPassword2):       #resetting the password to the new one
    pchecker = os.getcwd() + "\\customeraccounts\\" + name + ".txt"
    if os.path.isfile(os.getcwd() + "\\customeraccounts\\" + name + ".txt"):
        f = open(os.getcwd() + "\\customeraccounts\\" + name + ".txt")
        lines = f.readlines()
        f.close()
        passwordtocheck = lines[0].strip()
        if checker(passwordtocheck, currentPassword):       #checks the current password is correct
            if newPassword1 == newPassword2:                #checks the new passwords match
                newHashedPassword = hasher(newPassword1)    #hashes the new password
                with open(pchecker, "r") as file:
                    lines = file.readlines()
                    infoLine = lines[1]
                    howmanylines = len(lines)
                    file.close()
                    lines[0] = newHashedPassword            #replaces the old stored hashed password with the new one
                    writingstuff = []
                    writingstuff.append(lines[0] + "\n")
                    i = 1
                    while i < howmanylines:
                        writingstuff.append(lines[i])
                        i = i + 1

                    with open(pchecker, "w") as file:
                        for line in writingstuff:
                            file.write(line)                #rewrites the file with the new line password in it
                    file.close()
                    messagebox.showinfo("Reset Password Complete", "Your account password has been reset.")
                    customerLogin(canvas)
            else:
                messagebox.showinfo("New Passwords Don't Match", "Your new password entries do not match.")
        else:
            messagebox._show("Incorrect Password", "Password is incorrect")
    else:
        messagebox._show("Incorrect Username", "Username doesn't exist")


def viewMyDetails(canvas, username):        #veiwing personal details stored on the account
    canvas.destroy()
    user32 = ctypes.windll.user32
    w = str(user32.GetSystemMetrics(0))
    h = str(user32.GetSystemMetrics(1))
    viewMyDetails_canvas = Tk()
    viewMyDetails_canvas.geometry(w+'x'+h)
    viewMyDetails_canvas.configure(background='dark grey')
    viewMyDetails_canvas.title("My Details")
    viewMyDetails_canvas.grid_rowconfigure(0, weight=1)
    viewMyDetails_canvas.grid_rowconfigure(2, weight=1)
    viewMyDetails_canvas.grid_columnconfigure(0, weight=1)
    viewMyDetails_canvas.grid_columnconfigure(2, weight=1)

    file = open(os.getcwd() + "\\customeraccounts\\" + username + ".txt", "r")      #extracting all of the stored details
    lines = file.readlines()
    accountLine = lines[0]
    infoLine = lines[1]
    splitline = infoLine.split(";")
    title = splitline[0]
    name = splitline[1]
    surname = splitline[2]
    dob = splitline[3]
    address1 = splitline[4]
    address2 = splitline[5]
    postcode = splitline[6]
    email = splitline[7]
    mobile = splitline[8]
    file.close()

    Label(viewMyDetails_canvas, font=("Arial", 20), fg="purple", text="My Details").grid(row=0, column=0, columnspan=3)

    Label(viewMyDetails_canvas, font=("Arial", 14), text=("Title: " + title)).grid(row=2, column=0, padx=10)
    Label(viewMyDetails_canvas, font=("Arial", 14), text=("Name: " + name)).grid(row=3, column=0, pady=15, padx=10)
    Label(viewMyDetails_canvas, font=("Arial", 14), text=("Surname: " + surname)).grid(row=4, column=0, pady=15, padx=10)
    Label(viewMyDetails_canvas, font=("Arial", 14), text=("DOB: " + dob)).grid(row=5, column=0, pady=15, padx=10)
    Label(viewMyDetails_canvas, font=("Arial", 14), text=("Address line 1: " + address1)).grid(row=6, column=0, pady=15,
                                                                                 padx=10)
    Label(viewMyDetails_canvas, font=("Arial", 14), text=("Address line 2: " + address2)).grid(row=7, column=0, pady=15,
                                                                                 padx=10)
    Label(viewMyDetails_canvas, font=("Arial", 14), text=("Postcode: " + postcode)).grid(row=8, column=0, pady=15, padx=10)
    Label(viewMyDetails_canvas, font=("Arial", 14), text=("Email: " + email)).grid(row=9, column=0, pady=15, padx=10)
    Label(viewMyDetails_canvas, font=("Arial", 14), text=("Mobile: " + mobile)).grid(row=10, column=0, pady=(10, 100), padx=10)


    Button(viewMyDetails_canvas, width=17, height=4, text="Edit Account Details",
           command=lambda: editAccount(viewMyDetails_canvas, username)).grid(row=8, column=2, padx=10,
                                                                                   pady=10)
    Button(viewMyDetails_canvas, width=17, height=4, text="Back", command=lambda: viewMyAccount(username, viewMyDetails_canvas)).grid(
        row=9, column=2, padx=10, pady=10)


def staffLogin(canvas):         #logging in as a staff member
    canvas.destroy()
    user32 = ctypes.windll.user32
    w = str(user32.GetSystemMetrics(0))
    h = str(user32.GetSystemMetrics(1))
    staffLogin_canvas = Tk()
    staffLogin_canvas.geometry(w+'x'+h)
    staffLogin_canvas.configure(background='dark grey')
    staffLogin_canvas.title("Staff's Login")
    staffLogin_canvas.grid_rowconfigure(0, weight=1)
    staffLogin_canvas.grid_rowconfigure(2, weight=1)
    staffLogin_canvas.grid_columnconfigure(0, weight=1)
    staffLogin_canvas.grid_columnconfigure(2, weight=1)

    Label(staffLogin_canvas, font=("Arial", 25), text="Staff's Login", fg="purple").grid(row=0, column=0, columnspan=3)
    Label(staffLogin_canvas, font=("Arial", 12), text="Employee Number").grid(row=1, column=0, sticky=E, pady=(0, 5), padx=10)
    username_entry = Entry(staffLogin_canvas, width=30, font=("Arial", 15))
    username_entry.grid(row=1, column=1, sticky=E)
    Label(staffLogin_canvas, font=("Arial", 12), text="Password").grid(row=2, column=0, sticky=E, pady=(10, 0), padx=10)
    password_entry = Entry(staffLogin_canvas, show="*", width=30, font=("Arial", 15))
    password_entry.grid(row=2, column=1, sticky=E)

    Button(staffLogin_canvas, width=20, height=3, text='Log In',
           command=lambda: staffValidLogin(staffLogin_canvas, username_entry.get(), password_entry.get())).grid(row=3, column=1, sticky=W, padx=10)
    Button(staffLogin_canvas, width=20, height=3, text='Forgotten Password', command=lambda: messagebox.showinfo("Contact Manager", "Ask your manager to reset your password")).grid(row=4, column=1, sticky=W, padx=10)
    Button(staffLogin_canvas, width=20, height=3, text='Back', command=lambda: home_screen(staffLogin_canvas)).grid(row=5, column=1, sticky=W, padx=10, pady=(0, 80))

def staffValidLogin(canvas, username, password):        #checking the staff account exists
    usernames = get_usernamesStaff()
    if username in usernames:
        passwordCheckerStaff(canvas, username, password)
    else:
        messagebox._show("DED", "Username doesn't exist")


def passwordCheckerStaff(canvas, username, password):   #checking the staff login details are correct
    pchecker = os.getcwd()+"\\staffaccounts\\"+username+".txt"
    if os.path.isfile(os.getcwd()+"\\staffaccounts\\"+username+".txt"):
        f = open(os.getcwd()+"\\staffaccounts\\"+username+".txt")
        lines = f.readlines()
        passwordtocheck = lines[0].strip()
        if checker(passwordtocheck, password):
            staffHomeScreen(username, canvas)
        else:
            messagebox._show("Incorrect Password", "Password is incorrect")
        f.close()
    else:
        messagebox._show("Incorrect Username", "Username doesn't exist")

def staffHomeScreen(employeeNum, canvas):           #home screen once staff member is logged in
    canvas.destroy()
    user32 = ctypes.windll.user32
    w = str(user32.GetSystemMetrics(0))
    h = str(user32.GetSystemMetrics(1))
    staffHomeScreen_canvas = Tk()
    staffHomeScreen_canvas.geometry(w+'x'+h)
    staffHomeScreen_canvas.configure(background='dark grey')
    staffHomeScreen_canvas.title("Staff Home Screen")
    staffHomeScreen_canvas.grid_rowconfigure(0, weight=1)
    staffHomeScreen_canvas.grid_rowconfigure(2, weight=1)
    staffHomeScreen_canvas.grid_columnconfigure(0, weight=1)
    staffHomeScreen_canvas.grid_columnconfigure(2, weight=1)

    with open(os.getcwd() + "\\staffaccounts\\" + employeeNum + ".txt", "r") as f:
        lines = f.readlines()
        jobLine = lines[2]
        splitline = jobLine.split(";")
        jobTitle = splitline[0]         #sees what the position of the staff member is
    f.close()

    if jobTitle == "Supervisor":        #depending on their job title, staff members have permission to access differnet button features
        Button(staffHomeScreen_canvas, width=20, height=3, text="Print Tickets",
               command=lambda: printTickets(employeeNum, staffHomeScreen_canvas)).grid(row=1, column=0, padx=10,
                                                                                       pady=10)
        Button(staffHomeScreen_canvas, width=20, height=3, text="Today's Screenings",
               command=lambda: todaysScreenings(employeeNum, staffHomeScreen_canvas)).grid(row=1, column=1, padx=5,
                                                                                           pady=5)
        Button(staffHomeScreen_canvas, width=20, height=3, text="Customer Orders",
               command=lambda: customersOrders(employeeNum, staffHomeScreen_canvas)).grid(row=1, column=2, padx=5,
                                                                                          pady=5)
        Button(staffHomeScreen_canvas, width=20, height=3, text="Book Film for Customer",
               command=lambda: bookFilmForCustomer(employeeNum, staffHomeScreen_canvas, jobTitle)).grid(row=1, column=3,
                                                                                                        padx=(5, 150), pady=5)
        Button(staffHomeScreen_canvas, width=20, height=3, text="Book Food for Customer",
               command=lambda: bookFoodForCustomer(employeeNum, staffHomeScreen_canvas)).grid(row=2, column=0, padx=5,
                                                                                              pady=(5, 50))
        Button(staffHomeScreen_canvas, width=20, height=3, text="Staff Discount",
               command=lambda: staffDiscount(employeeNum, staffHomeScreen_canvas)).grid(row=2, column=1, padx=5, pady=(5, 50))
        Button(staffHomeScreen_canvas, width=20, height=3, text="View Account",
               command=lambda: viewMyAccountStaff(employeeNum, staffHomeScreen_canvas)).grid(row=2, column=2, padx=5,
                                                                                             pady=(5, 50))


    if jobTitle == "Sales":
        Button(staffHomeScreen_canvas, width=20, height=3, text="Print Tickets",
               command=lambda: printTickets(employeeNum, staffHomeScreen_canvas)).grid(row=1, column=0, padx=10,
                                                                                       pady=10)
        Button(staffHomeScreen_canvas, width=20, height=3, text="Today's Screenings",
               command=lambda: todaysScreenings(employeeNum, staffHomeScreen_canvas)).grid(row=1, column=1, padx=5,
                                                                                           pady=5)
        Button(staffHomeScreen_canvas, width=20, height=3, text="Customer Orders",
               command=lambda: customersOrders(employeeNum, staffHomeScreen_canvas)).grid(row=1, column=2, padx=5,
                                                                                          pady=5)
        Button(staffHomeScreen_canvas, width=20, height=3, text="Book Film for Customer",
               command=lambda: bookFilmForCustomer(employeeNum, staffHomeScreen_canvas, jobTitle)).grid(row=1, column=3,
                                                                                                        padx=(5, 150), pady=5)
        Button(staffHomeScreen_canvas, width=20, height=3, text="Book Food for Customer",
               command=lambda: bookFoodForCustomer(employeeNum, staffHomeScreen_canvas)).grid(row=2, column=0, padx=5,
                                                                                              pady=(5, 50))
        Button(staffHomeScreen_canvas, width=20, height=3, text="Staff Discount",
               command=lambda: staffDiscount(employeeNum, staffHomeScreen_canvas)).grid(row=2, column=1, padx=5, pady=(5, 50))
        Button(staffHomeScreen_canvas, width=20, height=3, text="View Account",
               command=lambda: viewMyAccountStaff(employeeNum, staffHomeScreen_canvas)).grid(row=2, column=2, padx=5,
                                                                                             pady=(5, 50))


    if jobTitle == "Security":
        Button(staffHomeScreen_canvas, width=20, height=3, text="Print Tickets",
               command=lambda: messagebox.showinfo("Unauthorised Access", "You do not have permission to access this")).grid(row=1, column=0, padx=10,
                                                                                       pady=10)
        Button(staffHomeScreen_canvas, width=20, height=3, text="Today's Screenings",
               command=lambda: todaysScreenings(employeeNum, staffHomeScreen_canvas)).grid(row=1, column=1, padx=5,
                                                                                           pady=5)
        Button(staffHomeScreen_canvas, width=20, height=3, text="Customer Orders",
               command=lambda: customersOrders(employeeNum, staffHomeScreen_canvas)).grid(row=1, column=2, padx=5,
                                                                                          pady=5)
        Button(staffHomeScreen_canvas, width=20, height=3, text="Book Film for Customer",
               command=lambda: messagebox.showinfo("Unauthorised Access", "You do not have permission to access this")).grid(row=1, column=3,
                                                                                                        padx=(5, 150), pady=5)
        Button(staffHomeScreen_canvas, width=20, height=3, text="Book Food for Customer",
               command=lambda: messagebox.showinfo("Unauthorised Access", "You do not have permission to access this")).grid(row=2, column=0, padx=5,
                                                                                              pady=(5, 50))
        Button(staffHomeScreen_canvas, width=20, height=3, text="Staff Discount",
               command=lambda: staffDiscount(employeeNum, staffHomeScreen_canvas)).grid(row=2, column=1, padx=5, pady=(5, 50))
        Button(staffHomeScreen_canvas, width=20, height=3, text="View Account",
               command=lambda: viewMyAccountStaff(employeeNum, staffHomeScreen_canvas)).grid(row=2, column=2, padx=5,
                                                                                             pady=(5, 50))


    if jobTitle == "Cleaner":
        Button(staffHomeScreen_canvas, width=20, height=3, text="Print Tickets",
               command=lambda: messagebox.showinfo("Unauthorised Access", "You do not have permission to access this")).grid(row=1, column=0, padx=10,
                                                                                       pady=10)
        Button(staffHomeScreen_canvas, width=20, height=3, text="Today's Screenings",
               command=lambda: messagebox.showinfo("Unauthorised Access", "You do not have permission to access this")).grid(row=1, column=1, padx=5,
                                                                                           pady=5)
        Button(staffHomeScreen_canvas, width=20, height=3, text="Customer Orders",
               command=lambda: messagebox.showinfo("Unauthorised Access", "You do not have permission to access this")).grid(row=1, column=2, padx=5,
                                                                                          pady=5)
        Button(staffHomeScreen_canvas, width=20, height=3, text="Book Film for Customer",
               command=lambda: messagebox.showinfo("Unauthorised Access", "You do not have permission to access this")).grid(row=1, column=3,
                                                                                                        padx=(5, 150), pady=5)
        Button(staffHomeScreen_canvas, width=20, height=3, text="Book Food for Customer",
               command=lambda: messagebox.showinfo("Unauthorised Access", "You do not have permission to access this")).grid(row=2, column=0, padx=5,
                                                                                              pady=(5, 50))
        Button(staffHomeScreen_canvas, width=20, height=3, text="Staff Discount",
               command=lambda: staffDiscount(employeeNum, staffHomeScreen_canvas)).grid(row=2, column=1, padx=5, pady=(5, 50))
        Button(staffHomeScreen_canvas, width=20, height=3, text="View Account",
               command=lambda: viewMyAccountStaff(employeeNum, staffHomeScreen_canvas)).grid(row=2, column=2, padx=5,
                                                                                             pady=(5, 50))


    Label(staffHomeScreen_canvas, text="Staff Home Screen", font=("Arial", 30), fg="purple").grid(row=0, column=0, columnspan=4)

    Button(staffHomeScreen_canvas, width=20, height=3, text="Logout", command=lambda: home_screen(staffHomeScreen_canvas)).grid(row=2, column=3, padx=(5, 150), pady=(5, 50))

def printTickets(employeeNum, canvas):          #finding an order to print
    canvas.destroy()
    user32 = ctypes.windll.user32
    w = str(user32.GetSystemMetrics(0))
    h = str(user32.GetSystemMetrics(1))
    printTickets_canvas = Tk()
    printTickets_canvas.geometry(w+'x'+h)
    printTickets_canvas.configure(background='dark grey')
    printTickets_canvas.title("Print Tickets")
    printTickets_canvas.grid_rowconfigure(0, weight=1)
    printTickets_canvas.grid_rowconfigure(2, weight=1)
    printTickets_canvas.grid_columnconfigure(0, weight=1)
    printTickets_canvas.grid_columnconfigure(2, weight=1)

    Label(printTickets_canvas, text="Print Tickets", font=("Arial", 30), fg="purple").grid(row=0, column=0, columnspan=3)
    Label(printTickets_canvas, font=("Arial", 14), text="Order Number: ").grid(row=1, column=0, padx=(250, 20), pady=10)
    orderNum_entry = Entry(printTickets_canvas, width=20, font=("Arial", 14))       #asks for an order number
    orderNum_entry.grid(row=1, column=0, sticky=E)

    Button(printTickets_canvas, width=15, height=3, text='Find Order', command=lambda: printTicketsOrder(employeeNum, printTickets_canvas, orderNum_entry.get())).grid(row=2, column=1, pady=(10, 150))
    Button(printTickets_canvas, width=15, height=3, text='Back', command=lambda: staffHomeScreen(employeeNum, printTickets_canvas)).grid(row=2, column=0, pady=(10, 150))

def printTicketsOrder(employeeNum, canvas, orderNum):       #displaying the tickets to print
    canvas.destroy()
    user32 = ctypes.windll.user32
    w = str(user32.GetSystemMetrics(0))
    h = str(user32.GetSystemMetrics(1))
    printTicketsOrder_canvas = Tk()
    printTicketsOrder_canvas.geometry(w+'x'+h)
    printTicketsOrder_canvas.configure(background='dark grey')
    printTicketsOrder_canvas.title("Print Tickets")
    printTicketsOrder_canvas.grid_rowconfigure(0, weight=1)
    printTicketsOrder_canvas.grid_rowconfigure(2, weight=1)
    printTicketsOrder_canvas.grid_columnconfigure(0, weight=1)
    printTicketsOrder_canvas.grid_columnconfigure(2, weight=1)

    Label(printTicketsOrder_canvas, text="Print Tickets", font=("Arial", 25), fg="purple").grid(row=0, column=0, columnspan=3)

    orderNumValid = False
    orderLine = ""

    for filename in os.listdir(os.getcwd() + "\\customeraccounts"):
        with open(os.getcwd() + "\\customeraccounts\\" + filename, "r") as f:
            lines = f.readlines()[2:]
            for line in lines:
                order = line.split(";")[0]
                if order == orderNum:
                    orderLine = line        #gets the line of the order starting with the order number
                    orderNumValid = True
                else:
                    print()

        f.close()
    for filenames in os.listdir(os.getcwd() + "\\staffaccounts"):
        with open(os.getcwd() + "\\staffaccounts\\" + filenames, "r") as f:
            lines = f.readlines()[3:]
            for line in lines:
                order = line.split(";")[0]
                if order == orderNum:
                    orderNumValid = True
                else:
                    print()
        f.close()

    if orderNumValid == True:
        Label(printTicketsOrder_canvas, text=("Order Number: " + orderNum)).grid(row=1, column=0, padx=10, pady=10)
        splitline = orderLine.split(";")
        ticketTypeChild = splitline[6]
        ticketTypeStudent = splitline[7]
        ticketTypeAdult = splitline[8]
        ticketTypeSenior = splitline[9]
        ticketTypes = []
        ticketType = ""
        if ticketTypeChild != "0":      #gets the type of ticket to be displayed on each ticket
            ticketTypeChild = int(ticketTypeChild)
            i = ticketTypeChild
            while i!=0:
                ticketTypes.append("Child")     #appends to the list for the number of times it appears
                i=i-1
        if ticketTypeStudent != "0":
            ticketTypeStudent = int(ticketTypeStudent)
            i = ticketTypeStudent
            while i!=0:
                ticketTypes.append("Student")
                i=i-1
        if ticketTypeAdult != "0":
            ticketTypeAdult = int(ticketTypeAdult)
            i = ticketTypeAdult
            while i!=0:
                ticketTypes.append("Adult")
                i=i-1
        if ticketTypeSenior != "0":
            ticketTypeSenior = int(ticketTypeSenior)
            i = ticketTypeSenior
            while i!=0:
                ticketTypes.append("Senior")
                i=i-1
        seats = splitline[10]
        splitseats = seats.split(", ")      #gets each individual seat in the order
        j=2
        for seat in splitseats:     #makes a new ticket for each seat
            ticketSeat = "Seat " + seat
            ticketSeat = str(ticketSeat)        #gets a seat number
            ticketBox = Text(printTicketsOrder_canvas, height=10, width=20)
            ticketType = ticketTypes[0]         #gets a ticket type
            ticketInfo = ("\nFilm: " + str(splitline[1]) + "\nDate: " + str(splitline[2]) +"\nTime: " + str(splitline[3]) + "\nScreen: " + str(splitline[5]) + "\nScreen Type: " + str(splitline[6]) + "\nTickets: " + str(ticketType) +  "\n" + str(ticketSeat))
            del ticketTypes[0]                  #removes a ticket type from the list as its just been used up for this ticket
            ticketBox.insert(END, ticketInfo)   #adds the info to the text box
            ticketBox.grid(row=j, column=0)     #displays the text box in a new column for each one
            j=j+1
        food = splitline[13]        #does the same for the food so there is a food ticket as well in a new text box
        foodInfo = ""
        foodBox = Text(printTicketsOrder_canvas, height=10, width=20)
        foodItems = food.split(" ")
        for item in foodItems:
            foodInfo = foodInfo + ("\n" + item)
        foodBox.insert(END, foodInfo)
        foodBox.grid(row=2, column=1)
    else:
        messagebox.showinfo("Invalid Order Number", "This order number does not exist")

    Button(printTicketsOrder_canvas, width=15, height=3, text='Back', command=lambda: printTickets(employeeNum, printTicketsOrder_canvas)).grid(row=12, column=0, pady=(10, 200))
    Button(printTicketsOrder_canvas, width=15, height=3, text='Print',
           command=lambda: printer(employeeNum, printTicketsOrder_canvas)).grid(row=12, column=1, pady=(10, 200))

def printer(employeeNum, canvas):       #sends the tickets to the 'printer'
    messagebox.showinfo("Print Successful", "Tickets have been sent to print")
    staffHomeScreen(employeeNum, canvas)

def todaysScreenings(employeeNum, canvas):          #gets all of the screening that are showing today
    canvas.destroy()
    user32 = ctypes.windll.user32
    w = str(user32.GetSystemMetrics(0))
    h = str(user32.GetSystemMetrics(1))
    todaysScreenings_canvas = Tk()
    todaysScreenings_canvas.geometry(w+'x'+h)
    todaysScreenings_canvas.configure(background='dark grey')
    todaysScreenings_canvas.title("Today's Screenings")
    todaysScreenings_canvas.grid_rowconfigure(0, weight=1)
    todaysScreenings_canvas.grid_rowconfigure(2, weight=1)
    todaysScreenings_canvas.grid_columnconfigure(0, weight=1)
    todaysScreenings_canvas.grid_columnconfigure(2, weight=1)

    Label(todaysScreenings_canvas, text="Today's Screenings", font=("Arial", 25), fg="purple").grid(row=0, column=0, columnspan=3)
    # dateToday = dt.datetime.today().strftime('%Y-%m-%d')      #gets todays date
    dateToday = "10-03-19"
    dateToday = dt.datetime.strptime(dateToday, "%d-%m-%y")
    dateToday = dt.datetime.strftime(dateToday, '%#d-%#m-%y')       #gets it in the correct format
    dateToday = str(dateToday)

    onToday = []
    i = 1
    for dir in os.listdir(os.getcwd() + "\\films"):         #goes through each folder
        try:
            for filename in os.listdir(os.getcwd() + "\\films\\" + dir):            #goes through each text file
                if dateToday in filename:           #checks if the date exists in the file name
                    onToday.append(filename)
                    with open(os.getcwd() + "\\films\\" + dir + "\\" + filename, "r") as f:
                        path = os.getcwd() + "\\films\\" + dir + "\\" + filename
                        film = dir
                        Label(todaysScreenings_canvas, font=("Arial", 14),
                              text=(dir + " " + filename.replace("-", "/").replace(".txt", ""))).grid(row=i,        #makes a label the screening in a new row
                                                                                                       column=0, pady=5)
                        Button(todaysScreenings_canvas, width=10, height=2, text='View',
                               command=lambda thisFilm=film, can=todaysScreenings_canvas, pth=path,     #assigns the variable inside the command as it changes each time the loop iterates
                                              scr=filename: todaysScreeningsView(employeeNum, can, pth, scr,
                                                                                  thisFilm)).grid(row=i,
                                                                                                  column=1, pady=5)
                        i = i + 1
                    f.close()
                else:
                    print()
        except:
            print()


    Button(todaysScreenings_canvas, width=15, height=3, text='Back', command=lambda: staffHomeScreen(employeeNum, todaysScreenings_canvas)).grid(row=i+1, column=2, pady=(10, 150))

def todaysScreeningsView(employeeNum, canvas, path, filename, film):        #showing details of the screening
    canvas.destroy()
    user32 = ctypes.windll.user32
    w = str(user32.GetSystemMetrics(0))
    h = str(user32.GetSystemMetrics(1))
    todaysScreeningsView_canvas = Tk()
    todaysScreeningsView_canvas.geometry(w+'x'+h)
    todaysScreeningsView_canvas.configure(background='dark grey')
    todaysScreeningsView_canvas.title("Today's Screenings")
    todaysScreeningsView_canvas.grid_rowconfigure(0, weight=1)
    todaysScreeningsView_canvas.grid_rowconfigure(2, weight=1)
    todaysScreeningsView_canvas.grid_columnconfigure(0, weight=1)
    todaysScreeningsView_canvas.grid_columnconfigure(2, weight=1)


    with open(path, "r") as f:
        lines = f.readlines()
        howmanylines = len(lines)
        i = 4
        s = 0
        takenSeats = ""
        numOrders = int(howmanylines) - i
        while i < howmanylines:
            orderLine = lines[i]
            splitline = orderLine.split(";")
            seats = splitline[2]
            username = splitline[1]
            splitseats = seats.split(", ")
            for seat in splitseats:     #gets each seat that has been taken
                s = s + 1
                takenSeats = takenSeats + str(seat) + " (" + str(username) + ") " + ", "        #shows who is sitting at that seat
            i = i + 1
    f.close()
    takenSeats = takenSeats[:-2]        #string of seats with the last comma taken off

    Label(todaysScreeningsView_canvas, text=("Details for Today's " + film + " " + filename.replace("-", "/").replace(".txt", "") + " Screening"), font=("Arial", 25), fg="purple").grid(row=0, column=0, columnspan=3)
    Label(todaysScreeningsView_canvas, font=("Arial", 14), text=("Film: " + str(film))).grid(row=1, column=0, padx=10, pady=10, columnspan=3)
    Label(todaysScreeningsView_canvas, font=("Arial", 14), text=("Date: " + str(lines[0].replace("-", "/")))).grid(row=2, column=0, padx=10, pady=10, columnspan=3)
    Label(todaysScreeningsView_canvas, font=("Arial", 14), text=("Time: " + str(lines[1].replace("-", "/")))).grid(row=3, column=0, padx=10, pady=10, columnspan=3)
    Label(todaysScreeningsView_canvas, font=("Arial", 14), text=("Screen: " + str(lines[2]))).grid(row=4, column=0, padx=10, pady=10, columnspan=3)
    Label(todaysScreeningsView_canvas, font=("Arial", 14), text=("Screen Type: " + str(lines[3]))).grid(row=5, column=0, padx=10, pady=10, columnspan=3)
    Label(todaysScreeningsView_canvas, font=("Arial", 14), text=("Capacity: 30")).grid(row=6, column=0, padx=10, pady=10, columnspan=3)
    Label(todaysScreeningsView_canvas, font=("Arial", 14), text=("Seats Taken: " + str(s) + "\n" + str(takenSeats))).grid(row=7, column=0, padx=10, pady=10, columnspan=3)
    Label(todaysScreeningsView_canvas, font=("Arial", 14), text=("Number of Different Orders: " + str(numOrders))).grid(row=8, column=0, padx=10, pady=10, columnspan=3)

    Button(todaysScreeningsView_canvas, width=15, height=3, text='Back', command=lambda: todaysScreenings(employeeNum, todaysScreeningsView_canvas)).grid(row=9, column=1, pady=(10, 150), sticky=E)

def customersOrders(employeeNum, canvas):       #viewing purchased orders
    canvas.destroy()
    user32 = ctypes.windll.user32
    w = str(user32.GetSystemMetrics(0))
    h = str(user32.GetSystemMetrics(1))
    customersOrders_canvas = Tk()
    customersOrders_canvas.geometry(w+'x'+h)
    customersOrders_canvas.configure(background='dark grey')
    customersOrders_canvas.title("Customer's Orders")
    customersOrders_canvas.grid_rowconfigure(0, weight=1)
    customersOrders_canvas.grid_rowconfigure(2, weight=1)
    customersOrders_canvas.grid_columnconfigure(0, weight=1)
    customersOrders_canvas.grid_columnconfigure(2, weight=1)

    Label(customersOrders_canvas, font=("Arial", 14), text="Username ").grid(row=1, column=0, sticky=E)
    username_entry = Entry(customersOrders_canvas, width=20, font=("Arial", 14))
    username_entry.grid(row=1, column=1, sticky=W, padx=(20, 0))

    Label(customersOrders_canvas, text="Customer's Orders", font=("Arial", 25), fg="purple").grid(row=0, column=0, columnspan=3)
    Button(customersOrders_canvas, width=15, height=3, text='Search', command=lambda: findCustomer(employeeNum, username_entry.get(), customersOrders_canvas)).grid(row=2, column=1, pady=(10, 150), padx=(300, 10))
    Button(customersOrders_canvas, width=15, height=3, text='Back', command=lambda: staffHomeScreen(employeeNum, customersOrders_canvas)).grid(row=2, column=0, pady=(10, 150), padx=(150, 0))

def findCustomer(employeeNum, username, canvas):        #checking the username exists on the system
    if os.path.isfile(os.getcwd() + "\\customeraccounts\\" + username + ".txt"):
        viewMyOrders(username, canvas)
    else:
        messagebox.showinfo("Username doesn't exist", "Enter a valid username")

def bookFilmForCustomer(employeeNum, canvas, jobTitle):         #booking tickets for a customer
    canvas.destroy()
    user32 = ctypes.windll.user32
    w = str(user32.GetSystemMetrics(0))
    h = str(user32.GetSystemMetrics(1))
    bookFilmForCustomer_canvas = Tk()
    bookFilmForCustomer_canvas.geometry(w+'x'+h)
    bookFilmForCustomer_canvas.configure(background='dark grey')
    bookFilmForCustomer_canvas.title("Book Tickets for Customer")
    bookFilmForCustomer_canvas.grid_rowconfigure(0, weight=1)
    bookFilmForCustomer_canvas.grid_rowconfigure(2, weight=1)
    bookFilmForCustomer_canvas.grid_columnconfigure(0, weight=1)
    bookFilmForCustomer_canvas.grid_columnconfigure(2, weight=1)

    Label(bookFilmForCustomer_canvas, font=("Arial", 14), text="Username ").grid(row=1, column=0, padx=10, pady=10, sticky=E)
    username_entry = Entry(bookFilmForCustomer_canvas, width=20, font=("Arial", 14))
    username_entry.grid(row=1, column=1, sticky=W, padx=10, pady=10)

    Label(bookFilmForCustomer_canvas, text="Book Tickets for Customer", font=("Arial", 25), fg="purple").grid(row=0, column=0, columnspan=3)
    Button(bookFilmForCustomer_canvas, width=20, height=3, text='Search for Screenings',
           command=lambda: bookFilmForCustomerValid(employeeNum, username_entry.get(), bookFilmForCustomer_canvas)).grid(row=2,
                                                                                                         column=1, pady=10, sticky=W)
    Button(bookFilmForCustomer_canvas, width=20, height=3, text='Back',
           command=lambda: staffHomeScreen(employeeNum, bookFilmForCustomer_canvas)).grid(row=4, column=1, pady=(10, 200), sticky=W)

    if jobTitle == "Supervisor":
        Button(bookFilmForCustomer_canvas, width=20, height=3, text="Add Customer Account",
               command=lambda: signUpUsername(bookFilmForCustomer_canvas)).grid(row=3, column=1, sticky=W, pady=10)
    else:
        Button(bookFilmForCustomer_canvas, width=20, height=3, text="Add Customer Account",
               command=lambda: messagebox.showinfo("Unauthorised Access", "Ask your supervisor or manager to log on and set up a customer account.")).grid(row=3, column=1, sticky=W, pady=10)



def bookFilmForCustomerValid(employeeNum, username, canvas):        #checking the username exists on the system
    if os.path.isfile(os.getcwd() + "\\customeraccounts\\" + username + ".txt"):
        bookTicket(username, canvas)
    else:
        messagebox.showinfo("Username doesn't exist", "Enter a valid username")

def bookFoodForCustomer(employeeNum, canvas):           #booking food for a customer
    canvas.destroy()
    user32 = ctypes.windll.user32
    w = str(user32.GetSystemMetrics(0))
    h = str(user32.GetSystemMetrics(1))
    bookFoodForCustomer_canvas = Tk()
    bookFoodForCustomer_canvas.geometry(w+'x'+h)
    bookFoodForCustomer_canvas.configure(background='dark grey')
    bookFoodForCustomer_canvas.title("Book Food for Customer")
    bookFoodForCustomer_canvas.grid_rowconfigure(0, weight=1)
    bookFoodForCustomer_canvas.grid_rowconfigure(2, weight=1)
    bookFoodForCustomer_canvas.grid_columnconfigure(0, weight=1)
    bookFoodForCustomer_canvas.grid_columnconfigure(2, weight=1)

    Label(bookFoodForCustomer_canvas, font=("Arial", 14), text="Username ").grid(row=1, column=0, padx=10, pady=10, sticky=E)
    username_entry = Entry(bookFoodForCustomer_canvas, width=20, font=("Arial", 14))
    username_entry.grid(row=1, column=1, sticky=W, padx=10, pady=10)

    Label(bookFoodForCustomer_canvas, text="Book Food for Customer", font=("Arial", 25), fg="purple").grid(row=0,
                                                                                                              column=0, columnspan=3)
    Button(bookFoodForCustomer_canvas, width=20, height=3, text='Search for Orders',
           command=lambda: bookFoodForCustomerValid(employeeNum, username_entry.get(),
                                                    bookFoodForCustomer_canvas)).grid(row=2,
                                                                                      column=1, pady=10, sticky=W)
    Button(bookFoodForCustomer_canvas, width=20, height=3, text='Back',
           command=lambda: staffHomeScreen(employeeNum, bookFoodForCustomer_canvas)).grid(row=3, column=1, pady=(10, 200), sticky=W)


def bookFoodForCustomerValid(employeeNum, username, canvas):        #getting the orders available to add food to
    if os.path.isfile(os.getcwd() + "\\customeraccounts\\" + username + ".txt"):
        file = open(os.getcwd() + "\\customeraccounts\\" + username + ".txt", "r")
        lines = file.readlines()
        howmanylines = len(lines)
        hasBeenDate = True
        hasBeenTime = True
        upcomingScreeningsList = []
        #upcomingScreenings = Listbox(customerHome_canvas)
        i = 2
        while i < howmanylines:
            orderLine = lines[i]
            splitline = orderLine.split(";")
            order = i - 1
            film = splitline[1] + " "
            date = splitline[2]
            time = splitline[3]
            if datetime.strptime(date.strip(), '%d/%m/%y') < dt.datetime.today():
                hasBeenDate = False
            if datetime.strptime(time.strip(), '%H:%M') < dt.datetime.now():
                hasBeenTime = False
            if hasBeenDate == False and hasBeenTime == False:       #checks its a future date and time
                screening = film + date + time
                upcomingScreeningsList.append(screening)            #adds screening to the list
                #upcomingScreenings.insert(END, screening)
            i = i + 1
        file.close()
        foodToExistingOrder(username, canvas, upcomingScreeningsList)
    else:
        messagebox.showinfo("Username doesn't exist", "Enter a valid username")

def staffDiscount(employeeNum, canvas):         #displays the discounts available for staff
    canvas.destroy()
    user32 = ctypes.windll.user32
    w = str(user32.GetSystemMetrics(0))
    h = str(user32.GetSystemMetrics(1))
    staffDiscount_canvas = Tk()
    staffDiscount_canvas.geometry(w + 'x' + h)
    staffDiscount_canvas.configure(background='dark grey')
    staffDiscount_canvas.title("Staff Discounts")
    staffDiscount_canvas.grid_rowconfigure(0, weight=1)
    staffDiscount_canvas.grid_rowconfigure(2, weight=1)
    staffDiscount_canvas.grid_columnconfigure(0, weight=1)
    staffDiscount_canvas.grid_columnconfigure(2, weight=1)

    Label(staffDiscount_canvas, font=("Arial", 25), fg="purple", text="Discounts Available for Staff").grid(row=0,
                                                                                                            column=0,
                                                                                                            columnspan=6)
    discount = PhotoImage(file="discountstar.png")      #gets an image

    deal1 = Canvas(staffDiscount_canvas, width=200, height=200)
    deal1Display = discount.zoom(1, 1)
    deal1.grid(row=1, column=0, pady=10)
    deal1.create_image(1, 1, anchor=NW, image=deal1Display)
    Label(staffDiscount_canvas, font=("Arial", 14), text="15% all tickets").grid(row=1, column=0)

    deal2 = Canvas(staffDiscount_canvas, width=200, height=200)
    deal2Display = discount.zoom(1, 1)
    deal2.grid(row=2, column=2, pady=10, padx=(0, 100))
    deal2.create_image(1, 1, anchor=NW, image=deal2Display)
    Label(staffDiscount_canvas, font=("Arial", 14), text="Free popcorn Fridays").grid(row=2, column=2, padx=(0, 100))

    deal3 = Canvas(staffDiscount_canvas, width=200, height=200)
    deal3Display = discount.zoom(1, 1)
    deal3.grid(row=1, column=3, pady=10, padx=(0, 100))
    deal3.create_image(1, 1, anchor=NW, image=deal3Display)
    Label(staffDiscount_canvas, font=("Arial", 14), text="15% off all snacks").grid(row=1, column=3, padx=(0, 100))

    deal4 = Canvas(staffDiscount_canvas, width=200, height=200)
    deal4Display = discount.zoom(1, 1)
    deal4.grid(row=2, column=4, pady=10, padx=(0, 100))
    deal4.create_image(1, 1, anchor=NW, image=deal4Display)
    Label(staffDiscount_canvas, font=("Arial", 14), text="Kids go free on Sundays").grid(row=2, column=4, padx=(0, 100))

    Button(staffDiscount_canvas, width=15, height=3, text='Back', command=lambda: staffHomeScreen(employeeNum, staffDiscount_canvas)).grid(
        row=3, column=3, pady=(10, 150))

    mainloop()


def viewMyAccountStaff(employeeNum, canvas):        #viewing details of a staff account - same as for customer
    canvas.destroy()
    user32 = ctypes.windll.user32
    w = str(user32.GetSystemMetrics(0))
    h = str(user32.GetSystemMetrics(1))
    viewMyAccountStaff_canvas = Tk()
    viewMyAccountStaff_canvas.geometry(w+'x'+h)
    viewMyAccountStaff_canvas.configure(background='dark grey')
    viewMyAccountStaff_canvas.title("My Account")
    viewMyAccountStaff_canvas.grid_rowconfigure(0, weight=1)
    viewMyAccountStaff_canvas.grid_rowconfigure(2, weight=1)
    viewMyAccountStaff_canvas.grid_columnconfigure(0, weight=1)
    viewMyAccountStaff_canvas.grid_columnconfigure(2, weight=1)

    Label(viewMyAccountStaff_canvas, font=("Arial", 20), fg="purple", text="My Account").grid(row=0, column=0, columnspan=3)

    Button(viewMyAccountStaff_canvas, width=15, height=4, text='Reset Password',
           command=lambda: resetPasswordRequestStaff(viewMyAccountStaff_canvas, employeeNum)).grid(row=1, column=2)
    Button(viewMyAccountStaff_canvas, width=18, height=4, text='View personal details',
           command=lambda: viewMyDetailsStaff(viewMyAccountStaff_canvas, employeeNum)).grid(row=1, column=1)
    Button(viewMyAccountStaff_canvas, width=15, height=4, text='Back', command=lambda: staffHomeScreen(employeeNum, viewMyAccountStaff_canvas)).grid(
        row=1, column=0)


def resetPasswordRequestStaff(canvas, employeeNum):     #resetting a password for a staff account - same as for customer
    canvas.destroy()
    user32 = ctypes.windll.user32
    w = str(user32.GetSystemMetrics(0))
    h = str(user32.GetSystemMetrics(1))
    resetPasswordRequestStaff_canvas = Tk()
    resetPasswordRequestStaff_canvas.geometry(w+'x'+h)
    resetPasswordRequestStaff_canvas.configure(background='dark grey')
    resetPasswordRequestStaff_canvas.title("Reset Your Password")
    resetPasswordRequestStaff_canvas.grid_rowconfigure(0, weight=1)
    resetPasswordRequestStaff_canvas.grid_rowconfigure(2, weight=1)
    resetPasswordRequestStaff_canvas.grid_columnconfigure(0, weight=1)
    resetPasswordRequestStaff_canvas.grid_columnconfigure(2, weight=1)

    Label(resetPasswordRequestStaff_canvas, font=("Arial", 20), text="Reset Your MovieMania Account Password", fg="purple",
          anchor='center').grid(row=0, column=0, columnspan=3, padx=(0, 50))
    Label(resetPasswordRequestStaff_canvas, font=("Arial", 14), text="Current Password").grid(row=1, column=0, sticky=E,
                                                                                         pady=10, padx=20)
    currentPassword_entry = Entry(resetPasswordRequestStaff_canvas, width=20, font=("Arial", 14))
    currentPassword_entry.grid(row=1, column=1, sticky=W)
    Label(resetPasswordRequestStaff_canvas, font=("Arial", 14), text="New Password").grid(row=2, column=0, sticky=E, pady=10,
                                                                                     padx=20)
    password1_entry = Entry(resetPasswordRequestStaff_canvas, show="*", width=20, font=("Arial", 14))
    password1_entry.grid(row=2, column=1, sticky=W)
    Label(resetPasswordRequestStaff_canvas, font=("Arial", 14), text="Confirm New Password").grid(row=3, column=0, sticky=E,
                                                                                             pady=10, padx=20)
    password2_entry = Entry(resetPasswordRequestStaff_canvas, show="*", width=20, font=("Arial", 14))
    password2_entry.grid(row=3, column=1, sticky=W)


    Button(resetPasswordRequestStaff_canvas, width=15, height=3, text="Reset",
           command=lambda: resetPasswordStaff(resetPasswordRequestStaff_canvas, employeeNum,
                                              currentPassword_entry.get(), password1_entry.get(),
                                              password2_entry.get())).grid(row=4, column=1, pady=(50, 200), padx=(250, 0), sticky=E)
    Button(resetPasswordRequestStaff_canvas, width=15, height=3, text="Back",
           command=lambda: viewMyAccountStaff(employeeNum, resetPasswordRequestStaff_canvas)).grid(row=4, column=0, pady=(50, 200))


def resetPasswordStaff(canvas, employeeNum, currentPassword, newPassword1, newPassword2):       #checking entries are valid to reset the password
    pchecker = os.getcwd() + "\\staffaccounts\\" + employeeNum + ".txt"
    if os.path.isfile(os.getcwd() + "\\staffaccounts\\" + employeeNum + ".txt"):
        f = open(os.getcwd() + "\\staffaccounts\\" + employeeNum + ".txt")
        lines = f.readlines()
        f.close()
        passwordtocheck = lines[0].strip()
        if checker(passwordtocheck, currentPassword):
            if newPassword1 == newPassword2:
                newHashedPassword = hasher(newPassword1)
                with open(pchecker, "r") as file:
                    lines = file.readlines()
                    infoLine = lines[1]
                    howmanylines = len(lines)
                    file.close()
                    lines[0] = newHashedPassword
                    writingstuff = []
                    writingstuff.append(lines[0] + "\n")
                    i = 1
                    while i < howmanylines:
                        writingstuff.append(lines[i])
                        i = i + 1

                    with open(pchecker, "w") as file:
                        for line in writingstuff:
                            file.write(line)
                    file.close()
                    messagebox.showinfo("Reset Password Complete", "Your account password has been reset.")
                    staffLogin(canvas)
            else:
                messagebox.showinfo("New Passwords Don't Match", "Your new password entries do not match.")
        else:
            messagebox._show("Incorrect Password", "Password is incorrect babe")
    else:
        messagebox._show("Incorrect Employee Number", "Employee Number doesn't exist hun")


def viewMyDetailsStaff(canvas, employeeNum):        #viewing personal details of a staff account
    canvas.destroy()
    user32 = ctypes.windll.user32
    w = str(user32.GetSystemMetrics(0))
    h = str(user32.GetSystemMetrics(1))
    viewMyDetailsStaff_canvas = Tk()
    viewMyDetailsStaff_canvas.geometry(w+'x'+h)
    viewMyDetailsStaff_canvas.configure(background='dark grey')
    viewMyDetailsStaff_canvas.title("My Details")
    viewMyDetailsStaff_canvas.grid_rowconfigure(0, weight=1)
    viewMyDetailsStaff_canvas.grid_rowconfigure(2, weight=1)
    viewMyDetailsStaff_canvas.grid_columnconfigure(0, weight=1)
    viewMyDetailsStaff_canvas.grid_columnconfigure(2, weight=1)

    file = open(os.getcwd() + "\\staffaccounts\\" + employeeNum + ".txt", "r")
    lines = file.readlines()
    accountLine = lines[0]
    infoLine = lines[1]
    jobLine = lines[2]
    splitline = infoLine.split(";")
    jsplitline = jobLine.split(";")
    title = splitline[0]
    name = splitline[1]
    surname = splitline[2]
    dob = splitline[3]
    address1 = splitline[4]
    address2 = splitline[5]
    postcode = splitline[6]
    email = splitline[7]
    mobile = splitline[8]
    jobTitle = jsplitline[0]
    contractedHours = jsplitline[1]
    wage = jsplitline[2]
    accountNum = jsplitline[3]
    sortCode = jsplitline[4]
    file.close()

    Label(viewMyDetailsStaff_canvas, font=("Arial", 20), fg="purple", text="My Details").grid(row=0, column=0, columnspan=3)

    Label(viewMyDetailsStaff_canvas, font=("Arial", 14), text=("Title: " + title)).grid(row=2, column=0, pady=5, padx=10)
    Label(viewMyDetailsStaff_canvas, font=("Arial", 14), text=("Name: " + name)).grid(row=3, column=0, pady=5, padx=10)
    Label(viewMyDetailsStaff_canvas, font=("Arial", 14), text=("Surname: " + surname)).grid(row=4, column=0, pady=5, padx=10)
    Label(viewMyDetailsStaff_canvas, font=("Arial", 14), text=("DOB: " + dob)).grid(row=5, column=0, pady=5, padx=10)
    Label(viewMyDetailsStaff_canvas, font=("Arial", 14), text=("Address line 1: " + address1)).grid(row=6, column=0, pady=5,
                                                                                padx=10)
    Label(viewMyDetailsStaff_canvas, font=("Arial", 14), text=("Address line 2: " + address2)).grid(row=7, column=0, pady=5,
                                                                                padx=10)
    Label(viewMyDetailsStaff_canvas, font=("Arial", 14), text=("Postcode: " + postcode)).grid(row=8, column=0, pady=5, padx=10)
    Label(viewMyDetailsStaff_canvas, font=("Arial", 14), text=("Email: " + email)).grid(row=9, column=0, pady=5, padx=10)
    Label(viewMyDetailsStaff_canvas, font=("Arial", 14), text=("Mobile: " + mobile)).grid(row=10, column=0, pady=5, padx=10)
    Label(viewMyDetailsStaff_canvas, font=("Arial", 14), text=("Job Title: " + jobTitle)).grid(row=11, column=0, pady=5, padx=10)
    Label(viewMyDetailsStaff_canvas, font=("Arial", 14), text=("Contracted Hours: " + contractedHours)).grid(row=12, column=0,
                                                                                         pady=5, padx=10)
    Label(viewMyDetailsStaff_canvas, font=("Arial", 14), text=("Wage (per hour): " + wage)).grid(row=13, column=0, pady=5,
                                                                             padx=10)
    Label(viewMyDetailsStaff_canvas, font=("Arial", 14), text=("Account Number: " + accountNum)).grid(row=14, column=0, pady=5,
                                                                                  padx=10)
    Label(viewMyDetailsStaff_canvas, font=("Arial", 14), text=("Sort Code: " + sortCode)).grid(row=15, column=0, pady=(5, 100), padx=10)

    Button(viewMyDetailsStaff_canvas, width=17, height=4, text="Back", command=lambda: viewMyAccountStaff(employeeNum, viewMyDetailsStaff_canvas)).grid(row=13, column=2, padx=10, rowspan=2)


def managerLogin(canvas):       #logging in as a manager
    canvas.destroy()
    user32 = ctypes.windll.user32
    w = str(user32.GetSystemMetrics(0))
    h = str(user32.GetSystemMetrics(1))
    managerLogin_canvas = Tk()
    managerLogin_canvas.geometry(w+'x'+h)
    managerLogin_canvas.configure(background='dark grey')
    managerLogin_canvas.title("Managers's Login")
    managerLogin_canvas.grid_rowconfigure(0, weight=1)
    managerLogin_canvas.grid_rowconfigure(2, weight=1)
    managerLogin_canvas.grid_columnconfigure(0, weight=1)
    managerLogin_canvas.grid_columnconfigure(2, weight=1)

    Label(managerLogin_canvas, font=("Arial", 25), text="Manager's Login", fg="purple").grid(row=0, column=0, columnspan=3)
    Label(managerLogin_canvas, font=("Arial", 12), text="Username").grid(row=1, column=0, sticky=E, pady=(0, 5), padx=10)
    username_entry = Entry(managerLogin_canvas, width=20, font=("Arial", 15))
    username_entry.grid(row=1, column=1, sticky=E)
    Label(managerLogin_canvas, font=("Arial", 12), text="Password").grid(row=2, column=0, sticky=E, pady=(10, 0), padx=10)
    password_entry = Entry(managerLogin_canvas, show="*", width=20, font=("Arial", 15))
    password_entry.grid(row=2, column=1, sticky=E)

    Button(managerLogin_canvas, width=20, height=3, text='Log In',
           command=lambda: managerValidLogin(managerLogin_canvas, username_entry.get(), password_entry.get())).grid(
        row=3, column=1, sticky=W, padx=10)
    Button(managerLogin_canvas, width=20, height=3, text='Back', command=lambda: home_screen(managerLogin_canvas)).grid(row=4, column=1,
                                                                                                    sticky=W, padx=10, pady=(0, 150))


def managerValidLogin(canvas, username_entry, password_entry):      #checks login details are valid
    if username_entry == "zxcv" and password_entry == "1234":       #only one manager so fixed username and password
        managerHome(canvas)
    else:
        messagebox.showinfo("Access Denied", "Incorrect Username or Password")



def managerHome(canvas):            #home screen for manager once logged in
    canvas.destroy()
    user32 = ctypes.windll.user32
    w = str(user32.GetSystemMetrics(0))
    h = str(user32.GetSystemMetrics(1))
    managerHome_canvas = Tk()
    managerHome_canvas.geometry(w+'x'+h)
    managerHome_canvas.configure(background='dark grey')
    managerHome_canvas.title("Manager Home Screen")
    managerHome_canvas.grid_rowconfigure(0, weight=1)
    managerHome_canvas.grid_rowconfigure(2, weight=1)
    managerHome_canvas.grid_columnconfigure(0, weight=1)
    managerHome_canvas.grid_columnconfigure(2, weight=1)

    Label(managerHome_canvas, font=("Arial", 25), text="Welcome to Your Manager Account", fg="purple").grid(row=0,
                                                                                                            column=0,
                                                                                                            columnspan=3)

    Button(managerHome_canvas, width=20, height=3, text='Add Film Title', command=lambda: addFilm(managerHome_canvas)).grid(row=1,
                                                                                                                 column=0)
    Button(managerHome_canvas, width=20, height=3, text='Add Film Screening', command=lambda: addScreening(managerHome_canvas)).grid(row=1, column=1)
    Button(managerHome_canvas, width=20, height=3, text='View Customer Accounts', command=lambda: lookUpCustomers(managerHome_canvas)).grid(row=2, column=0, pady=(0, 100))
    Button(managerHome_canvas, width=20, height=3, text='View Staff Accounts', command=lambda: lookUpStaff(managerHome_canvas)).grid(row=2, column=1, pady=(0, 100))
    Button(managerHome_canvas, width=20, height=3, text='View Sales', command=lambda: viewSales(managerHome_canvas)).grid(row=1, column=2)
    Button(managerHome_canvas, width=20, height=3, text='Logout', command=lambda: home_screen(managerHome_canvas)).grid(row=2, column=2, pady=(0, 100))

def viewSales(canvas):      #viewing the sales for the day and week
    canvas.destroy()
    user32 = ctypes.windll.user32
    w = str(user32.GetSystemMetrics(0))
    h = str(user32.GetSystemMetrics(1))
    viewSales_canvas = Tk()
    viewSales_canvas.geometry(w+'x'+h)
    viewSales_canvas.configure(background='dark grey')
    viewSales_canvas.title("View Sales")
    viewSales_canvas.grid_rowconfigure(0, weight=1)
    viewSales_canvas.grid_rowconfigure(2, weight=1)
    viewSales_canvas.grid_columnconfigure(0, weight=1)
    viewSales_canvas.grid_columnconfigure(2, weight=1)

    daySales, weekSales, weekFilms, weekFood, dayFilms, dayFood, filmSales, foodSales = 0, 0, 0, 0, 0, 0, 0, 0
    amount = ""

    #dateToday = dt.datetime.today().strftime('%Y-%m-%d')
    dateToday = "10-03-19"
    dateToday = dt.datetime.strptime(dateToday, "%d-%m-%y")
    dateToday = dt.datetime.strftime(dateToday, '%#d-%#m-%y')
    dateToday = str(dateToday)
    for dir in os.listdir(os.getcwd() + "\\films"):
        try:
            for filename in os.listdir(os.getcwd() + "\\films\\" + dir):
                if dateToday in filename:
                    with open(os.getcwd() + "\\films\\" + dir + "\\" + filename, "r") as f:
                        lines = f.readlines()[4:]
                        for line in lines:
                            amount = line.split(";")[3]     #finding the cost of the order
                            dayFilms = dayFilms + float(amount)     #totaling the costs from all of the orders
                        f.close()
        except:
            print()

    for filename in os.listdir(os.getcwd() + "\\food"):     #doing the same for food
        if dateToday in filename:
            with open(os.getcwd() + "\\food" + "\\" + filename, "r") as f:
                lines = f.readlines()
                for line in lines:
                    amount = line.split(";")[2]
                    dayFood = dayFood + float(amount)
                f.close()
    daySales = dayFilms + dayFood

    #today = dt.date.today()
    today = "10-03-19"
    today = dt.datetime.strptime(today, "%d-%m-%y")
    for i in range(0, 7):       #repeating for 7 days to make up the week's sales
        today = today - dt.timedelta(days=i)
        newtoday = dt.datetime.strftime(today, '%#d-%#m-%y')
        newtoday = str(newtoday).split(" ")[0]
        for dir in os.listdir(os.getcwd() + "\\films"):
            try:
                for filename in os.listdir(os.getcwd() + "\\films\\" + dir):
                    if newtoday.replace("/", "-") in filename:
                        with open(os.getcwd() + "\\films\\" + dir + "\\" + filename, "r") as f:
                            lines = f.readlines()[4:]
                            for line in lines:
                                amount = line.split(";")[3]
                                weekFilms = weekFilms + float(amount)
                            f.close()
            except:
                print()
        for filename in os.listdir(os.getcwd() + "\\food"):
            if newtoday.replace("/", "-") in filename:
                with open(os.getcwd() + "\\food" + "\\" + filename, "r") as f:
                    lines = f.readlines()
                    for line in lines:
                        amount = line.split(";")[2]
                        weekFood = weekFood + float(amount)
                    f.close()
    weekSales = weekFilms + weekFood

    daySales = ("%.2f" % daySales)      #displaying to 2 decimal places
    dayFilms = ("%.2f" % dayFilms)
    dayFood = ("%.2f" % dayFood)
    weekSales = ("%.2f" % weekSales)
    weekFilms = ("%.2f" % weekFilms)
    weekFood = ("%.2f" % weekFood)

    Label(viewSales_canvas, text="Current Sales", font=("Arial", 25), fg="purple").grid(row=0, column=0, columnspan=3)
    Label(viewSales_canvas, font=("Arial", 14), text="Today's date: " + str(dateToday)).grid(row=1, column=1, padx=(0, 150), sticky=E)
    Label(viewSales_canvas, font=("Arial", 14), text="Today's total sales: £" + str(daySales)).grid(row=2, column=1, padx=(0, 150), sticky=E)
    Label(viewSales_canvas, font=("Arial", 14), text="Sales from today's films: £" + str(dayFilms)).grid(row=3, column=1, padx=(0, 150), sticky=E, pady=10)
    Label(viewSales_canvas, font=("Arial", 14), text="Sales from today's food: £" + str(dayFood)).grid(row=4, column=1, padx=(0, 150), sticky=E, pady=10)
    Label(viewSales_canvas, font=("Arial", 14), text="This week's total sales: £" + str(weekSales)).grid(row=5, column=1, padx=(0, 150), sticky=E, pady=10)
    Label(viewSales_canvas, font=("Arial", 14), text="This week's film sales: £" + str(weekFilms)).grid(row=6, column=1, padx=(0, 150), sticky=E, pady=10)
    Label(viewSales_canvas, font=("Arial", 14), text="This week's food sales: £" + str(weekFood)).grid(row=7, column=1, padx=(0, 150), sticky=E, pady=10)

    Button(viewSales_canvas, width=15, height=3, text='Back', command=lambda: managerHome(viewSales_canvas)).grid(row=8, column=2, sticky=W, pady=(20, 200))

def addFilm(canvas):            #adding a new film title
    canvas.destroy()
    user32 = ctypes.windll.user32
    w = str(user32.GetSystemMetrics(0))
    h = str(user32.GetSystemMetrics(1))
    addFilm_canvas = Tk()
    addFilm_canvas.geometry(w+'x'+h)
    addFilm_canvas.configure(background='dark grey')
    addFilm_canvas.title("Add new film titles")
    addFilm_canvas.grid_rowconfigure(0, weight=1)
    addFilm_canvas.grid_rowconfigure(2, weight=1)
    addFilm_canvas.grid_columnconfigure(0, weight=1)
    addFilm_canvas.grid_columnconfigure(2, weight=1)

    Label(addFilm_canvas, text="Add Film Title", font=("Arial", 25), fg="purple").grid(row=0, column=0, columnspan=3)

    Label(addFilm_canvas, font=("Arial", 14), text="Film title").grid(row=1, column=0, sticky=E, pady=10, padx=10)
    newFilm_entry = Entry(addFilm_canvas, width=20, font=("Arial", 14))
    newFilm_entry.grid(row=1, column=1, sticky=W)

    Button(addFilm_canvas, width=15, height=3, text='Submit', command=lambda: addFilmValid(addFilm_canvas, newFilm_entry.get())).grid(row=2,
                                                                                                               column=1,
                                                                                                               sticky=W,
                                                                                                               pady=10)
    Button(addFilm_canvas, width=15, height=3, text='Back', command=lambda: managerHome(addFilm_canvas)).grid(row=3, column=1,
                                                                                                  sticky=W, pady=(0, 200))


def addFilmValid(canvas, newFilm):          #checking the title doesn't already exists on the system
    file = open(os.getcwd() + "\\films\\films.txt", "r")
    currentFilms = []
    exist = False
    for line in file.readlines():
        currentFilms.append(line.strip())
    for film in currentFilms:
        if newFilm == film:
            exist = True

    if exist == False:
        messagebox.showinfo("Title Added", "The film title has been added to the system")
        f = open(os.getcwd() + "\\films\\films.txt", "a")           #adds the new title to the text file
        f.write(newFilm)
        f.close()
    else:
        messagebox.showinfo("Invalid", "Film is already showing")
    file.close()


def addScreening(canvas):           #adding a new screening for a film
    canvas.destroy()
    user32 = ctypes.windll.user32
    w = str(user32.GetSystemMetrics(0))
    h = str(user32.GetSystemMetrics(1))
    addScreening_canvas = Tk()
    addScreening_canvas.geometry(w+'x'+h)
    addScreening_canvas.configure(background='dark grey')
    addScreening_canvas.title("Add new dates and times for films")
    addScreening_canvas.grid_rowconfigure(0, weight=1)
    addScreening_canvas.grid_rowconfigure(2, weight=1)
    addScreening_canvas.grid_columnconfigure(0, weight=1)
    addScreening_canvas.grid_columnconfigure(2, weight=1)

    file = open(os.getcwd() + "\\films\\films.txt", "r")
    currentFilms = []
    for line in file:
        currentFilms.append(line)       #gets a list of films to choose from
    file.close()

    Label(addScreening_canvas, font=("Arial", 25), fg="purple", text="Add Film Screening").grid(row=0, column=0,
                                                                                                columnspan=3)

    Label(addScreening_canvas, font=("Arial", 14), text="Film").grid(row=1, column=0, sticky=E, pady=10)
    filmTitle = ttk.Combobox(addScreening_canvas, width=17, font=("Arial", 14))
    filmTitle["values"] = currentFilms
    filmTitle.grid(row=1, column=1, sticky=W, padx=5)
    filmTitle.current(0)
    Label(addScreening_canvas, font=("Arial", 14), text="Day").grid(row=2, column=0, sticky=E, pady=10)
    filmDateDay_entry = Entry(addScreening_canvas, width=5, font=("Arial", 14))
    filmDateDay_entry.grid(row=2, column=1, sticky=W, padx=5)
    Label(addScreening_canvas, font=("Arial", 14), text="Month").grid(row=3, column=0, sticky=E, pady=10)
    filmDateMonth_entry = Entry(addScreening_canvas, width=5, font=("Arial", 14))
    filmDateMonth_entry.grid(row=3, column=1, sticky=W, padx=5)
    Label(addScreening_canvas, font=("Arial", 14), text="Year").grid(row=4, column=0, sticky=E, pady=10)
    filmDateYear_entry = Entry(addScreening_canvas, width=5, font=("Arial", 14))
    filmDateYear_entry.grid(row=4, column=1, sticky=W, padx=5)
    Label(addScreening_canvas, font=("Arial", 14), text="Time").grid(row=5, column=0, sticky=E, pady=10)
    filmScreenHour = ttk.Combobox(addScreening_canvas, width=17, font=("Arial", 14), values=(
    "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23"))
    filmScreenHour.grid(row=5, column=1, sticky=W, padx=5)
    filmScreenHour.current(0)
    filmScreenMin = ttk.Combobox(addScreening_canvas, width=17, font=("Arial", 14), values=("00", "15", "30", "45"))
    filmScreenMin.grid(row=5, column=2, sticky=W, padx=5)
    filmScreenMin.current(0)

    Label(addScreening_canvas, font=("Arial", 14), text="Screen").grid(row=6, column=0, sticky=E, pady=10)
    filmScreen = ttk.Combobox(addScreening_canvas, width=17, font=("Arial", 14), values=("1", "2", "3", "4", "5", "6"))
    filmScreen.grid(row=6, column=1, sticky=W, padx=5)
    filmScreen.current(0)
    Label(addScreening_canvas, font=("Arial", 14), text="Screen Type").grid(row=7, column=0, sticky=E, pady=10)
    filmScreenType = ttk.Combobox(addScreening_canvas, width=17, font=("Arial", 14), values=("2D", "3D"))
    filmScreenType.grid(row=7, column=1, sticky=W, padx=5)
    filmScreenType.current(0)

    Button(addScreening_canvas, width=15, height=3, text='Submit', command=lambda: addScreeningValid(addScreening_canvas, filmTitle.get(), filmDateDay_entry.get(), filmDateMonth_entry.get(), filmDateYear_entry.get(), filmScreenHour.get(), filmScreenMin.get(), filmScreen.get(), filmScreenType.get())).grid(row=8,
                                                                                                                  column=1,
                                                                                                                  sticky=W, padx=50, pady=(30, 0))
    Button(addScreening_canvas, width=15, height=3, text='Back', command=lambda: managerHome(addScreening_canvas)).grid(row=9, column=1, sticky=W, padx=50, pady=(5, 100))

def addScreeningValid(canvas, Film, Day, Month, Year, Hour, Min, Screen, ScreenType):       #checks all entries for the screening are valid
    isValid = True
    dateInput = str(Day + "/" + Month + "/" + Year)         #puts the date in the correct format
    Year = int(Year)                                        #sets it as an integer so it can be compared with another number

    try:
        if datetime.strptime(dateInput.strip(), '%d/%m/%Y') < dt.datetime.today():      #converts dateInput to datetime.datetime format and then compares
            messagebox.showinfo("Invalid Date", "This date has already been, select a future date")
            isValid = False
        if (datetime.now() + dt.timedelta(days=365)) < datetime.strptime(dateInput, '%d/%m/%Y'):        #checks if date is longer than a year from current date
            messagebox.showinfo("Invalid year", "The year must be within the range of this year")
            isValid = False
        if Month.isdigit():
            Month = int(Month)
            if Month < 1 or Month > 12:
                messagebox.showinfo("Invalid month", "Input a number in the range 1-12 corresponding to the month")
                isValid = False
        if Day.isdigit():
            Day = int(Day)
            if Day < 1 or Day > 31:
                messagebox.showinfo("Invalid day", "Input a number in the range 1-31 corresponding to the day")
                isValid = False

        if isValid:     #only if all entries are valid
            time = Hour+"-"+Min         #time is changed to a format that can be written in the text file name
            dateInput = dt.datetime.strptime(dateInput, '%d/%m/%Y')
            dateInput = dateInput.strftime('%#d/%#m/%y')
            dateInput = dateInput.replace("/", "-")
            toWrite = (dateInput+" "+time+" "+"Screen "+Screen+" "+ScreenType)      #whats being written to the file
            addScreeningWrite(toWrite, Film, dateInput, time, Screen, ScreenType, canvas)
    except ValueError:
        messagebox.showinfo("Incorrect format", "Input dates in correct format")


def addScreeningWrite(toWrite, Film, dateInput, time, Screen, ScreenType, canvas):      #adds the new screening to the system
    path = os.getcwd()+"\\films\\"+Film
    if os.path.isdir(path):             #see if the files exist already
        if os.path.isfile(path+"\\"+toWrite+".txt"):
            messagebox.showinfo("Invalid", "File already exists")
        else:
            with open(path.strip()+"\\"+toWrite+".txt", "w") as f:
                f.write(dateInput+"\n"+time+"\n"+"Screen "+Screen+"\n"+ScreenType+"\n")
                f.close()
                messagebox.showinfo("Done!", "Screening has been added")
                managerHome(canvas)

    else:
        os.makedirs(path)
        if os.path.isfile(path+"\\"+toWrite+".txt"):
            messagebox.showinfo("Invalid", "File already exists")
        else:
            with open(path.strip()+"\\"+toWrite+".txt", "w") as f:
                f.write(dateInput+"\n"+time+"\n"+"Screen "+Screen+"\n"+ScreenType+"\n")     #writes the details to the file
                f.close()
                messagebox.showinfo("Done!", "Screening has been added")
                managerHome(canvas)

def lookUpCustomers(canvas):            #list of customer accounts that exist on the system
    canvas.destroy()
    user32 = ctypes.windll.user32
    w = str(user32.GetSystemMetrics(0))
    h = str(user32.GetSystemMetrics(1))
    lookUpCustomers_canvas = Tk()
    lookUpCustomers_canvas.geometry(w+'x'+h)
    lookUpCustomers_canvas.configure(background='dark grey')
    lookUpCustomers_canvas.title("View Customer Accounts")
    lookUpCustomers_canvas.grid_rowconfigure(0, weight=1)
    lookUpCustomers_canvas.grid_rowconfigure(2, weight=1)
    lookUpCustomers_canvas.grid_columnconfigure(0, weight=1)
    lookUpCustomers_canvas.grid_columnconfigure(2, weight=1)

    usernames = []
    files = os.listdir(os.getcwd() + "\\customeraccounts")
    for file in files:
        file = os.path.splitext(file)[0]
        usernames.append(file)

    Label(lookUpCustomers_canvas, text="View Customer Accounts", fg="purple", font=("Arial", 25)).grid(row=0, column=0,
                                                                                                       columnspan=3)
    Label(lookUpCustomers_canvas, font=("Arial", 14), text="Usernames").grid(row=1, column=0, sticky=E, pady=10,
                                                                             padx=10)
    listOfUsernames = ttk.Combobox(lookUpCustomers_canvas, width=30, font=("Arial", 14))
    listOfUsernames["values"] = usernames           #drop down box to select from
    listOfUsernames.grid(row=1, column=1, sticky=W)
    if not usernames:           #incase there are no customers, so the box doesn't cause an error
        Label(lookUpCustomers_canvas, text="No Customers on the System Yet").grid(row=1, column=0, sticky=W, pady=10,
                                                                                  padx=10)
    else:
        listOfUsernames.current(0)          #default display selection

    Button(lookUpCustomers_canvas, width=20, height=3, text="View", command=lambda: viewCustomerDetails(lookUpCustomers_canvas, listOfUsernames.get())).grid(row=2, column=1, pady=10, padx=(0, 150))
    Button(lookUpCustomers_canvas, width=20, height=3, text="Add customer account", command=lambda: signUpUsername(lookUpCustomers_canvas)).grid(row=3, column=1, pady=(50, 10), padx=(0, 150))
    Button(lookUpCustomers_canvas, width=20, height=3, text="Back", command=lambda: managerHome(lookUpCustomers_canvas)).grid(row=10, column=1, padx=(0, 150), pady=(10, 100))

def viewCustomerDetails(canvas, username):          #displaying the information of the customer account
    canvas.destroy()
    user32 = ctypes.windll.user32
    w = str(user32.GetSystemMetrics(0))
    h = str(user32.GetSystemMetrics(1))
    viewCustomerDetails_canvas = Tk()
    viewCustomerDetails_canvas.geometry(w+'x'+h)
    viewCustomerDetails_canvas.configure(background='dark grey')
    viewCustomerDetails_canvas.title("View Customer Details")
    viewCustomerDetails_canvas.grid_rowconfigure(0, weight=1)
    viewCustomerDetails_canvas.grid_rowconfigure(2, weight=1)
    viewCustomerDetails_canvas.grid_columnconfigure(0, weight=1)
    viewCustomerDetails_canvas.grid_columnconfigure(2, weight=1)

    file = open(os.getcwd() + "\\customeraccounts\\" + username + ".txt", "r")
    lines = file.readlines()
    accountLine = lines[0]
    infoLine = lines[1]
    splitline = infoLine.split(";")
    title = splitline[0]
    name = splitline[1]
    surname = splitline[2]
    dob = splitline[3]
    address1 = splitline[4]
    address2 = splitline[5]
    postcode = splitline[6]
    email = splitline[7]
    mobile = splitline[8]
    howmanylines = len(lines)
    i=2
    orderLines = ""
    while i < howmanylines:
        orderLines = orderLines + "\n" + lines[i]           #gets information for all of the orders
        i=i+1
    file.close()

    Label(viewCustomerDetails_canvas, font=("Arial", 20), fg="purple", text=("Username: " + username)).grid(row=0, column=0, columnspan=3)
    Label(viewCustomerDetails_canvas, font=("Arial", 14), text=("Hashed password: " + accountLine)).grid(row=1, column=0, pady=5, padx=10)

    Label(viewCustomerDetails_canvas, font=("Arial", 14), text=("Title: " + title)).grid(row=2, column=0, pady=5, padx=10)
    Label(viewCustomerDetails_canvas, font=("Arial", 14), text=("Name: " + name)).grid(row=3, column=0, pady=5, padx=10)
    Label(viewCustomerDetails_canvas, font=("Arial", 14), text=("Surname: " + surname)).grid(row=4, column=0, pady=5, padx=10)
    Label(viewCustomerDetails_canvas, font=("Arial", 14), text=("DOB: " + dob)).grid(row=5, column=0, pady=5, padx=10)
    Label(viewCustomerDetails_canvas, font=("Arial", 14), text=("Address line 1: " + address1)).grid(row=6, column=0, pady=5, padx=10)
    Label(viewCustomerDetails_canvas, font=("Arial", 14), text=("Address line 2: " + address2)).grid(row=7, column=0, pady=5, padx=10)
    Label(viewCustomerDetails_canvas, font=("Arial", 14), text=("Postcode: " + postcode)).grid(row=8, column=0, pady=5, padx=10)
    Label(viewCustomerDetails_canvas, font=("Arial", 14), text=("Email: " + email)).grid(row=9, column=0, pady=5, padx=10)
    Label(viewCustomerDetails_canvas, font=("Arial", 14), text=("Mobile: " + mobile)).grid(row=10, column=0, pady=5, padx=10)

    Label(viewCustomerDetails_canvas, font=("Arial", 14), text=("Purchased Orders: " + orderLines)).grid(row=11, column=0, pady=(10, 100), padx=10)


    Button(viewCustomerDetails_canvas, width=15, height=3, text="Edit Account Details", command=lambda: editAccount(viewCustomerDetails_canvas, username)).grid(row=8, column=2, sticky=W, padx=10, pady=10, rowspan=1)
    Button(viewCustomerDetails_canvas, width=15, height=3, text="Delete Account", command=lambda: deleteAccount(viewCustomerDetails_canvas, username)).grid(row=9, column=2, sticky=W, padx=10, pady=10, rowspan=1)
    Button(viewCustomerDetails_canvas, width=15, height=3, text="Back", command=lambda: lookUpCustomers(viewCustomerDetails_canvas)).grid(row=10, column=2, sticky=W, padx=10, pady=10, rowspan=1)

def editAccount(canvas, username):          #edit information stored for the account
    canvas.destroy()
    user32 = ctypes.windll.user32
    w = str(user32.GetSystemMetrics(0))
    h = str(user32.GetSystemMetrics(1))
    editAccount_canvas = Tk()
    editAccount_canvas.geometry(w+'x'+h)
    editAccount_canvas.configure(background='dark grey')
    editAccount_canvas.title("Edit Customer Details")
    editAccount_canvas.grid_rowconfigure(0, weight=1)
    editAccount_canvas.grid_rowconfigure(2, weight=1)
    editAccount_canvas.grid_columnconfigure(0, weight=1)
    editAccount_canvas.grid_columnconfigure(2, weight=1)

    file = open(os.getcwd() + "\\customeraccounts\\" + username + ".txt", "r")
    lines = file.readlines()
    infoLine = lines[1]
    splitline = infoLine.split(";")
    title = splitline[0]
    name = splitline[1]
    surname = splitline[2]
    dob = splitline[3]
    dobsplit = dob.split("/")
    day = dobsplit[0]
    month = dobsplit[1]
    year = dobsplit[2]
    address1 = splitline[4]
    address2 = splitline[5]
    postcode = splitline[6]
    email = splitline[7]
    mobile = splitline[8]
    file.close()

    Label(editAccount_canvas, font=("Arial", 20), text="Edit Details", fg="purple", anchor='center').grid(
        row=0, column=0, columnspan=8)
    Label(editAccount_canvas, width=20, height=2, font=("Arial", 12), text="Title").grid(row=1, column=0, sticky=E,
                                                                                           pady=0, padx=10)
    titleMenu = ttk.Combobox(editAccount_canvas, font=("Arial", 12), width=28, values=("Mr", "Mrs", "Miss", "Ms"))
    titleMenu.grid(row=1, column=1, columnspan=5, sticky=W)
    titleMenu.insert(END, title)        #populates the entry box with the current details
    Label(editAccount_canvas, width=20, height=2, font=("Arial", 12), text="Name").grid(row=2, column=0, sticky=E,
                                                                                          pady=0, padx=10)
    Name_entry = Entry(editAccount_canvas, width=30, font=("Arial", 12))
    Name_entry.grid(row=2, column=1, columnspan=5, sticky=W)
    Name_entry.insert(END, name)
    Label(editAccount_canvas, width=20, height=2, font=("Arial", 12), text="Surname").grid(row=3, column=0, sticky=E,
                                                                                             pady=0, padx=10)
    Surname_entry = Entry(editAccount_canvas, width=30, font=("Arial", 12))
    Surname_entry.grid(row=3, column=1, columnspan=5, sticky=W)
    Surname_entry.insert(END, surname)
    Label(editAccount_canvas, width=20, height=2, font=("Arial", 12), text="Date of birth").grid(row=4, column=0,
                                                                                                   sticky=E, pady=0,
                                                                                                   padx=10)
    Label(editAccount_canvas, text="/").grid(row=4, column=2, sticky=W)
    Label(editAccount_canvas, text="/").grid(row=4, column=4, sticky=W)
    day_entry = Entry(editAccount_canvas, width=5, font=("Arial", 12))
    day_entry.grid(row=4, column=1, sticky=W)
    day_entry.insert(END, day)
    month_entry = Entry(editAccount_canvas, width=5, font=("Arial", 12))
    month_entry.grid(row=4, column=3, sticky=W)
    month_entry.insert(END, month)
    year_entry = Entry(editAccount_canvas, width=10, font=("Arial", 12))
    year_entry.grid(row=4, column=5, sticky=W)
    year_entry.insert(END, year)
    Label(editAccount_canvas, width=20, height=2, font=("Arial", 12), text="Address line 1").grid(row=5, column=0,
                                                                                                    sticky=E, pady=0,
                                                                                                    padx=10)
    Address1_entry = Entry(editAccount_canvas, width=30, font=("Arial", 12))
    Address1_entry.grid(row=5, column=1, columnspan=5, sticky=W)
    Address1_entry.insert(END, address1)
    Label(editAccount_canvas, width=20, height=2, font=("Arial", 12), text="Address line 2").grid(row=6, column=0,
                                                                                                    sticky=E, pady=0,
                                                                                                    padx=10)
    Address2_entry = Entry(editAccount_canvas, width=30, font=("Arial", 12))
    Address2_entry.grid(row=6, column=1, columnspan=5, sticky=W)
    Address2_entry.insert(END, address2)
    Label(editAccount_canvas, width=20, height=2, font=("Arial", 12), text="Postcode").grid(row=7, column=0, sticky=E,
                                                                                              pady=0, padx=10)
    Postcode_entry = Entry(editAccount_canvas, width=30, font=("Arial", 12))
    Postcode_entry.grid(row=7, column=1, columnspan=5, sticky=W)
    Postcode_entry.insert(END, postcode)
    Label(editAccount_canvas, width=20, height=2, font=("Arial", 12), text="Email address").grid(row=8, column=0,
                                                                                                   sticky=E, pady=0,
                                                                                                   padx=10)
    Email_entry = Entry(editAccount_canvas, width=30, font=("Arial", 12))
    Email_entry.grid(row=8, column=1, columnspan=5, sticky=W)
    Email_entry.insert(END, email)
    Label(editAccount_canvas, width=20, height=2, font=("Arial", 12), text="Mobile number").grid(row=9, column=0,
                                                                                                   sticky=E, pady=0,
                                                                                                   padx=10)
    Mobile_entry = Entry(editAccount_canvas, width=30, font=("Arial", 12))
    Mobile_entry.grid(row=9, column=1, columnspan=5, sticky=W)
    Mobile_entry.insert(END, mobile)

    Button(editAccount_canvas, width=20, height=3, text='Submit',
           command=lambda: addEditedInfo(username, editAccount_canvas, titleMenu.get(), Name_entry.get(), Surname_entry.get(),
                                   day_entry.get(), month_entry.get(), year_entry.get(), Address1_entry.get(), Address2_entry.get(), Postcode_entry.get(),
                                   Email_entry.get(), Mobile_entry.get())).grid(row=10, column=2, sticky=W, pady=(10, 10))
    Button(editAccount_canvas, width=20, height=3, text='Back', command=lambda: viewCustomerDetails(editAccount_canvas, username)).grid(row=11, column=2, sticky=W, pady=(0, 100))


def addEditedInfo(username, canvas, title, Name, Surname, day, month, year, Address1, Address2, Postcode, Email, Mobile):       #update the file with the new details
    canvas.destroy()
    user32 = ctypes.windll.user32
    w = str(user32.GetSystemMetrics(0))
    h = str(user32.GetSystemMetrics(1))
    addEditedInfo_canvas = Tk()
    addEditedInfo_canvas.geometry(w+'x'+h)
    addEditedInfo_canvas.configure(background='dark grey')
    addEditedInfo_canvas.title("Edit Customer Details")
    addEditedInfo_canvas.grid_rowconfigure(0, weight=1)
    addEditedInfo_canvas.grid_rowconfigure(2, weight=1)
    addEditedInfo_canvas.grid_columnconfigure(0, weight=1)
    addEditedInfo_canvas.grid_columnconfigure(2, weight=1)

    nameValid = False           #checks all entries are valid
    if not Name.isalpha():
        messagebox.showinfo("Invalid", "'First name' entered is not valid.")
    else:
        nameValid = True

    surnameValid = False
    if not Surname.isalpha():
        messagebox.showinfo("Invalid", "'Surname' entered is not valid.")
    else:
        surnameValid = True

    yearValid = False
    monthValid = False
    dayValid = False
    if year.isdigit():
        year = int(year)
        if year < 1910 or year > 2018:
            messagebox.showinfo("Invalid", "'DOB' entered is not valid.")
        else:
            yearValid = True
            if month.isdigit():
                month = int(month)
                if month < 1 or month > 12:
                    messagebox.showinfo("Invalid", "'DOB' entered is not valid.")
                else:
                    monthValid = True
                    if day.isdigit():
                        day = int(day)
                        if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
                            if day < 1 or day > 31:
                                messagebox.showinfo("Invalid", "'DOB' entered is not valid.")
                            else:
                                dayValid = True
                        if month == 2:
                            if day < 1 or day > 28:
                                messagebox.showinfo("Invalid", "'DOB' entered is not valid.")
                            else:
                                dayValid = True
                        if month == 4 or month == 6 or month == 9 or month == 11:
                            if day < 1 or day > 30:
                                messagebox.showinfo("Invalid", "'DOB' entered is not valid.")
                            else:
                                dayValid = True
                    else:
                        messagebox.showinfo("Invalid", "'DOB' entered is not valid.")
            else:
                messagebox.showinfo("Invalid", "'DOB' entered is not valid.")
    else:
        messagebox.showinfo("Invalid", "'DOB' entered is not valid.")

    address1Valid = False
    if len(Address1) > 20 or len(Address1) < 1:
        messagebox.showinfo("Invalid", "'Address 1' entered is not valid.")
    else:
        address1Valid = True

    address2Valid = False
    if len(Address2) > 20 or len(Address2) < 1:
        messagebox.showinfo("Invalid", "'Address 2' entered is not valid.")
    else:
        address2Valid = True

    postcodeValid = False
    postcode = Postcode.upper()
    if len(postcode) == 6 or len(postcode) == 7 or len(postcode) == 8:
        postcodeValid = True
    else:
        messagebox.showinfo("Invalid", "'Postcode' entered is not valid.")

    emailValid = False
    email = Email.replace(" ", "")
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        messagebox.showinfo("Invalid", "'Email' entered is not valid.")
    else:
        emailValid = True

    mobileValid = False
    if Mobile.isdigit():
        if len(Mobile) != 11:
            messagebox.showinfo("Invalid", "'Mobile' entered is not valid.")
        else:
            mobileValid = True
    else:
        messagebox.showinfo("Invalid", "'Mobile' entered is not valid.")


    if nameValid == True and surnameValid == True and dayValid == True and monthValid == True and yearValid == True and address1Valid == True and address2Valid == True and postcodeValid == True and emailValid == True and mobileValid == True:
        DOB = str(day) + "/" + str(month) + "/" + str(year)
        o = open(os.getcwd() + "\\customeraccounts\\" + username + ".txt", "r")
        lines = o.readlines()
        o.close()
        lines[1]= title + ";" + Name + ";" + Surname + ";" + DOB + ";" + Address1 + ";" + Address2 + ";" + postcode + ";" + Email + ";" + Mobile        #changes the line
        o = open(os.getcwd() + "\\customeraccounts\\" + username + ".txt", "w")
        for line in lines:
            o.write(line)           #re-writes the file to include the line with the updated information
        o.close()
        messagebox.showinfo("Account edited", "Your details have been changed")
        customerLogin(addEditedInfo_canvas)
    else:
        messagebox.showinfo("Invalid")
        editAccount(addEditedInfo_canvas, username)

def deleteAccount(canvas, username):            #deleting a customer account
    file = os.getcwd() + "\\customeraccounts\\" + username + ".txt"             #locates the file
    os.remove(file)                                                             #removes the file from the system
    messagebox.showinfo("Deleted Account", "This account has now been deleted")
    home_screen(canvas)

def lookUpStaff(canvas):            #gets a list of staff accounts - same as for the customers
    canvas.destroy()
    user32 = ctypes.windll.user32
    w = str(user32.GetSystemMetrics(0))
    h = str(user32.GetSystemMetrics(1))
    lookUpStaff_canvas = Tk()
    lookUpStaff_canvas.geometry(w+'x'+h)
    lookUpStaff_canvas.configure(background='dark grey')
    lookUpStaff_canvas.title("View Staff Accounts")
    lookUpStaff_canvas.grid_rowconfigure(0, weight=1)
    lookUpStaff_canvas.grid_rowconfigure(2, weight=1)
    lookUpStaff_canvas.grid_columnconfigure(0, weight=1)
    lookUpStaff_canvas.grid_columnconfigure(2, weight=1)

    usernames = []
    files = os.listdir(os.getcwd() + "\\staffaccounts")
    for file in files:
        file = os.path.splitext(file)[0]
        usernames.append(file)

    Label(lookUpStaff_canvas, text="View Staff Accounts", fg="purple", font=("Arial", 25)).grid(row=0, column=0, columnspan=3)
    Label(lookUpStaff_canvas, font=("Arial", 14), text="Employees").grid(row=1, column=0, sticky=E, pady=10, padx=10)
    listOfUsernames = ttk.Combobox(lookUpStaff_canvas, width=30, font=("Arial", 14))
    listOfUsernames["values"] = usernames
    listOfUsernames.grid(row=1, column=1, sticky=W)
    if not usernames:
        Label(lookUpStaff_canvas, text="No Employees on the System Yet").grid(row=1, column=0, sticky=W, pady=10, padx=10)
    else:
        listOfUsernames.current(0)

    Button(lookUpStaff_canvas, width=20, height=3, text="View", command=lambda: viewStaffDetails(lookUpStaff_canvas, listOfUsernames.get())).grid(row=2, column=1, padx=(0, 150), pady=10)
    Button(lookUpStaff_canvas, width=20, height=3, text="Add staff account", command=lambda: addStaffAccount(lookUpStaff_canvas)).grid(row=3, column=1, padx=(0, 150), pady=(50, 10))
    Button(lookUpStaff_canvas, width=20, height=3, text="Back", command=lambda: managerHome(lookUpStaff_canvas)).grid(row=10, column=1, padx=(0, 150), pady=(10, 100))

def viewStaffDetails(canvas, employeeNum):          #viewing details on the staff account - same as for customers
    canvas.destroy()
    user32 = ctypes.windll.user32
    w = str(user32.GetSystemMetrics(0))
    h = str(user32.GetSystemMetrics(1))
    viewStaffDetails_canvas = Tk()
    viewStaffDetails_canvas.geometry(w+'x'+h)
    viewStaffDetails_canvas.configure(background='dark grey')
    viewStaffDetails_canvas.title("View Staff Details")
    viewStaffDetails_canvas.grid_rowconfigure(0, weight=1)
    viewStaffDetails_canvas.grid_rowconfigure(2, weight=1)
    viewStaffDetails_canvas.grid_columnconfigure(0, weight=1)
    viewStaffDetails_canvas.grid_columnconfigure(2, weight=1)

    file = open(os.getcwd() + "\\staffaccounts\\" + employeeNum + ".txt", "r")
    lines = file.readlines()
    accountLine = lines[0]
    infoLine = lines[1]
    jobLine = lines[2]
    splitline = infoLine.split(";")
    jsplitline = jobLine.split(";")
    title = splitline[0]
    name = splitline[1]
    surname = splitline[2]
    dob = splitline[3]
    address1 = splitline[4]
    address2 = splitline[5]
    postcode = splitline[6]
    email = splitline[7]
    mobile = splitline[8]
    jobTitle = jsplitline[0]
    contractedHours = jsplitline[1]
    wage = jsplitline[2]
    accountNum = jsplitline[3]
    sortCode = jsplitline[4]

    file.close()

    Label(viewStaffDetails_canvas, font=("Arial", 20), fg="purple", text=("Employee Number: " + employeeNum)).grid(
        row=0, column=0, columnspan=3)
    Label(viewStaffDetails_canvas, font=("Arial", 14), text=("Hashed password: " + accountLine)).grid(row=1, column=0,
                                                                                                      pady=2, padx=10)

    Label(viewStaffDetails_canvas, font=("Arial", 14), text=("Title: " + title)).grid(row=2, column=0, pady=2, padx=10)
    Label(viewStaffDetails_canvas, font=("Arial", 14), text=("Name: " + name)).grid(row=3, column=0, pady=2, padx=10)
    Label(viewStaffDetails_canvas, font=("Arial", 14), text=("Surname: " + surname)).grid(row=4, column=0, pady=2,
                                                                                          padx=10)
    Label(viewStaffDetails_canvas, font=("Arial", 14), text=("DOB: " + dob)).grid(row=5, column=0, pady=2, padx=10)
    Label(viewStaffDetails_canvas, font=("Arial", 14), text=("Address line 1: " + address1)).grid(row=6, column=0,
                                                                                                  pady=2, padx=10)
    Label(viewStaffDetails_canvas, font=("Arial", 14), text=("Address line 2: " + address2)).grid(row=7, column=0,
                                                                                                  pady=2, padx=10)
    Label(viewStaffDetails_canvas, font=("Arial", 14), text=("Postcode: " + postcode)).grid(row=8, column=0, pady=2,
                                                                                            padx=10)
    Label(viewStaffDetails_canvas, font=("Arial", 14), text=("Email: " + email)).grid(row=9, column=0, pady=2, padx=10)
    Label(viewStaffDetails_canvas, font=("Arial", 14), text=("Mobile: " + mobile)).grid(row=10, column=0, pady=2,
                                                                                        padx=10)
    Label(viewStaffDetails_canvas, font=("Arial", 14), text=("Job Title: " + jobTitle)).grid(row=11, column=0, pady=2,
                                                                                             padx=10)
    Label(viewStaffDetails_canvas, font=("Arial", 14), text=("Contracted Hours: " + contractedHours)).grid(row=12,
                                                                                                           column=0,
                                                                                                           pady=2,
                                                                                                           padx=10)
    Label(viewStaffDetails_canvas, font=("Arial", 14), text=("Wage (per hour): " + wage)).grid(row=13, column=0, pady=2,
                                                                                               padx=10)
    Label(viewStaffDetails_canvas, font=("Arial", 14), text=("Account Number: " + accountNum)).grid(row=14, column=0,
                                                                                                    pady=2, padx=10)
    Label(viewStaffDetails_canvas, font=("Arial", 14), text=("Sort Code: " + sortCode)).grid(row=15, column=0, pady=(2, 100),
                                                                                             padx=10)

    Button(viewStaffDetails_canvas, width=15, height=3, text="Edit Account Details",
           command=lambda: editAccountStaff(viewStaffDetails_canvas, employeeNum)).grid(row=11, column=2, sticky=W,
                                                                                        padx=10, pady=10, rowspan=2)
    Button(viewStaffDetails_canvas, width=15, height=3, text="Delete Account",
           command=lambda: deleteAccountStaff(viewStaffDetails_canvas, employeeNum)).grid(row=13, column=2, sticky=W,
                                                                                          padx=10, pady=10, rowspan=2)
    Button(viewStaffDetails_canvas, width=15, height=3, text="Back",
           command=lambda: lookUpStaff(viewStaffDetails_canvas)).grid(row=14, column=2, sticky=W, padx=10, pady=10,
                                                                      rowspan=2)


def editAccountStaff(canvas, employeeNum):          #edit details stored on the staff account - same as for customers
    canvas.destroy()
    user32 = ctypes.windll.user32
    w = str(user32.GetSystemMetrics(0))
    h = str(user32.GetSystemMetrics(1))
    editStaffAccount_canvas = Tk()
    editStaffAccount_canvas.geometry(w+'x'+h)
    editStaffAccount_canvas.configure(background='dark grey')
    editStaffAccount_canvas.title("Edit Staff Details")
    editStaffAccount_canvas.grid_rowconfigure(0, weight=1)
    editStaffAccount_canvas.grid_rowconfigure(2, weight=1)
    editStaffAccount_canvas.grid_columnconfigure(0, weight=1)
    editStaffAccount_canvas.grid_columnconfigure(2, weight=1)

    file = open(os.getcwd() + "\\staffaccounts\\" + employeeNum + ".txt", "r")
    lines = file.readlines()
    infoLine = lines[1]
    jobLine = lines[2]
    splitline = infoLine.split(";")
    jsplitline = jobLine.split(";")
    title = splitline[0]
    name = splitline[1]
    surname = splitline[2]
    dob = splitline[3]
    dobsplit = dob.split("/")
    day = dobsplit[0]
    month = dobsplit[1]
    year = dobsplit[2]
    address1 = splitline[4]
    address2 = splitline[5]
    postcode = splitline[6]
    email = splitline[7]
    mobile = splitline[8]
    jobTitle = jsplitline[0]
    contractedHours = jsplitline[1]
    wage = jsplitline[2]
    accountNum = jsplitline[3]
    sortCode = jsplitline[4]
    sortsplit = sortCode.split("-")
    s1 = sortsplit[0]
    s2 = sortsplit[1]
    s3 = sortsplit[2]
    file.close()

    Label(editStaffAccount_canvas, font=("Arial", 20), text="Edit Employee " + employeeNum + " Details", fg="purple", anchor='center').grid(
        row=0, column=0, columnspan=8)
    Label(editStaffAccount_canvas, width=20, font=("Arial", 12), text="Title").grid(row=1, column=0, sticky=E,
                                                                                         pady=0, padx=10)
    titleMenu = ttk.Combobox(editStaffAccount_canvas, font=("Arial", 12), width=28, values=("Mr", "Mrs", "Miss", "Ms"))
    titleMenu.grid(row=1, column=1, columnspan=5, sticky=W)
    titleMenu.insert(END, title)
    Label(editStaffAccount_canvas, width=20, font=("Arial", 12), text="Name").grid(row=2, column=0, sticky=E,
                                                                                        pady=0, padx=10)
    Name_entry = Entry(editStaffAccount_canvas, width=30, font=("Arial", 12))
    Name_entry.grid(row=2, column=1, columnspan=5, sticky=W)
    Name_entry.insert(END, name)
    Label(editStaffAccount_canvas, width=20, font=("Arial", 12), text="Surname").grid(row=3, column=0, sticky=E,
                                                                                           pady=0, padx=10)
    Surname_entry = Entry(editStaffAccount_canvas, width=30, font=("Arial", 12))
    Surname_entry.grid(row=3, column=1, columnspan=5, sticky=W)
    Surname_entry.insert(END, surname)
    Label(editStaffAccount_canvas, width=20, font=("Arial", 12), text="Date of birth").grid(row=4, column=0,
                                                                                                 sticky=E, pady=0,
                                                                                                 padx=10)
    Label(editStaffAccount_canvas, text="/").grid(row=4, column=2, sticky=W)
    Label(editStaffAccount_canvas, text="/").grid(row=4, column=4, sticky=W)
    day_entry = Entry(editStaffAccount_canvas, width=5, font=("Arial", 12))
    day_entry.grid(row=4, column=1, sticky=W)
    day_entry.insert(END, day)
    month_entry = Entry(editStaffAccount_canvas, width=5, font=("Arial", 12))
    month_entry.grid(row=4, column=3, sticky=W)
    month_entry.insert(END, month)
    year_entry = Entry(editStaffAccount_canvas, width=10, font=("Arial", 12))
    year_entry.grid(row=4, column=5, sticky=W)
    year_entry.insert(END, year)
    Label(editStaffAccount_canvas, width=20, font=("Arial", 12), text="Address line 1").grid(row=5, column=0,
                                                                                                  sticky=E, pady=0,
                                                                                                  padx=10)
    Address1_entry = Entry(editStaffAccount_canvas, width=30, font=("Arial", 12))
    Address1_entry.grid(row=5, column=1, columnspan=5, sticky=W)
    Address1_entry.insert(END, address1)
    Label(editStaffAccount_canvas, width=20, font=("Arial", 12), text="Address line 2").grid(row=6, column=0,
                                                                                                  sticky=E, pady=0,
                                                                                                  padx=10)
    Address2_entry = Entry(editStaffAccount_canvas, width=30, font=("Arial", 12))
    Address2_entry.grid(row=6, column=1, columnspan=5, sticky=W)
    Address2_entry.insert(END, address2)
    Label(editStaffAccount_canvas, width=20, font=("Arial", 12), text="Postcode").grid(row=7, column=0, sticky=E,
                                                                                            pady=0, padx=10)
    Postcode_entry = Entry(editStaffAccount_canvas, width=30, font=("Arial", 12))
    Postcode_entry.grid(row=7, column=1, columnspan=5, sticky=W)
    Postcode_entry.insert(END, postcode)
    Label(editStaffAccount_canvas, width=20, font=("Arial", 12), text="Email address").grid(row=8, column=0,
                                                                                                 sticky=E, pady=0,
                                                                                                 padx=10)
    Email_entry = Entry(editStaffAccount_canvas, width=30, font=("Arial", 12))
    Email_entry.grid(row=8, column=1, columnspan=5, sticky=W)
    Email_entry.insert(END, email)
    Label(editStaffAccount_canvas, width=20, font=("Arial", 12), text="Mobile number").grid(row=9, column=0,
                                                                                                 sticky=E, pady=0,
                                                                                                 padx=10)
    Mobile_entry = Entry(editStaffAccount_canvas, width=30, font=("Arial", 12))
    Mobile_entry.grid(row=9, column=1, columnspan=5, sticky=W)
    Mobile_entry.insert(END, mobile)

    Label(editStaffAccount_canvas, width=20, font=("Arial", 12), text="Job Title").grid(row=10, column=0, sticky=E,
                                                                                             pady=0, padx=10)
    jobTitleMenu = ttk.Combobox(editStaffAccount_canvas, width=30, font=("Arial", 12),
                                values=("Supervisor", "Sales", "Security", "Cleaner"))
    jobTitleMenu.grid(row=10, column=1, sticky=W, columnspan=5)
    jobTitleMenu.insert(END, jobTitle)
    Label(editStaffAccount_canvas, width=20, font=("Arial", 12), text="Contracted hours").grid(row=11, column=0,
                                                                                                    sticky=E, pady=0,
                                                                                                    padx=10)
    contractedHours_entry = Entry(editStaffAccount_canvas, width=20, font=("Arial", 12))
    contractedHours_entry.grid(row=11, column=1, sticky=W, columnspan=5)
    contractedHours_entry.insert(END, contractedHours)
    Label(editStaffAccount_canvas, width=20, font=("Arial", 12), text="Wage (per hour)  £").grid(row=12, column=0,
                                                                                                      sticky=E, pady=0,
                                                                                                      padx=10)
    Wage_entry = Entry(editStaffAccount_canvas, width=20, font=("Arial", 12))
    Wage_entry.grid(row=12, column=1, sticky=W, columnspan=5)
    Wage_entry.insert(END, wage)
    Label(editStaffAccount_canvas, width=20, font=("Arial", 12), text="Account number").grid(row=13, column=0,
                                                                                                  sticky=E, pady=0,
                                                                                                  padx=10)
    accountNum_entry = Entry(editStaffAccount_canvas, width=20, font=("Arial", 12))
    accountNum_entry.grid(row=13, column=1, sticky=W, columnspan=5)
    accountNum_entry.insert(END, accountNum)
    Label(editStaffAccount_canvas, width=20, font=("Arial", 12), text="Sort code").grid(row=14, column=0, sticky=E,
                                                                                             pady=0, padx=10)
    Label(editStaffAccount_canvas, text="-").grid(row=14, column=2, sticky=W)
    Label(editStaffAccount_canvas, text="-").grid(row=14, column=4, sticky=W)
    s1_entry = Entry(editStaffAccount_canvas, width=5, font=("Arial", 12))
    s1_entry.grid(row=14, column=1, sticky=W)
    s1_entry.insert(END, s1)
    s2_entry = Entry(editStaffAccount_canvas, width=5, font=("Arial", 12))
    s2_entry.grid(row=14, column=3, sticky=W)
    s2_entry.insert(END, s2)
    s3_entry = Entry(editStaffAccount_canvas, width=5, font=("Arial", 12))
    s3_entry.grid(row=14, column=5, sticky=W)
    s3_entry.insert(END, s3)


    Button(editStaffAccount_canvas, width=15, height=3, text='Submit',
           command=lambda: addEditedInfoStaff(employeeNum, editStaffAccount_canvas, titleMenu.get(), Name_entry.get(), Surname_entry.get(),
                                   day_entry.get(), month_entry.get(), year_entry.get(), Address1_entry.get(), Address2_entry.get(), Postcode_entry.get(),
                                   Email_entry.get(), Mobile_entry.get(), jobTitleMenu.get(), contractedHours_entry.get(), Wage_entry.get(), accountNum_entry.get(), s1_entry.get(), s2_entry.get(), s3_entry.get())).grid(row=15, column=2, sticky=W, pady=(10, 10))
    Button(editStaffAccount_canvas, width=15, height=3, text='Reset Password', command=lambda: forgotPasswordStaff(editStaffAccount_canvas, employeeNum)).grid(row=16, column=2, sticky=W)
    Button(editStaffAccount_canvas, width=15, height=3, text='Back', command=lambda: viewStaffDetails(editStaffAccount_canvas, employeeNum)).grid(row=17, column=2, sticky=W, pady=(0, 100))


def addEditedInfoStaff(employeeNum, canvas, title, Name, Surname, day, month, year, Address1, Address2, Postcode, Email, Mobile, jobTitle, contractedHours, wage, accountNum, s1, s2, s3):          #updates the file with the new details - same as for the customer
    canvas.destroy()
    user32 = ctypes.windll.user32
    w = str(user32.GetSystemMetrics(0))
    h = str(user32.GetSystemMetrics(1))
    addEditedInfoStaff_canvas = Tk()
    addEditedInfoStaff_canvas.geometry(w+'x'+h)
    addEditedInfoStaff_canvas.configure(background='dark grey')
    addEditedInfoStaff_canvas.title("Edit Staff Details")
    addEditedInfoStaff_canvas.grid_rowconfigure(0, weight=1)
    addEditedInfoStaff_canvas.grid_rowconfigure(2, weight=1)
    addEditedInfoStaff_canvas.grid_columnconfigure(0, weight=1)
    addEditedInfoStaff_canvas.grid_columnconfigure(2, weight=1)

    nameValid = False
    if not Name.isalpha():
        messagebox.showinfo("Invalid", "'First name' entered is not valid.")
    else:
        nameValid = True

    surnameValid = False
    if not Surname.isalpha():
        messagebox.showinfo("Invalid", "'Surname' entered is not valid.")
    else:
        surnameValid = True

    yearValid = False
    monthValid = False
    dayValid = False
    if year.isdigit():
        year = int(year)
        if year < 1910 or year > 2018:
            messagebox.showinfo("Invalid", "'DOB' entered is not valid.")
        else:
            yearValid = True
            if month.isdigit():
                month = int(month)
                if month < 1 or month > 12:
                    messagebox.showinfo("Invalid", "'DOB' entered is not valid.")
                else:
                    monthValid = True
                    if day.isdigit():
                        day = int(day)
                        if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
                            if day < 1 or day > 31:
                                messagebox.showinfo("Invalid", "'DOB' entered is not valid.")
                            else:
                                dayValid = True
                        if month == 2:
                            if day < 1 or day > 28:
                                messagebox.showinfo("Invalid", "'DOB' entered is not valid.")
                            else:
                                dayValid = True
                        if month == 4 or month == 6 or month == 9 or month == 11:
                            if day < 1 or day > 30:
                                messagebox.showinfo("Invalid", "'DOB' entered is not valid.")
                            else:
                                dayValid = True
                    else:
                        messagebox.showinfo("Invalid", "'DOB' entered is not valid.")
            else:
                messagebox.showinfo("Invalid", "'DOB' entered is not valid.")
    else:
        messagebox.showinfo("Invalid", "'DOB' entered is not valid.")

    address1Valid = False
    if len(Address1) > 20 or len(Address1) < 1:
        messagebox.showinfo("Invalid", "'Address 1' entered is not valid.")
    else:
        address1Valid = True

    address2Valid = False
    if len(Address2) > 20 or len(Address2) < 1:
        messagebox.showinfo("Invalid", "'Address 2' entered is not valid.")
    else:
        address2Valid = True

    postcodeValid = False
    postcode = Postcode.upper()
    if len(postcode) == 6 or len(postcode) == 7 or len(postcode) == 8:
        postcodeValid = True
    else:
        messagebox.showinfo("Invalid", "'Postcode' entered is not valid.")

    emailValid = False
    email = Email.replace(" ", "")
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        messagebox.showinfo("Invalid", "'Email' entered is not valid.")
    else:
        emailValid = True

    mobileValid = False
    if Mobile.isdigit():
        if len(Mobile) != 11:
            messagebox.showinfo("Invalid", "'Mobile' entered is not valid.")
        else:
            mobileValid = True
    else:
        messagebox.showinfo("Invalid", "'Mobile' entered is not valid.")
    wageValid = False
    Wage = wage.replace(".", "")
    if Wage.isdigit():
        if len(Wage) > 5:
            messagebox.showinfo("Invalid", "'Wage' entered is not valid.")
        else:
            wageValid = True
    else:
        messagebox.showinfo("Invalid", "'Wage' entered is not valid.")
    hoursValid = False
    if contractedHours.isdigit():
        if len(contractedHours) > 3:
            messagebox.showinfo("Invalid", "'Contracted Hours' entered is not valid.")
        else:
            hoursValid = True
    else:
        messagebox.showinfo("Invalid", "'Contracted Hours' entered is not valid.")
    accountValid = False
    if accountNum.isdigit():
        if len(accountNum) != 8:
            messagebox.showinfo("Invalid", "'Account Number' entered is not valid.")
        else:
            accountValid = True
    else:
        messagebox.showinfo("Invalid", "'Account Number' entered is not valid.")
    sortValid = False
    if s1.isdigit() and s2.isdigit() and s3.isdigit():
        if len(s1) != 2 and len(s2) != 2 and len(s3) != 2:
            messagebox.showinfo("Invalid", "'Sort Code' entered is not valid.")
        else:
            sortValid = True
    else:
        messagebox.showinfo("Invalid", "'Sort Code' entered is not valid.")

    if nameValid == True and surnameValid == True and dayValid == True and monthValid == True and yearValid == True and address1Valid == True and address2Valid == True and postcodeValid == True and emailValid == True and mobileValid == True and wageValid == True and hoursValid == True and accountValid == True and sortValid == True:
        DOB = str(day) + "/" + str(month) + "/" + str(year)
        sortCode = str(s1) + "-" + str(s2) + "-" + str(s3)
        o = open(os.getcwd() + "\\staffaccounts\\" + employeeNum + ".txt", "r")
        lines = o.readlines()
        o.close()
        lines[1]= title + ";" + Name + ";" + Surname + ";" + DOB + ";" + Address1 + ";" + Address2 + ";" + postcode + ";" + Email + ";" + Mobile
        lines[2]= jobTitle + ";" + contractedHours + ";" + wage + ";" + accountNum + ";" + sortCode
        o = open(os.getcwd() + "\\staffaccounts\\" + employeeNum + ".txt", "w")
        for line in lines:
            o.write(line)
        o.close()
        messagebox.showinfo("Account edited", "The details have been changed")
        staffLogin(addEditedInfoStaff_canvas)
    else:
        messagebox.showinfo("Invalid")


def deleteAccountStaff(canvas, employeeNum):        #deletes a staff account - same as for the customers
    file = os.getcwd() + "\\staffaccounts\\" + employeeNum + ".txt"
    os.remove(file)
    messagebox.showinfo("Deleted Account", "This account has now been deleted")
    home_screen(canvas)

def forgotPasswordStaff(canvas, employeeNum):           #giving staff accounts a new temp password - same as for the customers
    canvas.destroy()
    user32 = ctypes.windll.user32
    w = str(user32.GetSystemMetrics(0))
    h = str(user32.GetSystemMetrics(1))
    forgotPasswordStaff_canvas = Tk()
    forgotPasswordStaff_canvas.geometry(w+'x'+h)
    forgotPasswordStaff_canvas.configure(background='dark grey')
    forgotPasswordStaff_canvas.title("Forgotten Staff Password")
    forgotPasswordStaff_canvas.grid_rowconfigure(0, weight=1)
    forgotPasswordStaff_canvas.grid_rowconfigure(2, weight=1)
    forgotPasswordStaff_canvas.grid_columnconfigure(0, weight=1)
    forgotPasswordStaff_canvas.grid_columnconfigure(2, weight=1)

    newPassword = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=10))

    Label(forgotPasswordStaff_canvas, font=("Arial", 30), text="Forgotten Password", fg="purple").grid(row=0, column=0,
                                                                                                  columnspan=3)

    Label(forgotPasswordStaff_canvas, text="Employee Number", font=("Arial", 12), width=20, height=2).grid(row=1, column=0, padx=10, pady=(10, 0), sticky=E)
    employeeNum_entry = Entry(forgotPasswordStaff_canvas, width=30, font=("Arial", 15))
    employeeNum_entry.grid(row=1, column=1, sticky=E)

    Button(forgotPasswordStaff_canvas, width=20, height=3, text="Get new password", command=lambda: tempPasswordStaff(forgotPasswordStaff_canvas, newPassword, employeeNum_entry.get())).grid(row=2, column=1, sticky=W, padx=10, pady=(5, 0))
    Button(forgotPasswordStaff_canvas, width=20, height=3, text="Back", command=lambda: editAccountStaff(forgotPasswordStaff_canvas, employeeNum)).grid(row=3, column=1, sticky=W, padx=10, pady=(0, 150))

def tempPasswordStaff(canvas, newPassword, employeeNum):        #resetting the password - same as for a customer account
    canvas.destroy()
    user32 = ctypes.windll.user32
    w = str(user32.GetSystemMetrics(0))
    h = str(user32.GetSystemMetrics(1))
    tempPasswordStaff_canvas = Tk()
    tempPasswordStaff_canvas.geometry(w+'x'+h)
    tempPasswordStaff_canvas.configure(background='dark grey')
    tempPasswordStaff_canvas.title("New Temporary Password")
    tempPasswordStaff_canvas.grid_rowconfigure(0, weight=1)
    tempPasswordStaff_canvas.grid_rowconfigure(2, weight=1)
    tempPasswordStaff_canvas.grid_columnconfigure(0, weight=1)
    tempPasswordStaff_canvas.grid_columnconfigure(2, weight=1)

    userEmail = ""
    file = open(os.getcwd() + "\\staffaccounts\\" + employeeNum + ".txt", "r")
    lines = file.readlines()
    infoLine = lines[1]
    howmanylines = len(lines)
    splitline = infoLine.split(";")
    for split in splitline:
        if "@" in split:
            userEmail = str(split)
    file.close()
    newPasswordHashed = hasher(newPassword)
    lines[0] = newPasswordHashed
    writingstuff = []
    writingstuff.append(lines[0]+"\n")
    i = 1
    while i < howmanylines:
        writingstuff.append(lines[i])
        i=i+1

    with open(os.getcwd() + "\\staffaccounts\\" + employeeNum + ".txt", "w") as file:
        for line in writingstuff:
            file.write(line)
    file.close()

    port = 587
    smtp_server = "smtp.gmail.com"
    sender_email = "bookings.moviemania@gmail.com"
    receiver_email = userEmail
    password = "QDD87kNV55P#8BC"
    subject = "Forgotton Passsword"
    message = (str(employeeNum) + ", here is your new temporary password: \n" + str(newPassword) + "\n You can now log into your account using this password and reset it from within 'My Account'.")

    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, 'Subject: {}\n\n{}'.format(subject, message))

    Label(tempPasswordStaff_canvas, width=60, height=10, font=("Arial", 12), text="An email has been sent with a new temporary password.").grid(row=1, column=1, sticky=W, padx=150)
    Button(tempPasswordStaff_canvas, width=20, height=3, text="Ok", command=lambda: managerHome(tempPasswordStaff_canvas)).grid(row=2, column=1, sticky=W, padx=(350, 0), pady=(0, 100))


def addStaffAccount(canvas):
    canvas.destroy()
    user32 = ctypes.windll.user32
    w = str(user32.GetSystemMetrics(0))
    h = str(user32.GetSystemMetrics(1))
    addStaffAccount_canvas = Tk()
    addStaffAccount_canvas.geometry(w+'x'+h)
    addStaffAccount_canvas.configure(background='dark grey')
    addStaffAccount_canvas.title("Add a new staff account")
    addStaffAccount_canvas.grid_rowconfigure(0, weight=1)
    addStaffAccount_canvas.grid_rowconfigure(2, weight=1)
    addStaffAccount_canvas.grid_columnconfigure(0, weight=1)
    addStaffAccount_canvas.grid_columnconfigure(2, weight=1)

    Label(addStaffAccount_canvas, font=("Arial", 30), text="Create a Staff Account", fg="purple",
          anchor='center').grid(row=0, column=0, columnspan=3)
    Label(addStaffAccount_canvas, font=("Arial", 12), text="Employee Number", width=20, height=2).grid(row=1, column=0,
                                                                                                       sticky=E,
                                                                                                       padx=10)
    employeeNum_entry = Entry(addStaffAccount_canvas, width=30, font=("Arial", 15))
    employeeNum_entry.grid(row=1, column=1, sticky=E)
    Label(addStaffAccount_canvas, font=("Arial", 12), text="Password", width=20, height=2).grid(row=2, column=0,
                                                                                                sticky=E, padx=10)
    password1_entry = Entry(addStaffAccount_canvas, show="*", width=30, font=("Arial", 15))
    password1_entry.grid(row=2, column=1, sticky=E)
    Label(addStaffAccount_canvas, font=("Arial", 12), text="Confirm Password", width=20, height=2).grid(row=3, column=0,
                                                                                                        sticky=E,
                                                                                                        padx=10)
    password2_entry = Entry(addStaffAccount_canvas, show="*", width=30, font=("Arial", 15))
    password2_entry.grid(row=3, column=1, sticky=E)

    Button(addStaffAccount_canvas, width=20, height=3, text='Back',
           command=lambda: lookUpStaff(addStaffAccount_canvas)).grid(row=5,
                                                                     column=1,
                                                                     sticky=W,
                                                                     padx=10, pady=(0, 100))
    Button(addStaffAccount_canvas, width=20, height=3, text='Next',
           command=lambda: addStaffAccountCheck(addStaffAccount_canvas, employeeNum_entry.get(), password1_entry.get(),
                                                password2_entry.get())).grid(row=4,
                                                                             column=1,
                                                                             sticky=W,
                                                                             padx=10, pady=(50, 10))


def addStaffAccountCheck(canvas, employeeNum, password1, password2):        #checks the new account is valid - same as for customer accounts
    if employeeNum == "" or password1 == "" or password2 == "":
        messagebox.showinfo("Invalid", "Enter an employee number/password")
    else:
        if employeeNum.isdigit() and len(employeeNum)==6:           #employee number has to be 6 digits
            if password1 == password2:
                if os.path.isfile(os.getcwd() + "\\staffaccounts\\" + employeeNum + ".txt"):
                    messagebox.showinfo("Employee number unavailable", "Employee number is already taken")
                else:
                    if not os.path.isdir(os.getcwd() + "\\staffaccounts"):
                        os.makedirs(os.getcwd() + "\\staffaccounts")
                    file = open(os.getcwd() + "\\staffaccounts\\" + employeeNum + ".txt", "w")
                    file.write(hasher(password1))
                    file.close()
                    signUpStaff(canvas, employeeNum)
            else:
                messagebox.showinfo("Incorrect Password", "Passwords do not match")
        else:
            messagebox.showinfo("Invalid", "An employee number must be 6 digits")


def signUpStaff(canvas, employeeNum):       #signing up for a staff account - same as for customer accounts
    canvas.destroy()
    user32 = ctypes.windll.user32
    w = str(user32.GetSystemMetrics(0))
    h = str(user32.GetSystemMetrics(1))
    signUpStaff_canvas = Tk()
    signUpStaff_canvas.geometry(w+'x'+h)
    signUpStaff_canvas.configure(background='dark grey')
    signUpStaff_canvas.title("Sign Up")
    signUpStaff_canvas.grid_rowconfigure(0, weight=1)
    signUpStaff_canvas.grid_rowconfigure(2, weight=1)
    signUpStaff_canvas.grid_columnconfigure(0, weight=1)
    signUpStaff_canvas.grid_columnconfigure(2, weight=1)

    Label(signUpStaff_canvas, font=("Arial", 20), text="Create a MovieMania Account \n Enter Personal Details",
          fg="purple", anchor='center').grid(
        row=0, column=0, columnspan=8)
    Label(signUpStaff_canvas, width=20, font=("Arial", 12), text="Title").grid(row=1, column=0, sticky=E,
                                                                                           pady=0, padx=10)
    titleMenu = ttk.Combobox(signUpStaff_canvas, font=("Arial", 12), width=28, values=("Mr", "Mrs", "Miss", "Ms"))
    titleMenu.grid(row=1, column=1, columnspan=5, sticky=W)
    titleMenu.current(0)
    Label(signUpStaff_canvas, width=20, font=("Arial", 12), text="Name").grid(row=2, column=0, sticky=E,
                                                                                          pady=0, padx=10)
    Name_entry = Entry(signUpStaff_canvas, width=30, font=("Arial", 12))
    Name_entry.grid(row=2, column=1, columnspan=5, sticky=W)
    Label(signUpStaff_canvas, width=20, font=("Arial", 12), text="Surname").grid(row=3, column=0, sticky=E,
                                                                                             pady=0, padx=10)
    Surname_entry = Entry(signUpStaff_canvas, width=30, font=("Arial", 12))
    Surname_entry.grid(row=3, column=1, columnspan=5, sticky=W)
    Label(signUpStaff_canvas, width=20, font=("Arial", 12), text="Date of birth").grid(row=4, column=0,
                                                                                                   sticky=E, pady=0,
                                                                                                   padx=10)
    Label(signUpStaff_canvas, text="/").grid(row=4, column=2, sticky=W)
    Label(signUpStaff_canvas, text="/").grid(row=4, column=4, sticky=W)
    day_entry = Entry(signUpStaff_canvas, width=5, font=("Arial", 12))
    day_entry.grid(row=4, column=1, sticky=W)
    month_entry = Entry(signUpStaff_canvas, width=5, font=("Arial", 12))
    month_entry.grid(row=4, column=3, sticky=W)
    year_entry = Entry(signUpStaff_canvas, width=10, font=("Arial", 12))
    year_entry.grid(row=4, column=5, sticky=W)
    Label(signUpStaff_canvas, width=20, font=("Arial", 12), text="Address line 1").grid(row=5, column=0,
                                                                                                    sticky=E, pady=0,
                                                                                                    padx=10)
    Address1_entry = Entry(signUpStaff_canvas, width=30, font=("Arial", 12))
    Address1_entry.grid(row=5, column=1, columnspan=5, sticky=W)
    Label(signUpStaff_canvas, width=20, font=("Arial", 12), text="Address line 2").grid(row=6, column=0,
                                                                                                    sticky=E, pady=0,
                                                                                                    padx=10)
    Address2_entry = Entry(signUpStaff_canvas, width=30, font=("Arial", 12))
    Address2_entry.grid(row=6, column=1, columnspan=5, sticky=W)
    Label(signUpStaff_canvas, width=20, font=("Arial", 12), text="Postcode").grid(row=7, column=0, sticky=E,
                                                                                              pady=0, padx=10)
    Postcode_entry = Entry(signUpStaff_canvas, width=30, font=("Arial", 12))
    Postcode_entry.grid(row=7, column=1, columnspan=5, sticky=W)
    Label(signUpStaff_canvas, width=20, font=("Arial", 12), text="Email address").grid(row=8, column=0,
                                                                                                   sticky=E, pady=0,
                                                                                                   padx=10)
    Email_entry = Entry(signUpStaff_canvas, width=30, font=("Arial", 12))
    Email_entry.grid(row=8, column=1, columnspan=5, sticky=W)
    Label(signUpStaff_canvas, width=20, font=("Arial", 12), text="Mobile number").grid(row=9, column=0,
                                                                                                   sticky=E, pady=0,
                                                                                                   padx=10)
    Mobile_entry = Entry(signUpStaff_canvas, width=30, font=("Arial", 12))
    Mobile_entry.grid(row=9, column=1, columnspan=5, sticky=W)

    Label(signUpStaff_canvas, width=20, font=("Arial", 12), text="Job Title").grid(row=10, column=0, sticky=E,
                                                                                             pady=0, padx=10)
    jobTitleMenu = ttk.Combobox(signUpStaff_canvas, width=30, font=("Arial", 12),
                                values=("Supervisor", "Sales", "Security", "Cleaner"))
    jobTitleMenu.grid(row=10, column=1, sticky=W, columnspan=5)
    jobTitleMenu.current(0)
    Label(signUpStaff_canvas, width=20, font=("Arial", 12), text="Contracted hours").grid(row=11, column=0,
                                                                                                    sticky=E, pady=0,
                                                                                                    padx=10)
    contractedHours_entry = Entry(signUpStaff_canvas, width=20, font=("Arial", 12))
    contractedHours_entry.grid(row=11, column=1, sticky=W, columnspan=5)
    Label(signUpStaff_canvas, width=20, font=("Arial", 12), text="Wage (per hour)  £").grid(row=12, column=0,
                                                                                                      sticky=E, pady=0,
                                                                                                      padx=10)
    Wage_entry = Entry(signUpStaff_canvas, width=20, font=("Arial", 12))
    Wage_entry.grid(row=12, column=1, sticky=W, columnspan=5)
    Label(signUpStaff_canvas, width=20, font=("Arial", 12), text="Account number").grid(row=13, column=0,
                                                                                                  sticky=E, pady=0,
                                                                                                  padx=10)
    accountNum_entry = Entry(signUpStaff_canvas, width=20, font=("Arial", 12))
    accountNum_entry.grid(row=13, column=1, sticky=W, columnspan=5)
    Label(signUpStaff_canvas, width=20, font=("Arial", 12), text="Sort code").grid(row=14, column=0, sticky=E,
                                                                                             pady=0, padx=10)
    Label(signUpStaff_canvas, text="-").grid(row=14, column=2, sticky=W)
    Label(signUpStaff_canvas, text="-").grid(row=14, column=4, sticky=W)
    s1_entry = Entry(signUpStaff_canvas, width=5, font=("Arial", 12))
    s1_entry.grid(row=14, column=1, sticky=W)
    s2_entry = Entry(signUpStaff_canvas, width=5, font=("Arial", 12))
    s2_entry.grid(row=14, column=3, sticky=W)
    s3_entry = Entry(signUpStaff_canvas, width=5, font=("Arial", 12))
    s3_entry.grid(row=14, column=5, sticky=W)

    Button(signUpStaff_canvas, width=20, height=3, text='Submit',
           command=lambda: addStaffInfo(employeeNum, signUpStaff_canvas, titleMenu.get(), Name_entry.get(),
                                        Surname_entry.get(),
                                        day_entry.get(), month_entry.get(), year_entry.get(), Address1_entry.get(),
                                        Address2_entry.get(), Postcode_entry.get(),
                                        Email_entry.get(), Mobile_entry.get(), jobTitleMenu.get(),
                                        contractedHours_entry.get(), Wage_entry.get(), accountNum_entry.get(),
                                        s1_entry.get(), s2_entry.get(), s3_entry.get())).grid(row=15, column=2,
                                                                                              sticky=W, pady=(10, 10))
    Button(signUpStaff_canvas, width=20, height=3, text='Back',
           command=lambda: signUpBackStaff(signUpStaff_canvas, employeeNum)).grid(row=16, column=2,
                                                                                  sticky=W,
                                                                                  pady=(0, 100))


def signUpBackStaff(canvas, employeeNum):           #backing out of setting up a staff account - same as for customer accounts
    file = os.getcwd() + "\\staffaccounts\\" + employeeNum + ".txt"
    os.remove(file)
    addStaffAccount(canvas)


def addStaffInfo(employeeNum, canvas, title, Name, Surname, day, month, year, Address1, Address2, Postcode, Email, Mobile, jobTitle, contractedHours, wage, accountNum, s1, s2, s3):       #checks details are a valid and writes to text file - same as for customer accounts
    nameValid = False
    if not Name.isalpha():
        messagebox.showinfo("Invalid", "'First name' entered is not valid.")
    else:
        nameValid = True

    surnameValid = False
    if not Surname.isalpha():
        messagebox.showinfo("Invalid", "'Surname' entered is not valid.")
    else:
        surnameValid = True

    yearValid = False
    monthValid = False
    dayValid = False
    if year.isdigit():
        year = int(year)
        if year < 1910 or year > 2018:
            messagebox.showinfo("Invalid", "'DOB' entered is not valid.")
        else:
            yearValid = True
            if month.isdigit():
                month = int(month)
                if month < 1 or month > 12:
                    messagebox.showinfo("Invalid", "'DOB' entered is not valid.")
                else:
                    monthValid = True
                    if day.isdigit():
                        day = int(day)
                        if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
                            if day < 1 or day > 31:
                                messagebox.showinfo("Invalid", "'DOB' entered is not valid.")
                            else:
                                dayValid = True
                        if month == 2:
                            if day < 1 or day > 28:
                                messagebox.showinfo("Invalid", "'DOB' entered is not valid.")
                            else:
                                dayValid = True
                        if month == 4 or month == 6 or month == 9 or month == 11:
                            if day < 1 or day > 30:
                                messagebox.showinfo("Invalid", "'DOB' entered is not valid.")
                            else:
                                dayValid = True
                    else:
                        messagebox.showinfo("Invalid", "'DOB' entered is not valid.")
            else:
                messagebox.showinfo("Invalid", "'DOB' entered is not valid.")
    else:
        messagebox.showinfo("Invalid", "'DOB' entered is not valid.")

    address1Valid = False
    if len(Address1) > 20 or len(Address1) < 1:
        messagebox.showinfo("Invalid", "'Address 1' entered is not valid.")
    else:
        address1Valid = True

    address2Valid = False
    if len(Address2) > 20 or len(Address2) < 1:
        messagebox.showinfo("Invalid", "'Address 2' entered is not valid.")
    else:
        address2Valid = True

    postcodeValid = False
    postcode = Postcode.upper()
    if len(postcode) == 6 or len(postcode) == 7 or len(postcode) == 8:
        postcodeValid = True
    else:
        messagebox.showinfo("Invalid", "'Postcode' entered is not valid.")

    emailValid = False
    email = Email.replace(" ", "")
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        messagebox.showinfo("Invalid", "'Email' entered is not valid.")
    else:
        emailValid = True

    mobileValid = False
    if Mobile.isdigit():
        if len(Mobile) != 11:
            messagebox.showinfo("Invalid", "'Mobile' entered is not valid.")
        else:
            mobileValid = True
    else:
        messagebox.showinfo("Invalid", "'Mobile' entered is not valid.")
    wageValid = False
    Wage = wage.replace(".", "")
    if Wage.isdigit():
        if len(Wage) > 5:
            messagebox.showinfo("Invalid", "'Wage' entered is not valid.")
        else:
            wageValid = True
    else:
        messagebox.showinfo("Invalid", "'Wage' entered is not valid.")
    hoursValid = False
    if contractedHours.isdigit():
        if len(contractedHours) > 3:
            messagebox.showinfo("Invalid", "'Contracted Hours' entered is not valid.")
        else:
            hoursValid = True
    else:
        messagebox.showinfo("Invalid", "'Contracted Hours' entered is not valid.")
    accountValid = False
    if accountNum.isdigit():
        if len(accountNum) != 8:
            messagebox.showinfo("Invalid", "'Account Number' entered is not valid.")
        else:
            accountValid = True
    else:
        messagebox.showinfo("Invalid", "'Account Number' entered is not valid.")
    sortValid = False
    if s1.isdigit() and s2.isdigit() and s3.isdigit():
        if len(s1) !=2 and len(s2) != 2 and len(s3) !=2:
            messagebox.showinfo("Invalid", "'Sort Code' entered is not valid.")
        else:
            sortValid = True
    else:
        messagebox.showinfo("Invalid", "'Sort Code' entered is not valid.")


    if nameValid == True and surnameValid == True and dayValid == True and monthValid == True and yearValid == True and address1Valid == True and address2Valid == True and postcodeValid == True and emailValid == True and mobileValid == True and wageValid==True and hoursValid==True and accountValid==True and sortValid==True:
        DOB = str(day) + "/" + str(month) + "/" + str(year)
        sortCode = str(s1) + "-" + str(s2) + "-" + str(s3)
        o = open(os.getcwd() + "\\staffaccounts\\" + employeeNum + ".txt", "a")
        o.write("\n" + title + ";" + Name + ";" + Surname + ";" + DOB + ";" + Address1 + ";" + Address2 + ";" + Postcode + ";" + Email + ";" + Mobile + "\n" +
                jobTitle + ";" + contractedHours + ";" + wage + ";" + accountNum + ";" + sortCode + "\n")
        o.close()
        staffLogin(canvas)
    else:
        messagebox.showinfo("Invalid")

def foodHome(canvas, name, existingOrdersList):             #main screen for refreshments
    canvas.destroy()
    user32 = ctypes.windll.user32
    w = str(user32.GetSystemMetrics(0))
    h = str(user32.GetSystemMetrics(1))
    foodMenu_canvas = Tk()
    foodMenu_canvas.geometry(w + 'x' + h)
    foodMenu_canvas.config(background='dark grey')
    foodMenu_canvas.title("Refreshments Menu")
    foodMenu_canvas.grid_rowconfigure(0, weight=1)
    foodMenu_canvas.grid_rowconfigure(2, weight=1)
    foodMenu_canvas.grid_columnconfigure(0, weight=1)
    foodMenu_canvas.grid_columnconfigure(2, weight=1)

    snacksDict = {}
    with open('snacks.json', 'r') as f:
        snacksDict = json.load(f)       #dictionary with a json file containing the menu
        text = (
            "Food \n\nLarge Popcorn                  £2.00 \nSmall Popcorn                  £1.50 \nChocolate Buttons              £1.25 \nNachos                         £1.75 \nFruit Pastilles                £1.25 \nIce Cream                      £2.00 \nPic n' Mix                     £1.60\n\n")

        text2 = (
            "Drinks \n\nCoke                           £1.10 \nFanta                          £1.10 \nWater                          £1.00 \nTango Ice Blast                £2.20 \nRed Wine                       £15.00 \nWhite Wine                     £15.00\n\n")
    f.close()
    text_frame = Frame(foodMenu_canvas, borderwidth=1, relief="flat")
    text_entry = Text(text_frame, wrap=WORD, height=20, width=50, borderwidth=1)
    vertical_scroll = Scrollbar(text_frame, orient=VERTICAL, command=text_entry.yview)
    text_entry["yscroll"] = vertical_scroll.set
    vertical_scroll.pack(side="right", fill="y")
    text_entry.pack(side="left", fill="both", expand=True)
    text_frame.grid(row=3, column=0, rowspan=3, pady=(0, 150))
    text_entry.insert(END, text)
    text_entry.insert(END, text2)       #adding menu to a scroll bar text box

    Label(foodMenu_canvas, text="Refreshments Menu", font=("Arial", 20), fg="purple", anchor='center').grid(row=0,
                                                                                                            column=0,
                                                                                                            columnspan=4)
    Label(foodMenu_canvas, text="Order Your Refreshments While Booking Tickets", font=("Arial", 20),
          anchor='center').grid(
        row=1, column=0, columnspan=4)
    Label(foodMenu_canvas, font=("Arial", 20), text="Menu").grid(row=2, column=0)



    Button(foodMenu_canvas, width=20, height=3, text='Deals', command=lambda: foodDeals(foodMenu_canvas, name, existingOrdersList)).grid(row=3, column=2, padx=10, pady=(50, 0), sticky=W)
    Button(foodMenu_canvas, width=20, height=3, text='Add To Existing Order', command=lambda: foodToExistingOrder(name, foodMenu_canvas, existingOrdersList)).grid(row=4, column=2, padx=10, pady=0, sticky=W)
    Button(foodMenu_canvas, width=20, height=3, text='Back', command=lambda: customerHomeScreen(name, foodMenu_canvas)).grid(row=5, column=2, padx=10, pady=(0, 180), sticky=W)


def foodDeals(canvas, name, existingOrdersList):                #showing discounts on food
    canvas.destroy()
    user32 = ctypes.windll.user32
    w = str(user32.GetSystemMetrics(0))
    h = str(user32.GetSystemMetrics(1))
    foodDeals_canvas = Tk()
    foodDeals_canvas.geometry(w+'x'+h)
    foodDeals_canvas.config(background='dark grey')
    foodDeals_canvas.title("Deals on Our Refreshments")
    foodDeals_canvas.grid_rowconfigure(0, weight=1)
    foodDeals_canvas.grid_rowconfigure(2, weight=1)
    foodDeals_canvas.grid_columnconfigure(0, weight=1)
    foodDeals_canvas.grid_columnconfigure(2, weight=1)

    Label(foodDeals_canvas, text=(name + ", Deals are on NOW \n Limited Time Only"), font=("Arial", 20), fg="purple", anchor='center').grid(row=0, column=0, columnspan=6)

    discount = PhotoImage(file="discountstar.png")

    deal1 = Canvas(foodDeals_canvas, width=200, height=200)
    deal1Display = discount.zoom(1, 1)
    deal1.grid(row=1, column=0, pady=10)
    deal1.create_image(1, 1, anchor=NW, image=deal1Display)
    Label(foodDeals_canvas, font=("Arial", 14), text="Upgrade to a large popcorn for just an extra 50p").grid(row=1, column=0)

    deal2 = Canvas(foodDeals_canvas, width=200, height=200)
    deal2Display = discount.zoom(1, 1)
    deal2.grid(row=2, column=2, pady=10)
    deal2.create_image(1, 1, anchor=NW, image=deal2Display)
    Label(foodDeals_canvas, font=("Arial", 14), text="2 for 1 drinks on Wednesdays").grid(row=2, column=2, padx=(0, 10))

    deal3 = Canvas(foodDeals_canvas, width=200, height=200)
    deal3Display = discount.zoom(1, 1)
    deal3.grid(row=1, column=3, pady=10)
    deal3.create_image(1, 1, anchor=NW, image=deal3Display)
    Label(foodDeals_canvas, font=("Arial", 14), text="Family combo - 2 popcorn and 4 drinks for £8").grid(row=1, column=3, padx=(0, 10))

    deal4 = Canvas(foodDeals_canvas, width=200, height=200)
    deal4Display = discount.zoom(1, 1)
    deal4.grid(row=2, column=4, pady=10)
    deal4.create_image(1, 1, anchor=NW, image=deal4Display)
    Label(foodDeals_canvas, font=("Arial", 14), text="Drink + Popcorn + Sweet for £4").grid(row=2, column=4, padx=(0, 10))

    Button(foodDeals_canvas, width=15, height=3, text='Back', command=lambda: foodHome(foodDeals_canvas, name, existingOrdersList)).grid(row=3, column=3, pady=(10, 150))

    mainloop()

def foodToExistingOrder(name, canvas, existingOrdersList):          #adding refreshments to an existing screening order
    canvas.destroy()
    user32 = ctypes.windll.user32
    w = str(user32.GetSystemMetrics(0))
    h = str(user32.GetSystemMetrics(1))
    foodToExistingOrder_canvas = Tk()
    foodToExistingOrder_canvas.geometry(w+'x'+h)
    foodToExistingOrder_canvas.config(background='dark grey')
    foodToExistingOrder_canvas.title("Add Refreshments To An Existing Order")
    foodToExistingOrder_canvas.grid_rowconfigure(0, weight=1)
    foodToExistingOrder_canvas.grid_rowconfigure(2, weight=1)
    foodToExistingOrder_canvas.grid_columnconfigure(0, weight=1)
    foodToExistingOrder_canvas.grid_columnconfigure(2, weight=1)

    Label(foodToExistingOrder_canvas, text="Add Refreshments to an Existing Order \n Food Ready on Arrival",
          font=("Arial", 20), fg="purple", anchor='center').grid(row=0, column=0, columnspan=8)
    Label(foodToExistingOrder_canvas, font=("Arial", 14), text="Add to order").grid(row=1, column=0, sticky=E,
                                                                                    pady=(100, 0))
    orderMenu = ttk.Combobox(foodToExistingOrder_canvas, width=30, font=("Arial", 14))
    orderMenu["values"] = existingOrdersList        #list of upcoming screening bookings that food can be added to
    orderMenu.grid(row=1, column=1, sticky=W, padx=10, pady=(100, 0))
    orderMenu.current(0)
    foodList = ["Large Popcorn", "Small Popcorn", "Chocolate Buttons", "Nachos", "Fruit Pastilles", "Ice Cream",
                "Pic n' mix"]
    Label(foodToExistingOrder_canvas, font=("Arial", 14), text="Food").grid(row=2, column=0, sticky=E)
    foodMenu = ttk.Combobox(foodToExistingOrder_canvas, width=30, font=("Arial", 14))
    foodMenu["values"] = foodList           #drop down box of items to select from the menu
    foodMenu.grid(row=2, column=1, sticky=W, padx=10)
    foodMenu.current(0)
    drinkList = ["Coke", "Fanta", "Water", "Tango Ice Blast", "Red Wine", "White Wine"]
    Label(foodToExistingOrder_canvas, font=("Arial", 14), text="Drink").grid(row=3, column=0, sticky=E)
    drinkMenu = ttk.Combobox(foodToExistingOrder_canvas, width=30, font=("Arial", 14))
    drinkMenu["values"] = drinkList
    drinkMenu.grid(row=3, column=1, sticky=W, padx=10)
    drinkMenu.current(0)

    Label(foodToExistingOrder_canvas, font=("Arial", 14), text="Basket").grid(row=1, column=4, padx=(0, 20))
    refreshmentsBasket = Listbox(foodToExistingOrder_canvas, font=("Arial", 14), width=18, height=13)       #list box with items added to it
    refreshmentsBasket.grid(row=2, column=4, rowspan=3, padx=(20, 50))

    Button(foodToExistingOrder_canvas, width=20, height=2, text='Add To Basket', command=lambda: refreshmentsBasket.insert(END, foodMenu.get())).grid(row=2, column=2)
    Button(foodToExistingOrder_canvas, width=20, height=2, text='Add To Basket', command=lambda: refreshmentsBasket.insert(END, drinkMenu.get())).grid(row=3, column=2)
    Button(foodToExistingOrder_canvas, width=20, height=2, text='Remove From Basket', command=lambda: deleteFromBasket(refreshmentsBasket, foodMenu.get())).grid(row=2, column=3)
    Button(foodToExistingOrder_canvas, width=20, height=2, text='Remove From Basket', command=lambda: deleteFromBasket(refreshmentsBasket, drinkMenu.get())).grid(row=3, column=3)
    Button(foodToExistingOrder_canvas, width=20, height=4, text='Place Order', command=lambda: foodOrder(foodToExistingOrder_canvas, orderMenu.get(), refreshmentsBasket.get(0, END), existingOrdersList, name)).grid(row=6, column=4, pady=(50, 100), sticky=W)
    Button(foodToExistingOrder_canvas, width=20, height=4, text='Back', command=lambda: foodHome(foodToExistingOrder_canvas, name, existingOrdersList)).grid(row=6, column=0, sticky=E, pady=(50, 100))

def deleteFromBasket(basket, item):         #removing an item from the list box
    label = item
    try:
        idx = basket.get(0, END).index(label)       #finds the item in the list box
        basket.delete(idx)                          #deletes the item
        return basket                               #sends the updated box back
    except:
        messagebox.showinfo("Item not in basket", "Item wasn't even in there sis")

def foodOrder(canvas, orderScreening, results, existingOrdersList, name):           #summary of the food order
    canvas.destroy()
    user32 = ctypes.windll.user32
    w = str(user32.GetSystemMetrics(0))
    h = str(user32.GetSystemMetrics(1))
    foodOrder_canvas = Tk()
    foodOrder_canvas.geometry(w+'x'+h)
    foodOrder_canvas.config(background='dark grey')
    foodOrder_canvas.title("Your Order")
    foodOrder_canvas.grid_rowconfigure(0, weight=1)
    foodOrder_canvas.grid_rowconfigure(2, weight=1)
    foodOrder_canvas.grid_columnconfigure(0, weight=1)
    foodOrder_canvas.grid_columnconfigure(2, weight=1)

    file = open(os.getcwd() + "\\customeraccounts\\" + name + ".txt", "r")
    lines = file.readlines()
    howmanylines = len(lines)
    i = 2
    valid = False
    while i < howmanylines:
        orderLine = lines[i]
        lst = orderLine.split(";")
        stringcount = len(lst)
        stringcount=int(stringcount)
        film = lst[1].strip()
        date = lst[2].strip()
        time = lst[3].strip()
        print(film + date + time)
        if film in orderScreening and date in orderScreening and time in orderScreening:        #finds the line in the text file that the selected screening is in
            if stringcount < 14:                #counts how many splits there are in the line to determine if food has already been added to that screening order
                print()
                valid = True

        i = i + 1
    file.close()

    if valid==True:
        prices = getPrices()            #gets the prices of the items in the menu
        priceList = []
        displayList = []
        for item in results:
            price = str(prices[item.replace(" ", "_")]*results.count(item))     #calculates the total price if multiple of the same item have been selected
            price = float(price)
            price = ("%.2f" % price)
            toAppend = str(results.count(item))+"x "+item +" : £"+ price        #displays the item, quantity and price for each different item in the basket
            if toAppend not in displayList:
                displayList.append(toAppend)

        orderDisplay = Listbox(foodOrder_canvas, font=("Arial", 14), width=20, height=5)
        for toAdd in displayList:
            orderDisplay.insert(END, toAdd)     #adds all of the order information to the box
        itemsToPurchase = orderDisplay.get(0, END)
        total = 0
        order = ""
        for item in itemsToPurchase:
            split = item.split(": ")
            itemPrice = float(split[1].replace("£", ""))
            total = total + itemPrice           #calculates the overall price for the order
            item = split[0]
            order = order + str(item)

        total = ("%.2f" % total)


        Label(foodOrder_canvas, text="Order Summary", font=("Arial", 30), fg="purple", anchor='center').grid(row=0, column=0, columnspan=3)
        Label(foodOrder_canvas, font=("Arial", 14), text="Name: ").grid(row=1, column=0, pady=10, sticky=E)
        Label(foodOrder_canvas, font=("Arial", 14), text=name).grid(row=1, column=1)
        Label(foodOrder_canvas, font=("Arial", 14), text="For Film: ").grid(row=2, column=0, pady=10, sticky=E)
        Label(foodOrder_canvas, font=("Arial", 14), text=orderScreening).grid(row=2, column=1)
        Label(foodOrder_canvas, font=("Arial", 14), text="Order: ").grid(row=3,column=0, pady=10, sticky=E)
        orderDisplay.grid(row=3, column=1)
        Label(foodOrder_canvas, font=("Arial", 14), text=("Total: ")).grid(row=4, column=0, pady=20, sticky=E)
        Label(foodOrder_canvas, font=("Arial", 14), text="£" + str(total)).grid(row=4, column=1)
        Button(foodOrder_canvas, width=15, height=4, text='Back', command=lambda: foodToExistingOrder(name, foodOrder_canvas, existingOrdersList)).grid(row=5, column=0, pady=(20, 100))
        Button(foodOrder_canvas, width=15, height=4, text='Proceed to Payment', command=lambda: foodPayment(foodOrder_canvas, name, total, order, orderScreening, existingOrdersList, results)).grid(row=5, column=2, pady=(20, 100))

    else:
        messagebox.showinfo("Invalid", "Food has already been added to this order")
        foodToExistingOrder(name, foodOrder_canvas, existingOrdersList)

def getPrices():        #gets the prices of the items in the menu
    with open("snacks.json", "r") as f:
        foodDic = json.load(f)          #opens the json file and assigns the contents to a dictionary
    f.close()
    return foodDic                      #populated dictionary is sent back to be used by the other function


def foodPayment(canvas, name, total, order, orderScreening, existingOrdersList, results):       #paying for the order - same as for paying for tickets
    canvas.destroy()
    user32 = ctypes.windll.user32
    w = str(user32.GetSystemMetrics(0))
    h = str(user32.GetSystemMetrics(1))
    foodPayment_canvas = Tk()
    foodPayment_canvas.geometry(w+'x'+h)
    foodPayment_canvas.configure(background='dark grey')
    foodPayment_canvas.title("Payment")
    foodPayment_canvas.grid_rowconfigure(0, weight=1)
    foodPayment_canvas.grid_rowconfigure(2, weight=1)
    foodPayment_canvas.grid_columnconfigure(0, weight=1)
    foodPayment_canvas.grid_columnconfigure(2, weight=1)

    Label(foodPayment_canvas, text="Payment", fg="purple", font=("Arial", 20)).grid(row=0, column=0, columnspan=4)

    Label(foodPayment_canvas, font=("Arial", 14), text="Total cost: £" + str(total)).grid(row=1, column=0, padx=10, pady=10)
    Label(foodPayment_canvas, font=("Arial", 14), text="Card name").grid(row=2, column=0, padx=10, pady=10)
    cardName_entry = Entry(foodPayment_canvas, width=20, font=("Arial", 14))
    cardName_entry.grid(row=2, column=1, sticky=W, columnspan=4)
    Label(foodPayment_canvas, font=("Arial", 14), text="Card number").grid(row=3, column=0, padx=10, pady=10)
    cardNumber_entry = Entry(foodPayment_canvas, width=20, font=("Arial", 14))
    cardNumber_entry.grid(row=3, column=1, sticky=W, columnspan=4)
    Label(foodPayment_canvas, font=("Arial", 14), text="Expiry date").grid(row=4, column=0, padx=10, pady=10)
    cardDateMonth_entry = Entry(foodPayment_canvas, width=10, font=("Arial", 14))
    cardDateMonth_entry.grid(row=4, column=1, sticky=W)
    Label(foodPayment_canvas, font=("Arial", 14), text="/").grid(row=4, column=2, sticky=W)
    cardDateYear_entry = Entry(foodPayment_canvas, width=10, font=("Arial", 14))
    cardDateYear_entry.grid(row=4, column=3, sticky=W, padx=(0, 50))
    Label(foodPayment_canvas, font=("Arial", 14), text="CCV").grid(row=5, column=0, padx=10, pady=10)
    cardCCV_entry = Entry(foodPayment_canvas, width=20, font=("Arial", 14))
    cardCCV_entry.grid(row=5, column=1, sticky=W, columnspan=4)


    Button(foodPayment_canvas, width=12, height=4, text="Confirm", command=lambda: validFoodPayment(foodPayment_canvas, name, order, orderScreening, total, cardName_entry.get(), cardNumber_entry.get(), cardDateMonth_entry.get(), cardDateYear_entry.get(), cardCCV_entry.get())).grid(row=6, column=2, padx=10, pady=(50, 200))
    Button(foodPayment_canvas, width=12, height=4, text="Back", command=lambda: foodOrder(foodPayment_canvas, orderScreening, results, existingOrdersList, name)).grid(row=6, column=0, padx=(10, 0), pady=(50, 200))


def validFoodPayment(canvas, name, order, orderScreening, total, cardName, cardNumber, cardDateMonth, cardDateYear, cardCCV):       #checking the payment details are valid - same as for paying for a ticket
    validCardName = False
    validCardNum = False
    validCardDateMonth = False
    validCardDateYear = False
    validCardCCV = False

    def luhn_checksum(card_number):
        def digits_of(n):
            return [int(d) for d in str(n)]

        digits = digits_of(card_number)
        odd_digits = digits[-1::-2]
        even_digits = digits[-2::-2]
        checksum = 0
        checksum += sum(odd_digits)
        for d in even_digits:
            checksum += sum(digits_of(d * 2))
        return checksum % 10

    def is_luhn_valid(card_number):
        return luhn_checksum(card_number) == 0

    result = is_luhn_valid(cardNumber)
    if str(result) == 'True':
        validCardNum = True
    else:
        messagebox.showinfo("Invalid card number", "Enter valid card details")

    cardName = cardName.replace(" ", "")
    if cardName.isalpha() == False:
        messagebox.showinfo("Invalid card name", "Enter valid card details")
    else:
        validCardName = True

    if cardDateMonth.isdigit():
        cardDateMonth = int(cardDateMonth)
        if cardDateMonth < 1 or cardDateMonth > 12:
            messagebox.showinfo("Invalid card date", "Enter valid card details")
        else:
            validCardDateMonth = True

    if cardDateYear.isdigit():
        cardDateYear = int(cardDateYear)
        if cardDateYear < 19 or cardDateYear > 23:
            messagebox.showinfo("Invalid card date", "Enter valid card details")
        else:
            validCardDateYear = True

    if cardCCV.isdigit():
        if len(cardCCV) == 3:
            validCardCCV = True
        else:
            messagebox.showinfo("Invalid CCV number", "Enter valid card details")



    if validCardName == True and validCardNum == True and validCardDateMonth == True and validCardDateYear == True and validCardCCV == True:
        print()
        addFoodToOrder(name, order, canvas, orderScreening, total, cardNumber)
    else:
        print()



def addFoodToOrder(name, order, canvas, orderScreening, total, cardNumber):         #adds the order to text files once valid
    canvas.destroy()
    user32 = ctypes.windll.user32
    w = str(user32.GetSystemMetrics(0))
    h = str(user32.GetSystemMetrics(1))
    addFoodToOrder_canvas = Tk()
    addFoodToOrder_canvas.geometry(w+'x'+h)
    addFoodToOrder_canvas.configure(background='dark grey')
    addFoodToOrder_canvas.title("Booking Complete")
    addFoodToOrder_canvas.grid_rowconfigure(0, weight=1)
    addFoodToOrder_canvas.grid_rowconfigure(2, weight=1)
    addFoodToOrder_canvas.grid_columnconfigure(0, weight=1)
    addFoodToOrder_canvas.grid_columnconfigure(2, weight=1)

    date = ""
    time = ""
    orderNum = ""
    with open(os.getcwd() + "\\customeraccounts\\" + name + ".txt", "r") as f:
        lines = f.readlines()
        f.close()
    f = open(os.getcwd() + "\\customeraccounts\\" + name + ".txt", "w")
    for line in lines:
        if orderScreening in line.replace(" ;", " ").replace(";", " "):     #finds the line the screening is in
            date = line.split(";")[2]
            time = line.split(";")[3]
            orderNum = line.split(";")[0]
            newLine = line + ";" + str(order) + ";" + str(total) + ";" + str(
                cardNumber[-4:].rjust(len(cardNumber), "*"))                #adds the food order onto the original line
            f.write(newLine)                                                #writes the new line to the file to replace the old one
        else:
            f.write(line)
    f.close()
    date = date.replace("/", "-")
    if os.path.isfile(os.getcwd() + "\\food\\" + date + ".txt"):        #gets the food file for the date the order is needed
        f = open(os.getcwd() + "\\food\\" + date + ".txt", "a")
        f.write(str(name) + ";" + str(order) + ";" + str(total) + ";" + str(time) + "\n")           #adds the order to the food text file
        f.close()
    else:
        with open(os.getcwd() + "\\food\\" + date + '.txt', "w") as f:
            f.write(str(name) + ";" + str(order) + ";" + str(total) + ";" + str(time) + "\n")
            f.close()

    userEmail = ""
    file = open(os.getcwd() + "\\customeraccounts\\" + name + ".txt", "r")
    lines = file.readlines()
    infoLine = lines[1]
    splitline = infoLine.split(";")
    for split in splitline:
        if "@" in split:
            userEmail = str(split)
    file.close()

    port = 587
    smtp_server = "smtp.gmail.com"
    sender_email = "bookings.moviemania@gmail.com"
    receiver_email = userEmail
    password = "QDD87kNV55P#8BC"
    subject = "Order Confirmation"
    message = ("Thank you " + str(name) + ". Here is your order summary: \n" + "Order number: " + str(orderNum) + "\n" + str(order) + " for " + str(orderScreening) + ".\nTotal cost: " + str(total) + " GBP \nPayment: Card " + str(cardNumber[-4:].rjust(len(cardNumber), "*")))

    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, 'Subject: {}\n\n{}'.format(subject, message))     #sends email confirmation

    Label(addFoodToOrder_canvas, font=("Arial", 15), text=(
        "Booking Summary \n\n Thank you for choosing MovieMania. \n\n A confirmation email will be sent shortly. \n\n Present your order confirmation upon arrival.")).grid(
        row=1, column=0, padx=50, pady=20, columnspan=3)

    Button(addFoodToOrder_canvas, font=("Arial", 12), width=15, height=4, text='Exit', command=quit).grid(row=2,
                                                                                                          column=0,
                                                                                                          padx=50,
                                                                                                          pady=(0, 50))
    Button(addFoodToOrder_canvas, font=("Arial", 12), width=15, height=4, text='Home',
           command=lambda: home_screen(addFoodToOrder_canvas)).grid(row=2,
                                                                    column=2,
                                                                    pady=(0, 50),
                                                                    padx=50)
    Label(addFoodToOrder_canvas, font=("Arial", 20), text="Booking Summary", fg="purple").grid(row=0, column=0,
                                                                                               columnspan=3)


window = Tk()           #creates a blank canvas to begin with
home_screen(window)     #calls the first function
window.mainloop()       #runs the application/events
