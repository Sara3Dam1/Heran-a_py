from veiculo import veiculo, Carro, Moto
v1 = Carro('Fiat ', 'Strada Volcano 1.3', 2024, 4)
v2 = Moto('Honda', 'PCX 160', 2026, 156.9)
v3 = Carro('Toyota', 'Corolla XEi 2.0', 2024, 4)

garagem = [v1, v2, v3]

for v in garagem:
    print (v)

carros = [v for v in garagem if isinstance(v, Carro)]
motos = [ v for v in garagem if isinstance(v, Moto)]
print(f'Carros: {len(carros)} | Motos: {len(motos)}')