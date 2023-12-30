import os
import pyaes
import time

## abrir o arquivo criptografado
file_name = input('Digite o nome do arquivo criptografado (padrão: arquivo.txt.ran): ')
file = open(file_name, "rb")
file_data = file.read()
file.close()

## chave para descriptografia
key = b"ransonwareattack"
aes = pyaes.AESModeOfOperationCTR(key)
decrypt_data = aes.decrypt(file_data)

## remover o arquivo criptografado
os.remove(file_name)

## criar o arquivo descriptografado
new_file = file_name[:-3]
new_file = open(f'{new_file}', "wb")
new_file.write(decrypt_data)
new_file.close()

## mostrar mensagem
print('Descriptografado com êxito')
time.sleep(5)