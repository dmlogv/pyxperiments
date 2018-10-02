"""Logging module usage"""
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s:%(name)s:%(levelname)s:%(message)s')
                    
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')
