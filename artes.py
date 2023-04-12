import ascii

url = input('Insira o URL da imagem: ')

output = ascii.loadFromUrl(url)

print(output)