# Concatenar cadenas de caracteres.
# Supongamos que queremos crear una cadena que diga:
#   Aprende a programar con ____________

# organizacion = "freCodeCamp"
# print("Aprende a programar con " + organizacion)
# # otra manera
# print("Aprende a programar con {}".format(organizacion))
# # con f-string
# print(f"Aprende a programar con {organizacion}")
adj = input("Adjetivo: ")
verb1 = input("Verbo 1: ")
verb2 = input("Verbo 2: ")
sust = input("Sustantivo (plural): ")

madlib = f"Programar es tan {adj}! Siempre me emociona por que me encanta {verb1} problemas. ¡Aprende a {verb2} con FreeCodeCamp y alcanza tus {sust}!"

print(madlib)