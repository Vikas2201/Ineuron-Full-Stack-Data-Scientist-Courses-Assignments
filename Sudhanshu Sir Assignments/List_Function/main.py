from Logging.logger import logger_app
from List_package import list_function
import warnings
warnings.filterwarnings("ignore")

logFilepath = "logging_file/Main_Log_File.txt"
logger_object = logger_app()
logfile = open(logFilepath, mode='a')

try:
    logger_object.log(logfile,'Entered in main.py python file')

    List = [2 , 4, 6, "Vikas" , "yogesh" , 4 , 3+2j]
    logger_object.log(logfile, "Given List : " + str(List))
    logger_object.log(logfile, "Length of Given List : " + str(list_function.length(List)))
    logger_object.log(logfile, "New List After Appending " + str(4) +" in the given list : " + str(list_function.Append(List,4)))
    logger_object.log(logfile, "New List After Removing " + str(3+2j) +" from the given list : " + str(list_function.Remove(List,3+2j)))
    logger_object.log(logfile, "Index of "+ "'Vikas' " + "in given list : " + str(list_function.Index(List,"Vikas")))
    logger_object.log(logfile, "4 Occur in the given list : " + str(list_function.Count(List,4)))
    logger_object.log(logfile, "Reverse of given list : " + str(list_function.Reverse(List)))
    logger_object.log(logfile, "Sorting a list : " + str(list_function.Sort(List)))
    logger_object.log(logfile, "Delete all element form list : " + str(list_function.Clear(List)))

except Exception as error:
    logger_object.log(logfile, 'Exception occurred in main.py file. Exception message :  ' + str(error))
    logger_object.log(logfile, 'Exited from the file')
    logfile.close()
