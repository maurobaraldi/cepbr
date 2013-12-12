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
    {u'bairro': u'Campos El\xedseos', u'uf': u'SP', u'logradouro': u'Rua Pirineus', u'localidade': u'S\xe3o Paulo', u'cep': u'01201040'}

A coleta está correta, mas e se eu passar um campo vazio? ::

    >>> vazio = c.get_cep('')
    Traceback (most recent call last):
    ...
    ValueError: É necessário informar um CEP.
