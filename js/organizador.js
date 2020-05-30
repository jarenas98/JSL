google.charts.load('current', { 'packages': ['corechart', "gauge"] });
google.charts.setOnLoadCallback(dibujarGraficaParticiones);
google.charts.setOnLoadCallback(dibujarGraficaUsoDeRam);
google.charts.setOnLoadCallback(dibujarGraficaUsoDeDisco);
google.charts.setOnLoadCallback(dibujarGraficaUsoDeCadaDisco);
google.charts.setOnLoadCallback(dibujarGraficaTopProcesos);
google.charts.setOnLoadCallback(dibujarGraficaUsoDeCPU);
google.charts.setOnLoadCallback(dibujarGraficaUsoSwap);


var datos =

    //ZonaDeCambio+
{'nombreEquipo': 'montes-VirtualBox', 'usuariosReales': {'1000': {'nombre': 'montes', 'nombreCompleto': 'montes', 'noHab': '', 'telOficina': '', 'telCasa': ''}}, 'todosLosUsuarios': {'0': {'nombre': 'root', 'nombreCompleto': 'root'}, '1': {'nombre': 'daemon', 'nombreCompleto': 'daemon'}, '2': {'nombre': 'bin', 'nombreCompleto': 'bin'}, '3': {'nombre': 'sys', 'nombreCompleto': 'sys'}, '4': {'nombre': 'sync', 'nombreCompleto': 'sync'}, '5': {'nombre': 'games', 'nombreCompleto': 'games'}, '6': {'nombre': 'man', 'nombreCompleto': 'man'}, '7': {'nombre': 'lp', 'nombreCompleto': 'lp'}, '8': {'nombre': 'mail', 'nombreCompleto': 'mail'}, '9': {'nombre': 'news', 'nombreCompleto': 'news'}, '10': {'nombre': 'uucp', 'nombreCompleto': 'uucp'}, '13': {'nombre': 'proxy', 'nombreCompleto': 'proxy'}, '33': {'nombre': 'www-data', 'nombreCompleto': 'www-data'}, '34': {'nombre': 'backup', 'nombreCompleto': 'backup'}, '38': {'nombre': 'list', 'nombreCompleto': 'Mailing List Manager'}, '39': {'nombre': 'irc', 'nombreCompleto': 'ircd'}, '41': {'nombre': 'gnats', 'nombreCompleto': 'Gnats Bug-Reporting System (admin)'}, '65534': {'nombre': 'nobody', 'nombreCompleto': 'nobody'}, '100': {'nombre': 'systemd-network', 'nombreCompleto': 'systemd Network Management', 'noHab': '', 'telOficina': '', 'telCasa': ''}, '101': {'nombre': 'systemd-resolve', 'nombreCompleto': 'systemd Resolver', 'noHab': '', 'telOficina': '', 'telCasa': ''}, '102': {'nombre': 'syslog', 'nombreCompleto': ''}, '103': {'nombre': 'messagebus', 'nombreCompleto': ''}, '104': {'nombre': '_apt', 'nombreCompleto': ''}, '105': {'nombre': 'uuidd', 'nombreCompleto': ''}, '106': {'nombre': 'cups-pk-helper', 'nombreCompleto': 'user for cups-pk-helper service', 'noHab': '', 'telOficina': '', 'telCasa': ''}, '107': {'nombre': 'kernoops', 'nombreCompleto': 'Kernel Oops Tracking Daemon', 'noHab': '', 'telOficina': '', 'telCasa': ''}, '108': {'nombre': 'rtkit', 'nombreCompleto': 'RealtimeKit', 'noHab': '', 'telOficina': '', 'telCasa': ''}, '109': {'nombre': 'avahi-autoipd', 'nombreCompleto': 'Avahi autoip daemon', 'noHab': '', 'telOficina': '', 'telCasa': ''}, '110': {'nombre': 'usbmux', 'nombreCompleto': 'usbmux daemon', 'noHab': '', 'telOficina': '', 'telCasa': ''}, '111': {'nombre': 'systemd-coredump', 'nombreCompleto': 'systemd core dump processing', 'noHab': '', 'telOficina': '', 'telCasa': ''}, '112': {'nombre': 'lightdm', 'nombreCompleto': 'Light Display Manager'}, '113': {'nombre': 'dnsmasq', 'nombreCompleto': 'dnsmasq', 'noHab': '', 'telOficina': '', 'telCasa': ''}, '114': {'nombre': 'saned', 'nombreCompleto': ''}, '115': {'nombre': 'nm-openvpn', 'nombreCompleto': 'NetworkManager OpenVPN', 'noHab': '', 'telOficina': '', 'telCasa': ''}, '116': {'nombre': 'avahi', 'nombreCompleto': 'Avahi mDNS daemon', 'noHab': '', 'telOficina': '', 'telCasa': ''}, '117': {'nombre': 'colord', 'nombreCompleto': 'colord colour management daemon', 'noHab': '', 'telOficina': '', 'telCasa': ''}, '118': {'nombre': 'speech-dispatcher', 'nombreCompleto': 'Speech Dispatcher', 'noHab': '', 'telOficina': '', 'telCasa': ''}, '119': {'nombre': 'pulse', 'nombreCompleto': 'PulseAudio daemon', 'noHab': '', 'telOficina': '', 'telCasa': ''}, '120': {'nombre': 'hplip', 'nombreCompleto': 'HPLIP system user', 'noHab': '', 'telOficina': '', 'telCasa': ''}, '121': {'nombre': 'geoclue', 'nombreCompleto': ''}, '1000': {'nombre': 'montes', 'nombreCompleto': 'montes', 'noHab': '', 'telOficina': '', 'telCasa': ''}, '999': {'nombre': 'vboxadd', 'nombreCompleto': ''}}, 'cantidadUsuariosReales': 1, 'cantidadTotalUsuarios': 42, 'ipEquipo': '192.168.0.127', 'mac': '08:00:27:ee:75:8a', 'totalRAM': 3039, 'totalSwap': 969, 'particiones': {'/dev/sda1': 20029}, 'cpuCores': 3, 'cpuFrec': 3591.684, 'topProcesos': {'1401': {'usuarioPropietario': 'montes', 'Nombre del proceso': 'cinnamon', 'Porcentaje de uso de CPU': '18.5', 'Tiempo de ejecución': '83:51'}, '1628': {'usuarioPropietario': 'montes', 'Nombre del proceso': '/usr/share/code/code', 'Porcentaje de uso de CPU': '6.2', 'Tiempo de ejecución': '28:06'}, '11826': {'usuarioPropietario': 'montes', 'Nombre del proceso': '/usr/bin/python3', 'Porcentaje de uso de CPU': '4.0', 'Tiempo de ejecución': '0:00'}, '1035': {'usuarioPropietario': 'root', 'Nombre del proceso': '/usr/lib/xorg/Xorg', 'Porcentaje de uso de CPU': '1.7', 'Tiempo de ejecución': '7:43'}, '1739': {'usuarioPropietario': 'montes', 'Nombre del proceso': '/usr/share/code/code', 'Porcentaje de uso de CPU': '1.4', 'Tiempo de ejecución': '6:23'}}, 'usoDeCPU': 11.3, 'usoDeRAM': 67.1, 'usoDeSWAP': 10.93, 'usoDeDisco': {'/dev/sda1': 41}, 'fecha': 'Reporte generado el día 29 del mes 05 del año 2020, a las 17:32:46'}


