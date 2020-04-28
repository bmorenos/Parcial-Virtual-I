listaCliente = list()
listaProyecto= list()
listaRegion= list()
listaRegistros= list()


class Cliente:
    codigo=""
    nombre=""
    direccion=""
    numTelefono=""

class Proyecto:
    id=""
    nombreProyecto=""
    descripcion=""
    proyecto_CLiente=""
    codigo_Ciente=""
    direccion_Cliente=""
    numTelefono_Cliente=""

class DepartamentoMunicipio:
    departamento=""
    municipio=""
    depto_idproyecto=""
    depto_Proyecto=""
    depto_Descripcion=""
    depto_cliente=""
    depto_IdCliente=""
    depto_Direccion=""
    depto_telefono=""

class Registros:
    reg_Id=""
    reg_Proyecto=""
    reg_Descripcion=""
    reg_cliente=""
    reg_codigo=""
    reg_direccion=""
    reg_telefono=""
    reg_departamento=""
    reg_municipio=""

def registrarCliente():
    print("** REGISTRO DE CLIENTES **")
    client= Cliente()

    client.codigo= raw_input("Codigo: ")
    client.nombre= raw_input("Nombre: ")
    client.direccion= raw_input("Direccion: ")
    client.numTelefono= raw_input("Telefono: ")
    listaCliente.append(client)

def listarCliente():
    print("** MOSTRAR CLIENTES **")
    print("CODIGO".ljust(20, " ") + "NOMBRE".ljust(35, " ") + "DIRECCION".ljust(35, " ") + "TELEFONO".ljust(35, " "))
    for client in listaCliente:
        print client.codigo.ljust(20, " "), client.nombre.ljust(35, " "), client.direccion.ljust(33, " "), client.numTelefono.ljust(35, " ")

def registrarProyecto():
    proyect = Proyecto()

    proyect.id= raw_input("Id de proyecto: ")
    proyect.nombreProyecto= raw_input("Titulo de Proyecto: ")
    proyect.descripcion= raw_input("Descripcion: ")
    print("CODIGO".ljust(20, " ") + "NOMBRE".ljust(35, " ") + "DIRECCION".ljust(35, " ") + "TELEFONO".ljust(35, " "))
    for client in listaCliente:
            print client.codigo.ljust(20, " "), client.nombre.ljust(35, " "), client.direccion.ljust(35," "), client.numTelefono.ljust(35, " ")
    relacion= raw_input("Ingrese el Codigo del Cliente para asignar el proyecto: ")
    for client in listaCliente:
        if client.codigo == relacion:
            proyect.proyecto_CLiente=client.nombre
            proyect.codigo_Ciente=client.codigo
            proyect.direccion_Cliente=client.direccion
            proyect.numTelefono_Cliente=client.numTelefono
            listaProyecto.append(proyect)

def listarProyectos():
    print("** MOSTRAR PROYECTOS **")
    print("ID DE PROYECTO".ljust(20, " ") + "TITULO DE PROYECTO".ljust(35, " ") + "DESCRIPCION".ljust(35, " ") + "CLIENTE".ljust(35, " ") + "CODIGO DE CLIENTE".ljust(35, " "))
    for proyect in listaProyecto:
        print proyect.id.ljust(20, " "), proyect.nombreProyecto.ljust(35, " "), proyect.descripcion.ljust(35, " "), proyect.proyecto_CLiente.ljust(35, " "), proyect.codigo_Ciente.ljust(35, " ")

def registrarRegion():
    depmun=DepartamentoMunicipio()

    depmun.departamento= raw_input("Ingrese Departamento: ")
    depmun.municipio= raw_input("Ingrese Municipio: ")
    print("ID DE PROYECTO".ljust(20, " ") + "TITULO DE PROYECTO".ljust(35, " ") + "DESCRIPCION".ljust(35, " ") + "CLIENTE".ljust(35, " "))
    for proyect in listaProyecto:
        print proyect.id.ljust(20, " "), proyect.nombreProyecto.ljust(35, " "), proyect.descripcion.ljust(35," "), proyect.proyecto_CLiente.ljust(35, " ")
    relacion2= raw_input("Ingrese el Id del proyecto que desea asignar: ")
    for proyect in listaProyecto:
        if proyect.id == relacion2:
            depmun.depto_idproyecto=proyect.id
            depmun.depto_Proyecto=proyect.nombreProyecto
            depmun.depto_Descripcion=proyect.descripcion
            depmun.depto_cliente=proyect.proyecto_CLiente
            depmun.depto_IdCliente=proyect.codigo_Ciente
            depmun.depto_Direccion=proyect.direccion_Cliente
            depmun.depto_telefono=proyect.numTelefono_Cliente
            listaRegion.append(depmun)

def listarRegiones():
    print("** MOSTRAR PROYECTOS **")
    print("DEPARTAMENTO".ljust(20, " ") + "MUNICIPIO".ljust(50, " ") + "TITULO DE PROYECTO".ljust(35, " ") + "DESCRIPCION".ljust(35, " "))
    for depmun in listaRegion:
        print depmun.departamento.ljust(20, " "), depmun.municipio.ljust(50, " "), depmun.depto_Proyecto.ljust(35, " "), depmun.depto_Descripcion.ljust(35, " ")

