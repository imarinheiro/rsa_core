# RSA Core #

[Documentação](https://rsa-core.readthedocs.io/en/latest/)

***


## Instalação ##

* ``` $ pip install -r requirements.txt ```
* ``` $ python setup.py sdist ```
* ``` $ pip install -e  rsa_core/ ```

***


## Testes ##

* ``` $ tests ```

***


## CLI ##

### Geração de Chaves (Pública e Privada), Criptografia e Descriptografia com Chave ###

* ``` $ keygen ```
    * ```-k``` (número) (número)
    * ```-p``` (opcional: caminho para salvar o relatório)
* ``` $ cipher ```
    * ```-k``` (número) (número)
    * ```-t``` (mensagem)
    * ```--is-number``` ou ```--is-text``` (default --is-number) (tipo da criptografia)
    * ```-p``` (opcional: caminho para salvar o relatório)
* ``` $ decipher```
    * ```-k``` (número) (número)
    * ```-t``` (mensagem criptografada) 
    * ```--is-number``` ou ```--is-text``` (default --is-number)  (tipo da criptografia)
    * ```-p``` (opcional: caminho para salvar o relatório)

### Criptografia e Descriptografia sem Chave ###

* ``` $ encryptor ```
    * ```-k``` (número primo) (número primo)
    * ```-t``` (mensagem)
    * ```--is-number``` ou ```--is-text``` (default --is-number) (tipo da criptografia)
    * ```-p``` (opcional: caminho para salvar o relatório)
* ``` $ decryptor ```
    * ```-k``` (número primo) (número primo)
    * ```-t``` (mensagem)
    * ```--is-number``` ou ```--is-text``` (default --is-number)  (tipo da criptografia)
    * ```-p``` (opcional: caminho para salvar o relatório)

***