// Método que se encarga de ejecutar los diferentes métodos
function main() {
    console.log(this.datos.ipEquipo)
    // cambiar el titrulo del documento
    document.getElementById('tituloPrincipal').innerText = `GNU Linux - Reporte de información | Máquina: ${this.datos.nombreEquipo}`;
    // cambiar el contedido del IP
    document.getElementById('campoIp').innerText = `${this.datos.ipEquipo}`;
    // cambiar el contedido del MAC
    document.getElementById('campoMAC').innerText = `${this.datos.mac}`;
    // cambiar el contedido del RAM TOTAL
    document.getElementById('ramTotal').innerText = `${this.datos.totalRAM} MB`;
    // cambiar el contedido del SWAP TOTAL
    document.getElementById('swapTotal').innerText = `${this.datos.totalSwap} MB`;
    // cambiar el contedido del CPU cores
    document.getElementById('corestotales').innerText = `${this.datos.cpuCores}`;
    // cambiar el contedido del CPU Frec
    document.getElementById('frecTotal').innerText = `${this.datos.cpuFrec} MHz`;

    document.getElementById('totalUsuariosCreados').innerText = `Usuarios creados - Total : ${this.datos.cantidadUsuariosReales}`;

    document.getElementById('totalUsuariosSistema').innerText = `Listado de usuarios del sistema - Total : ${this.datos.cantidadTotalUsuarios}`;
    // llenar tabla de particiones
    this.insertDataParticiones();
    // llena tabla de usuarios creados
    this.insertarDataUsuariosCreados();
    this.insertarDataUsuariosDelSistema();

    this.insertarFecha();

}
// variable que almacenara la data para las particiones de la tabla 1
var datatablePart1 = [["Partición", "MB"]];
// Variable que almacenara el total de almacenamiento en MB
var totalAlmacenamiento = 0;
// permite pintar las particiones en la tabla de particiones
function insertDataParticiones() {

    let res = "";
    let contador = 1;

    // Obteniendo todas las particiones de datos
    for (var particion in this.datos.particiones) {
        res = res + `<tr><th scope="row">${contador}</th><td>${particion}</td> <td>${this.datos.particiones[particion]} MB</td></tr>`;
        totalAlmacenamiento = totalAlmacenamiento + this.datos.particiones[particion];
        datatablePart1.push([particion, this.datos.particiones[particion]]);
        contador++;
    }

    document.getElementById('bodyTablaParticiones').innerHTML = `${res}`;
}



