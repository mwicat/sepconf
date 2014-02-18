#!/usr/bin/env python

import csv
import os
import sys

from itertools import (combinations_with_replacement,
                       count, izip, islice, chain)

import sepconf
print sepconf.__file__

from jinja2 import Template
from argh import ArghParser, arg

COLUMNS = ['sep', 'name', 'phone', 'line']


def format_sep(mac):
    return 'SEP%s' % ''.join(['%02X' % b for b in mac])


def render_users(template, users):
    fn = template if os.path.exists(template) else sepconf.get_data('templates/' + template)
    f = open(fn)
    s = Template(f.read()).render(users=users)
    sys.stdout.write(s)


@arg('n', type=int)
@arg('--phone', default=7940)
@arg('--render')
def generate(args):
    mac_gen = ([0x00, 0x00, 0x00] + list(c)
               for c in combinations_with_replacement(range(255), 3))
    sep_gen = (format_sep(mac) for mac in mac_gen)
    user_gen = ('User %d' % i for i in count(1))
    line_gen = (str(i) for i in count(1001))

    users = ({'sep': sep,
              'name': user,
              'phone': args.phone,
              'line': line}
             for sep, user, line
             in izip(sep_gen, user_gen, line_gen))
    users = islice(users, args.n)

    if args.render:
        render_users(args.render, users)
    else:
        writer = csv.DictWriter(sys.stdout, COLUMNS)
        writer.writerows(users)


@arg('template')
def render(args):
    users = csv.DictReader(sys.stdin, COLUMNS)
    render_users(args.template, users)


def main():
    p = ArghParser()
    p.add_commands([generate, render])
    p.dispatch()


if __name__ == "__main__":
    main()
