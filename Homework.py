# 1. Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя
# несколько чисел и строк и сохраните в переменные, выведите на экран.

Hello_word = 'Здравствуй, дорогой друг!'
print(Hello_word)
user_name = input('Введите имя пользователя: ')
number = int(input('Введите ваше счастливое число: '))
number2 = number**2
print(f"Привет {user_name}, твоё счастливое число {number}, представляешь в квадрате твоё число будет {number2}"
      f" \n Нуу, хорошего дня!")

# 2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды
# и выведите в формате чч:мм:сс. Используйте форматирование строк.

time = int(input('Введите кол-во секунд которое нужно перевести: '))
hours = time // 3600
minutes = (time - hours * 3600) // 60
sec = time - (hours * 3600 + minutes * 60)
print(f'Время в формате чч:мм:сс : {hours} : {minutes} : {sec}')

# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например,
# пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

n = int(input('Введите число n, сейчас мы будем его складывать: '))
summary = int(n) + int(str(n) + str(n)) + int(str(n) + str(n) + str(n))
print(f'Итак, мы решили найти сумму чисел n + nn + nnn и она равна = {summary}')

# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

number = abs(int(input("Введите целое положительное число: ")))
high_number = number % 10
while number >= 1:
    number = number // 10
    if number % 10 > high_number:
        high_number = number % 10
    elif number > 9:
        continue
    else:
        print('Самая большая цифра в вашем числе:', high_number)
        break

# 5. Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым
# результатом работает фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки
# (соотношение прибыли к выручке). Далее запросите численность сотрудников фирмы
# и определите прибыль фирмы в расчете на одного сотрудника.

print('Давайте посчитем рентабельность вашей фирмы')
proceeds = int(input('Введите значение вашей выручки: '))
costs = int(input('Введите значение издержек вашей фирмы: '))
if proceeds > costs:
    print('Ваша фирма выходит в плюс, так держать')
    income = proceeds - costs
    profit = income / proceeds
    print('Рентабельность выручки составляет:', profit)
    worker = int(input('Сколько у вас сотрудников?'))
    profit_worker = round(profit / worker, 2)
    print('Прибыль для каждого сотрудника составила:', profit_worker)
elif costs > proceeds:
    loss = abs(proceeds - costs)
    print('Кажется у вас небольшие проблемы, вы в убытке на', loss)

# 6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
# Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
# Например: a = 2, b = 3.
# Результат:
# 1-й день: 2
# 2-й день: 2,2
# 3-й день: 2,42
# 4-й день: 2,66
# 5-й день: 2,93
# 6-й день: 3,22
#
# Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.

print('Посчитаем сколько дней тебе нужно чтобы достичь нужного результата')
a = (float(input('Со скольки километров начнём? >>')))
b = (float(input('Какая цель? >>')))
days = 1
km = a
while km < b:
    x = a * 0.1
    a += x
    days += 1
    km = round(km + x, 2)
print(f'Ваша цель будет вас ждать на {days} день')
print(f'Такими темпами на {days} день вы пробежите {km} км')