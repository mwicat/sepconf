from argh import *


from itertools import combinations_with_replacement
import sys
import pickle


from collections import namedtuple

UserSpec = namedtuple('UserSpec', ['sep', 'name', 'phone', 'line'])

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
def generate_macs(args):
    macs = mac_gen()
    phone = '7640'
    users = [UserSpec(format_sep(mac), user, phone, line)._asdict() for i, mac, user, line in zip(range(args.count), mac_gen(), user_gen(), line_gen())]
    config = {'users': users}
    pickle.dump(config, sys.stdout)


def main():
    p = ArghParser()
    p.add_commands([generate_macs])
    p.dispatch()
    device = sys.argv[1]


#-------------------------------------------------------------------------------
if __name__ == "__main__":
    main()
