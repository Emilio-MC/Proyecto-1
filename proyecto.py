 
#-----------------------------------------------------------------------------------------------


            
#----------------------------------------------------------------------------------------------
def OpcionesGenerales():
     print ("(/)  Consulta de viajes")
     
     print ("(*)  Reservación de viaje")

     print ("(=)  Cancelación de reservación")

     print ("(F)  Atras")

     print ("(3)  Salir")

     opcion = input("Cual opcion selecciona: ")
     if isinstance(opcion,str):
          if (opcion=='/'):
              return ConsultaViajes()
            
          elif (opcion=='*'):
              return ReservaciónViaje()
                           
          elif (opcion=='='):
              return CancelaciónRservación()
          
          elif (opcion=='F'):
              return OpcionesAdministrativas()
            
                           
          elif (opcion=='3'):
              return print("Hasta luego")
          
          else:
               print("Error, opcion incorrecta")
#-------------------------------------------------------------------------------------------------
def IncluirEmpresas():
    if(0==0):
                pass
    print("Debe de tener 9 digitos")
    cedula = (input("Ingrese la cedula: "))
    contador = len(str(cedula))
    contador = str(contador)
    nombre = input("Ingrese el nombre: ")
    Direccion = input("Ubicación de la empresa: ")
    proyecto = "gestionEmpresa.txt"

    anexarContenidoArchivo(proyecto, cedula, nombre, Direccion, contador)

def anexarContenidoArchivo(proyecto, cedula, nombre, Direccion, contador):
        f = open (proyecto,'a')
        if(contador<"9"):
                return print("La cedula no puede tener menos de 9 digitos")
        elif(contador>"9"):
                return print("La cedula no puede tener más de 9 digitos")
        elif(contado=="6"):
            return print ("No puede existir dos empresas con la misma cedula")
#-----------------------------------------------------------------------------------------------
def EliminarEmpresas():
    proyecto = "gestionEmpresa.txt"
    nombre = input("Digite el nombre: ")
    NumeroLinea = 0
    with open("gestionEmpresa.txt", "r") as ObjFichero:
        for line in ObjFichero:
            NumeroLinea = NumeroLinea + 1
            PosicionTexto = line.find(nombre)
            if PosicionTexto >= 0:
                NumeroLinea = int(NumeroLinea)
                return EliminarEmpresas_aux(NumeroLinea)
        else:
            return print("No existe empresa con el nombre que pusiste")
            
def EliminarEmpresas_aux(NumeroLinea):
    initial_line = 1
    file_lines = {}
    with open("gestionEmpresa.txt") as f:
        content = f.readlines()
    for line in content:
        file_lines[initial_line] = line.strip()
        initial_line += 1
    f = open("gestionEmpresa.txt", "w")
    for line_number, line_content in file_lines.items():
        if line_number != NumeroLinea:
            f.write('{}\n'.format(line_content))
    f.close()
    print("Empresa eliminada con exito")
#-----------------------------------------------------------------------------------------------
def iniciaModificarEmpresas(nombre):
    if(0==0):
        pass 
    contador = len(str(nombre))
    contador = str(contador)
    cedula = input("Ingrese la cedula: ")
    Contador = str(Contador)
    Direccion = input("Ubicación de la empresa: ")
    proyecto = "gestionEmpresa.txt"

    anexariniciaModificarEmpresas(proyecto, nombre, cedula, Direccion ,contador, Contador)

def anexariniciaModificarEmpresas(proyecto, nombre, Direccion ,contador, Contador):
    f = open (proyecto,'a')
    if(contador<"9"):
        return print("La cedula no puede tener menos de 9 digitos")
    elif(contador>"9"):
        return print("La cedula no puede tener más de 9 digitos")
#-------------------------------------------------------------------------------------------------
def ModificarEmpresas():
    print("Recordatorio: Si al modificar un empresa y falla al modificarlo, su empresa sera eliminada y debera ingresarla de nuevo en incluir empresa")
    proyecto = "gestionEmpresa.txt"
    nombre = input("Digite el nombre de la empresa: ")
    NumeroLinea = 0
    with open("gestionEmpresa.txt", "r") as ObjFichero:
        for line in ObjFichero:
            NumeroLinea = NumeroLinea + 1
            PosicionTexto = line.find(nombre)
            if PosicionTexto >= 0:
                NumeroLinea = int(NumeroLinea)
                return ModificarEmpresas_aux(NumeroLinea, nombre)
        else:
            return print("Nombre no encontrado")
            
