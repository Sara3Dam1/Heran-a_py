class veiculo:
    def __init__(self, marca, modelo, ano):
        self._marca = marca
        self._modelo = modelo
        self._ano = ano

    @property
    def marca(self):
        return self._marca
    
    @property
    def modelo(self):
        return self._modelo

    @property
    def ano(self):
        return self._ano

    def descrever(self):
        return f"{self.ano} {self.marca} {self.modelo}"
    
    def __str__(self):
        return self.descrever()


class Carro(veiculo):
    def __init__(self, marca, modelo, ano, num_portas):
        super().__init__(marca, modelo, ano)
        self._num_portas = num_portas

    @property
    def num_portas(self):
        return self._num_portas

    def descrever(self):
        base = super().descrever()
        return f"{base} | {self._num_portas} portas"


class Moto(veiculo):
    def __init__(self, marca, modelo, ano, cilindradas):
        super().__init__(marca, modelo, ano)
        self._cilindradas = cilindradas

    @property
    def cilindradas(self):
        return self._cilindradas

    def descrever(self):
        base = super().descrever()
        return f"{base} | {self._cilindradas}cc"


c = Carro('Toyota', 'Corola', 2023, 4)
m = Moto('Honda', 'CG 160', 2022, 160)

print(c)
print(m)
print(c.marca)
print(isinstance(c, veiculo))
print(isinstance(m, Carro))