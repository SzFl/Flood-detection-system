import pandas as pd

from facades.FloodReaderFacade import FloodReaderFacade
from models.FloodYes import FloodYes
from models.FloodNo import FloodNo

floodReaderFacade = FloodReaderFacade()



messages = pd.read_csv('Server_source/tests/messages.csv')

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