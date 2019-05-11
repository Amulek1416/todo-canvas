import json
from collections import namedtuple

settingsPath = 'resources/settings.json'

class Settings:
    def __init__(self, data):
        self.__dict__ = json.load(data)

    def getCalendarPath(self):
        return self.icsPath

    def setCalendarPath(self, path):
        self.icsPath = path
        # self.saveSettings()

    def saveSettings(self):
        with open('resources/settings.json', 'w') as outfile:
            json.dump(self, outfile)

def loadSettings():
    settingsFile = open(settingsPath)
    setting = Settings(settingsFile)
    settingsFile.close()
    return setting

