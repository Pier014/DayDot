# Fechador DayDots
 
Herramienta web para calcular con facilidad y exactitud la fecha de vencimiento que se escribe en los DayDots, a partir del tiempo de vida de un producto.

Puedes usarlo aquí: https://pier014.github.io/DayDot/

## ¿Cómo funciona?
 
1. Elige la **hora de fechado** (10 pm y 11 pm son las más frecuentes, pero están disponibles las 24 horas).
2. Ingresa el **tiempo de vida** del producto en días, o usa los botones rápidos (1, 3, 4, 5, 7, 10, 15, 30, 90 y 180 días).
3. Obtén el DayDot listo, por ejemplo: `Viernes 20/11/2026 10 pm`.
El cálculo suma el tiempo de vida a la fecha de hoy y resta 1 día para contar el día actual.

## Características
 
- Selector de hora de fechado, con las horas más usadas a la mano.
- Botones rápidos de tiempo de vida.
- Historial de los últimos 5 cálculos.

Diseñado originalmente en Python y migrado a JavaScript con interfaz web en HTML.
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