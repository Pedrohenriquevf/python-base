#!/usr/bin/env python3

# Este programa imprime Hello, world!

# Hello, world - multi linguas

__version__ = "0.01"
__author__ = "Pedro Franzoi"
__license__ = "Unlicense"

current_language = os.getenv("LANG")[:5]

msg = "Hello, world!"

if current_language == "pt.BR":
    msg = "Olá, mundo!"
elif  current_language == "it.IT":
    msg = "Ciao, mondo!"

print (msg)


