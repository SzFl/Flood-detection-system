import sys
print("Python import search path (sys.path):")
for idx, p in enumerate(sys.path):
    print(f"{idx:2d}: {p!r}")


import os, sys
print("cwd         =", os.getcwd())
print("sys.path[0] =", sys.path[0])

from facades.FloodReaderFacade import FloodReaderFacade
from models.FloodYes import FloodYes
from models.FloodNo import FloodNo

floodReaderFacade = FloodReaderFacade()

messages : list = []

with open('./tests/test_good_tweets.txt', 'r') as file:
    messages = file.readlines()

for index, message in enumerate(messages):
    print('[] [] [] []' + str(index))

    try:
        response =  floodReaderFacade.ask_floodreader(message)

        if isinstance(response, FloodYes):
            response.print()
        elif isinstance(response, FloodNo):
            response.print()

    except ValueError:
        print("[] [] [] !! Model returned not a JSON.")
    except:
        print("[] [] [] !! Some error.")
    
    

# "There is a huge hole in a dam that is causing a flood in Gliwice on Kłodinca river. I am standing right now on it a 12:21 Today"