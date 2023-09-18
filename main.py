
import sys
print("valor maximo do sistema = {}".format(sys.maxsize))

user = input('teste: ')
teste = user.split(" ")
casas = len(teste)
valCasaUm = teste[0]
bin_data = user.replace(' ', '')

print('valor original: {}'.format(user))
print('valor com split: {}'.format(teste))
print('valor com split sem espaco: {}'.format(bin_data))
print('quantas casas tem: {}'.format(casas))
print('valor casa um: {}'.format(valCasaUm))


def binaryToDecimal(binary):
	eita = len(valCasaUm)
	if eita > 8:
		print('seu binario tem que ser menor que oito digitos')
	elif all(c in '01' for c in bin_data):
		string = int(bin_data, 2)
		return string
	else:
		print('tem algarismo nao binario')

if __name__ == '__main__':
	if binaryToDecimal(int(bin_data)) == None:
		print("por favor somente insira valores binarios (numeros 0 e 1)")
	else:
		print('o seu numero em decimal e: {0}'.format(binaryToDecimal(int(bin_data))))


print("valor do binario: {}".format(bin_data))
str_data = ''
for i in range(0, len(bin_data), 8):
	temp_data = bin_data[i:i + 8]
	decimal_data = binaryToDecimal(temp_data)
	str_data = str_data + chr(decimal_data)

print(str(str_data))