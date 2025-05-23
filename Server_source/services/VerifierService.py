from os import listdir
from os.path import isfile, join

from models.PipeStage import PipeStage
import pandas as pd


class VerifierService(PipeStage):

    def flow(self,path_to_input_folder:str):
        print('[Info][VerifierService]: start')
        verification_results = self.check_all_files(path_to_input_folder)
        self.print_results(verification_results,path_to_input_folder)
        print('[Info][VerifierService]: end')

    def print_results(self,verification_results:dict,path_to_input_folder) -> None:

        sources = []
        corrects = []
        totals = []
        ratios = []



        all_matches = 0
        all_totals = 0

        print('Verification results for each source.')
        print('-------------------------------------')
        print(f"{'Source':<20} | {'Correct':>10} | {'Total':>10} | {'Ratio (Correct/Total)':>10}")

        for key, value in verification_results.items():
            match = value[0]
            total = value[1]

            print(f"{key:<20} | {match:>10} | {total:>10} | {match / total:>10}")

            all_matches = all_matches + match
            all_totals = all_totals + total

            sources.append(key)
            corrects.append(match)
            totals.append(total)
            ratios.append(match / total)

        print('-------------------------------------')
        print(f"{'All Correct':<10} | {'All Total':>10} | {'Ratio (All Correct / All Total)':>10}")
        print(f"{all_matches:<10} | {all_totals:>10} | {all_matches / all_totals:>10}")

        sources.append('All Tools')
        corrects.append(all_matches)
        totals.append(all_totals)
        ratios.append(all_matches / all_totals)

        results = {
            "Source":sources,
            "Correct":corrects,
            "Total":totals,
            "Ratio (Correct/Total)":ratios
        }

        result_path = path_to_input_folder + '/result.csv'
        pd.DataFrame(results).to_csv(result_path,sep=';',quoting=1,index=False)


    def check_all_files(self,path_to_input_folder) -> dict:
        files = [f for f in listdir(path_to_input_folder) if isfile(join(path_to_input_folder, f))] # tylko dla csv z danymi a nie odpowiedziami

        verification_results = {}

        for file in files:
            if file[-12:] == 'messages.csv':
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

            print(f"File: {file} Match: {matches} Total: {total}")
            return matches, total

        except Exception as e:
            print(f'[Erro][VerifierService] verify_for_file() {e}') 
            return 0, 0

