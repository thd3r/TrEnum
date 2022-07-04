# TrEnum - Enumerate subdomains & Fetches all url paths


![Build](https://img.shields.io/badge/Built%20with-Python-Blue)
![License](https://img.shields.io/github/license/thd3rBoy/TrEnum.svg)


**TrEnum** is a python tool designed to enumerate subdomains of websites and fetches all url paths. This helps penetration testers and bug hunters to collect subdomains or retrieve all url paths for their targeted domains.

**TrEnum** is being actively developed by [@thd3rBoy](https://twitter.com/thd3rBoy)


Table of Contents
------------
* [Installation](#installation)
* [Dependencies](#dependencies)
* [Options](#options)
* [Usage](#usage)
* [License](#license)


Installation
------------

**Requirement: python 3.7 or higher**

```
https://github.com/thd3rBoy/TrEnum.git
```

Dependencies
------------

**Dependencies can be installed using the requirements file:**
  - Installation on Windows:
  ```
  c:\python27\python.exe -m pip install -r requirements.txt
  ```

  - Installation on Linux
  ```
  sudo pip install -r requirements.txt
  ```
          
Options
-------

```

 _____    _____                      
|_   _|  |  ___|                     
  | |_ __| |__ _ __  _   _ _ __ ___  
  | | '__|  __| '_ \| | | | '_ ` _ \ 
  | | |  | |__| | | | |_| | | | | | |
  \_/_|  \____/_| |_|\__,_|_| |_| |_|

                        @thd3rBoy


usage: TrEnum.py [ -m options mode [default arguments] ] [ -d domain [default arguments] ] [ arguments ]

Options:
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit
  -m MODE, --options-mode MODE
                        Mode options can be set by choice (ex: subs, norx)
  -d DOMAIN, --domain DOMAIN
                        Domain name to enumerate
  -o OUTPUT, --output OUTPUT
                        file to write output results
  -s, --silent          Silent mode, Only print the result and ignore the error
  --no-subs             Use this to exclude subdomains in searches. This only applies to the norx mode option

See github.com/thd3rBoy/TrEnum for more info
```

Usage
-----

**Summary:**
  - `--options-mode` Mode options can be set by choice (subs, norx). This is the default argument
  - `--domain` Domain name to enumerate. This is the default argument
  - `--silent` Silent mode, Only print the result and ignore the error
  - `--no-subs` argument This only applies to the norx mode option
  - `--output` **TrEnum** will automatically save the result to a file if the --output argument is not used
  
**Example for subs option**

    Using only --domain arguments:
    
         python TrEnum.py -m subs -d example.com
         
    Use the --silent argument to print the result and ignore errors:
    
        python TrEnum.py -m subs -d example.com --silent
        
    Use --output to save the result to a file:
        
        python TrEnum.py -m subs -d example.com -o filename
        
    TrEnum will automatically save the result to a file if the --output argument is not used
    
    
**Example for norx option**
    
    Using only --domain arguments:
    
         python TrEnum.py -m norx -d example.com
         
    Use --no-subs to exclude subdomains in search:
    
         python TrEnum.py -m norx -d example.com --no-subs
         
    Use the --silent argument to print the result and ignore errors:
    
        python TrEnum.py -m norx -d example.com --silent
        
    Use --output to save the result to a file:
        
        python TrEnum.py -m norx -d example.com -o filename
        
    TrEnum will automatically save the result to a file if the --output argument is not used
    

License
---------------
Copyright (C) Thunder (thd3rBoy@github.io)

License: GNU General Public License, version 2
                                                                                    
