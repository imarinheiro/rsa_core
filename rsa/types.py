# coding: utf-8
import argparse
import os


def type_dir_path(path):
    """
    Veerifica se o diretório existe. Caso não exista uma exception é lançada.

    :param path: string representando um diretório
    :return: diretório válido
    """
    if os.path.isdir(path):
        return path
    else:
        raise argparse.ArgumentTypeError("{}: não é um local válido".format(path))


def type_message(text):
    """
    Verifica o tipo do texto Alfa ou Númerico e realiza a transformação.
    Caso não seja um tipo válido é lançada uma exceção.

    :param text: string
    :return: mensagem transformada (type<int> ou type<str>)
    """
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
