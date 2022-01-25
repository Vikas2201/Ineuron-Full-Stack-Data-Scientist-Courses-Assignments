from Logging.logger import logger_app
import warnings
warnings.filterwarnings("ignore")

logFilepath = "logging_file/List_Log_File.txt"
logger_object = logger_app()

# Implementation of len() method of a list
def length(lt):
    logfile = open(logFilepath, mode='a')
    logger_object.log(logfile,'Entered in length method')
    try:
        if Type(lt) == list:
            c = 0
            for i in lt:
                c += 1
            logger_object.log(logfile, 'Length Of Entered List : ' + str(c))
            return c
        else:
            logger_object.log(logfile, 'Entered data structure is not a list')
    except Exception as error:
        logger_object.log(logfile,'Exception occurred in length function. Exception message :  ' + str(error))
        logger_object.log(logfile,'Exited from the length function')
        logfile.close()

# Implementation of type method of a list
def Type(lt):
    logfile = open(logFilepath, mode='a')
    logger_object.log(logfile, 'Entered in Type function')
    try:
        logger_object.log(logfile, 'Type Of Entered data structure : ' + str(type(lt)))
        return type(lt)
    except Exception as error:
        logger_object.log(logfile, 'Exception occurred in Type function. Exception message :  ' + str(error))
        logger_object.log(logfile, 'Exited from the Type function')
        logfile.close()

# Implementation of append() method of a list
def Append(lt,element):
    logfile = open(logFilepath, mode='a')
    logger_object.log(logfile, 'Entered in Append method')
    try:
        if Type(lt) == list:
            lt[length(lt):] = [element]
            logger_object.log(logfile, 'New List After Appending A Element : ' + str(lt))
            return lt
        else:
            logger_object.log(logfile, 'Entered data structure is not a list')
    except Exception as error:
        logger_object.log(logfile, 'Exception occurred in Append function. Exception message :  ' + str(error))
        logger_object.log(logfile, 'Exited from the Append function')
        logfile.close()

# Implementation of remove() method of a list
def Remove(lt,ele):
    logfile = open(logFilepath, mode='a')
    logger_object.log(logfile, 'Entered in Remove method')
    try:
        if Type(lt) == list:
            l = []
            for i in lt:
                if i != ele :
                    Append(l,i)
            logger_object.log(logfile, 'New List After Removing A Element : ' + str(l))
            return l
        else:
            logger_object.log(logfile, 'Entered data structure is not a list')
    except Exception as error:
        logger_object.log(logfile, 'Exception occurred in Remove function. Exception message :  ' + str(error))
        logger_object.log(logfile, 'Exited from the Remove function')
        logfile.close()


# Implementation of pop() method of a list
def POP(lt,index):
    logfile = open(logFilepath, mode='a')
    logger_object.log(logfile, 'Entered in POP method')
    try:
        if Type(lt) == list:
            for i in range(0,length(lt)):
                if i == index:
                    lt = Remove(lt,lt[i])
            logger_object.log(logfile, 'New List After Removing A Element : ' + str(lt))
            return lt
        else:
            logger_object.log(logfile, 'Entered data structure is not a list')
    except Exception as error:
        logger_object.log(logfile, 'Exception occurred in POP function. Exception message :  ' + str(error))
        logger_object.log(logfile, 'Exited from the POP function')
        logfile.close()


# Implementation of clear() method of a list
def Clear(lt):
    logfile = open(logFilepath, mode='a')
    logger_object.log(logfile, 'Entered in Clear method')
    try:
        if Type(lt) == list:
            logger_object.log(logfile, 'New List After Removing A Remove all items from the list : ' + str([]))
            return []
        else:
            logger_object.log(logfile, 'Entered data structure is not a list')
    except Exception as error:
        logger_object.log(logfile, 'Exception occurred in Clear function. Exception message :  ' + str(error))
        logger_object.log(logfile, 'Exited from the Clear function')
        logfile.close()


# Implementation of index() method of a list
def Index(lt,val):
    logfile = open(logFilepath, mode='a')
    logger_object.log(logfile, 'Entered in Index method')
    try:
        if Type(lt) == list:
            c = 0
            for i in lt:
                if i == val:
                    logger_object.log(logfile, 'Index Of Given Value In List : ' + str(c))
                    return c
                c += 1
            logger_object.log(logfile, 'Value Does Not Exist In Given List : ')
            return -1
        else:
            logger_object.log(logfile, 'Entered data structure is not a list')
    except Exception as error:
        logger_object.log(logfile, 'Exception occurred in Index function. Exception message :  ' + str(error))
        logger_object.log(logfile, 'Exited from the Index function')
        logfile.close()


# Implementation of count() method of a list
def Count(lt,val):
    logfile = open(logFilepath, mode='a')
    logger_object.log(logfile, 'Entered in Count method')
    try:
        if Type(lt) == list:
            c = 0
            for i in lt:
                if i == val:
                    c += 1
            logger_object.log(logfile, 'Number Of Times ' + str(val) + ' Appears In The List : ' + str(c))
            return c
        else:
            logger_object.log(logfile, 'Entered data structure is not a list')
    except Exception as error:
        logger_object.log(logfile, 'Exception occurred in Count function. Exception message :  ' + str(error))
        logger_object.log(logfile, 'Exited from the Count function')
        logfile.close()


# Implementation of reverse() method of a list
def Reverse(lt):
    logfile = open(logFilepath, mode='a')
    logger_object.log(logfile, 'Entered in Reverse method')
    try:
        if Type(lt) == list:
            new_lt = lt[::-1]
            logger_object.log(logfile, 'Reverse of A Given List : ' + str(new_lt))
            return new_lt
        else:
            logger_object.log(logfile, 'Entered data structure is not a list')
    except Exception as error:
        logger_object.log(logfile, 'Exception occurred in Reverse function. Exception message :  ' + str(error))
        logger_object.log(logfile, 'Exited from the Reverse function')
        logfile.close()


# Implementation of sort() method of a list
def Sort(lt):
    logfile = open(logFilepath, mode='a')
    logger_object.log(logfile, 'Entered in Sort method')
    try:
        if Type(lt) == list:
            new_lt = lt.sort()
            logger_object.log(logfile, 'Sorted Ordered Of A Given List : ' + str(new_lt))
            return new_lt
        else:
            logger_object.log(logfile, 'Entered data structure is not a list')
    except Exception as error:
        logger_object.log(logfile, 'Exception occurred in Sort function. Exception message :  ' + str(error))
        logger_object.log(logfile, 'Exited from the Sort function')
        logfile.close()

