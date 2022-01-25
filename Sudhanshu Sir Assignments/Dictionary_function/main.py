from Logging.logger import logger_app
from dictionary_package import dictionary
import warnings
warnings.filterwarnings("ignore")

logFilepath = "logging_file/Main_Log_File.txt"
logger_object = logger_app()
logfile = open(logFilepath, mode='a')

try:
    logger_object.log(logfile,'Entered in main.py python file')

    Dict = {1 : "Vikas" , 2 : "Yogesh" , 3 : "Vicky" , 4 : "Khushi" ,5 : "Riya"}
    logger_object.log(logfile, "Given List : " + str(Dict))
    logger_object.log(logfile, "List of Keys of given dictionary : " + str(dictionary.Keys(Dict)))
    logger_object.log(logfile, "List of Values Of Dictionary : " + str(dictionary.Values(Dict)))
    logger_object.log(logfile, "A list of dictionary in (key, value) tuple pairs : " + str(dictionary.Items(Dict)))
    logger_object.log(logfile, "Value of " + str(3) + " key in the dictionary : " + str(dictionary.Get(Dict,3)))
    logger_object.log(logfile, "Value of " + str(6) + " key in the dictionary : " + str(dictionary.Setdefault(Dict,6)))
    logger_object.log(logfile, "Remove key " + str(6) + " in the dictionary : " + str(dictionary.POP(Dict,6)))
    logger_object.log(logfile, "Delete all element form dictionary : " + str(dictionary.Clear(Dict)))

except Exception as error:
    logger_object.log(logfile, 'Exception occurred in main.py file. Exception message :  ' + str(error))
    logger_object.log(logfile, 'Exited from the file')
    logfile.close()