precos = [100, 250, 80, 300]

resultado = list(map(lambda p: p * 1.10, precos))

print([round(n, 2) for n in resultado])