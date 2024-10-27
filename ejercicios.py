# 1. Perímetro de un cuadrado
def calcular_perimetro():
    lado = float(input("Ingrese el lado del cuadrado: "))
    perimetro = lado * 4
    print(f"El perímetro del cuadrado es: {perimetro}")

# 2. Cálculo de precio total
def calcular_precio_total():
    precio = float(input("Ingrese el precio del artículo: "))
    cantidad = int(input("Ingrese la cantidad: "))
    total = precio * cantidad
    print(f"Total a abonar: ${total:.2f}")

# 3. Verificar dígitos de un número
def verificar_digitos():
    numero = int(input("Ingrese un número entero positivo (hasta 3 dígitos): "))
    if numero > 999:
        print("Error: el número tiene más de 3 dígitos")
    else:
        digitos = len(str(numero))
        print(f"El número tiene {digitos} dígito(s)")

# 4. Test de capacitación
def evaluar_test():
    total_preguntas = int(input("Ingrese el total de preguntas: "))
    correctas = int(input("Ingrese cantidad de respuestas correctas: "))
    
    porcentaje = (correctas * 100) / total_preguntas
    
    if porcentaje >= 90:
        print("Nivel máximo")
    elif porcentaje >= 75:
        print("Nivel medio")
    elif porcentaje >= 50:
        print("Nivel regular")
    else:
        print("Fuera de nivel")

# 5. Determinar cuadrante
def determinar_cuadrante():
    x = int(input("Ingrese coordenada x (distinto de 0): "))
    y = int(input("Ingrese coordenada y (distinto de 0): "))
    
    if x > 0 and y > 0:
        print("1º Cuadrante")
    elif x < 0 and y > 0:
        print("2º Cuadrante")
    elif x < 0 and y < 0:
        print("3º Cuadrante")
    elif x > 0 and y < 0:
        print("4º Cuadrante")
    else:
        print("El punto está en un eje")

# 6. Calcular aumento de sueldo
def calcular_aumento():
    sueldo = float(input("Ingrese el sueldo del operario: "))
    antiguedad = int(input("Ingrese los años de antigüedad: "))
    
    if sueldo < 500:
        if antiguedad >= 10:
            sueldo = sueldo * 1.20
        else:
            sueldo = sueldo * 1.05
    
    print(f"Sueldo a pagar: ${sueldo:.2f}")

# 7. Contar pares e impares
def contar_pares_impares():
    n = int(input("¿Cuántos números desea ingresar? "))
    pares = 0
    impares = 0
    
    for i in range(n):
        num = int(input(f"Ingrese número {i+1}: "))
        if num % 2 == 0:
            pares += 1
        else:
            impares += 1
    
    print(f"Cantidad de números pares: {pares}")
    print(f"Cantidad de números impares: {impares}")

# 8. Múltiplos de 8
def mostrar_multiplos_8():
    for i in range(8, 501, 8):
        print(i, end=" - " if i < 496 else "")
    print()

# 9. Acumular valores hasta 9999
def acumular_valores():
    suma = 0
    while True:
        valor = int(input("Ingrese un valor (9999 para terminar): "))
        if valor == 9999:
            break
        suma += valor
    
    print(f"Valor acumulado: {suma}")
    if suma == 0:
        print("El valor es cero")
    elif suma > 0:
        print("El valor es mayor a cero")
    else:
        print("El valor es menor a cero")

# Menú principal para ejecutar los ejercicios
def menu():
    while True:
        print("\n=== MENÚ DE EJERCICIOS ===")
        print("1. Calcular perímetro de un cuadrado")
        print("2. Calcular precio total")
        print("3. Verificar dígitos de un número")
        print("4. Evaluar test de capacitación")
        print("5. Determinar cuadrante")
        print("6. Calcular aumento de sueldo")
        print("7. Contar pares e impares")
        print("8. Mostrar múltiplos de 8")
        print("9. Acumular valores")
        print("0. Salir")
        
        opcion = input("\nSeleccione un ejercicio (0-9): ")
        
        if opcion == "0":
            break
        elif opcion == "1":
            calcular_perimetro()
        elif opcion == "2":
            calcular_precio_total()
        elif opcion == "3":
            verificar_digitos()
        elif opcion == "4":
            evaluar_test()
        elif opcion == "5":
            determinar_cuadrante()
        elif opcion == "6":
            calcular_aumento()
        elif opcion == "7":
            contar_pares_impares()
        elif opcion == "8":
            mostrar_multiplos_8()
        elif opcion == "9":
            acumular_valores()
        else:
            print("Opción inválida")

if __name__ == "__main__":
    menu()