import datetime
import urllib.request
from urllib.parse import urlparse
from icalendar import Calendar, Event
import settings
import json
from collections import namedtuple

programSettings = settings.loadSettings()

####################################################
# MAIN()
####################################################
def main():
   calendarPath = programSettings.getCalendarPath()
   if calendarPath == "":
      getICS()
   todo = Todo(loadICS())
   todo.displayTODO()
   return

####################################################
# Gets the link to the .ics file from the user and 
# downloads the file
####################################################
def getICS():
   url = input("Enter Canvas url for .ics file: ")
   savePath = 'resources/cal.ics' #input("Enter to save file: ")
   urllib.request.urlretrieve(url, savePath)
   programSettings.setCalendarPath(savePath)
   
def loadICS():
   assignments = []
   g = open(programSettings.getCalendarPath(), 'rb')
   gcal = Calendar.from_ical(g.read())
   for i in gcal.walk():
      if i.name == "VEVENT":
         assignments.append(Assignment(i))
   g.close()
   return assignments

####################################################
# CLASS: Todo
# SUMMARY: Class contains an array of assignments 
#          that can be accessed weeks at a time
####################################################
class Todo:
   def __init__(self, assignments):
      self.assignments = assignments
      self.date = datetime.datetime.now()

   ####################################################
   # Returns a specific assignment's URL
   ####################################################
   def getLink(self, index):
      self.assignments[index].getURL

   ####################################################
   # Returns an array containing all the assignments 
   # due for a given week
   ####################################################
   def getWeek(self, week):
      return

   def displayTODO(self):
      weekAssign = self.getWeek(0)
      self.displayWeek()
      self.printAssignments()
   
   def displayWeek(self):
      self.displayDay()

   def displayDay(self):
      return

   def printAssignments(self):
      for i in self.assignments:
         print (i.name)

####################################################
# CLASS: Assignment
# SUMMARY: Contains information of an assignment's
#          due-date, name, course, and link to the 
#          webpage of the assignment
####################################################
class Assignment:
   def __init__(self, calItem):
      self.name = calItem.get("summary")
      self.dueDate = calItem.get("dtend").dt
      self.UID = calItem.get("UID")
      self.course = self.name
      self.courseID = calItem.get("URL")
      self.cleanData()

   ####################################################
   # Returns link to assignment in canvas
   ####################################################
   def getURL(self):
      url = "https://byui.instructure.com/courses/" + self.courseID + "/assignments/" + self.UID
      print (url)
      return url

   ####################################################
   # Clears up the not needed data coming in
   ####################################################
   def cleanData(self):
      temp = self.courseID
      temp = urlparse(temp).query
      self.courseID = temp[24:29]
      
      self.course = self.name[self.name.find("[")+1:self.name.find("]")]
      self.name = self.name[0:self.name.find("[")]
      self.UID = self.UID.replace('event-assignment-', '')

# define main function
if __name__ == '__main__':
   main()