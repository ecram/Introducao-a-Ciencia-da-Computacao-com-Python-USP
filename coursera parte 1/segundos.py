"""
# Nombre: ejercicio04
# Descripción: segundos a dias...
# Fecha: 06/04/2018
"""

segs_str = input("Por favor, entre com o número de segundos que deseja converter: ")

segs_int = int(segs_str)

dias = segs_int // (3600 * 24)
segs_int = segs_int % (3600 * 24)
horas = segs_int // 3600
segs_int = segs_int % 3600

minutos = segs_int // 60
segs = segs_int % 60

print(dias, "dias,", horas, "horas,", minutos, "minutos e", segs, "segundos.")
