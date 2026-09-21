"""Ataque interactivo por analisis de frecuencias a una sustitucion simple."""

import argparse
from collections import Counter
import string


MENSAJE = """RIJ AZKKZHC PIKCE XT ACKCUXJHX SZX, E NZ PEJXKE, PXGIK XFDKXNEQE RIPI RIPQEHCK ET OENRCNPI AXNAX ZJ RKCHXKCI AX CJAXDXJAXJRCE AX RTENX, E ACOXKXJRCE AXT RITEQIKERCIJCNPI OKXJHXDIDZTCNHE AX TE ACKXRRCIJ EJEKSZCNHE.

AZKKZHC OZX ZJ OERHIK AX DKCPXK IKAXJ XJ XT DEDXT AX TE RTENX IQKXKE XJ REHETZJVE XJ GZTCI AX 1936. DXKI AZKKZHC, RIPI IRZKKX RIJ TEN DXKNIJETCAEAXN XJ TE MCNHIKCE, JI REVI AXT RCXTI. DXKNIJCOCREQE TE HKEACRCIJ KXvITZRCIJEKCE AX TE RTENX IQKXKE. NZ XJIKPX DIDZTEKCAEA XJHKX TE RTENX HKEQEGEAIKE, KXOTXGEAE XJ XT XJHCXKKI PZTHCHZACJEKCI XJ QEKRXTIJE XT 22 AX JIvCXPQKX AX 1936, PZXNHKE XNE CAXJHCOCRERCIJ. NZ PZXKHX OZX NCJ AZAE ZJ UITDX IQGXHCvI ET DKIRXNI KXvITZRCIJEKCI XJ PEKRME. NCJ AZKKZHC SZXAI PEN TCQKX XT REPCJI DEKE SZX XT XNHETCJCNPI, RIJ TE RIPDTCRCAEA AXT UIQCXKJI AXT OKXJHX DIDZTEK V AX TE ACKXRRCIJ EJEKSZCNHE, HXKPCJEKE XJ PEVI AX 1937 TE HEKXE AX TCSZCAEK TE KXvITZRCIJ, AXNPIKETCLEJAI E TE RTENX IQKXKE V OERCTCHEJAI RIJ XTTI XT DINHXKCIK HKCZJOI OKEJSZCNHE."""

ALFABETO = string.ascii_lowercase + "ñ"
# Orden de frecuencia indicado en Fecuencias.png.
FRECUENCIAS_ES = "e a o l s n d r u i t c p m y q b h g f v j ñ z x k w".split()


def letras_del_mensaje(mensaje):
	return [caracter.lower() for caracter in mensaje if caracter.lower() in ALFABETO]


def obtener_frecuencias(mensaje):
	"""Devuelve las letras del criptograma ordenadas por frecuencia."""
	letras = letras_del_mensaje(mensaje)
	contador = Counter(letras)
	total = len(letras)
	return [(letra, contador[letra], contador[letra] * 100 / total) for letra in contador.most_common()]


def crear_mapa_inicial(mensaje):
	"""Asocia las letras mas frecuentes del criptograma a las del castellano."""
	orden_cifrado = [letra for letra, _, _ in obtener_frecuencias(mensaje)]
	return dict(zip(orden_cifrado, FRECUENCIAS_ES))


def aplicar_mapa(mensaje, mapa):
	resultado = []
	for caracter in mensaje:
		letra = caracter.lower()
		descifrada = mapa.get(letra, letra)
		resultado.append(descifrada.upper() if caracter.isupper() else descifrada)
	return "".join(resultado)


def mostrar_frecuencias(mensaje):
	print("\nFrecuencias del criptograma:")
	print("Letra   Apariciones   Porcentaje")
	for letra, cantidad, porcentaje in obtener_frecuencias(mensaje):
		print(f"  {letra}        {cantidad:3}         {porcentaje:5.2f}%")
	print("\nOrden castellano de referencia:")
	print(" ".join(FRECUENCIAS_ES))


def mostrar_mapa(mapa):
	print("\nMapa actual (letra cifrada -> letra clara):")
	for cifrada in sorted(mapa):
		print(f"{cifrada} -> {mapa[cifrada]}", end="    ")
	print()


def cambiar_sustitucion(mapa, cifrada, clara):
	"""Cambia una sustitucion y mantiene el mapa uno a uno."""
	cifrada = cifrada.lower()
	clara = clara.lower()
	anterior = mapa.get(cifrada, cifrada)
	otra_cifrada = next((letra for letra, valor in mapa.items() if valor == clara), None)
	mapa[cifrada] = clara
	if otra_cifrada is not None and otra_cifrada != cifrada:
		mapa[otra_cifrada] = anterior


def ayuda():
	print("""
Comandos:
  mostrar                 muestra el texto descifrado con el mapa actual
  cambiar C L            asigna la letra cifrada C a la letra clara L
  mapa                   muestra las sustituciones actuales
  frecuencias            muestra las frecuencias del criptograma
  reiniciar              vuelve a la propuesta por frecuencia
  salir                  termina el programa
""")


def ataque_interactivo(mensaje):
	mapa_inicial = crear_mapa_inicial(mensaje)
	mapa = mapa_inicial.copy()
	mostrar_frecuencias(mensaje)
	print("\nPropuesta inicial por frecuencia:")
	print(aplicar_mapa(mensaje, mapa))
	ayuda()

	while True:
		try:
			orden = input("\ncesar-simple> ").strip().split()
		except EOFError:
			print()
			break

		if not orden:
			continue
		comando = orden[0].lower()
		if comando in {"salir", "exit", "q"}:
			break
		if comando in {"mostrar", "m"}:
			print(aplicar_mapa(mensaje, mapa))
		elif comando == "mapa":
			mostrar_mapa(mapa)
		elif comando == "frecuencias":
			mostrar_frecuencias(mensaje)
		elif comando == "reiniciar":
			mapa = mapa_inicial.copy()
			print(aplicar_mapa(mensaje, mapa))
		elif comando == "cambiar" and len(orden) == 3:
			if len(orden[1]) != 1 or len(orden[2]) != 1:
				print("Usa una sola letra en cada posicion: cambiar C L")
			else:
				cambiar_sustitucion(mapa, orden[1], orden[2])
				print(aplicar_mapa(mensaje, mapa))
		else:
			ayuda()


def main():
	parser = argparse.ArgumentParser(description="Ataque por frecuencia a una sustitucion simple")
	parser.add_argument("--mensaje", help="fichero con el criptograma; por defecto usa el enunciado")
	args = parser.parse_args()
	mensaje = MENSAJE if args.mensaje is None else open(args.mensaje, encoding="utf-8").read()
	ataque_interactivo(mensaje)


if __name__ == "__main__":
	main()
