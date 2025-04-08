import os
import json
import requests
from modules.updater import updaterMethods
#from modules.logo import showLogo

###lets check for updater
class appHandler():
    @staticmethod
    def startHandling():
        globalVersion = updaterMethods.getGlobalVersion()
        localVersion = updaterMethods.currentVersion('config.json')
       
        if not globalVersion or not localVersion:
                  print('something went wrong may be yoir data connction broken down')
        else:
            if not updaterMethods.isUpdatedVersion(globalVersion,localVersion):
                 print('new update is avilable')
                 usersChoiceAboutAutoUpdate = updaterMethods.showOptionsAndGetChoice()
                 if (usersChoiceAboutAutoUpdate):
                     if usersChoiceAboutAutoUpdate in ["1","01"]:
                         updaterMethods.triggerUpdate()
                     elif usersChoiceAboutAutoUpdate in ["02","2"]:
                         print('updates are paused for now ')
                     elif usersChoiceAboutAutoUpdate in ["03","3"]:
                            updaterMethods.openChangeLogs()
