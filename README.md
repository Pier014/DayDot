# DayDot
Fechado rapido y correcto

Recomiendo usar esta compilador online: https://onecompiler.com/python

```python
from datetime import date, timedelta

hoy = date.today()  #Obtiene la fecha de hoy

while True:
    tiempoDeVida = input("Ingrese el tiempo de vida del producto (o escriba 'salir'): ")

    if tiempoDeVida.lower() == "salir":
        break

    try:
        TDV = int(tiempoDeVida)

        if TDV <= 0:
            print("El tiempo de vida debe ser mayor que 0.\n")
            continue

        print("Tiempo de vida:", TDV, "días")

        #Suma el tiempo de vida y resta 1 para contar el día actual
        fechado = hoy + timedelta(days=TDV - 1)
        formateado = fechado.strftime("%d/%m/%Y")
        nombres_dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
        dia_semana = nombres_dias[fechado.weekday()]

        print(f"DayDot: {dia_semana} {formateado} 10 pm\n")

    except ValueError:
        print("Ingrese un número válido o escriba 'salir'.\n")

print("Saliendo...")
```

![logo](https://github.com/Pier014/DayDot/blob/main/image.png)
