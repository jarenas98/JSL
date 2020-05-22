#!/usr/bin/python3
#-*- coding: utf-8 -*-

#Script que consulta datos de la máquina anfitrión
#Autor: Sebastian Montes
#Licencia GNU GPL v4

import subprocess, re, sys

resultSet = {}

##################################################################################################

p = subprocess.Popen ("hostname", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
#Se espera que acabe el subproceso para mostrar la salida decodificada
p.wait()
nombreEquipo = p.stdout.read().decode()

resultSet['nombreEquipo'] = nombreEquipo.strip()

##################################################################################################

usuariosDict={}
archivoUsusarios = open('/etc/passwd')
for usuarioRow in archivoUsusarios:
    usuarioRow = usuarioRow.split(":")
    usuarioDict={}
    usuarioDict["nombre"] = usuarioRow[0] 
    GECOS = usuarioRow[4].split(",")
    try:
        usuarioDict["nombreCompleto"] = GECOS[0] 
        usuarioDict["noHab"] = GECOS[1] 
        usuarioDict["telOficina"] = GECOS[2] 
        usuarioDict["telCasa"] = GECOS[3] 
        usuarioDict["otros"] = GECOS[4]
    except:
        pass
    usuariosDict[usuarioRow[2]] = usuarioDict
usuariosDict["usuarios"] = usuarioDict 

resultSet['usuarios'] = usuariosDict

##################################################################################################

p = subprocess.Popen ("hostname -I", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
#Se espera que acabe el subproceso para mostrar la salida decodificada
p.wait()
ipEquipo = p.stdout.read().decode()

resultSet['ipEquipo'] = ipEquipo.strip()

##################################################################################################

p = subprocess.Popen ("ifconfig | grep ':[0-9|a-z][0-9|a-z]:'", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
#Se espera que acabe el subproceso para mostrar la salida decodificada
p.wait()
mac = re.sub(" +"," ", p.stdout.read().decode()).split(" ")[2]

resultSet['mac'] = mac.strip()

##################################################################################################

p = subprocess.Popen ("free -m | head -n2 | tail -n1", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
#Se espera que acabe el subproceso para mostrar la salida decodificada
p.wait()
totalRAM = re.sub(" +"," ", p.stdout.read().decode()).split(" ")[1]

resultSet['totalRAM'] = int(totalRAM)

##################################################################################################

p = subprocess.Popen ("free -m | head -n3 | tail -n1", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
#Se espera que acabe el subproceso para mostrar la salida decodificada
p.wait()
totalSwap = re.sub(" +"," ", p.stdout.read().decode()).split(" ")[1]

resultSet['totalSwap'] = int(totalSwap)

##################################################################################################

p = subprocess.Popen ("df -h -m", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
#Se espera que acabe el subproceso para mostrar la salida decodificada
p.wait()
discos = re.sub(" +"," ", p.stdout.read().decode()).split("\n")

discosDict={}
for discoRaw in discos:
    discoRaw = discoRaw.split(" ")
    if('/sd' in discoRaw[0]):
        discosDict[discoRaw[0]]=int(discoRaw[1])

resultSet['discos'] = discosDict

##################################################################################################

p = subprocess.Popen ("nproc", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
#Se espera que acabe el subproceso para mostrar la salida decodificada
p.wait()
cpuCores=p.stdout.read().decode()

resultSet['cpuCores'] = int(cpuCores.strip())

##################################################################################################

cpuinfo = open('/proc/cpuinfo')
cpuFrec = 0
for row in cpuinfo:
    if('cpu MHz' in row):
        cpuFrec = re.sub(" +","", row).split(":")[1]
        break
resultSet['cpuFrec'] = float(cpuFrec.strip())

##################################################################################################

p = subprocess.Popen ("ps aux --sort -pcpu | head -n6 | tail -n5", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
p.wait()
topProcesos = re.sub(" +"," ", p.stdout.read().decode().strip()).split("\n")

procesosDict={}
for procesoRaw in topProcesos:
    procesoRaw = re.sub(" +"," ", procesoRaw).split(" ")
    infoProceso={}
    infoProceso["usuarioPropietario"] = procesoRaw[0]
    infoProceso["Nombre del proceso"] = procesoRaw[10]
    infoProceso["Porcentaje de uso de CPU"] = procesoRaw[2]
    infoProceso["Tiempo de ejecución"] = procesoRaw[9]
    procesosDict[procesoRaw[1]] = infoProceso

resultSet["topProcesos"] = procesosDict

sys.stdout.write(str(resultSet)+"\n")
