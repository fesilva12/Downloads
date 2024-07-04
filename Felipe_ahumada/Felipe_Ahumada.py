from os import system
system("cls")
from random import randint
pedidos = []

def registrar_pedido():
    global seis
    global diez
    global veinte
    seis = 0
    diez = 0
    veinte = 0
    global nombre
    global apellido
    global comuna
    global direccion
    global id
    nombre = input("Ingrese nombre: ")
    apellido = input("Ingrese apellido: ")
    while True:
        print("Las comunas disponibles son Concepción, Chiguayante, Talcahuano, Hualpén y San Pedro")
        comuna = input("Ingrese comuna: ")
        if comuna == "concepcion" or comuna == "chiguayante" or comuna == "talcahuano" or comuna == "hualpen" or comuna == "san pedro":
            break
        else:
            print("Comuna no disponible")
    direccion = input("Ingrese dirección: ")
    id = randint(0, 999999)
    while True:
        while True:
            dispensador = int(input("¿Desea un dispensador de 6lts, 10lts o 20lts?: "))
            if dispensador == 6:
                seis = seis + 1
                break
            elif dispensador == 10:
                diez += 1
                break
            elif dispensador == 20:
                veinte += 1
                break
            else:
                print("Ingrese un número correcto de dispensadores")
        pedidos.append([id, nombre, apellido, direccion, comuna, seis, diez, veinte])
        otro = input("¿Desea realizar otro pedido?(si/no): ")
        if otro == "si":
            pass
        elif otro == "no":
            print(f"""
    ID pedido       cliente         Dirección        Sector         Disp.6lts        Disp.10lts         Disp.20lts
    {id}        {nombre} {apellido}    {direccion}         {comuna}          {seis}                     {diez}             {veinte} """)
            break
            
        print(f"""
        ID pedido       cliente         Dirección        Sector         Disp.6lts        Disp.10lts         Disp.20lts
        {id}        {nombre} {apellido}    {direccion}         {comuna}         {seis}                     {diez}             {veinte} """)
            
def listar_pedidos():
    for usuarios in pedidos:
        print(f"""
    ID pedido       cliente         Dirección        Sector         Disp.6lts        Disp.10lts         Disp.20lts
    {usuarios[0]}        {usuarios[1]} {usuarios[2]}    {usuarios[3]}         {usuarios[4]}         {usuarios[5]}                     {usuarios[6]}             {usuarios[7]} """)

def hoja_ruta():
    sector = input("¿Qué sector busca?: ")
    for usuarios in pedidos:
        if usuarios[4] == sector:
            #Arreglar
            archivo = open("hoja.csv", "w")
            archivo.write(f"""
    ID pedido       cliente         Dirección        Sector         Disp.6lts        Disp.10lts         Disp.20lts
    {usuarios[0]}        {usuarios[1]} {usuarios[2]}    {usuarios[3]}         {usuarios[4]}         {usuarios[5]}                     {usuarios[6]}             {usuarios[7]} """)


def buscar_pedido():
    buscar_id = int(input("Ingrese ID de su pedido: "))
    for usuarios in pedidos:
        if usuarios[0] == buscar_id:
            print(f"""
    ID pedido       cliente         Dirección        Sector         Disp.6lts        Disp.10lts         Disp.20lts
    {usuarios[0]}        {usuarios[1]} {usuarios[2]}    {usuarios[3]}         {usuarios[4]}         {usuarios[5]}                     {usuarios[6]}             {usuarios[7]} """)


while True:
    print("""
    1. Registrar pedido
    2. Listar los todos los pedidos
    3. Imprimir hoja de ruta
    4. Buscar un pedido por ID
    5. Salir del programa """)

    op = input("Ingrese opcion: ")
    match op:
        case "1":
            registrar_pedido()
        case "2":
            listar_pedidos()
        case "3":
            hoja_ruta()
        case "4":
            buscar_pedido()
        case "5":
            break