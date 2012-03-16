#!/usr/bin/env python
from argh import *

from itertools import combinations_with_replacement
import sys
import pickle
import csv

from StringIO import StringIO

from collections import namedtuple

UserSpec = namedtuple('UserSpec', ['sep', 'name', 'phone', 'line'])

PHONE = '7940'

def format_sep(mac):
    mac_str = ''.join(['%02X' % b for b in mac])
    sep = 'SEP%s' % mac_str
    return sep

def mac_gen():
    for c in combinations_with_replacement(range(255), 3):
        yield [0x00, 0x00, 0x00] + list(c)


def user_gen():
    i = 1
    while True:
        yield 'User %d' % i
        i += 1

def line_gen():
    l = 1001
    while True:
        yield '%s' % l
        l += 1


@arg('count', type=int)
@arg('--format', default='pickle')
def generate(args):
    users = [UserSpec(format_sep(mac), user, PHONE, line)._asdict() for i, mac, user, line in zip(range(args.count), mac_gen(), user_gen(), line_gen())]
    sys.stdout.write(dump_format(users, args.format))

@arg('--format', default='pickle')
def transform(args):
    reader = csv.reader(sys.stdin)
    users = [UserSpec(*row)._asdict() for row in reader]
    sys.stdout.write(dump_format(users, args.format))

def dump_format(users, format):
    if format == 'pickle':
        data = pickle.dumps({'users': users})
    else:
        buf = StringIO()
        writer = csv.writer(buf)
        writer.writerows([user.values() for user in users])
        data = buf.getvalue()
    return data
    
def main():
    p = ArghParser()
    p.add_commands([generate, transform])
    p.dispatch()
    device = sys.argv[1]


#-------------------------------------------------------------------------------
if __name__ == "__main__":
    main()
