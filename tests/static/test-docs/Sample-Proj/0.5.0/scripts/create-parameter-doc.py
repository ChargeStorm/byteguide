#!/usr/bin/env python3
import os
import json
import argparse


settings = []


def createparamlist(injson, outfile):
    print('Using "{}" to create "{}"'.format(injson, outfile))

    with open(injson) as fp:
        data = json.load(fp)

    lines = []
    for section in data:
        print(section['label'])
        lines.append('\pagebreak')
        lines.append('\section{{{}}}\n'.format(section['label']))
        lines.append('\n\\begin{description}\n')

        for item in section['params']:
            try:
                hidden = item['hidden']
                if hidden is True:
                    continue
            except KeyError:
                pass
            try:
                source = item['source']
            except KeyError:
                    source = ''

            ini = item['ini']
            if ini.startswith('ocpp/'):
                ini = ini[5:]
            if source == 'platform.ini':
                ini = 'platform/' + ini
            try:
                ocppname = item['ocppname']
                ini = ocppname
            except KeyError:
                pass
            ini = ini.replace('_', r'\_')
            summary = item['summary']
            if not summary:
                summary = 'Add summary'
            lines.append('\item[{}] {}\\\\\n'.format(ini, summary))
            try:
                default = item['default']
                lines.append('  Default value: {}\\\\\n'.format(default))
            except KeyError:
                pass
            try:
                range = item['range']
                lines.append('  Value range: {}\\\\\n'.format(range))
            except KeyError:
                pass
            try:
                type = item['type']
                lines.append('  Type: {}\\\\\n'.format(type))
            except KeyError:
                lines.append('  Type: ADD TYPE INFO\\\\\n')
            try:
                ro = item['readonly']
                if isinstance(ro, bool) and ro == True:
                    lines.append('  Readonly: Yes\\\\\n')
            except KeyError:
                try:
                    runtime = item['runtime']
                    if runtime == 'yes' or runtime == 'custom':
                        runtime_change = 'No'
                except KeyError:
                    runtime_change = 'Yes'
                lines.append('  Reset required after change: {}\\\\\n'.format(runtime_change))
            try:
                comment = item['comment']
                lines.append('  {}\\\\\n'.format(comment))
            except KeyError:
                pass
            try:
                license = item['license']
                if isinstance(license, bool):
                    lines.append('  \emph{License: extra license option is required!}\\\\\n')
                else:
                    lines.append('  \emph{{License: {}}}\\\\\n'.format(license))
            except KeyError:
                pass

            try:
                deprecated = item['deprecated']
                lines.append('  Deprecated: {}\\\\\n'.format(deprecated))
            except KeyError:
                pass
            try:
                conflictingParameters = item['conflicting']
                lines.append('  Conflicting parameters: {}\\\\\n'.format(conflictingParameters))
            except KeyError:
                pass

            lines.append('\n')
        lines.append('\end{description}\n')
    with open(outfile, mode='w') as fp:
        fp.writelines(lines)


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("--cfg", dest="cfg", required=True, help="Path to configuration cfg.json")
    parser.add_argument("--out", dest="dest",  required=True, help="Path to configuration cfg.json")
    args = parser.parse_args()

    createparamlist(args.cfg, args.dest)


if __name__ == "__main__":
    main()