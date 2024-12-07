#
import os

__app_name__ = "fims"
__version__ = "0.1.0"
TITLE = "File Integrity Monitoring System"

monitor = [
    {
        'path':'C:\\Users\\kushc\\Desktop\\projects\\py35.dev\\lecture-07\\monitoring', 'recursive':True
    }
]

DATABASE_PATH = os.path.dirname(os.path.realpath(__file__))
DATABASE_NAME = "shelve.db"
DATABASE = f"{DATABASE_PATH}/{DATABASE_NAME}"