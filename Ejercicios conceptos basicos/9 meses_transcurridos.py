"""
Mostrar en pantalla
la cantidad de meses
transcurridos desde 
la fecha de fecha_nacimiento
de un usuario.
"""
from datetime import date


fecha_nacimiento = date(1999, 1, 20)
fecha_actual = date.today()

if fecha_nacimiento < fecha_actual:
    meses = ((fecha_actual.year - fecha_nacimiento.year) * 12) + (fecha_actual.month - fecha_nacimiento.month)
    if fecha_actual.day < fecha_nacimiento.day:
        meses -= 1
    print(meses)
