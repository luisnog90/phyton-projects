def devolver_distintos(num1, num2, num3):
    suma = num1 + num2 + num3
    
    if suma>15:
        if num1 > num2 and num1 > num3:
            print("el numero mayor es:", num1)
            
        elif num2 > num1 and num2 > num3:
            print("el numero mayor es:", num2)
            
        else:
            print("el numero mayor es:", num3)
        return
        
    elif (suma< 10):
        if num1 < num2 and num1 < num3:
            print("El número menor es:", num1)
        elif num2 < num1 and num2 < num3:
            print("El número menor es:", num2)
        else:
            print("El número menor es:", num3)
        return
        
    else:
        if num1 < num2 and num1 > num3:
            print("El número intermedio es:", num1)
        elif num2 < num1 and num2 > num3:
            print("El número intermedio es:", num2)
        else:
            print("El número intermedio es:", num3)
        



num1 = int(input('ingrese primer numero:'))
num2 = int(input('ingrese segundo numero:'))
num3 = int(input('ingrese tercer numero:'))

devolver_distintos(num1, num2, num3)