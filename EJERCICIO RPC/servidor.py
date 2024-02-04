from xmlrpc.server import SimpleXMLRPCServer

def suma(num1, num2):
    return num1 + num2

def resta(num1, num2):
    return num1 - num2

def multiplicacion(num1, num2):
    return num1 * num2

def division(num1, num2):
    return num1 / num2

def potencia(num1,num2):
    return num1 ** num2

server = SimpleXMLRPCServer(("localhost", 5048))

# Registrando las funciones en el servidor
server.register_function(suma, "suma")
server.register_function(resta, "resta")
server.register_function(multiplicacion, "multiplicacion")
server.register_function(division, "division")
server.register_function(potencia, "potencia")

print("Servidor en ejecución en http://localhost:5048")
server.serve_forever()
