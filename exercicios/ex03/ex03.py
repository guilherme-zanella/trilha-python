produtos = [
    ('Notebook', 2500),
    ('Mouse', 100),
    ('Teclado', 150),
    ('Monitor', 1200)
]

ordenados = sorted(produtos, key=lambda p: p[1])

print(ordenados)