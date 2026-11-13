import time

WATER_PER_KG = 30

print("Добро пожаловать в приложение FitLife!")
time.sleep(1.5)
user_name = input('Как вас зовут? ')
user_name = user_name.title().strip()

while True:
    try:
        user_age = input('Сколько вам лет? ')
        user_age = int(user_age)
        if 1 <= int(user_age) <= 100:
            break
        else:
            print('Введите настоящий возраст в диапазоне от 1 до 99')
            continue
    except ValueError:
        print('Пожалуйста, введите возраст. Например, 23')

while True:
    try:
        weight = input('Введите ваш вес в кг ')
        if ',' in weight:
            weight = weight.replace(',', '.')
            weight = float(weight)
        else:
            weight = float(weight)
        break
    except ValueError:
        print('Введите вес в кг. Например, 70.5')

while True:
    try:
        height = input('Введите ваш рост в метрах ')
        if ',' in height:
            height = height.replace(',', '.')
            height = float(height)
        else:
            height = float(height)
        break
    except ValueError:
        print('Введите ваш рост в метрах. Например, 1.8')


def calculate_bmi(weight, height):
    """Calculate the BMI based on the weight and height."""
    return round(weight / (height ** 2), 1)


def calculate_water_intake(weight):
    """Calculate the water intake based on the weight."""
    water_ml = weight * WATER_PER_KG
    return water_ml / 1000


bmi_result = calculate_bmi(weight, height)
water_intake_result = calculate_water_intake(weight)

print('\n----------------------')
print(f'Отчет для пользователя: {user_name} ({user_age} г.)')
print(f'Твой Индекс Массы Тела: {bmi_result}.')
print(f'Рекомендуемая норма воды: {water_intake_result} л. в день. '
      f'\n \nРасчет окончен.'
      f' Будьте здоровы!')
