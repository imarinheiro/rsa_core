# coding: utf-8
import argparse
import os


def type_dir_path(path):
    if os.path.isdir(path):
        return path
    else:
        raise argparse.ArgumentTypeError("{}: não é um local válido".format(path))


def type_message(text):
    if type(text) is str:
        if text.isdigit():
            return int(text)
        elif text.isalpha() and len(text) == 1:
            return text
        else:
            raise argparse.ArgumentTypeError(
                "{}: não é válido [deve possuir um caractere ou um número inteiro]".format(text))
    else:
        raise argparse.ArgumentTypeError("{}: não é uma texto válido".format(text))