def buscarProyectosDeCliente():
    print("** BUSQUEDA DE PROYECTOS DE CLIENTES **")
    palabraClave= raw_input("Ingrese el Codigo o el Nombre del cliente que desea buscar: ")
    for proyect in listaProyecto:
        if proyect.codigo_Ciente == palabraClave or proyect.proyecto_CLiente == palabraClave:
            print("ID DE PROYECTO".ljust(20, " ") + "PROYECTO".ljust(35, " ") + "DESCRIPCION".ljust(35, " ") + "CLIENTE".ljust(35," ") + "CODIGO DE CLIENTE".ljust(35, " "))
            print proyect.id.ljust(20, " "), proyect.nombreProyecto.ljust(35, " "), proyect.descripcion.ljust(33, " "), proyect.proyecto_CLiente.ljust(35," "), proyect.codigo_Ciente.ljust(35, " ")

def listarRegistrosCompletos():
    print("** MOSTRAR PROYECTOS **")
    print("CODIGO DE CLIENTE".ljust(20, " ") + "CLIENTE".ljust(35, " ") + "DIRECCION".ljust(35, " ") + "TELEFONO".ljust(35, " ")+ "ID DE PROYECTO".ljust(35, " ") + "TITULO DE PROYECTO".ljust(35, " ")+ "DESCRIPCION DE PROYECTO".ljust(35, " ")+ "DEPARTAMENTO".ljust(35, " ")+ "MUNICIPIO".ljust(35, " "))
    for depmun in listaRegion:
        print depmun.depto_IdCliente.ljust(20, " "), depmun.depto_cliente.ljust(35, " "), depmun.depto_Direccion.ljust(35, " "), depmun.depto_telefono.ljust(35, " "), depmun.depto_idproyecto.ljust(35, " "), depmun.depto_Proyecto.ljust(35, " "), depmun.depto_Descripcion.ljust(35, " "), depmun.departamento.ljust(35, " "), depmun.municipio.ljust(35, " ")

def eliminarUnRegistro():
    print("** MOSTRAR PROYECTOS **")
    print("CODIGO DE CLIENTE".ljust(20, " ") + "CLIENTE".ljust(35, " ") + "DIRECCION".ljust(35, " ") + "TELEFONO".ljust(35, " ") + "ID DE PROYECTO".ljust(35, " ") + "TITULO DE PROYECTO".ljust(35," ") + "DESCRIPCION DE PROYECTO".ljust(35, " ") + "DEPARTAMENTO".ljust(35, " ") + "MUNICIPIO".ljust(35, " "))
    for depmun in listaRegion:
        print depmun.depto_IdCliente.ljust(20, " "), depmun.depto_cliente.ljust(35, " "), depmun.depto_Direccion.ljust(35, " "), depmun.depto_telefono.ljust(35, " "), depmun.depto_idproyecto.ljust(35," "), depmun.depto_Proyecto.ljust(35, " "), depmun.depto_Descripcion.ljust(35, " "), depmun.departamento.ljust(35," "), depmun.municipio.ljust(35, " ")
    borrar = raw_input("Ingrese el Id del Proyecto que desea borrar: ")
    for depmun in listaRegion:
        if depmun.depto_idproyecto == borrar:
            print("Usted elimino el proyecto '" + depmun.depto_Proyecto + "' en" + " '" + depmun.departamento + "', '" + depmun.municipio+ "' de el cliente '"+ depmun.depto_cliente + "' que se identifica con el id '"+ depmun.depto_IdCliente + "'.")
            listaRegion.remove(depmun)
    for proyect in listaProyecto:
        if proyect.id == borrar:
            listaProyecto.remove(proyect)

def menu():
    print"*************** Menu ***************"
    print"|  1. Registrar un Cliente         |"
    print"|  2. Mostrar Clientes             |"
    print"|  3. Registrar un Proyecto        |"
    print"|  4. Mostrar Proyectos            |"
    print"|  5. Registrar Region             |"
    print"|  6. Listar Regiones              |"
    print"|  7. Buscar Proyectos de Cliente  |"
    print"|  8. Mostrar Registros Completos  |"
    print"|  9. Eliminar un registro         |"
    print"|  10. Cerrar Programa.            |"

def mostrarMenu():
    opcionMenu=0
    cerrarPrograma=10

    while opcionMenu != cerrarPrograma:
            menu()
            opcionMenu = input("Digite una Opcion: ")

            if opcionMenu == 1:
                registrarCliente()
            elif opcionMenu == 2:
                listarCliente()
            elif opcionMenu == 3:
                registrarProyecto()
            elif opcionMenu == 4:
                listarProyectos()
            elif opcionMenu == 5:
                registrarRegion()
            elif opcionMenu == 6:
                listarRegiones()
            elif opcionMenu == 7:
                buscarProyectosDeCliente()
            elif opcionMenu == 8:
                listarRegistrosCompletos()
            elif opcionMenu == 9:
                eliminarUnRegistro()
            elif opcionMenu == 10:
                print("Gracias por utilizar nuestros servicios. Vuelve pronto.")
            else:
                print("La opcion que ingreso no es valida")

mostrarMenu()


