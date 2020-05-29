#!/usr/bin/python3
#-*- coding: utf-8 -*-

# Script que genera el reporte html y pdf, consultando la información 
# mediante el script de recursos y adjutando el bloque de datos a la
# plantilla del reporte
# Autor: Sebastian Montes. Jefferson Arenas, Luis Figueroa
# Licencia GNU GPL v4

import re, subprocess, sys

nombreReporte = "reporte"
nombreScriptRecursos = "resources.py"

indiceDeInsercion = 0

reporte = open(nombreReporte + ".html", "r")
for row in reporte:
    if("//ZonaDeCambio+" in row):
        break
    indiceDeInsercion = indiceDeInsercion + 1
reporte.close()

reporte = open(nombreReporte + ".html", "r")
contenidoReporte = reporte.readlines()


#Se cargan los datos
p = subprocess.Popen ("./" + nombreScriptRecursos, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    #Se espera que acabe el subproceso para mostrar la salida decodificada
p.wait()
datos = p.stdout.read().decode()
sys.stderr.write(p.stderr.read().decode())

contenidoReporte.remove(contenidoReporte[indiceDeInsercion + 1])
contenidoReporte.insert(indiceDeInsercion + 1,datos)

reporte = open(nombreReporte + ".html", "w")
contenidoReporte = "".join(contenidoReporte)
reporte.write(contenidoReporte)
reporte.close()

print("Generando informe de gestión en PDF por favor espere...")
# Se transforma el reporte a pdf
p = subprocess.Popen ("wkhtmltopdf --javascript-delay 8000 " + nombreReporte + ".html " + nombreReporte + ".pdf", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    #Se espera que acabe el subproceso para mostrar la salida decodificada
p.wait()
sys.stdout.write(p.stdout.read().decode())
sys.stderr.write(p.stderr.read().decode())

# Se abre el PDF con el xreader
p = subprocess.Popen ("xreader " + nombreReporte + ".pdf &", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    #Se espera que acabe el subproceso para mostrar la salida decodificada