def ModificarEmpresas_aux(NumeroLinea,nombre):
    initial_line = 1
    file_lines = {}
    with open("gestionEmpresa.txt") as f:
        content = f.readlines()
    for line in content:
        file_lines[initial_line] = line.strip()
        initial_line += 1
    f = open("gestionEmpresa.txt", "w")
    for line_number, line_content in file_lines.items():
        if line_number != NumeroLinea:
            f.write('{}\n'.format(line_content))
    f.close()
    return iniciaModificarEmpresas(nombre)
#----------------------------------------------------------------------------------------------
def VerEmpresas():
    f = open ("gestionEmpresa.txt",'r')
    for mensaje in f.readlines():
        print(mensaje)
    f.close()
#-----------------------------------------------------------------------------------------------
def GestiónEmpresas():
     print ("(G)  Incluir Empresas")
     
     print ("(H)  Eliminar Empresas")

     print ("(I)  Modificar Empresas")

     print ("(J)  Ver Empresas")

     opcion = input("Cual opcion selecciona: ")
     if isinstance(opcion,str):
          if (opcion=='G'):
              return IncluirEmpresas()
            
          elif (opcion=='H'):
              return EliminarEmpresas()
            
            
          elif (opcion=='I'):
              return ModificarEmpresas()
            
                           
          elif (opcion=='J'):
              return VerEmpresas()
            
#--------------------------------------------------------------------------------------------------
def IncluirTransporte():
    if(0==0):
                pass
    print("Debe de tener 6 digitos")
    placa = (input("Ingrese la placa: "))
    contador = len(str(placa))
    contador = str(contador)
    marca = input("Ingrese el marca: ")
    Contador = len (str(marca))
    Contador = str(Contador)
    modelo = input("Ingrese el modelo del vehiculo: ")
    año = input("Ingrese el año del vehiculo:")
    print("El vehiculo debe de ser de las empresas ingresadas anteriormente")
    empresa = input("A que emprese pertenece el vehiculo:")
    asientosvip = input("Cantidad de asientos de clase vip: ")
    asientosnormales = input("Cantidad de asientos normales: ")
    asientoseco = input("Cantidad de asientos de clase económica: ")
    proyecto = "transportes.txt"

    anexarContenidoArchivo(proyecto, placa, marca, modelo, año, empresa, asientosvip, asientosnormales, asientoseco, contador, Contador)

def anexarContenidoArchivo(proyecto, placa, marca, modelo, año, empresa, asientosvip, asientosnormales, asientoseco, contador, Contador):
        f = open (proyecto,'a')
        if(contador<"6"):
                return print("La placa no puede tener menos de 6 digitos")
        elif(contador>"6"):
                return print("La placa no puede tener más de 6 digitos")
        elif(contado=="6"):
            return print ("No puede existir dos transportes con la misma placa")
#---------------------------------------------------------------------------------------------------
def EliminarTransporte():
    proyecto = "transportes.txt"
    placa = input("Digite la placa: ")
    NumeroLinea = 0
    with open("transportes.txt", "r") as ObjFichero:
        for line in ObjFichero:
            NumeroLinea = NumeroLinea + 1
            PosicionTexto = line.find(nombre)
            if PosicionTexto >= 0:
                NumeroLinea = int(NumeroLinea)
                return EliminarTransporte_aux(NumeroLinea)
        else:
            return print("Numero de placa no encontrado")
            
def EliminarTransporte_aux(NumeroLinea):
    initial_line = 1
    file_lines = {}
    with open("transportes.txt") as f:
        content = f.readlines()
    for line in content:
        file_lines[initial_line] = line.strip()
        initial_line += 1
    f = open("transportes.txt", "w")
    for line_number, line_content in file_lines.items():
        if line_number != NumeroLinea:
            f.write('{}\n'.format(line_content))
    f.close()
    print("Transporte eliminado con exito")
#---------------------------------------------------------------------------------------------------
def iniciaModificarTransporte(marca):
    if(0==0):
        pass 
    contador = len(str(marca))
    contador = str(contador)
    marca = input("Ingrese la placa: ")
    Contador = len (str(placa))
    Contador = str(Contador)
    modelo = input("Ingrese el modelo del vehiculo: ")
    año = input("Ingrese el año del vehiculo:")
    print("El vehiculo debe de ser de las empresas ingresadas anteriormente")
    empresa = input("A que emprese pertenece el vehiculo:")
    asientosvip = input("Cantidad de asientos de clase vip: ")
    asientosnormales = input("Cantidad de asientos normales: ")
    asientoseco = input("Cantidad de asientos de clase económica: ")
    proyecto = "transportes.txt"

    anexariniciaModificarTransporte(proyecto, placa, modelo, año, empresa, asientosvip, asientosnormales, asientoseco, contador, Contador)

