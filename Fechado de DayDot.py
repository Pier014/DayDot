from datetime import date, timedelta

tiempoDeVida = input("Ingrese el tiempo de vida del producto: ")
print("Tiempo de vida:",tiempoDeVida,"días")
TDV = int(tiempoDeVida) 

hoy = date.today() #Obtiene la fecha de hoy

fechado = hoy + timedelta(TDV-1) #Suma la fecha actual con el tiempo de vida y resta 1 día para contar desde hoy
formateado = fechado.strftime("%d/%m/%Y") #Formato en días / meses / años

dia_semana_num = fechado.weekday() #Obtiene la fecha del día
nombres_dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"] #Listado de días

print("DayDot:", nombres_dias[dia_semana_num], formateado, 10 ,"pm") #Muestra lo que tienes que colocar en el DayDot