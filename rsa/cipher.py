# coding: utf-8
# !/usr/bin/env python
import argparse
import json

from rsa.report import set_context_encrypt_string, set_context_encrypt_number
from rsa.types import type_message, type_dir_path
from rsa.validators import message_length


def main():
    parser = argparse.ArgumentParser(description='Algoritmo de criptografia RSA simplificado')
    parser.add_argument('-k', action='store', dest='key', required=True,
                        help='Deve possuir a chave pública', type=int, nargs='+')
    parser.add_argument('-t', action='store', dest='text', required=True,
                        help='Texto para ser criptografado', type=type_message)
    parser.add_argument('-p', action='store', dest='path',
                        help='Local para salvar o relatório', type=type_dir_path)
    parser.add_argument('--is-number', dest='type', action='store_true', help='Tipo da criptografia é para números')
    parser.add_argument('--is-text', dest='type', action='store_false', help='Tipo da Criptografia é para textos')
    parser.set_defaults(type=True)
    args = parser.parse_args()
    if args.path:
        args.path = str(args.path)
    else:
        args.path = ''
    message_length(args.text)
    with open(args.path + 'report.json', 'w') as outfile:
        if args.type:
            json.dump(set_context_encrypt_number(args.text, args.key[0], args.key[1]), outfile, indent=4)
        else:
            json.dump(set_context_encrypt_string(args.text, args.key[0], args.key[1]), outfile, indent=4)


if __name__ == '__main__':
    main()
