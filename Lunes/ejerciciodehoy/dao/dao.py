from clases import Empleado as e

class Dao:
    def __init__(self):
        self.lista = []

    def agregarEmpleado(self, empleado):
        self.lista.append(empleado)

    def listar (self, empleado):
        return self.lista
    
    def actualizar (self, empleado):
        for empleado in self.lista:
            if empleado == empleado:
                self.lista.remove(empleado)
                self.lista.append(empleado)