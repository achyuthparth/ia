from ActivityServices import *
from datetime import datetime

def TestActivityAdd():
    activity = Activity(
        "test1", 
        datetime(2022, 3, 15, 22, 54), 
        4, 
        5)

    activityFile = ActivityFile()
    activityFile.AddActivity(activity)
    activity = Activity(
        "Test2", 
        datetime(2022, 3, 15, 23, 1),
        5,
        4)

    activityFile.AddActivity(activity)

def TestGetActivity():
    file = ActivityFile()
    activities = file.ReadFile()
    print(activities)

#TestActivityAdd()
TestGetActivity()

