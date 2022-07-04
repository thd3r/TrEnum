#!/usr/bin/env python3

from datetime import datetime
import os

class bcolors:
    PURPLE = '\033[95m'
    OKBLUE = '\033[94m'
    BLUE = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def write_file(filename, content):
    try:
        if filename:
            filename = f"{filename.replace('.', '_')}-{str(datetime.now().strftime('%Y-%m-%d-%H:%M:%S'))}.txt"
        if '.' not in filename:
            filename = f"{filename}-{str(datetime.now().strftime('%Y-%m-%d-%H:%M:%S'))}"
        else:
            filename = filename
        print(f"{bcolors.BOLD}[{bcolors.GREEN}Info{bcolors.END}{bcolors.BOLD}]: Saving results to file %s{bcolors.END}" % str(filename))
        with open(str(filename), "wt") as f:
            for subdomains in content:
                f.write(subdomains + os.linesep)
    except:
        print(f"{bcolors.BOLD}[{bcolors.FAIL}Error{bcolors.END}{bcolors.BOLD}]: Cannot save result to file: %s{bcolors.END}" % str(filename))
