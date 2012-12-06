=========================================
Doctests para CepBr
=========================================

O módulo CepBR foi criado para prover fácil acesso as informações de CEP do Brasil.

Vamos verificar se está tudo funcionando::
    
    >>> from cep import CEP

Após importar o módulo, podemos realizar os primeiros testes::

    >>> c = CEP()
    >>> pirineus = c.get_cep('01201040')
    >>> pirineus
    {'bairro': u'Campos El\xedseos', 'cidade': u'S\xe3o Paulo', 'uf': u'SP', 'logradouro': u'Rua Pirineus', 'cep': u'01201040'}

A coleta está correta, mas e se eu passar um campo vazio? ::

    >>> vazio = c.get_cep('')
    Traceback (most recent call last):
    ...
    ValueError: É necessário importar um CEP.
