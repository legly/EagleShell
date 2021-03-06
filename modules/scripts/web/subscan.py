#!/usr/bin/python3

from assets.headers import subscan_header
from assets.colors import *
from assets.prefixes import invalid_input_prefix, website_prefix, wordlist_prefix, eagleshell_prefix
from assets.shortcuts import Exit
from modules.scripts.web.web import Web
import os
import requests


class SubScan:
    def __init__(self):
        self.configuration()
        self.sub_scan()
        self.result()

    def configuration(self):
        try:
            subscan_header()
            print('Website:')
            print('\n\tExample: google.com')
            print('\n\tZ): Back')
            print('\tX): Exit\n')
            self.web_set = input(website_prefix).lower()
            if self.web_set == 'z':
                Web()
            elif self.web_set == 'x':
                Exit()
            subscan_header()
            print('Wordlist:')
            print('\n\tExample: /usr/share/wordlists/mylist.txt')
            print('\n\tZ): Back')
            print('\tX): Exit\n')
            self.sub_list_set = input(wordlist_prefix)
            if self.sub_list_set == 'z' or self.sub_list_set == 'Z':
                Web()
            elif self.sub_list_set == 'x' or self.sub_list_set == 'X':
                Exit()
        except KeyboardInterrupt:
            Exit()

    def sub_scan(self):
        try:
            subscan_header()
            print('Output:')
            print('\n\tControls')
            print('\t--------')
            print('\tStop: CTRL+C\n')
            self.total_found = 0
            domain = self.web_set
            file = open(self.sub_list_set)
            content = file.read()
            subdomains = content.splitlines()
            for subdomain in subdomains:
                url = f"http://" + subdomain + "." + domain
                try:
                    requests.get(url)
                except requests.exceptions.HTTPError:
                    pass
                else:
                    print(YELLOW + BOLD + '\t[+] ' + GREEN + BOLD + 'Discovered SubDomain ' + WHITE + BOLD + '>> ' + BLUE + BOLD + str(url))
                    self.total_found = self.total_found + 1
        except UnicodeError:
            print(RED + '[+] Wordlist Size Too Big..' + WHITE)
            os.system('sleep 2')
            Exit()
        except KeyboardInterrupt:
            self.result()

    def result(self):
        try:
            subscan_header()
            print('Result:')
            print('\n\tInput')
            print('\t-----')
            if self.total_found < 1:
                print('\tWEBSITE: ' + RED + BOLD + self.web_set + WHITE)
            else:
                print('\tWEBSITE: ' + GREEN + BOLD + self.web_set + WHITE)
            if self.total_found < 1:
                print('\tWORDLIST: ' + RED + BOLD + self.sub_list_set + WHITE)
            else:
                print('\tWORDLIST: ' + GREEN + BOLD + self.sub_list_set + WHITE)
            print('\n\tOutput')
            print('\t------')
            if self.total_found < 1:
                print('\tSUBDOMAINS FOUND: ' + RED + BOLD + '0' + WHITE)
            else:
                print('\tSUBDOMAINS FOUND: ' + GREEN + BOLD + str(self.total_found) + WHITE)
            print('\n\tY): New')
            print('\tZ): Menu')
            print('\tX): Exit\n')
            while True:
                cmd = input(eagleshell_prefix).lower()
                if cmd == 'y':
                    SubScan()
                elif cmd == 'z':
                    Web()
                elif cmd == 'x':
                    Exit()
                else:
                    print(invalid_input_prefix)
                    continue
        except KeyboardInterrupt:
            Exit()
