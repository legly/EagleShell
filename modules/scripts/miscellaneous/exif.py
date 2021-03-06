#!/usr/bin/python3

from assets.banners import exif_banner
from assets.colors import *
from assets.designs import logo, author
from assets.prefixes import eagleshell_prefix, invalid_input_prefix, image_prefix
from assets.properties import clear_screen
from assets.shortcuts import Exit
from .miscellaneous import Miscellaneous
import os
from PIL import Image
from PIL.ExifTags import TAGS


class Exif:
    def __init__(self):
        self.configuration()
        self.extractor()
        self.result()

    def header(self):
        os.system(clear_screen)
        print(logo)
        print(exif_banner)
        print(author)

    def configuration(self):
        try:
            self.header()
            print('Configuration:')
            print('\n\tINFO:')
            print('\t-----')
            print('\tSupported Extensions:')
            print('\t".jpg", ".jpeg"')
            print('\n\tInput:')
            print('\t------')
            print('\tInput Path To Image Location')
            print('\tExample: /tmp/images/puppy.jpg\n')
            self.image_set = input(image_prefix).lower()
        except KeyboardInterrupt:
            Exit()

    def extractor(self):
        imagename = self.image_set
        image = Image.open(imagename)
        exifdata = image.getexif()
        for tag_id in exifdata:
            tag = TAGS.get(tag_id, tag_id)
            data = exifdata.get(tag_id)
            if isinstance(data, bytes):
                data = data.decode()
            print(f"{tag:25}: {data}")

    def result(self):
        try:
            self.header()
            print('Result:\n')
            print('\n\tY): New')
            print('\tZ): Menu')
            print('\tX): Exit\n')
            while True:
                cmd = input(eagleshell_prefix).lower()
                if cmd == 'y':
                    Exif()
                elif cmd == 'z':
                    Miscellaneous()
                elif cmd == 'x':
                    Exit()
                else:
                    print(invalid_input_prefix)
                    continue
        except KeyboardInterrupt:
            Exit()
