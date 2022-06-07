# All Modules
import wikipedia
import webbrowser
import os
from datetime import datetime
# Global Variables
query = "wish"


# Global Functions
def getcom():
    query = input("Enter your command: ")
    return query

def initialize():
    mode = input("Enter mode :")
    if mode == "red":
        obj2 = red()
        mo = obj2
    elif mode == "blue":
        obj3 = blue()
        mo = obj3
    else:
        obj1 = white()
        mo = obj1
    return mo

def help():
    print("|Help :")
    print("|1. Help : lists all the command for the current mod")
    print("|2. Mode : lets you enable other modes of JARVIS\n|\t1. red : To change the list contents and edit user profile\n|\t2: blue : to access jarvis as a server from other devices or other computers")
    print("|3. open : opens predefined websites for the user.\nExample\n\topen spotify : opens spotify in browser")
    print("|4. wikipedia : to search anything on wikipedia just use term wikipedia in the command.\nexample:\n\twikipedia ocean : this will give results of wikipedia ocean page in terminal")


# All classes

# default class where basic functions are defined
class white:
    def __init__(self):
        print("------------------------------------------")
        print("-This is JARVIS activated in Default mode-")
        print("------------------------------------------")
        print("\n type Help for list of basic commands")

    def wishme(self):
        d = datetime.now()
        hour = int(d.hour)
        print("\n")
        if hour>=6 and hour<12:
            print("good morning")
        elif hour>=12 and hour<18:
            print("good afternoon")
        elif hour>=18 and hour<21:
            print("good evening")
        elif hour>=21 and hour<0:
            print("hello")
        elif hour>=0 and hour<6:
            print("sun is busy on the other side of earth you should sleep now...")
        print("\n")

# red class for red mode to change the user profiles and make changes in lists
class red(white):
    def __init__(self):
        os.system("color 04")
        print("------------------------------------------")
        print("-  This is JARVIS activated in Red mode  -")
        print("------------------------------------------")


# blue class for blue mode 
class blue(white):
    def __init__(self):
        os.system("color 0B")
        print("------------------------------------------")
        print("-  This is JARVIS activated in Blue mode -")
        print("------------------------------------------")


# main function starts here

if __name__ == '__main__':
    m = initialize()
    ch = 1
    m.wishme()
    while ch != 0:
        query = getcom()
        if 'hello' in query:
            print('hello sir input some command!')

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open studio' in query:
            webbrowser.open("studio.youtube.com")

        elif 'open spotify' in query:
            webbrowser.open("open.spotify.com")

        elif 'open bing' in query:
            webbrowser.open("bing.com")

        elif 'open mail' in query:
            webbrowser.open("mail.google.com")

        elif 'open browser' in query:
            webbrowser.open("www.bing.com")

        elif 'count from 1 to 10' in query:
            print("1 2 3 4 5 6 7 8 9 10") 

        elif 'open fb' in query:
            webbrowser.open("facebook.com")

        elif 'countdown' in query:
            print("10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10") 

        elif 'wikipedia' in query:
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)

        elif 'Help' == query:
            help()
    #all the code ahead of this point is written to exit the jarvis module
        elif 'bye' == query:
            print("bye sir, have a good time.")
            exit()
            break

        elif 'exit' == query:
            print("exiting Jarvis assistance module")
            exit()
            break

        elif 'terminate' == query:
            print("terminating Jarvis assistance module")
            exit()
            break

        elif 'quit' == query:
            print("quiting assistant module")
            exit()
            break

        else:
            print("invalid command!")