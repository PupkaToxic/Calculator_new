operator = input("Для работы с калькулятором нажмите любую клавишу, для завершения работы с калькулятором введите 'Выход'") #начало работы
while operator != 'Выход':
    operator = input('Введите математический оператор: "+", "-", "*", "/", "Выход"') #Заполнение нужных данных
    num1 = float(input('Введите первое число'))
    num2 = float(input('Введите второе число'))

    def addition ():   #Функция сложения
        result = num1 + num2
        return result

    def subtraction (): #Функция вычитания
        result = num1 - num2
        return result

    def multiple (): #функция умножения
        result = num1 * num2
        return result

    def division (): #функция деления
        result = num1 / num2
        return result


    if operator == '+': #определение математического знака
        print(addition())

    elif operator == '-':
        print(subtraction())

    elif operator == '/':
        print(division())

    elif operator == '*':
        print(multiple())
    
    elif operator == 'Выход':
        break

    else:
        print('Неверная операция')

print('Работа с калькулятором завершена') #конец работы
