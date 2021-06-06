#!/usr/bin/env python


import os.path, time, argparse


import Krakatau
from Krakatau.assembler import parse
from Krakatau import script_util

def assembleSource(source, basename, fatal=False):
    source = source.replace('\t', '  ') + '\n'
    return list(parse.assemble(source, basename, fatal=fatal))

def assembleClass(filename):
    basename = os.path.basename(filename)
    with open(filename, 'rU') as f:
        source = f.read()
    return assembleSource(source, basename)

def main(args):
    log = script_util.Logger('warning' if args.q else 'info')
    log.info(script_util.copyright)

    out = script_util.makeWriter(args.out, '.class')
    targets = script_util.findFiles(args.target, args.r, '.j')

    start_time = time.time()
    with out:
        for i, target in enumerate(targets):
            log.info('Processing file {}, {}/{} remaining'.format(target, len(targets)-i, len(targets)))

            pairs = assembleClass(target)
            for name, data in pairs:
                filename = out.write(name, data)
                log.info('Class written to', filename)
    print('Total time', time.time() - start_time)

def set_parser_opts(parser):
    parser.add_argument('-out', help='Path to generate files in')
    parser.add_argument('-r', action='store_true', help="Process all files in the directory target and subdirectories")
    parser.add_argument('-q', action='store_true', help="Only display warnings and errors")
    parser.add_argument('target', help='Name of file to assemble')

if __name__== "__main__":
    parser = argparse.ArgumentParser(description='Krakatau bytecode assembler')
    set_parser_opts(parser)
    main(parser.parse_args())
