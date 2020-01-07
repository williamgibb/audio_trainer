import os
import sys
import logging
import argparse
import trainer.core as t_core

from pprint import pprint

log = logging.getLogger(__name__)

def main(argv):
    pars = makeArgParse()
    opts = pars.parse_args(argv)

    logging.basicConfig(level=logging.DEBUG)

    print(opts)

    proc = t_core.AudioCore(dirn=opts.directory)

    print(len(proc.samples))
    pprint(proc.samples)

    proc.run()

    return 0

def _main():
    pass

def makeArgParse():
    pars = argparse.ArgumentParser(prog='trainer')
    pars.add_argument('directory', help='Directory to play from')

    return pars

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
