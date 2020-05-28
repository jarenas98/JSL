#!/bin/bash

NOMBRE="Reporte.html"

cat inicial.txt > $NOMBRE

DATOS=$(python3 ./resources.py)

cat datos.txt > $DATOS
cat datos.txt >>$NOMBRE
cat final.txt >>$NOMBRE

wkhtmltopdf --javascript-delay 15000 ./Reporte.html Reporte.pdf