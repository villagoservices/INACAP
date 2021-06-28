'''
Nombre: Daniel Alejandro Villalon Gonzalez
BD:
•	Precio del certificado        : Debe estar entre $0 y $50.000
•	Tipo de tramite               : 1-Presencial,	2-Online.
•	Especificación del certificado: 1-Nacimiento, 	2-Defuncion,	3-Matrimonio.
'''
bd = [
    [], #Precio del certificado digitarPrecios()
    [], #Tipo de tramite digitarTipos()
    []  #Especificación del certificado digitarEspecificaciones()
]

vuelta = 0


def validarNumero(desde,hasta,pregunta):
    ci = desde -1
    while ci < desde or ci > hasta:
        try:
            ci = int(input(pregunta))
            if ci >= desde and ci <= hasta:
                return ci
            else:
                print("Digito Incorrecto!, Debe estar entre: ", desde, " y ", hasta)
        except:
            print ("Debe ser un numero!")

def validarSiNo(p):
    alerta = "Debe ser [Si,si,s] para si o [No,no,n] para no: "
    while True:
        interaccion = input(p)
        if interaccion.lower() not in ('Si', 'si', 'No', 'no', 's', 'n'):
            print(alerta)
        else:
            if interaccion.count("s") or interaccion.count("S"):
                return True
            else:
                return False

def digitarPrecios():
    global bd
    bd[0].append(validarNumero(0,50000,'''
    Ingrese el precio del certificado:
    Debe estar entre $0 y $50.000
    '''))

def digitarTipos():
    global bd
    bd[1].append(validarNumero(1,2,'''
    Ingrese el tipo de tramite
    Ingresa el numero correspondiente:
    1-Presencial,	2-Online
    '''))

def digitarEspecificaciones():
    global bd
    bd[2].append(validarNumero(1,3,'''
    Ingrese la especificacion del Certificado
    Ingresa el numero correspondiente:
    1-Nacimiento, 	2-Defuncion,	3-Matrimonio
    '''))

def digitarCantidadIngresos():
    global vuelta
    vuelta = vuelta + 1
    print("_____________________________________")
    print("Numero de Vuelta o Registro: ".upper(), vuelta)
    print("-------------------------------------")
    digitarPrecios()
    digitarTipos()
    digitarEspecificaciones()
    print("_____________________________________")

def presentarResultados():
    a = len(bd[0])
    pos = -1
    b = 0
    c = 0
    d = 0
    e = 0
    pos = -1
    for ba in bd[1]:
        pos = pos + 1
        if ba == 1:
            #calculando presenciales
            b = b + 1
            #calculando promedio de precios presenciales
            d = d + bd[0][pos]
        if ba == 2:
            #calculando Online
            c = c + 1
            #calculando promedio de precios online
            e = e + bd[0][pos]
    #calculando promedio de precios presenciales
    if b == 0:b = 1
    d = d / b
    #calculando promedio de precios online
    if c == 0:c = 1
    e = e / c
    
    f = 0
    g = 0
    h = 0
    i = 0
    j = 0
    k = 0
    pos = -1
    for fa in bd[2]:
        if fa == 1:
            f = f + 1
            i = i + bd[0][pos]
        if fa == 2:
            g = g + 1
            j = j + bd[0][pos]
        if fa == 3:
            h = h + 1
            k = k + bd[0][pos]
    #calculando promedio de precios nacimiento
    if f == 0: f = 1
    i = i / f
    if g == 0: g = 1
    j = j / g
    if h == 0: h = 1
    k = k / h

    print('''
    PRESENTANDO REGISTROS:
    -----------------------------------
    •	Cantidad total de certificados: ''', a,'''
    •	Cantidad de certificados presenciales solicitados: ''', b, '''
    •	Cantidad de certificados online solicitados: ''', c, '''
    •	Promedio de precios de certificados presenciales solicitados: $''', d,'''
    •	Promedio de precios de certificados online solicitados: $''', e,'''
    •	Cantidad de certificados de nacimiento solicitados: ''', f, '''
    •	Cantidad de certificados de defunción solicitados: ''', g, '''
    •	Cantidad de certificados de matrimonio solicitados: ''', h, '''
    •	Promedio de precios de certificados de nacimiento solicitados: $''', i,'''
    •	Promedio de precios de certificados de defunción solicitados: $''', j, '''
    •	Promedio de precios de certificados de matrimonio solicitados: $''', k, '''
    •	Cantidad de certificados presenciales y de nacimiento solicitados: ''', b + f,'''
    •	Cantidad de certificados presenciales y de defunción solicitados: ''', b + g,'''
    •	Cantidad de certificados presenciales y de matrimonio solicitados: ''', b + k,'''
    •	Cantidad de certificados online y de nacimiento solicitados: ''', c + f, '''
    •	Cantidad de certificados online y de defunción solicitados: ''', c + g, '''
    •	Cantidad de certificados online y de matrimonio solicitados: ''', c + h, '''
    ''')

def EjecutarPrograma():
    porRegistrar = validarNumero(0,4294967296,'''
        INDIQUE LA CANTIDAD DE REGISTROS QUE DESEA INGRESAR
        Digito 0 = cantidad de registros sin definir
        ''')
    if porRegistrar == 0:
        while porRegistrar == 0:
            digitarCantidadIngresos()
            if validarSiNo('''
                ¿Desea continuar ingresando mas registros?
                Escriba Si o No segun corresponda
                '''):
                pass
            else:
                break
    if porRegistrar > 0:
        conteo = 0
        while conteo < porRegistrar:
            conteo = conteo + 1
            digitarCantidadIngresos()
    presentarResultados()


EjecutarPrograma()