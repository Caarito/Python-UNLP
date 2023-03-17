
from random import choice, randrange
from datetime import datetime

operators = ["+", "-","*","/"] # Operadores posibles
times = 5  # Cantidad de cuentas a resolver
init_time = datetime.now() # Contador inicial de tiempo,Esto toma la fecha y hora actual.
print(f"¡Veremos cuanto tardas en responder estas {times} operaciones!")
correcto=0  #contador
incorrecto=0 #contador
for i in range(0, times):  # itera 5 veces
  number_1 = randrange(10) # Se eligen número 1 random
  number_2 = randrange(10) # Se eligen número 2 random
  operator = choice(operators) # operador al azar
  print(f"{i+1}- ¿Cuánto es {number_1} {operator} {number_2}?")   # Se imprime la cuenta.
  result = float(input("resultado: "))  # Le pedimos al usuario el resultado
  match operator:
    case"+": 
      resultado_correcto=number_1+number_2
    case "-":
      resultado_correcto=number_1-number_2
    case "*":
      resultado_correcto=number_1*number_2
    case"/":
      resultado_correcto=number_1/number_2 
      
  if resultado_correcto == result:
    print('El Resultado es correcto.')
    correcto +=1
  else:
    print('El Resultado es Incorrecto.')  
    incorrecto +=1
# Al terminar toda la cantidad de cuentas por resolver.
end_time = datetime.now() # Se vuelve a tomar la fecha y la hora.
total_time = end_time - init_time # Restando las fechas obtenemos el tiempo transcurrido.
print(f"\n Tardaste {total_time.seconds} segundos.") # Mostramos ese tiempo en segundos.
print('Cantidad de resultas correctos ingresados: ',correcto)
print('Cantidad de resultados incorrectos ingresados: ',incorrecto)