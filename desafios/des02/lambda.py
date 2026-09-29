numeros = [1,2,3,4,5,6,7,8,9]

dobro = lambda x: x * 2

dobrados = [n * 2 for n in numeros if n % 2 == 0]

print(dobrados)
