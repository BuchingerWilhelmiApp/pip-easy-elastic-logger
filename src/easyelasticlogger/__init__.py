from requests import post

class EasyLogger():
    HARDCODEDURL = "http://easy-elastic-logging-receiver-service/"
    
    def __init__(self, appname, indexname = "error"):
        self.appname = appname
        self.indexname = indexname
    
    def log(self, message, indexname = None, severity = "NORMAL"):
        if indexname is None:
            indexname = self.indexname
        return post(self.HARDCODEDURL, json={"message": message, "indexname" : indexname, "app": self.appname, "severity" : severity})


