# coding: utf-8
# !/usr/bin/env python
import argparse
import json

from rsa.report import set_context_key
from rsa.types import type_dir_path
from rsa.validators import is_prime


def main():
    parser = argparse.ArgumentParser(description='Algoritmo de criptografia RSA simplificado - Gerador de Chaves')
    parser.add_argument('-k', action='store', dest='key', required=True,
                        help='Deve possuir dois primos', type=int, nargs='+')
    parser.add_argument('-p', action='store', dest='path',
                        help='Local para salvar o relatório', type=type_dir_path)
    args = parser.parse_args()
    if args.path:
        args.path = str(args.path)
    else:
        args.path = ''
    is_prime(args.key[0])
    is_prime(args.key[1])
    with open(args.path + 'report.json', 'w') as outfile:
        json.dump(set_context_key(args.key[0], args.key[1]), outfile, indent=4)


if __name__ == '__main__':
    main()
