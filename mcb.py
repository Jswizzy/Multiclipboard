#! /usr/bin/env python3
# mcb.py allows for stories and copying multiple items to the clipboard

import pyperclip
import shelve
import sys
import pprint


def do_command(command, key):
    if command == 'save':
        mcbShelf[k] = pyperclip.paste()
    if command == 'del':
        del mcbShelf[key]


def do_lookup(key):
    if key == 'list':
        pprint.pprint(str(list(mcbShelf.keys())))
    elif key in mcbShelf:
        pyperclip.copy(mcbShelf[key])

mcbShelf = shelve.open('mcb')

ln = len(sys.argv)

if ln == 3:
    cmd = sys.argv[1]
    k = sys.argv[2]

    do_command(cmd, k)
elif ln == 2:
    k = sys.argv[1].lower()
    do_lookup(k)

mcbShelf.close()



