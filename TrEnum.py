#!/usr/bin/env python3

import multiprocessing
import argparse
import os
import sys

from colorama import Fore
from urllib.parse import urlparse
from datetime import datetime

from lib.core.providers.threatcrowd import ThreatcrowdEnums
from lib.core.providers.virustotal import VirustotalEnums
from lib.core.providers.crtsh import CrtshSearch
from lib.core.providers.whoisxmlapi import Whoisxmlapi
from lib.core.providers.urlscan import Urlscan
from lib.core.providers.wayback import BaseEnumerateUrls
from lib.core.output import write_file
from lib.core.options import OptionsArgs

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

if not os.path.exists("lib/core/config/apikey.json"):
    print(f"{bcolors.BOLD}[{bcolors.FAIL}Error{bcolors.END}{bcolors.BOLD}]: The config file for apikey.json is not in the specified path{bcolors.END}")
    sys.exit(1)

def print_banner():
    banner = """{}{}
 _____    _____                      
|_   _|  |  ___|                     
  | |_ __| |__ _ __  _   _ _ __ ___  
  | | '__|  __| '_ \| | | | '_ ` _ \ 
  | | |  | |__| | | | |_| | | | | | |
  \_/_|  \____/_| |_|\__,_|_| |_| |_|

                        {}{}@thd3rBoy

{}""".format(bcolors.BOLD, bcolors.OKBLUE, bcolors.END, bcolors.WARNING, bcolors.END)

    print(banner)

class EnumerateSUbs(multiprocessing.Process):

    def __init__(self, subdomains=None):
        multiprocessing.Process.__init__(self)
        self.subdomains = subdomains
        self.optionsArgs = OptionsArgs()
        self.default_mode = [
            "subs", "norx"
        ]

        return

    def fetchURls(self, domain, filename, no_subs, silent):
        waybacks = BaseEnumerateUrls(domain, filename, no_subs, silent)
        waybacks.run()

    def SubsEnums(self, domain, filename, silent):
        engines = [VirustotalEnums, Whoisxmlapi, CrtshSearch, Urlscan, ThreatcrowdEnums]
        enums = [enum(domain, silent) for enum in engines]

        for enum in enums:
            domain_list = enum.enumerate()
            # remove subdomains duplicate from list
            res = [subs for i, subs in enumerate(domain_list) if subs not in domain_list[:i]]
            for subdomain in res:
                self.subdomains.append(subdomain)

        if not filename:
            write_file(filename=domain, content=self.subdomains)
        else:
            write_file(filename=filename, content=self.subdomains)
        
    def run(self):
        print_banner()
        args = self.optionsArgs._options()
        mode = args.mode
        domain = args.domain
        output = args.output
        silent = args.silent
        no_subs = args.no_subs

        try:
            if domain.startswith("http://") or domain.startswith("https://"):
                domain = urlparse(domain).netloc

            if mode.lower() not in self.default_mode:
                print(f"{bcolors.BOLD}[{bcolors.FAIL}Error{bcolors.END}{bcolors.BOLD}]: The mode option you entered does not match the available options{bcolors.END}")
                sys.exit(1)

            if mode.lower() == self.default_mode[0]:
                print(f"{bcolors.BOLD}[{bcolors.GREEN}Info{bcolors.END}{bcolors.BOLD}]: Enumerating subdomains now for {domain}{bcolors.END}")
                self.SubsEnums(domain, output, silent)
            
            if mode.lower() == self.default_mode[1]:
                print(f"{bcolors.BOLD}[{bcolors.GREEN}Info{bcolors.END}{bcolors.BOLD}]: Searching now on available engines for {domain}{bcolors.END}")
                self.fetchURls(domain, output, no_subs, silent)

        except Exception:
            print(f"{bcolors.BOLD}[{bcolors.FAIL}Error{bcolors.END}{bcolors.BOLD}]: Use {sys.argv[0]} --help for more information{bcolors.END}")
            sys.exit()

    
if __name__ == '__main__':
    subdomains_queue = multiprocessing.Manager().list()

    enumerates = [EnumerateSUbs]
    enums = [enum(subdomains_queue) for enum in enumerates]
    for enum in enums:
        enum.start()
    for enum in enums:
        enum.join()

    for subs in subdomains_queue:
        print(subs)