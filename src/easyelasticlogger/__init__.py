from requests import post

class EasyLogger():
    HARDCODEDURL = "http://easy-elastic-logging-receiver/log"
    
    def __init__(self, appname):
        self.appname = appname
    
    def log(self, message, indexname = "error", severity = "NORMAL"):
        return post(self.HARDCODEDURL, json={"message": message, "indexname" : indexname, "app": self.appname, "severity" : severity})


