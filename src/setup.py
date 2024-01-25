import sys
import os
from cx_Freeze import setup, Executable

# ADD FILES
files = {"packages": ['sys', 'os', 'sqlite3', 'cx_Freeze', 'httplib2'],
         "include_files": ['1.jpg', '2.jpg', 'icon.ico', 'gui', 'plumbing.db', 'qt_core.py', 'Google.py', 'settings.json', 'token_drive_v3.pickle', 'client_secret.json', 'fabData.json']}

# TARGET
target = Executable(
    script="main.py",
    base="Win32GUI",
    icon="icon.ico"
)

# SETUP CX FREEZE
setup(
    name = "3azmy",
    version = "1.0.0",
    description = "the first shot to make a system",
    author = "M & A",
    options = {'build_exe' : files},
    executables = [target]
)