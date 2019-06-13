import logging
import inspect

def CustomLogger(logLevel=logging.DEBUG):
    # Get the name of the class / method from where this method is called
    loggerName = inspect.stack()[1][3]
    logger  = logging.getLogger(loggerName)
    # by Default logs all the message
    logger.setLevel(logging.DEBUG)


    fileHandler =  logging.FileHandler("automation.log", mode='a')
    fileHandler.setLevel(logLevel)

    formatter =  logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s',
                                   datefmt='%m/%d/%Y %I:%M:%S %p')

    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)
    return logger






