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


class KaraokeLocal():

    def __init__(self, fich):
        parser = make_parser()
        cHandler = SmallSMILHandler()
        parser.setContentHandler(cHandler)
        parser.parse(open(file_smil))
        self.my_file = cHandler.get_tags()

    def __str__(self):
        archivo_smil = []
        for linea in self.my_file:
            lista_final = []
            etiqueta = linea[0]
            lista_final.append(etiqueta)
            for atributo, valor in linea[1].items():
                lista_final.append(atributo + "=" + '"' + valor + '"')
            lista_final = '\t'.join(lista_final)
            archivo_smil.append(lista_final + '\n')
        print(archivo_smil)

    def to_json(self, fjson):
        with open(file_json, "w"):
            json.dumps(self.my_file)

    def do_local(self):
        for linea in self.my_file:
                for atributo, valor in linea[1].items():
                    if valor[:7] == "http://":
                        name_local = valor.split('/')[-1]
                        urlretrieve(valor, name_local)
                        print("Descargando %s..." % valor)


if __name__ == "__main__":

    try:
        file_smil = sys.argv[1]
        file_json = sys.argv[1].replace(".smil", ".json")
        file_karaoke = KaraokeLocal(file_smil)
        file_karaoke.__str__()
        file_karaoke.to_json(file_json)
        file_karaoke.do_local()
        file_karaoke.to_json('file_json.json')
        file_karaoke.__str__()

    except IndexError:

        sys.exit("Usage:python3 karaoke.py file.smil")
