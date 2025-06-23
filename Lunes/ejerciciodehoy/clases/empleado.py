class Empleado:
    def __init__(self, nombre, apellido, salario, cargo):
        self.nombre = nombre
        self.apellido = apellido
        self.salario = salario
        self.cargo = cargo

    def __str__(self):
        return f"Empleado: {self.nombre} {self.apellido}, Salario: {self.salario}, Cargo: {self.cargo}"