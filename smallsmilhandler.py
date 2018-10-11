#!/usr/bin/python3
# -*- coding: utf-8 -*-
from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class SmallSMILHandler(ContentHandler):

    def __init__(self):

        atb_rootlayout = {"width": "", "height": "", "background-color": ""}
        atb_region = {"id": "", "top": "", "bottom": "", "left": "",
                      "right": ""}
        atb_img = {"src": "", "region": "", "begin": "", "dur": ""}
        atb_audio = {"src": "", "begin": "", "dur": ""}
        atb_textstream = {"src": "", "region": ""}
        self.etiquetas = {"root-layout": atb_rootlayout, "region": atb_region,
                          "img": atb_img, "audio": atb_audio,
                          "textstream": atb_textstream}
        self.datos = []

    def startElement(self, name, attrs):

        if name in self.etiquetas:
            dic = {}
            for atb in self.etiquetas[name]:
                dic[atb] = attrs.get(atb, "")
            self.datos.append([name, dic])

    def get_tags(self):

        print(self.datos)


if __name__ == "__main__":

    parser = make_parser()
    cHandler = SmallSMILHandler()
    parser.setContentHandler(cHandler)
    parser.parse(open('karaoke.smil'))
    cHandler.get_tags()
