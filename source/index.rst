.. RSA CORE documentation master file, created by
sphinx-quickstart on Mon Mar  9 13:51:04 2020.
You can adapt this file completely to your liking, but it should at least
contain the root `toctree` directive.

Documentação S_AES
==================

.. toctree::
   functions/functions


Algoritmo
---------

Implementação em Python de um algoritmo RSA simplificado que segue o design estrutural do saeslib desenvolvido pela Larissa Lopes

`Repositório do projeto <https://github.com/imarinheiro/rsacorelib>`_

`Exemplo de uso <https://github.com/lopeslarissa/S-AES-Web>`_



Instalação
----------

* ``$ pip install -r requirements.txt``
* ``$ python setup.py sdist``
* ``$ pip install -e  rsa/``



CLI
---

Criptografia
++++++++++++

* ``$ encrypt -k (chave) -t (texto)``
* ``$ encrypt -k (chave) -t (texto) -p (opcional: caminho para salvar o relatório)``


Descriptografia
+++++++++++++++

* ``$ decrypt -k (chave) -t (texto)``


Testes
++++++

* ``$ tests``
