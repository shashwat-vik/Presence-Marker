import sys, os, logging

# Expand Python classes path
# Default will point in Apache24/bin
root = os.getcwd().replace("\\","/")
root = root.split('/Apache24/bin')[0]
import_path = os.path.abspath("{0}/seed/application".format(root))
if import_path not in sys.path:
    sys.path.insert(0, import_path)

'''
logging.basicConfig(filename='H:/X/seed/python_logs/info.log',level=logging.INFO)
logging.basicConfig(filename='H:/X/seed/python_logs/error.log',level=logging.ERROR)
logging.basicConfig(filename='H:/X/seed/python_logs/warning.log',level=logging.WARNING)
logging.basicConfig(filename='H:/X/seed/python_logs/debug.log', level=logging.DEBUG)
'''

from app import app

# Initialize WSGI app object
application = app
