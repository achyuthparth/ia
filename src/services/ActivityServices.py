"""LanguageServices.py: This file has classes and methods for Vocabulary management."""

__author__ = "Achyuthaa Parthasarathy"

import json
from os import path
import datetime as dateTime


class Activity:

    def __init__(self, vocabId, dateTime, numCorrect, numWrong):
        self.VocabId = vocabId
        self.DateTime = dateTime
        self.NumCorrect = numCorrect
        self.NumWrong = numWrong
        
class ActivityEncoder(json.JSONEncoder):
    def default(self, o):
        dict = {
            "VocabId" : o.VocabId,
            "DateTime" : o.DateTime.__str__(),
            "NumCorrect" : o.NumCorrect,
            "NumWrong" : o.NumWrong
            }
        return dict

class ActivityDecoder(json.JSONDecoder):
    def __init__(self):
        json.JSONDecoder.__init__(self, object_hook=self.toObject)

    def toObject(self, dict):
        # TODO: may be convert to datetime properly here
        return Activity(
            dict["VocabId"], 
            dict["DateTime"], 
            dict["NumCorrect"], 
            dict["NumWrong"])

class ActivityFile:
    def __init__(self, fileName="D:\\Users\\achyu\\Source\\repos\\ia\\src\\ActivityList.json"):
        self.FileName = fileName

    def ReadFile(self):
        fileExists = path.exists(self.FileName)
        if fileExists:
            with open(self.FileName, 'r') as infile:
                json_object = json.load(infile, cls=ActivityDecoder)
        else:
            json_object = []

        return json_object

    def WriteFile(self, activityList):
        with open(self.FileName, "w") as outfile:
            json.dump(
                activityList, 
                outfile, 
                cls=ActivityEncoder)
        return

        
    def AddActivity(self, activity):
        # read all activity from file
        activityList = self.ReadFile()
        
            
        # append
        activityList.append(activity)
        
        # write
        self.WriteFile(activityList)
        return