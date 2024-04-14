import socket
conector = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
direccion = ('127.0.0.1',27000)
conector.bind(direccion)
conector.listen(5)
while True:
    
    conexion,dirConexion = conector.accept()
    try:
        dato = conexion.recv(23)
        if dato:
            datoFormateado = dato.decode()
            print(datoFormateado)
            datoRetorno = input("indique dato a devolver")
            datoRetornoFormateado = datoRetorno.encode('utf-8')
            conexion.send(datoRetornoFormateado)
        else:
            datoFormateado = dato.decode()
            if datoFormateado == " final": 
                conexion.close()
    except:
            print("Chau")
            conexion.close()