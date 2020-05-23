#!/usr/bin/python3
#-*- coding: utf-8 -*-

# Script que consulta datos de la máquina anfitrión
# Autor: Sebastian Montes
# Licencia GNU GPL v4

import subprocess, re, sys

# Función que retorna el nombre del host o máquina actual
def getHostname():

    p = subprocess.Popen ("hostname", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    #Se espera que acabe el subproceso para mostrar la salida decodificada
    p.wait()
    nombreEquipo = p.stdout.read().decode()
    return nombreEquipo.strip()

# Función que retorna un diccionario de diccionarios de usuarios cuya UID es la llave de un diccionario
def getUsuarios():

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
    return usuariosDict

# Función que retorna la IP actual del equipo
def getIp():

    p = subprocess.Popen ("hostname -I", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    #Se espera que acabe el subproceso para mostrar la salida decodificada
    p.wait()
    return p.stdout.read().decode().strip()

# Función que retorna la dirección MAC del equipo
def getMACAdd():

    p = subprocess.Popen ("ifconfig | grep ':[0-9|a-z][0-9|a-z]:'", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    #Se espera que acabe el subproceso para mostrar la salida decodificada
    p.wait()
    return re.sub(" +"," ", p.stdout.read().decode()).split(" ")[2].strip()

# Función que retorna el total de memoria RAM del equipo en megabytes
def getTotalRAM():

    p = subprocess.Popen ("free --mega | head -n2 | tail -n1", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    #Se espera que acabe el subproceso para mostrar la salida decodificada
    p.wait()
    return int(re.sub(" +"," ", p.stdout.read().decode()).split(" ")[1])

# Función que retorna el total de memoria SWAP del equipo en megabytes
def getTotalSWAP():

    p = subprocess.Popen ("free --mega | head -n3 | tail -n1", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    #Se espera que acabe el subproceso para mostrar la salida decodificada
    p.wait()
    return int(re.sub(" +"," ", p.stdout.read().decode()).split(" ")[1])

# Función que retorna un diccionario de diccionarios con información de discos, 
# la llave de cada diccionario es el nombre del disco y su contenido es la cantidad 
# de espacio libre en Megabytes que tiene ese disco
def getAllDisksFree():

    p = subprocess.Popen ("df -h -m", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    #Se espera que acabe el subproceso para mostrar la salida decodificada
    p.wait()
    discos = re.sub(" +"," ", p.stdout.read().decode()).split("\n")

    discosDict={}
    for discoRaw in discos:
        discoRaw = discoRaw.split(" ")
        if('/sd' in discoRaw[0]):
            discosDict[discoRaw[0]]=int(discoRaw[1])
    return discosDict

# Función que retorna la cantidad de nucleos que tiene el CPU de la máquina
def getCPUCores():
    
    p = subprocess.Popen ("nproc", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    #Se espera que acabe el subproceso para mostrar la salida decodificada
    p.wait()
    return  int(p.stdout.read().decode())

# Función que retorna la frecuencia del procesador del equipo en MHz
def getCPUFreq():
    
    cpuinfo = open('/proc/cpuinfo')
    cpuFrec = 0
    for row in cpuinfo:
        if('cpu MHz' in row):
            cpuFrec = re.sub(" +","", row).split(":")[1]
            break
    return float(cpuFrec.strip())

# Función que retorna un diccionario de diccionarios, la llave de cada diccionario es el PID y contiene información como
# el dueño del proceso, el uso de CPU que está haciendo ese proceso y el tiempo de ejecución que lleva ese proceso.
def getTopPS():

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
    
    return procesosDict

resultSet = {}

resultSet['nombreEquipo'] = getHostname()
resultSet['usuarios'] = getUsuarios()
resultSet['ipEquipo'] = getIp()
resultSet['mac'] = getMACAdd()
resultSet['totalRAM'] = getTotalRAM()
resultSet['totalSwap'] = getTotalSWAP()
resultSet['discos'] = getAllDisksFree()
resultSet['cpuCores'] = getCPUCores()
resultSet['cpuFrec'] = getCPUFreq()
resultSet["topProcesos"] = getTopPS()

sys.stdout.write(str(resultSet)+"\n")
