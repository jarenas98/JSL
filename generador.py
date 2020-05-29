#!/usr/bin/python3
#-*- coding: utf-8 -*-

# Script que consulta datos de la máquina anfitrión
# Autor: Sebastian Montes. Jefferson Arenas, Luis Figueroa
# Licencia GNU GPL v4

import re, subprocess, sys

nombreReporte = "reporte"
nombreScriptRecursos = "resources.py"

#Se registra la parte inicial
p = subprocess.Popen ("cat " + nombreReporte + ".html", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    #Se espera que acabe el subproceso para mostrar la salida decodificada
p.wait()
inicial = p.stdout.read().decode().split("//ZonaDeCambio+")[0]
sys.stderr.write(p.stderr.read().decode())

#Se cargan los datos
p = subprocess.Popen ("./" + nombreScriptRecursos, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    #Se espera que acabe el subproceso para mostrar la salida decodificada
p.wait()
datos = "//ZonaDeCambio+\n" + p.stdout.read().decode() + "//ZonaDeCambio-"
sys.stderr.write(p.stderr.read().decode())

#Se cargar la parte final
p = subprocess.Popen ("cat " + nombreReporte + ".html", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    #Se espera que acabe el subproceso para mostrar la salida decodificada
p.wait()
final = p.stdout.read().decode().split("//ZonaDeCambio-")[1]
sys.stderr.write(p.stderr.read().decode())


#Juntar todo en el reporte
f = open (nombreReporte + ".html", "w")
archivo = (inicial+datos+final).splitlines(True)

#Escribir el reporte linea a linea
for fila in archivo:
    f.write(fila)
f.close()

# Se transforma el reporte a pdf y se abre con el xreader
p = subprocess.Popen ("wkhtmltopdf --javascript-delay 8000 " + nombreReporte + ".html " + nombreReporte + ".pdf && xreader " + nombreReporte + ".pdf", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    #Se espera que acabe el subproceso para mostrar la salida decodificada
p.wait()
sys.stdout.write(p.stdout.read().decode())
sys.stderr.write(p.stderr.read().decode())