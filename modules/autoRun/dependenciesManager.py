import os
import time
import importlib

def check(requirementsFilePath, attempt=1, total_attempts=5, waitingTime=6):
    # requiremwentsFilePath = '/'.join(os.getcwd('').split('/'))
    missing_modules = []
    while attempt < total_attempts:
        attempt += 1
        
        with open(requirementsFilePath, 'r') as f:
            all_modules = f.read().splitlines()
            
            for m in all_modules:
                try:
                    print(f'checking {m}')
                    importlib.import_module(m)
                    #the main module name goes hear
                except Exception as e:
                    print(e)
                    missing_modules.append(m)
                    
            for m in missing_modules:
                os.system(f'pip install {m}')

        while waitingTime > 0:
            time.sleep(1)
            waitingTime = waitingTime - 1
            print(f'\r retrying after {waitingTime} seconds')

        if not missing_modules: break
            
        missing_modules.clear()
            
        check(requirementsFilePath)

home_path = os.getcwd() # it will return the home path of project becas its going to get imported their

check(home_path + '/requirements.txt')