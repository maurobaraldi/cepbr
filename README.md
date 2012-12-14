CEP-BR
======

### Biblioteca em Python para acesso à base de CEP dos Correios do Brasil

Inicialmente inspirada no [postmon](https://github.com/CodingForChange/postmon), a proposta era deixa-la mais simples e modular. Entretanto oo projeto postmon utiliza uma url de busca dos site dos Correios do Brasil. Sua disponibilidade esta diretamente associada a disponibilidade dessa url.

A nova versão utiliza a [API](http://avisobrasil.com.br/api-de-consulta-de-cep/) de consulta a CEP do Correio Control da [Aviso](http://avisobrasil.com.br/)

### Mudanças de versão

- Puramente em Python. Somente bibliotecas da standard lib.
- Código otimizado
- Resultado em JSON nativo


### Modo de uso
```
>>> from cepbr import CEP
>>> c = CEP()
>>> c.get_cep('01154030')
{u'bairro': u'Barra Funda', u'uf': u'SP', u'logradouro': u'Rua Margarida', u'localidade': u'S\xe3o Paulo', u'cep': '01154030'}
>>> 
>>> c.get_cep('05437001')
{u'bairro': u'Sumarezinho', u'uf': u'SP', u'logradouro': u'Rua Heitor Penteado', u'localidade': u'S\xe3o Paulo', u'cep': u'05437001'}
>>> 
```

### Testes
- Doctests

```
python -m doctest cep_doctest.rst -v
```

### Contribuições
[Lucas Magnum](https://github.com/LucasMagnum) (Doctests e Refactoring)

### Contato
Mauro Navarro Baraldi (mauro.baraldi@gmail.com)
[github](https://github.com/maurobaraldi) & [twitter](http://twitter.com/mauro_baraldi)


Keep Hacking in a Free World!