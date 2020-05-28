#!/usr/bin/python3
#-*- coding: utf-8 -*-

import re, subprocess

nombreReporte = "reporte"
nombreScriptRecursos = "resources.py"

#Se registra la parte inicial
p = subprocess.Popen ("cat reporte.html", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    #Se espera que acabe el subproceso para mostrar la salida decodificada
p.wait()
inicial = p.stdout.read().decode().split("//ZonaDeCambio+")[0]

#Se cargan los datos
p = subprocess.Popen ("./" + nombreScriptRecursos, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    #Se espera que acabe el subproceso para mostrar la salida decodificada
p.wait()
datos = "//ZonaDeCambio+\n" + p.stdout.read().decode() + "//ZonaDeCambio-"

#Se cargar la parte final
p = subprocess.Popen ("cat reporte.html", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    #Se espera que acabe el subproceso para mostrar la salida decodificada
p.wait()
final = p.stdout.read().decode().split("//ZonaDeCambio-")[1]

f = open (nombreReporte + ".html", "w")
archivo = (inicial+datos+final).splitlines(True)
print(str(archivo))
for fila in archivo:
    f.write(fila)
f.close()

# Se transforma el reporte a pdf y se abre con el xreader
p = subprocess.Popen ("wkhtmltopdf --javascript-delay 8000 index.html " + nombreReporte + ".pdf && xreader " + nombreReporte, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    #Se espera que acabe el subproceso para mostrar la salida decodificada
p.wait()


