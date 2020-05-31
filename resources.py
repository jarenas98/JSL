#!/usr/bin/python3
#-*- coding: utf-8 -*-

# Script que consulta datos de la máquina anfitrión
# Autor: Sebastian Montes. Jefferson Arenas, Luis Figueroa
# Licencia GNU GPL v4

import subprocess, re, sys, os
from datetime import datetime
from datetime import timedelta

# Función que retorna el nombre del host o máquina actual
def getHostname():

    p = subprocess.Popen ("hostname", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    #Se espera que acabe el subproceso para mostrar la salida decodificada
    p.wait()
    nombreEquipo = p.stdout.read().decode()
    return nombreEquipo.strip()

# Función que retorna un diccionario de diccionarios de usuarios cuya UID es la llave de un diccionario
# Recibe como parámetro una opción "a" en la cual se indica si se desean todos los usuarios o "r" 
# si solo se desean los "reales" 
def getAllUsers(opcion):

    usuariosDict={}
    archivoUsusarios = open('/etc/passwd')
    for usuarioRow in archivoUsusarios:
        
        usuarioRow = usuarioRow.split(":")
        if(opcion == 'r' and \
        not isPathInHome(usuarioRow[5])):
            continue
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
    return usuariosDict

# Función auxiliar que define si una ruta /home/[usuario] 
# del campo GECOS existe en realidad en el directorio /home
def isPathInHome(path):
    try:
        homeDir = os.listdir("/home")
        username = path.split("/")[2]
        for userFolderName in homeDir:
            if (username == userFolderName):
                return True
        return False
    except:
        return False

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

# Función que retorna un diccionario de diccionarios con información de particiones y particiones, 
# la llave de cada diccionario es el nombre del disco-partición y su contenido es la cantidad 
# de espacio en Megabytes que tiene.
def getAllPartitions():

    p = subprocess.Popen ("df -h -m", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    #Se espera que acabe el subproceso para mostrar la salida decodificada
    p.wait()
    particiones = re.sub(" +"," ", p.stdout.read().decode()).split("\n")

    particionesDict={}
    for particionRaw in particiones:
        particionRaw = particionRaw.split(" ")
        if('/sd' in particionRaw[0]):
            particionesDict[particionRaw[0]]=int(particionRaw[1])
    return particionesDict

# Función que retorna el total de almacenamiento SATA que tiene la máquina en GB.
def getAllSpace():

    p = subprocess.Popen ("df -h -m", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    #Se espera que acabe el subproceso para mostrar la salida decodificada
    p.wait()
    particiones = re.sub(" +"," ", p.stdout.read().decode()).split("\n")

    total = 0
    for particionesRaw in particiones:
        particionesRaw =  particionesRaw.split(" ") 
        if('/sd' in particionesRaw[0]):
            total = total + int(particionesRaw[1])
    return round(total/1000,1)

# Función que retorna el total de discos SATA que tiene la máquina.
def getAllDisks():

    p = subprocess.Popen ("df -h -m", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    #Se espera que acabe el subproceso para mostrar la salida decodificada
    p.wait()
    particiones = re.sub(" +"," ", p.stdout.read().decode()).split("\n")

    diskList=[]
    for particionesRaw in particiones:
        disco =  re.sub("[0-9]+","",particionesRaw.split(" ")[0]) 
        if(('/sd' in disco) and (disco not in diskList)):
            diskList.append(disco)
    return len(diskList)

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

#Función que retorna el porcentaje de uso de cpu de la máquina basado en el comando top
def getCPUUsagePercentage():
    p = subprocess.Popen("top -n1 | head -n3 | tail -n1",stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
    p.wait()
    CPU = p.stdout.read().decode().strip()
    return round(100-float(re.sub(" +"," ",re.sub("inact",".", CPU).split(".")[0].strip()).split(" ")[7].replace(",",".")),1)
    
#Función que retorna el porcentaje de uso de la memoria RAM del equipo
def getRAMUsagePercentage():
  
    #Se llama al subproceso ejecutando ese comando
    pMemoria = subprocess.Popen("free | head -n2 | tail -n1",stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
    pMemoria.wait()
    #Se suprime el exceso de espacios y se realiza el split con base al caracter " "
    memoria = re.sub(" +"," ", pMemoria.stdout.read().decode()).split(" ")
    return round((int(memoria[2])/int(memoria[1]))*100,1)

#Función que retorna el porcentaje de uso de la memoria SWAP del equipo
def getSWAPUsagePercentage():

    #Se llama al subproceso ejecutando ese comando
    pMemoria = subprocess.Popen("free | head -n3 | tail -n1",stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
    pMemoria.wait()
    #Se suprime el exceso de espacios y se realiza el split con base al caracter " "
    memoria = re.sub(" +"," ", pMemoria.stdout.read().decode()).split(" ")
    return round((int(memoria[2])/int(memoria[1]))*100,2)

# Función que retorna un diccionario de diccionarios con información de particiones, 
# la llave de cada diccionario es el nombre de la partición y su contenido es el porcentaje
# de uso de espacio en esa particion
def getAllPartitionsUsagePercentage():

    p = subprocess.Popen ("df -h -m", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    #Se espera que acabe el subproceso para mostrar la salida decodificada
    p.wait()
    particiones = re.sub(" +"," ", p.stdout.read().decode()).split("\n")

    particionesDict={}
    for particionRaw in particiones:
        particionRaw = particionRaw.split(" ")
        if('/sd' in particionRaw[0]):
            particionesDict[particionRaw[0]]=round((int(particionRaw[2])/int(particionRaw[1]))*100,1)
    return particionesDict

# Función que retorna el porcentaje de uso del espacio de la máquina
def getSpaceUsagePercentage():

    p = subprocess.Popen ("df -h -m", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    #Se espera que acabe el subproceso para mostrar la salida decodificada
    p.wait()
    particiones = re.sub(" +"," ", p.stdout.read().decode()).split("\n")

    totalDeEspacio = 0
    totalOcupado = 0
    for particionRaw in particiones:
        particionRaw = particionRaw.split(" ")
        if('/sd' in particionRaw[0]):
            totalDeEspacio = totalDeEspacio + int(particionRaw[1])
            totalOcupado = totalOcupado + int(particionRaw[2])
    return round((totalOcupado/totalDeEspacio)*100,1)

resultSet = {}

# Se puede llamar a cada una de las llaver mostradas para obtener información 
# o un diccionario con más información
resultSet['nombreEquipo'] = getHostname()
resultSet['usuariosReales'] = getAllUsers('r')
resultSet['todosLosUsuarios'] = getAllUsers('a')
resultSet['cantidadUsuariosReales'] = len(resultSet['usuariosReales'])
resultSet['cantidadTotalUsuarios'] = len(resultSet['todosLosUsuarios'])
resultSet['ipEquipo'] = getIp()
resultSet['mac'] = getMACAdd()
resultSet['totalRAM'] = getTotalRAM()
resultSet['totalSwap'] = getTotalSWAP()
resultSet['particiones'] = getAllPartitions()
resultSet['cpuCores'] = getCPUCores()
resultSet['cpuFrec'] = getCPUFreq()
resultSet["topProcesos"] = getTopPS()
resultSet["usoDeCPU"] = getCPUUsagePercentage()
resultSet["usoDeRAM"] = getRAMUsagePercentage()
resultSet["usoDeSWAP"] = getSWAPUsagePercentage()
resultSet["usoDeAlmacenamientoTotal"] = getSpaceUsagePercentage()
resultSet["usoDeParticiones"] = getAllPartitionsUsagePercentage()
resultSet["totalAlmacenamiento"] = getAllSpace()
resultSet["totalParticiones"] = getAllDisks()
resultSet["fecha"] = datetime.now().strftime("Reporte generado el día %d del mes %m del año %Y, a las %H:%M:%S")

sys.stdout.write(str(resultSet)+"\n")