# -*- coding: utf-8 -*-
"""request.ipynb
 Recoger datos de una Web. previo al manejo de alertas de cambios en la propia página
Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1SLhFQ8LtL0DKfhiwZSxN_7Ui3BZoFe8r
"""

import requests
response = requests.get('https://www.ucm.es/')
type(response)
response.headers

import requests

response = requests.get('https://www.ucm.es/')
print(response.status_code)
print(len(response.text))
#print(response.cookies.get('guest_id'))
#print(response.headers.get('content-encoding'))
print(response.headers)
print(response.content)
