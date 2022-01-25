from Logging.logger import logger_app
import warnings
warnings.filterwarnings("ignore")

logFilepath = "logging_file/dictionary_Log_File.txt"
logger_object = logger_app()

# Implementation of type method of a dictionary
def Type(dt):
    logfile = open(logFilepath, mode='a')
    logger_object.log(logfile, 'Entered in Type function')
    try:
        logger_object.log(logfile, 'Type Of Entered data structure : ' + str(type(dt)))
        return type(dt)
    except Exception as error:
        logger_object.log(logfile, 'Exception occurred in Type function. Exception message :  ' + str(error))
        logger_object.log(logfile, 'Exited from the Type function')
        logfile.close()

# Implementation of clear() method of a dictionary
def Clear(dt):
    logfile = open(logFilepath, mode='a')
    logger_object.log(logfile, 'Entered in Clear function')
    try:
        if Type(dt) == dict:
            logger_object.log(logfile, 'New dictionary After Removing A Remove all items from the dictionary : ' + str({}))
            return {}
        else:
            logger_object.log(logfile, 'Entered data structure is not a dictionary')
    except Exception as error:
        logger_object.log(logfile, 'Exception occurred in Clear function. Exception message :  ' + str(error))
        logger_object.log(logfile, 'Exited from the Clear function')
        logfile.close()

# Implementation of get() method of a dictionary
def Get(dt,key):
    logfile = open(logFilepath, mode='a')
    logger_object.log(logfile, 'Entered in Get function')
    try:
        if Type(dt) == dict:
            for k , v in dt.items():
                if k == key:
                    logger_object.log(logfile, 'for ' + str(key) +' key value in the dictionary : ' + str(v))
                    return v
            logger_object.log(logfile, 'for ' + str(key) + ' key value in the dictionary does not exit ')
            return None
        else:
            logger_object.log(logfile, 'Entered data structure is not a dictionary')
    except Exception as error:
        logger_object.log(logfile, 'Exception occurred in Get function. Exception message :  ' + str(error))
        logger_object.log(logfile, 'Exited from the Get function')
        logfile.close()

# Implementation of items() method of a dictionary
def Items(dt):
    logfile = open(logFilepath, mode='a')
    logger_object.log(logfile, 'Entered in Items function')
    try:
        if Type(dt) == dict:
            logger_object.log(logfile, 'A list of dictionary in (key, value) tuple pairs : ' + str(dt.items()))
            return dt.items()
        else:
            logger_object.log(logfile, 'Entered data structure is not a dictionary')
    except Exception as error:
        logger_object.log(logfile, 'Exception occurred in Items function. Exception message :  ' + str(error))
        logger_object.log(logfile, 'Exited from the Items function')
        logfile.close()


# Implementation of keys() method of a dictionary
def Keys(dt):
    logfile = open(logFilepath, mode='a')
    logger_object.log(logfile, 'Entered in Keys function')
    try:
        if Type(dt) == dict:
            lt = []
            for k , v in dt.items():
                lt.append(k)
            logger_object.log(logfile, 'A list of dictionary keys : ' + str(lt))
            return lt
        else:
            logger_object.log(logfile, 'Entered data structure is not a dictionary')
    except Exception as error:
        logger_object.log(logfile, 'Exception occurred in Keys function. Exception message :  ' + str(error))
        logger_object.log(logfile, 'Exited from the Keys function')
        logfile.close()

# Implementation of values() method of a dictionary
def Values(dt):
    logfile = open(logFilepath, mode='a')
    logger_object.log(logfile, 'Entered in Values function')
    try:
        if Type(dt) == dict:
            lt = []
            for k , v in dt.items():
                lt.append(v)
            logger_object.log(logfile, 'A list of dictionary Values : ' + str(lt))
            return lt
        else:
            logger_object.log(logfile, 'Entered data structure is not a dictionary')
    except Exception as error:
        logger_object.log(logfile, 'Exception occurred in Values function. Exception message :  ' + str(error))
        logger_object.log(logfile, 'Exited from the Values function')
        logfile.close()

# Implementation of setdefault() method of a dictionary
def Setdefault(dt,key):
    logfile = open(logFilepath, mode='a')
    logger_object.log(logfile, 'Entered in Values function')
    try:
        if Type(dt) == dict:
            if Get(dt,key) != None:
                logger_object.log(logfile, 'for ' + str(key) + ' key value in the dictionary : ' + str(Get(dt,key)))
                return Get(dt,key)
            else:
                dt.setdefault()
                logger_object.log(logfile, 'New dictionary : ' + str(dt))
                return dt
        else:
            logger_object.log(logfile, 'Entered data structure is not a dictionary')
    except Exception as error:
        logger_object.log(logfile, 'Exception occurred in Setdefault function. Exception message :  ' + str(error))
        logger_object.log(logfile, 'Exited from the Setdefault function')
        logfile.close()


# Implementation of pop() method of a dictionary
def POP(dt,key):
    logfile = open(logFilepath, mode='a')
    logger_object.log(logfile, 'Entered in POP method')
    try:
        if Type(dt) == dict:
            dt.pop(key)
            logger_object.log(logfile, 'New dictionary After Removing A key-value pair : ' + str(dt))
            return dt
        else:
            logger_object.log(logfile, 'Entered data structure is not a dictionary')
    except Exception as error:
        logger_object.log(logfile, 'Exception occurred in POP function. Exception message :  ' + str(error))
        logger_object.log(logfile, 'Exited from the POP function')
        logfile.close()

