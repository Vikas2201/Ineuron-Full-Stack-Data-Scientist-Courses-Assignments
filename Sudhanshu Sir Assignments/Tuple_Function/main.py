from Logging.logger import logger_app
from Tuple_Package import tuplefunction as tf
import warnings
warnings.filterwarnings("ignore")

logFilepath = "logging_file/Main_Log_File.txt"
logger_object = logger_app()
logfile = open(logFilepath, mode='a')


try:
    logger_object.log(logfile,'Entered in main.py python file')

    Tuple = (4,6,7,8,9,11,4,6,4)
    logger_object.log(logfile, "Given Tuple : " + str(Tuple))
    logger_object.log(logfile, "Length of Given Tuple : " + str(tf.length(Tuple)))
    logger_object.log(logfile, "Index of "+ "'11' " + "in given Tuple : " + str(tf.Index(Tuple,11)))
    logger_object.log(logfile, "4 Occur in the given Tuple : " + str(tf.Count(Tuple,4)))

except Exception as error:
    logger_object.log(logfile, 'Exception occurred in main.py file. Exception message :  ' + str(error))
    logger_object.log(logfile, 'Exited from the file')
    logfile.close()