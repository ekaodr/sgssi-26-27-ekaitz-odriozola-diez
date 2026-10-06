from collections import Counter

mensaje = """RIJ AZKKZHC PIKCE XT ACKCUXJHX SZX, E NZ PEJXKE, PXGIK XFDKXNEQE RIPI RIPQEHCK ET OENRCNPI AXNAX ZJ RKCHXKCI AX CJAXDXJAXJRCE AX RTENX, E ACOXKXJRCE AXT RITEQIKERCIJCNPI OKXJHXDIDZTCNHE AX TE ACKXRRCIJ EJEKSZCNHE. AZKKZHC OZX ZJ OERHIK AX DKCPXK IKAXJ XJ XT DEDXT AX TE RTENX IQKXKE XJ REHETZJVE XJ GZTCI AX 1936. DXKI AZKKZHC, RIPI IRZKKX RIJ TEN DXKNIJETCAEAXN XJ TE MCNHIKCE, JI REVI AXT RCXTI. DXKNIJCOCREQE TE HKEACRCIJ KXvITZRCIJEKCE AX TE RTENX IQKXKE. NZ XJIKPX DIDZTEKCAEA XJHKX TE RTENX HKEQEGEAIKE, KXOTXGEAE XJ XT XJHCXKKI PZTHCHZACJEKCI XJ QEKRXTIJE XT 22 AX JIvCXPQKX AX 1936, PZXNHKE XNE CAXJHCOCRERCIJ. NZ PZXKHX OZX NCJ AZAE ZJ UITDX IQGXHCvI ET DKIRXNI KXvITZRCIJEKCI XJ PEKRME. NCJ AZKKZHC SZXAI PEN TCQKX XT REPCJI DEKE SZX XT XNHETCJCNPI, RIJ TE RIPDTCRCAEA AXT UIQCXKJI AXT OKXJHX DIDZTEK V AX TE ACKXRRCIJ EJEKSZCNHE, HXKPCJEKE XJ PEVI AX 1937 TE HEKXE AX TCSZCAEK TE KXvITZRCIJ, AXNPIKETCLEJAI E TE RTENX IQKXKE V OERCTCHEJAI RIJ XTTI XT DINHXKCIK HKCZJOI OKEJSZCNHE."""

alfabeto = "abcdefghijklmnopqrstuvwxyz"


# Contar cuántas veces aparece cada letra
frecuencias = Counter(mensaje.lower())

print("FRECUENCIAS:")
for letra, cantidad in frecuencias.most_common(): # Muestra las letras más frecuentes.
    if letra in alfabeto: # Si la letra está en el alfabeto.
        print(letra, "->", cantidad) # Imprime la letra y su frecuencia.


# Diccionario de sustituciones
sustituciones = {} 


while True: 

    print("\nMensaje:") # Imprime el mensaje con las sustituciones aplicadas.
    
    for letra in mensaje:
        if letra.lower() in sustituciones:
            print(sustituciones[letra.lower()], end="") # Imprime la letra sustituida.
        else:
            print("_", end="") # Imprime un guion bajo si la letra no está en el diccionario de sustituciones.

    print()

    entrada = input("\nIntroduce una sustitución (ejemplo: R E): ")

    if entrada == "salir": 
        break # Sale del bucle si se introduce "salir".

    partes = entrada.lower().split() # Divide la entrada en dos partes.

    if len(partes) == 2:
        letra_cifrada = partes[0] # La primera parte es la letra cifrada.
        letra_original = partes[1] # La segunda parte es la letra original.

        sustituciones[letra_cifrada] = letra_original # Añade la sustitución al diccionario.