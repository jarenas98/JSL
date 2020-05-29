#!/usr/bin/python3
#-*- coding: utf-8 -*-

# Script que actualiza el organizador.js y genera el pdf del reporte, consultando la información 
# mediante el script de recursos y adjutando el bloque de datos a la plantilla del reporte
# Autor: Sebastian Montes. Jefferson Arenas, Luis Figueroa
# Licencia GNU GPL v4

import re, subprocess, sys

# Se instancian los nombres de los archivos del organizador y del script que consulta los datos 

nombreReporte = "reporte"
archivoOrganizador = "js/organizador.js"
nombreScriptRecursos = "resources.py"

# El índice de inserción indica la linea en la cual se van a insertar la linea de datos correcpondiente al cuerpo de un objeto JavaScript.
indiceDeInsercion = 0

# Se abre el organizador y se busca el signo de la zona de cambio
organizador = open(archivoOrganizador, "r")
for row in organizador:
    if("//ZonaDeCambio+" in row):
        break
    indiceDeInsercion = indiceDeInsercion + 1
organizador.close()

organizador = open(archivoOrganizador, "r")
contenidoOrganizador = organizador.readlines()


# Se cargan los datos
p = subprocess.Popen ("./" + nombreScriptRecursos, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

# Se espera que acabe el subproceso para mostrar la salida decodificada
p.wait()
datos = p.stdout.read().decode()
sys.stderr.write(p.stderr.read().decode())

# Se insertan los datos depués del signo de la zona de cambio
contenidoOrganizador.remove(contenidoOrganizador[indiceDeInsercion + 1])
contenidoOrganizador.insert(indiceDeInsercion + 1,datos)

# Se escribe todo el organizador nuevamente
organizador = open(archivoOrganizador, "w")
contenidoOrganizador = "".join(contenidoOrganizador)
organizador.write(contenidoOrganizador)
organizador.close()

print("Generando informe de gestión en PDF por favor espere...")
# Se transforma el reporte a pdf
p = subprocess.Popen ("wkhtmltopdf --javascript-delay 8000 " + nombreReporte + ".html " + nombreReporte + ".pdf", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
#Se espera que acabe el subproceso para mostrar la salida decodificada
p.wait()
sys.stdout.write(p.stdout.read().decode())
sys.stderr.write(p.stderr.read().decode())

# Se abre el PDF del reporte con el xreader
p = subprocess.Popen ("xreader " + nombreReporte + ".pdf &", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
