import datetime
import urllib.request
from urllib.parse import urlparse
from icalendar import Calendar, Event
import settings

programSettings = settings.Settings()
tempPath = '/home/zac/git/personal/todo-canvas/cal.ics'

def main():
   # calendarPath = programSettings.getCalendarPath()
   # if calendarPath == "":
   #    getICS()

   todo = Todo()
   todo.load(tempPath)
   return

def getICS():
   url = input("Enter Canvas url for .ics file: ")
   savePath = input("Enter to save file: ")
   savePath = tempPath
   urllib.request.urlretrieve(url, '')
   programSettings.setCalendarPath(savePath)
   

class Todo:
   def __init__(self):
      self.assignments = []
      return

   def load(self, path):
      g = open(path, 'rb')
      gCal = Calendar.from_ical(g.read())
      for i in gCal.walk():
         if i.name == "VEVENT":
            self.assignments.append(Assignment(i))
      g.close()

   def getLink(self, index):
      self.assignments[index].getURL

class Assignment:
   def __init__(self, calItem):
      self.name = calItem.get("summary")
      self.dueDate = calItem.get("dtend").dt
      self.UID = calItem.get("UID")
      self.course = self.name
      self.courseID = calItem.get("URL")
      self.cleanData()
      self.getURL()

   def getURL(self):
      url = "https://byui.instructure.com/courses/" + self.courseID + "/assignments/" + self.UID
      print (url)
      return url

   def cleanData(self):
      temp = self.courseID
      temp = urlparse(temp).query
      self.courseID = temp[24:29]
      
      self.course = self.name[self.name.find("[")+1:self.name.find("]")]
      self.name = self.name[0:self.name.find("[")]
      self.UID = self.UID.replace('event-assignment-', '')

if __name__ == '__main__':
   main()