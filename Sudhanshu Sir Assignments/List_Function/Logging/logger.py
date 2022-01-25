from datetime import datetime

class logger_app :
    def __init__(self):
        pass

    def log(self,file , message):
        self.now = datetime.now()
        self.time = self.now.strftime("%H:%M:%S")
        self.date = self.now.date()

        # write the message in file in the format of date/time
        file.write("\n" + str(self.date) + "/" + str(self.time) + "\t\t" + message + "\n")