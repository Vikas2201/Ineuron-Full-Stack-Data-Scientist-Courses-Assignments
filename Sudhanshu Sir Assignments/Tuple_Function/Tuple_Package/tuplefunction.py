from Logging.logger import logger_app
import warnings
warnings.filterwarnings("ignore")

logFilepath = "logging_file/Tuple_Log_File.txt"
logger_object = logger_app()

# Implementation of len() method of a tuple
def length(tu):
    logfile = open(logFilepath, mode='a')
    logger_object.log(logfile,'Entered in length method')
    try:
        if Type(tu) == tuple:
            c = 0
            for i in tu:
                c += 1
            logger_object.log(logfile, 'Length Of Entered Tuple : ' + str(c))
            return c
        else:
            logger_object.log(logfile, 'Entered data structure is not a tuple')
    except Exception as error:
        logger_object.log(logfile,'Exception occurred in length function. Exception message :  ' + str(error))
        logger_object.log(logfile,'Exited from the length function')
        logfile.close()

# Implementation of type method of a tuple
def Type(tu):
    logfile = open(logFilepath, mode='a')
    logger_object.log(logfile, 'Entered in Type function')
    try:
        logger_object.log(logfile, 'Type Of Entered data structure : ' + str(type(tu)))
        return type(tu)
    except Exception as error:
        logger_object.log(logfile, 'Exception occurred in Type function. Exception message :  ' + str(error))
        logger_object.log(logfile, 'Exited from the Type function')
        logfile.close()

# Implementation of index() method of a list
def Index(tu,val):
    logfile = open(logFilepath, mode='a')
    logger_object.log(logfile, 'Entered in Index method')
    try:
        if Type(tu) == tuple:
            c = 0
            for i in tu:
                if i == val:
                    logger_object.log(logfile, 'Index Of Given Value In tuple : ' + str(c))
                    return c
                c += 1
            logger_object.log(logfile, 'Value Does Not Exist In Given tuple : ')
            return None
        else:
            logger_object.log(logfile, 'Entered data structure is not a tuple')
    except Exception as error:
        logger_object.log(logfile, 'Exception occurred in Index function. Exception message :  ' + str(error))
        logger_object.log(logfile, 'Exited from the Index function')
        logfile.close()


# Implementation of count() method of a list
def Count(tu,val):
    logfile = open(logFilepath, mode='a')
    logger_object.log(logfile, 'Entered in Count method')
    try:
        if Type(tu) == tuple:
            c = 0
            for i in tu:
                if i == val:
                    c += 1
            logger_object.log(logfile, 'Number Of Times ' + str(val) + ' Appears In The tuple : ' + str(c))
            return c
        else:
            logger_object.log(logfile, 'Entered data structure is not a tuple')
    except Exception as error:
        logger_object.log(logfile, 'Exception occurred in Count function. Exception message :  ' + str(error))
        logger_object.log(logfile, 'Exited from the Count function')
        logfile.close()
