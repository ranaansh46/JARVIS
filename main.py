# All Modules
import wikipedia
import webbrowser
import os
from datetime import datetime
from rich.prompt import Prompt
from rich.console import Console
from rich.table import Table
from rich import print
from rich.panel import Panel
# Global Variables
query = "wish"

# Global Functions
def getcom():
    query = Prompt.ask("enter your command")
    query = query.lower()
    return query

def initialize():
    mode = Prompt.ask("Enter mode", choices=["default", "red", "blue"], default="default")
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

# All classes

# default class where basic functions are defined
class white:
    def __init__(self):
        print(Panel.fit("Jarvis at your service, working in [bold]default[/bold] mode", title="Welcome", subtitle="type help for list of commands"))

    def wishme(self):

        d = datetime.now()
        hour = int(d.hour)
        
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

    def website(self):    
        url = query.replace("open ","https//:www.")
        ext = ".com"
        url = url + ext
        webbrowser.open(url)   

    def wiki(self):        
        query = query.replace("wiki", "")
        result = wikipedia.summary(query, sentences=2)

    def help(self):
        table = Table(title="Basic commands for Jarvis module")
        table.add_column("Command", justify="right", style="cyan", no_wrap=True)
        table.add_column("Function", style="magenta")
        table.add_row("help", "prints all the commands")
        table.add_row("open", "to open any website")
        table.add_row("exit", "exit command can be accessed using multiple keywords like bye,exit,terminate or quit")
        table.add_row("wiki", "this will search the provided keyword and return a result summary from wikipedia")
        console = Console()
        console.print(table)

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

        elif 'open ' in query:
            m.website()
            
        elif 'count from 1 to 10' in query:
            print("1 2 3 4 5 6 7 8 9 10") 

        elif 'countdown' in query:
            print("10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10") 

        elif 'wiki' in query:
            wiki()
        elif 'help' == query:
            m.help()
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
