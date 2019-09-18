# -*- coding: utf-8 -*-
#!/usr/bin/env python

import argparse
import os

def activate(string):
    print("Activando Ambiente")
    os.system('source ../../ambientes/ven_pyerp/bin/activate')



def hello(string):
    print("#################################################################")
    print("# Es una aplicacion adminitrar PYERP                            #")
    print("# www.falconsolutions.cl                                        #")
    print("# Autor: Marlon Falcon Herandez                                 #")
    print("# mail: mfalcon@ynext.cl                                        #")
    print("#################################################################")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose", help="Mostrar información de depuración", action="store_true")

    parser.add_argument("-a", help="Activate",
                        type=activate,
                        action="store")

    parser.add_argument("-hello", help="Hello",
                        nargs='*',
                        type=hello,
                        action="store")


    args = parser.parse_args()

    # Aquí procesamos lo que se tiene que hacer con cada argumento
    if args.verbose:
        print("depuración activada!!!")

if __name__ == "__main__":main()

