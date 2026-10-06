mensaje = "ATAQUE AL AMANECER"
clave = "CLAVE1234567890123"
#la clave del encunciado solo tiene 16 bytes por lo que añado el 2 y el 3 para llegar a 18 como el mensaje.

mensaje = mensaje.encode() #convertir el mensaje a bytes
clave = clave.encode() #convertir la clave a bytes

if len(mensaje) != len(clave): #comprobar que el mensaje y la clave tienen la misma longitud
    print("Error: el mensaje y la clave deben tener la misma longitud.")
    print("Mensaje:", len(mensaje), "bytes")
    print("Clave:", len(clave), "bytes")
else:
    # Cifrado XOR
    criptograma = bytes(a ^ b for a, b in zip(mensaje, clave)) 
    # El operador ^ realiza la operación XOR entre los bytes del mensaje y la clave, y zip() combina los bytes de ambos en pares.

    # Descifrado XOR
    mensaje_descifrado = bytes(a ^ b for a, b in zip(criptograma, clave))
    # El descifrado se realiza aplicando nuevamente la operación XOR entre el criptograma y la clave, recuperando así el mensaje original.

    print("Mensaje:           ", mensaje.hex()) # Imprime el mensaje en formato hexadecimal.
    print("Clave:             ", clave.hex())
    print("Criptograma:       ", criptograma.hex())
    print("Mensaje descifrado:", mensaje_descifrado.decode()) # Imprime el mensaje descifrado en formato de texto.