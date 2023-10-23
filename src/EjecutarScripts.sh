#!/bin/bash

# Ruta al ejecutable de Python 3 que deseas utilizar
PYTHON3_EXECUTABLE=/Library/Frameworks/Python.framework/Versions/3.11/bin/python3

# ##############TEST PATH #############
cd ./Tests
$PYTHON3_EXECUTABLE -m pytest tst_1048.py  --html=../Results/GallardoRocio.html --self-contained-html
