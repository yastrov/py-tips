#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
"""

__author__ = 'Yuri Astrov <yuriastrov@gmail.com>'
__copyright__ = "Copyright 2014, The My Project"
__credits__ = ["Yuri Astrov", ]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Yuriy Astrov"
__email__ = "yuriastrov@gmail.com"
__status__ = "Production"

import os
import sys
import logging

ERROR_FORMAT = "%(levelname)s at %(asctime)s in %(funcName)s in %(filename) at line %(lineno)d: %(message)s"
DEBUG_FORMAT = "%(lineno)d in %(filename)s at %(asctime)s: %(message)s"
LOG_CONFIG = {'version':1,
              'formatters':{'error':{'format':ERROR_FORMAT},
                            'debug':{'format':DEBUG_FORMAT}},
                            'default': {
                                'format': '%(asctime)s %(levelname)s %(name)s %(message)s %(user)s'
                            },
              'handlers':{'console':{'class':'logging.StreamHandler',
                                     'formatter':'debug',
                                     'level':logging.DEBUG},
                          'file':{'class':'logging.FileHandler',
                                  'filename':'/usr/local/logs/DatabaseUpdate.log',
                                  'formatter':'error',
                                  'level':logging.ERROR,
                                  'mode': 'w',
                                  'encoding': 'utf-8',}
                        },
              'root':{'handlers':('console', 'file')}}
logging.config.dictConfig(LOG_CONFIG)

logger = logging.getLogger(__name__)
#fnname = os.path.join(os.getcwd(), 'debug.log')
#FORMAT = '%(asctime)-15s %(levelname)s - %(message)s %(user)s'
#logging.basicConfig(filename=fnname, 
#                    format=FORMAT,
#                    level=logging.DEBUG)

def main():
    try:
        # args = sys.argv[1:]
        import argparse # May use click http://click.pocoo.org/
        parser = argparse.ArgumentParser(description='Convert audiofiles with SoX.')
        parser.add_argument("path",
                            help="path with original sound files (required)")
        parser.add_argument("-b", "--bitrate",
                            default=32, help="bitrate (default: 64)")
        parser.add_argument("-v", "--verbose", action="store_true",
                            help="verbose output")
        parser.add_argument("--version", action='version',
                            version='%(prog)s {}'.format(__version__),
                            help="print version")
        args = parser.parse_args()
        
        if sys.platform.find('win') >= 0 and\
            sys.platform != 'darwin':
            # Windows here
            # args.append(os.getcwd())
            pass
        elif sys.platform is 'linux':
            # Linux
            pass
        else:
            pass
        if sys.stdout.isatty():
            # You're running in a real terminal
            # Use output format for user
            pass
        else:
            # You're being piped or redirected
            # Use output format for simple parsing with other utilitys
            pass
        # Example
        d = {'user': 'root'}
        logger.info(extra=d)
    except KeyboardInterrupt:
        print("Process stopped manually")
    except Exception as e:
        #traceback.print_exc()
        logger.exception(e)

if __name__ == "__main__":
    main()
