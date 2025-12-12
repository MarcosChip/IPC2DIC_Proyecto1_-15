# Lista madre
# nodo1      ->     nodo2       ->      nodo3  
#  \-centro1          
#         \-nodo1      ->     nodo2       ->      nodo3 
#              \-maquinaVirtual
#                   \-nodo1      ->     nodo2       ->      nodo3 

class Centro:
    def __init__(self, id, nombre, pais, ciudad, cpu, ram, almacenamiento, listaMVs):
        id = id
        nombre = nombre
        pais = pais
        ciudad = ciudad
        cpu = cpu
        ram = ram
        almacenamiento = almacenamiento
        listaMaquinasVirtuales = listaMVs

class maquinasVirtuales:
    def __init__(self, id, centroAsignado, so, cpu, ram, almacenamiento, ip, listaContenedores, estado):
        id = id
        centroAsignado = centroAsignado
        so = so
        cpu = cpu
        ram = ram
        almacenamiento = almacenamiento
        ip = ip
        listaContenedores = listaContenedores
        estado = estado

class contenedore:
    def __init__(self, id, nombre, imagen, cpu, ram, puerto, maquinaAsignada):
        id = id
        nombre = nombre
        imagen = imagen
        cpu = cpu
        ram = ram
        puerto = puerto
        maquinaAsignada = maquinaAsignada