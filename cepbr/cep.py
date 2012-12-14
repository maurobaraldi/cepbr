# -*- coding: utf-8 -*-

#####################################################################
# CEPBR - Biblioteca consulta ao CEP pelo site dos correios do Brasil
#
# v1.0
# - Puramente em Python. Somente bibliotecas da standard lib.
# - Código otimizado.
# - Resultado em JSON.
####################################################################

import json
import urllib

class CEP():

    def __init__(self):
        self.url = 'http://cep.correiocontrol.com.br/%s.json'

    def get_cep(self, cep):

        _cep_ = cep

        if not _cep_:
            raise ValueError('É necessário infortar um CEP.')

        query = urllib.urlopen(self.url % _cep_).read()

        try:
            return json.loads(query)
        except ValueError:
            raise ValueError('CEP inválido ou incompleto.')
