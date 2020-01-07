import os
import sys
import logging
import argparse
import trainer.core as t_core

log = logging.getLogger(__name__)

def main(argv):
    pars = makeArgParse()
    opts = pars.parse_args(argv)

    print(opts)

    return 0

def _main():
    pass

def makeArgParse():
    pars = argparse.ArgumentParser(prog='trainer')
    pars.add_argument('directory', help='Directory to play from')


    return pars

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))


