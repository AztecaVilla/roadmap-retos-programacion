"""
Operadores

"""

#Operadores aritméticos
print(f'suma: 2 + 2 = {2+2}')
print(f'resta: 2 - 2 = {2-2}')
print(f'multiplicación: 2 * 2 = {2*2}')
print(f'división: 2/2 = {2/2}')
print(f'Módulo: 2 % 2 = {2%2 }')
print(f'Exponente: 2 ** 2 = {2**2 }')
print(f'División entera: 2 // 2 = {2//2 }')

#Operadores de comparación
print(f'Igualdad: 10 == 2 {10 == 3}')
print(f'Desigualdad: 10 != 2 {10 != 3}')
print(f'mayor que: 10 > 2 {10 > 3}')
print(f'menor que: 10 < 2 {10 < 3}')
print(f'menor o igual que: 10 <= 2 {10 <= 3}')
print(f'mayor o igual que: 10 >= 2 {10 >= 3}')

#operadores lógicos
print(f'and: 1 + 1 = 2 and 2 + 2 = 4 {1 + 1 == 2 and 2 + 2 == 4}')
print(f'or: 1 + 1 = 2 and 2 + 2 = 4 {1 + 1 == 2 or 2 + 2 == 5}')
print(f'not : 1 + 1 == 2 es {not 1 + 1 == 3}')

#Operadore de asignción

my_number = 11 #asignación
print(my_number)

my_number += 2 #suma y asignación
print(my_number)

my_number -= 1
print(my_number)

my_number *= 2
print(my_number)

my_number /= 2
print(my_number)

my_number %= 5
print(my_number)

my_number **= 2
print(my_number)

my_number //= 2
print(my_number)

#operadores de identidad

number = 1.0
print(my_number is number) #compara el valor en memoria
print(my_number is not number)

#operadores de pertenencia
print(f"'E' in 'Eduardo' = {'E' in 'Eduardo'}")
print(f"'B' not in 'Eduardo' = {'B' not in 'Eduardo'}")

#Operadores de bit
a = 10
b = 3

#condicionales
number = 7
if number % 2 == 0:
    print(f'el número {number} es par')
else:
    print(f'el número {number} es impar')
    
#Iterativas

for i in range(11):
    print(i)
    
contador = 0

while contador <= 10:
    contador += 1
    print(contador)
    
    
#Manejo de execepciones
try:
    print(10/0)
except:
    print("Se ha producido un error")
finally:
    print('Ha finalizado el manejo de excepciones')
    
    
    
    