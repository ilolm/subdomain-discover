#!/usr/bin/env python3

import requests, optparse


def get_options():
    parser = optparse.OptionParser()

    parser.add_option("-d", "--domain", dest="domain", help="Specify a domain which you wish to discover subdomains on.")
    parser.add_option("-w", "--wordlist", dest="wordlist", help="Specify a wordlist path.")

    options = parser.parse_args()[0]

    if not options.domain:
        print("\033[91m[-] Please specify a domain. --help for more info.")
    elif not options.wordlist:
        print("\033[91m[-] Please specify a wordlist. --help for more info.")
    return options

def request(url):
    try:
        return requests.get("http://" + url)
    except requests.exceptions.ConnectionError:
        pass


options = get_options()

main_domain = options.domain
wordlist_path = options.wordlist

with open(wordlist_path, "r",) as wordlist_file:
    for line in wordlist_file:
        word = line.strip()
        test_url = word + "." + main_domain

        response = request(test_url)

        if response:
            print("[+] Discovered subdomain --> " + test_url)
