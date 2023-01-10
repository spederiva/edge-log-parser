Parser Log to CSV
===========

This script helps to parse and save the file as .CSV

Installation
-------------

### Prerequisites
Make sure you have installed python in the computer. In order to check which version is installed following the next steps

```
1. Open a terminal/cmd window
2. python --version
```

The python version should be a 3.x version or higher

In case it's not installed click on the next links:
* Windows: https://www.python.org/downloads/release/python-3111/
* Mac: https://docs.python-guide.org/starting/install3/osx/


### Create v-environment and install dependencies
After Python is installed and working well, need to follow the next steps in order to setup the environment

```
Into the project folder run the following commands

$ python -m venv venv
$ source ./venv/bin/activate
$ pip install -r requirements.txt
```

Parse a log file
-------------
Use the following instructions:

```
python ./log_parser.py --file log-filename.txt --output output-file.csv
```

For more information: 
```
python ./log_parser.py --help
```