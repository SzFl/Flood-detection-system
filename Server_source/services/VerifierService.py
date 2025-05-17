from os import listdir
from os.path import isfile, join

from models.PipeStage import PipeStage
import pandas as pd


class VerifierService(PipeStage):

    def flow(self,path_to_input_folder:str):
        print('[Info][VerifierService]: start')
        verification_results = self.check_all_files(path_to_input_folder)
        self.print_results(verification_results)
        print('[Info][VerifierService]: end')

    def print_results(self,verification_results:dict) -> None:

        all_matches = 0
        all_totals = 0

        print('Verification results for each source.')
        print('-------------------------------------')
        print(f"{'Source':<20} | {'Match':>10} | {'Total':>10} | {'Ratio (Match/Total)':>10}")

        for key, value in verification_results.items():
            match = value[0]
            total = value[1]

            print(f"{key:<20} | {match:>10} | {total:>10} | {match / total:>10}")

            all_matches = all_matches + match
            all_totals = all_totals + total

        print('-------------------------------------')
        print(f"{'All Matches':<10} | {'All Total':>10} | {'Ratio (All Match / All Total)':>10}")
        print(f"{all_matches:<10} | {all_totals:>10} | {all_matches / all_totals:>10}")


    def check_all_files(self,path_to_input_folder) -> dict:
        files = [f for f in listdir(path_to_input_folder) if isfile(join(path_to_input_folder, f))]

        verification_results = {}

        for file in files:
            verification_results[file] = self.verify_for_file(path_to_input_folder,file)

        return verification_results

    def verify_for_file(self,path_to_input_folder:str,file:str) -> tuple[int, int]:
        path_to_file = path_to_input_folder + '/' + file
        
        try:
            df = pd.read_csv(path_to_file,sep=';')
            pred_col: str = 'predictions'
            true_col: str = 'is_about_flood'
            out_col: str = 'verification'

            missing = {pred_col, true_col} - set(df.columns)
            if missing:
                raise KeyError(f"DataFrame is missing columns: {missing}")
            
            df[out_col] = (df[pred_col] == df[true_col]).astype(int)

            total = len(df)
            matches = int(df[out_col].sum())

            return matches, total

        except Exception as e:
            print(f'[Erro][VerifierService] verify_for_file() {e}') 
            return 0, 0

