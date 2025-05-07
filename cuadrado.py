class FiguraGeometrica:
    def __init__(self, alto, ancho):
        self._alto = alto
        self._ancho = ancho
    def get_alto(self):
        return self._alto
    def set_alto(self, alto):
        self._alto = alto
    def get_ancho(self):
        return self._ancho
    def set_ancho(self, ancho):
        self._ancho = ancho
    def __str__(self):  # Corrección del nombre del método
        return f'Alto: {self._alto}, Ancho: {self._ancho}'

class Cuadrado(FiguraGeometrica):
    def __init__(self, lado):
        super().__init__(lado, lado)
    def area(self):
        return self._alto * self._ancho
    def __str__(self):  # Corrección del nombre del método
        return f'Cuadrado de lado {self._alto}, área {self.area()}'
cuadrado = Cuadrado(5)
print(cuadrado)