function dibujarGraficaUsoDeRam() {

    var data = google.visualization.arrayToDataTable([
        ['Label', 'Value'],
        ['RAM', { v: this.datos.usoDeRAM, f: this.datos.usoDeRAM+"%" }],

    ]);

    var options = {
        width: 460, height: 180,
        redFrom: 90, redTo: 100,
        yellowFrom: 75, yellowTo: 90,
        minorTicks: 5
    };

    var chart = new google.visualization.Gauge(document.getElementById('uso-de-ram'));

    chart.draw(data, options);


}
function dibujarGraficaUsoDeCPU() {

    var data = google.visualization.arrayToDataTable([
        ['Label', 'Value'],
        ['CPU', { v: this.datos.usoDeCPU, f: this.datos.usoDeCPU+"%" }],

    ]);

    var options = {
        width: 460, height: 180,
        redFrom: 90, redTo: 100,
        yellowFrom: 75, yellowTo: 90,
        minorTicks: 5
    };

    var chart = new google.visualization.Gauge(document.getElementById('uso-de-cpu'));

    chart.draw(data, options);


}

function dibujarGraficaUsoSwap(){

    var data = google.visualization.arrayToDataTable([
        ['Label', 'Value'],
        ['CPU', { v: this.datos.usoDeSWAP, f: this.datos.usoDeSWAP+"%" }],

    ]);

    var options = {
        width: 460, height: 180,
        redFrom: 90, redTo: 100,
        yellowFrom: 75, yellowTo: 90,
        minorTicks: 5
    };

    var chart = new google.visualization.Gauge(document.getElementById('uso-de-swap'));

    chart.draw(data, options);

}
function dibujarGraficaTopProcesos() {


    var data = new google.visualization.DataTable();
    data.addColumn('string', 'Nombre del proceso');
    data.addColumn('number', 'Porcentaje de uso del CPU');

    Object.values(datos.topProcesos).forEach(element => {
        let porcentaje = parseFloat(element["Porcentaje de uso de CPU"])/100;
        data.addRow([element["Nombre del proceso"],{ v: porcentaje , f: porcentaje*100+"%" }]);
       
    });
    
    var options = {

        chartArea: { width: '50%' },
        hAxis: {
            title: 'Porcentaje de uso de CPU',
            format : 'percent',
            minValue: 0
        },
        vAxis: {
            title: 'Nombre del proceso'
        },
        legend: 'none' 
    };

    var chart = new google.visualization.BarChart(document.getElementById('top-procesos'));

    chart.draw(data, options);
}
function dibujarGraficaUsoDeDisco() {

    const total_discos = Object.values(this.datos.particiones).reduce((a, b) => a + b, 0)

    console.log(total_discos)


    obj = this.datos.usoDeDisco
    let uso_por_disco = []

    for (const prop in obj) {
        uso_por_disco.push((this.datos.usoDeDisco[prop] * this.datos.particiones[prop]) / 100)
    }

    const total_usado_discos = uso_por_disco.reduce((a, b) => a + b, 0)

    const info = (total_usado_discos * 100) / total_discos

    var data = google.visualization.arrayToDataTable([
        ['Label', 'Value'],
        ['Total', { v: info, f: info+"%" }],

    ]);

    var options = {
        width: 460, height: 180,
        redFrom: 90, redTo: 100,
        yellowFrom: 75, yellowTo: 90,
        minorTicks: 5
    };

    var chart = new google.visualization.Gauge(document.getElementById('uso-de-disco'));

    chart.draw(data, options);


}
function dibujarGraficaUsoDeCadaDisco() {

    let info = [['Label', 'Value']];

    obj = this.datos.usoDeDisco

    for (const prop in obj) {
        info = info.concat([[prop, { v: this.datos.usoDeDisco[prop], f: this.datos.usoDeDisco[prop]+"%"}]])
    }


    var data = google.visualization.arrayToDataTable(info);

    var options = {
        width: 460, height: 180,
        redFrom: 90, redTo: 100,
        yellowFrom: 75, yellowTo: 90,
        minorTicks: 5
    };

    var chart = new google.visualization.Gauge(document.getElementById('uso-por-disco'));

    chart.draw(data, options);


}
function dibujarGraficaParticiones() {


    var data = google.visualization.arrayToDataTable(this.datatablePart1, false);


    var options = {
        title: "Total = " + `${this.totalAlmacenamiento}` + " MB",
        width: 500,
        height: 350,
        pieHole: 0.4,
        colors: ['#d1a36e', '#fde38d', '#e99d56', '#f3b49f', '#a15f3e', '#353839'],
    };

    var chart = new google.visualization.PieChart(document.getElementById('donutchart'));
    chart.draw(data, options);
}
// Obteniendo todas los usuarios creados y los pinta
function insertarDataUsuariosCreados() {
    let res = "";

    for (var usuario in this.datos.usuariosReales) {


        res = res + `
  <tr>
      <th scope="row">${usuario}</th>
      <td>${this.datos.usuariosReales[usuario].nombre}</td>
      <td>${this.datos.usuariosReales[usuario].nombreCompleto}</td>
      <td>${this.datos.usuariosReales[usuario].noHab}</td>
      <td>${this.datos.usuariosReales[usuario].telOficina}</td>
      <td>${this.datos.usuariosReales[usuario].telCasa}</td>
  </tr>`;


    }

    document.getElementById('bodyTablaUsuariosCreados').innerHTML = `${res}`;
}
function insertarDataUsuariosDelSistema() {
    let res = "";

    for (var usuario in this.datos.todosLosUsuarios) {


        res = res + `
  <tr>
      <th scope="row">${usuario}</th>
      <td>${this.datos.todosLosUsuarios[usuario].nombre}</td>
      <td>${this.datos.todosLosUsuarios[usuario].nombreCompleto}</td>
  </tr>`;


    }

    document.getElementById('bodyTablaUsuariosDelSistema').innerHTML = `${res}`;
}

function insertarFecha(){
    f = new Date();
    document.getElementById("piePg").innerHTML = "Universidad del Quindío - GNU Linux 1 | " + datos.fecha ;
}

this.main();
