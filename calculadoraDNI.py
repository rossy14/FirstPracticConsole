#programa para cálcular si un DNI es Válido.


#Relación número Letra
def calcularLetra(num):
  letras = {
    0: 'T',
    1: 'R',
    2: 'W',
    3: 'A',
    4: 'G',
    5: 'M',
    6: 'Y',
    7: 'F',
    8: 'P',
    9: 'D',
    10: 'X',
    11: 'B',
    12: 'N',
    13: 'J',
    14: 'Z',
    15: 'S',
    16: 'Q',
    17: 'V',
    18: 'H',
    19: 'L',
    20: 'C',
    21: 'K',
    22: 'E'
  }
  #cálcular
  num = num % 23
  resultado = letras.get(num)
  if resultado is None:
    print('Los número ingresados no son válido')
  else:
    return resultado


def ValidarDNI(dni):
  num = dni[:8] #obtener la parte númerica
  letra = dni[-1].upper()  #obtener la letra final

  if len(dni) != 9:
    print("Indicar un DNI con 8 números y una letra.")
 
  if num.isnumeric():
    caracter = calcularLetra(int(num)) 
    if caracter == letra:
      print(f"El DNI {dni.upper()} es válido.")
    else:
      print(f"El DNI {dni.upper()} no es válido.")
  else:
      print(f"Estos {num} son caracteres no válidos, ingresar solo números.")

print("*" * 10)
print("Programa para validar el DNI")
print("*" * 10)

res = input("Indicar su DNI:") #solicitar DNI al Usuario

ValidarDNI(res)
