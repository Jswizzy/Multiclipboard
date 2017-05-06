#! /usr/bin/env python3
# mcb.py allows for copying multiple items to the clipboard

import pyperclip
import shelve
import sys
import pprint

HELP = "Usage: 'key' | save 'key' | del 'key' | read 'key' | list | help"
NO_SUCH_KEY = "key not found: use save 'key' first to save clipboard to key"


def do_command(command, key):
    if command == 'save':
        mcbShelf[k] = pyperclip.paste()
    elif command == 'del':
        del mcbShelf[key]
    elif command == 'read':
        print(mcbShelf[key])
    else:
        print(HELP)


def do_lookup(key):
    if key == 'list':
        pprint.pprint(str(list(mcbShelf.keys())))
    elif key in mcbShelf:
        pyperclip.copy(mcbShelf[key])
    else:
        print(NO_SUCH_KEY)

mcbShelf = shelve.open('mcb')

ln = len(sys.argv)

if ln == 3:
    cmd = sys.argv[1]
    k = sys.argv[2]

    do_command(cmd, k)
elif ln == 2:
    k = sys.argv[1].lower()
    do_lookup(k)
else:
    print(HELP)

mcbShelf.close()



