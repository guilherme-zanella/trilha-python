produtos = [
    ('Notebook', 2500),
    ('Mouse', 100),
    ('Teclado', 150),
    ('Monitor', 1200)
]

produtos_ordenados = sorted(produtos, key=lambda produto: produto[1])
print(produtos_ordenados)