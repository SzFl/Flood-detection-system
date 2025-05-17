from models.PipeStage import PipeStage
import pandas as pd

class LabelerService(PipeStage):

    def flow(self,path_to_input_folder:str):
        print('[Info][LabelerService]: start')
        self.label_tweets(path_to_input_folder)
        self.label_rss(path_to_input_folder)
        print('[Info][LabelerService]: end')

    def label_tweets(self,path_to_input_folder:str) -> None:
        path_to_rss_file = path_to_input_folder + '/tweeter_messages.csv'
        self.add_labels(path_to_rss_file)
        
    def label_rss(self,path_to_input_folder:str) -> None:
         path_to_rss_file = path_to_input_folder + '/rss_messages.csv'
         self.add_labels(path_to_rss_file)

    def add_labels(self,path_to_file:str) -> None:
        try:
            df = pd.read_csv(path_to_file)

            is_about_flood = []

            for index, row in df.iterrows():

                incorrect = True
                while(incorrect):
                    print('=== MESSAGE:')
                    print(row['message'])
                    print('=== IS ABOUT FLOOD?:')
                    response = input()
                    print('=== === === === ===:')

                    if response.isdigit() and (int(response) == 0 or int(response) == 1):
                        is_about_flood.append(response)
                        incorrect = False
                    else:
                         print('Wrong value! Repeat answear')
                         incorrect = True
                     
            df.insert(loc = 0, column = 'is_about_flood', value = is_about_flood)

            df.to_csv(path_to_file, index=False, encoding="utf-8",sep=';', quoting=1)

        except Exception as e:
                print(f'[Erro][LabelerService]: add_labels() {e}')