def anexariniciaModificarTransporte(proyecto, placa, modelo, año, empresa, asientosvip, asientosnormales, asientoseco, contador, Contador):
    f = open (proyecto,'a')
    if(contador<"6"):
        return print("La placa no puede tener menos de 6 digitos")
    elif(contador>"6"):
        return print("La placa no puede tener más de 9 digitos")
    elif(contado=="6"):
            return print ("No puede existir dos transportes con la misma placa")
#-------------------------------------------------------------------------------------------------
def ModificarTransporte():
    print("Recordatorio: Si al modificar un transpote y falla al modificarlo, su empresa sera eliminada y debera ingresarla de nuevo en incluir empresa")
    proyecto = "transportes.txt"
    placa = input("Digite la placa del vehiculo: ")
    NumeroLinea = 0
    with open("transportes.txt", "r") as ObjFichero:
        for line in ObjFichero:
            NumeroLinea = NumeroLinea + 1
            PosicionTexto = line.find(nombre)
            if PosicionTexto >= 0:
                NumeroLinea = int(NumeroLinea)
                return ModificarTransporte_aux(NumeroLinea, placa)
        else:
            return print("Nombre no encontrado")
            
def ModificarTransporte_aux(NumeroLinea,placa):
    initial_line = 1
    file_lines = {}
    with open("transportes.txt") as f:
        content = f.readlines()
    for line in content:
        file_lines[initial_line] = line.strip()
        initial_line += 1
    f = open("transportes.txt", "w")
    for line_number, line_content in file_lines.items():
        if line_number != NumeroLinea:
            f.write('{}\n'.format(line_content))
    f.close()
    return iniciaModificarTransporte(placa)
#--------------------------------------------------------------------------------------------------
def VerTransporte():
    f = open ("transportes.txt",'r')
    for mensaje in f.readlines():
        print(mensaje)
    f.close()
    
#---------------------------------------------------------------------------------------------------
def GestiónTransporteEmpresas():
     print ("(K)  Incluir Transporte")
     
     print ("(L)  Eliminar Transporte")

     print ("(M)  Modificar Transporte")

     print ("(N)  Ver Transporte")

     opcion = input("Cual opcion selecciona: ")
     if isinstance(opcion,str):
          if (opcion=='K'):
              return IncluirTransporte()
            
          elif (opcion=='L'):
              return EliminarTransporte()
            
            
          elif (opcion=='M'):
              return ModificarTransporte()
            
                           
          elif (opcion=='N'):
              return VerTransporte()
            
#--------------------------------------------------------------------------------------------------
def GestionarViaje():
     print ("(Ñ)  Incluir Viaje")
     
     print ("(O)  Eliminar Viaje")

     print ("(P)  Ver Viajes")

     opcion = input("Cual opcion selecciona: ")
     if isinstance(opcion,str):
          if (opcion=='Ñ'):
              return IncluirViaje()
            
          elif (opcion=='O'):
              return EliminarViaje()
                            
          elif (opcion=='P'):
              return VerViajes()
#--------------------------------------------------------------------------------------------------
def OpcionesAdministrativas():
     print ("(A)  Gestión de empresas")
     
     print ("(B)  Gestión de transporte por empresa")

     print ("(C)  Gestión de viaje")

     print ("(D)  Consultar historial de reservaciones")

     print ("(E)  Estadísticas de viaje")

     print ("(F)  Atras")

    
     opcion = input("Cual opcion selecciona: ")
     if isinstance(opcion,str):
          if (opcion=='A'):
              return GestiónEmpresas()
            
          elif (opcion=='B'):
              return GestiónTransporteEmpresas()
            
            
          elif (opcion=='C'):
              return GestionarViaje()
            
                           
          elif (opcion=='D'):
              return ConsultarHistorialReservaciones()
          
          elif (opcion=='E'):
              return EstadísticasViaje()
            
                           
          elif (opcion=='F'):
              return reservacionBoletos()
          
          else:
               print("Error, opcion incorrecta")

          print("\n")
          reservacionBoletos()  





#---------------------------------------------------------------
def reservacionBoletos():
    print ("Seleccione una de las opciones a mostrar")
    print ("(1)    Opciones administrativas")
    print ("(2)    Opciones de usuario normal")
    print ("\n")
    print ("(3)     Salir")
    opcion = input("\nCual opcion selecciona: ")

    if (opcion=='3'):
            return print("Hasta luego")

    if (isinstance(opcion,str)):
           if(opcion=='1'):
                    OpcionesAdministrativas()
            
           elif(opcion=='2'):
                   OpcionesGenerales()
            
           else:
               print("Error, opcion incorrecta")


    print("\n")
    reservacionBoletos()         

      
reservacionBoletos()
