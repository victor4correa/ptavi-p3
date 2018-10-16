#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 11:04:29 2018

@author: victor
"""
import sys
import json
from xml.sax import make_parser
from smallsmilhandler import SmallSMILHandler
from urllib.request import urlretrieve

if __name__ == "__main__":
    
    try:
        file_smil = sys.argv[1]
        file_json = sys.argv[1].replace(".smil", ".json")
        archivo_smil = []
        parser = make_parser()
        cHandler = SmallSMILHandler()
        parser.setContentHandler(cHandler)
        parser.parse(open(file_smil))
        
        with open(file_json, "w") as fjson:
        
            listavalores = cHandler.get_tags()
            for linea in listavalores:
                lista_final = []
                etiqueta = linea[0]
                lista_final.append(etiqueta)
                for atributo, valor in linea[1].items():
                    lista_final.append (atributo + "=" + '"' + valor + '"')   
                lista_final = '\t'.join(lista_final)
                archivo_smil.append(lista_final + '\n')
                
            for linea in listavalores:
                lista_final = []
                etiqueta = linea[0]
                for atributo, valor in linea[1].items():
                    if valor[:7] == "http://":
                        urlretrieve(valor, valor.split("/")[-1])
                        print("Descargando %s..." % valor)
                
                
        """fjson = json.dumps(archivo_smil)
        print(fjson)"""
        
                
                
                
    except IndexError:
        
        sys.exit("Usage:python3 karaoke.py file.smil")