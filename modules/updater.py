import requests
import json
import os

class updaterMethods():
    @staticmethod
    def getGlobalVersion():
        try:
            resp = requests.get('https://raw.githubusercontent.com/hackesofice/Acode-live-server-backend/refs/heads/main/config.json')
            config = resp.json()
            globalVersion = config.get('version')
            return globalVersion
        except Exception as rr:
            print(f'Unable to check for updates')
    
    @staticmethod
    def currentVersion(configFilePath):
        try:
            with open(configFilePath, 'r') as config:
                data = json.load(config)
                localVersion = data.get('version')
                return localVersion
        except Exception as e:
            print(f'unable to open the local file {e}')

    @staticmethod
    def isUpdatedVersion(localVersion, globalVersion):
      ## for now ill jisy omly comoare the both as strings later ill update it with actual int comparision
        if localVersion == globalVersion:
            return True
        else:
            return False

    @staticmethod
    def showOptionsAndGetChoice():
        print("[01] UPDATE NOW")
        print("[02] SKIP FOR NOW")
        print("[03] SEE CHANGELOGS")
        choice = input("ENETR YOUR CHOICE : => ")
        return choice
  
  
    @staticmethod
    def triggerUpdate():
        print('UPDATE HAS BE STARTED')
        os.system('cd ~ && rm -rf Acode-live-server-backend')
        os.system('pkg update && pkg upgrade -y')
        os.system('pkg install git -y')
        os.system('git clone https://github.com/hackesofice/Acode-live-server-backend.git')
        os.system('cd Acode-live-server-backend')
        os.system('pip install -r requirements.txt')
        os.system('python main.py')

    @staticmethod
    def openChangeLogs():
        print('opening changelogs')
        os.system('xdg-open https://raw.githubusercontent.com/hackesofice/Acode-live-server-backend/refs/heads/main/changelogs.md')
        print('not redirected yet???? ===>>> visit manually https://raw.githubusercontent.com/hackesofice/Acode-live-server-backend/refs/heads/main/README.md')
    
