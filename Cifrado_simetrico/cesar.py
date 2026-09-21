"""Ataque de fuerza bruta contra un cifrado César en castellano."""

import argparse
import re


ALFABETO = "abcdefghijklmnopqrstuvwxyz"

# Palabras frecuentes suficientes para distinguir una frase castellana.
PALABRAS_ES = {
	"a",
	"al",
	"con",
	"corazones",
	"de",
	"del",
	"el",
	"en",
	"es",
	"la",
	"las",
	"los",
	"mundo",
	"nuevo",
	"nuestros",
	"por",
	"que",
	"un",
	"una",
	"y",
}


def descifrar_cesar(mensaje, clave):
	"""Descifra un mensaje aplicando un desplazamiento hacia la izquierda."""
	resultado = []

	for caracter in mensaje:
		alfabeto = ALFABETO.upper() if caracter.isupper() else ALFABETO
		if caracter.lower() in ALFABETO:
			posicion = alfabeto.index(caracter)
			resultado.append(alfabeto[(posicion - clave) % len(alfabeto)])
		else:
			resultado.append(caracter)

	return "".join(resultado)


def puntuar_espanol(texto):
	"""Asigna más puntos a los candidatos que parecen castellano."""
	palabras = re.findall(r"[a-záéíóúüñ]+", texto.lower())
	puntuacion = sum(5 if palabra in PALABRAS_ES else 0 for palabra in palabras)
	puntuacion += sum(texto.lower().count(grupo) for grupo in (" que ", " en ", " de ", "os "))
	return puntuacion


def ataque_fuerza_bruta(mensaje):
	"""Devuelve los candidatos ordenados del más probable al menos probable."""
	candidatos = []
	for clave in range(len(ALFABETO)):
		texto = descifrar_cesar(mensaje, clave)
		candidatos.append((puntuar_espanol(texto), clave, texto))

	return sorted(candidatos, reverse=True)


def main():
	parser = argparse.ArgumentParser(description="Ataque de fuerza bruta al cifrado César")
	parser.add_argument(
		"mensaje",
		nargs="?",
		default="Uunejvxb dw vdwmx wdnex jzdr, nw wdnbcaxb lxajixwnb",
		help="mensaje cifrado que se quiere atacar",
	)
	args = parser.parse_args()

	candidatos = ataque_fuerza_bruta(args.mensaje)
	_, clave, texto = candidatos[0]

	print("Candidatos ordenados por probabilidad:")
	for puntuacion, clave_candidato, texto_candidato in candidatos:
		print(f"Clave {clave_candidato:2}: {texto_candidato} (puntuación: {puntuacion})")

	print(f"\nClave inferida: {clave}")
	print(f"Mensaje descifrado: {texto}")


if __name__ == "__main__":
	main()
