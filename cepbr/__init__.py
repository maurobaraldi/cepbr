# -*- coding: utf-8 -*-

"""
CEP-BR
~~~~~

CEP-BR é uma biblioteca para consulta de CEP (Código de Endereçamento Postal) 
a partir do site dos correios do Brasil. Ela foi inspirada na postmon [1].

A CEP-BR utiliza uma url de consulta do site dos correios do Brasil. Não há 
garantia quanto a disponibilidade dessa url em tempo integral.
Para maiores informações sobre o acesso à base de CEP a partir da sua fonte,
procure no site dos Correios do Brasil [2].

[1] https://github.com/CodingForChange/postmon
[2] http://www.correios.com.br/

Método de uso:

   >>> from cepbr import CEP
   >>> cep = CEP()
   >>> cep.get('01154-030')
   {'bairro': u'Barra Funda', 'cidade': u'S\xe3o Paulo', 'uf': u'SP', 'logradouro': u'Rua Margarida', 'cep': u'01154030'}

:copyright: (c) 2012 by Mauro Baraldi.
:license: ISC, see LICENSE for more details.

Keep Hacking in a Free World! =)
"""

__title__ = 'cepbr'
__version__ = '0.0.1'
__build__ = 0x000001
__author__ = 'Mauro Baraldi'
__license__ = 'ISC'
__copyright__ = 'Copyright 2012 Mauro Baraldi'

from .cep import CEP