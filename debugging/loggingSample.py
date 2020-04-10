import logging
#logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# log to file
logging.basicConfig(filename='debugLogging.txt',level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')



# Disable logging ( CRITICAL IS THE HIGHEST LEVEL )
# logging.DEBUG,INFO,WARNING,ERROR,CRITICAL
# logging.disable(logging.CRITICAL)

# logging.debug()
# logging.info()
# logging.warning()
# logging.error()
# logging.critical()


logging.debug('Start of Program')

def factorial(n):
    logging.debug('Start of factorial (%s)' % (n))
    total = 1
    for i in range(1,n + 1):
        total *= i
        logging.critical('i is %s,total is %s' % (i,total))
    logging.debug('Return value is %s' % (total))
    return total


print(factorial(5))

logging.debug('End of Program')
