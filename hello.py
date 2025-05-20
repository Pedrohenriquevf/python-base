#!/usr/bin/env python3

# Este programa imprime Hello, world!

# Hello, world - multi linguas

#os.getenv("LANG")[:5]

__version__ = "0.01"
__author__ = "Pedro Franzoi"
__license__ = "Unlicense"

import os

current_language = os.getenv("LANG", "en.US")[:5]

msg = "Hello, world!"

if current_language == "pt.BR":
    msg = "Olá, mundo!"
elif  current_language == "it.IT":
    msg = "Ciao, mondo!"
elif  current_language == "es.SP":
    msg = "Hola, Mundo!"
elif  current_language == "fr.FR":
    msg = "Bonjour Monde!"
        
print (msg)


