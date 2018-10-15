#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 11:04:29 2018

@author: victor
"""
import sys
from xml.sax import make_parser
from smallsmilhandler import SmallSMILHandler


if __name__ == "__main__":
    try:
        
        file = sys.argv[1]
        parser = make_parser()
        cHandler = SmallSMILHandler()
        parser.setContentHandler(cHandler)
        parser.parse(open(file))
        listavalores = cHandler.get_tags()
        
        
        for linea in listavalores:
            lista_final = []
            etiqueta = linea[0]
            lista_final.append(etiqueta)
            for atributo, valor in linea[1].items():
                lista_final.append (atributo + "=" + '"' + valor + '"')
            lista_final = "\\".join(lista_final)
            print(lista_final) 
    except IndexError:
        
        sys.exit("Usage:python3 karaoke.py file.smil")