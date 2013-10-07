mport logging
import psutil
import random
import logging.config
import sys

logging.config.fileConfig('./logging.conf')
logger = logging.getLogger('monkey')

exclusionList = ['cron']

def main():
    procs = psutil.get_pid_list()
    guess = random.randint(0,len(procs)-1)
    try:
        proc = psutil.Process(procs[guess])
    except Exception as e:
        logger.error("Process with ID %d died while I was trying to mess with it. Error: %s", procs[guess], e)
        exit()
    for exclusion in exclusionList:
        if not exclusion in proc.name.lower():
            logger.info("About to kill process with id: %d, and the name %s", procs[guess], proc.name)
            proc.kill()

if __name__ == '__main__':
    main()
