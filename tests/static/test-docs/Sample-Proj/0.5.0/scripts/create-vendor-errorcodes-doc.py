#!/usr/bin/env python3
import os
import json
import argparse

settings = []

def createparamlist(injson, outfile):
    print('Using "{}" to create "{}"'.format(injson, outfile))

    with open(injson) as fp:
        data = json.load(fp)

    ocppcodes = []
    vendorcodes = []

    for item in data:
        code = item['code']
        nonfaulty = item['nonfaulty']
        summary = item['summary']

        vendorerrorcode = ''
        try:
            vendorerrorcode = item['vendorerrorcode']
        except KeyError:
            pass
        if not vendorerrorcode:
            d = {'code': code,
                 'nonfaulty': nonfaulty,
                 'summary': summary}
            ocppcodes.append(d)
        else:
            d = {'code': code,
                 'nonfaulty': nonfaulty,
                 'summary': summary,
                 'vendorerrorcode': vendorerrorcode}
            vendorcodes.append(d)

    lines = []
    print('OCPP standard error codes')
    lines.append('\pagebreak')
    lines.append('\section{{{}}}\n'.format('OCPP standard error codes'))
    lines.append('\\begin{description}\n')
    for item in sorted(ocppcodes, key=lambda item: item['code']):
        code = item['code']
        summary = item['summary']
        nonfaulty = item['nonfaulty']
        line = '\item[{}] {}'.format(code, summary)
        if nonfaulty:
            line += '\\\\This can also be sent together with a non-error status.'
        lines.append(line)
    lines.append('\\end{description}\n')

    print('CTEK E-Mobility AB specific error codes')
    lines.append('\pagebreak')
    lines.append('\section{{{}}}\n'.format('CTEK E-Mobility AB specific error codes'))
    lines.append('\\begin{description}\n')
    for item in sorted(vendorcodes, key=lambda item: item['vendorerrorcode']):
        code = item['code']
        summary = item['summary']
        nonfaulty = item['nonfaulty']
        vendorerrorcode = item['vendorerrorcode']
        if '_' in vendorerrorcode:
            vendorerrorcode = vendorerrorcode.replace('_', '\\_')
        line='\item[{}] {}'.format(vendorerrorcode, summary)
        if nonfaulty:
            line += '\\\\This can also be sent together with a non-error status.'
        lines.append(line)
    lines.append('\\end{description}\n')

    lines.append('\end{document}')
    for line in lines:
        print(line)

    with open(outfile, mode='w') as fp:
        fp.writelines([f'{line}\n' for line in lines])


def main():


    parser = argparse.ArgumentParser()
    parser.add_argument("--cfg", dest="cfg", required=True, help="Path to configuration errorcodes.json")
    parser.add_argument("--out", dest="dest",  required=True, help="Path to configuration ccu-docs/ccu-errorcodes.tex")
    args = parser.parse_args()

    createparamlist(args.cfg, args.dest)


if __name__ == "__main__":
    main()