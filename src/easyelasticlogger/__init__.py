from requests import post

class EasyLogger():
    HARDCODEDURL = "http://easy-elastic-logging-receiver/log"
    
    def __init__(self, appname):
        self.appname = appname
    
    def log(self, message, severity = "NORMAL"):
        return post(self.HARDCODEDURL, json={"message": message, "app": self.appname, "severity" : severity})


