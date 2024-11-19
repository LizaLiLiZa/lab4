from LOGIC_FUNC import *

def run_all_functions():
    print("\n--- Проверка деления ---")
    try:
        print(devision_func(42, 7))  # Успешно
        print(devision_func(42, 0))  # Ошибка
    except Exception as e:
        print(f"Ошибка в `devision_func`: {e}")

    print("\n--- Проверка строки ---")
    try:
        print(string_4("Привет"))  # Успешно
        print(string_4("abc"))    # Ошибка
    except Exception as e:
        print(f"Ошибка в `string_4`: {e}")
    print("\n--- Проверка ФИО ---")
    print(fio_func("Иван", "Иванович", "Иванов"))  # Успешно
    print(fio_func("Иван", None, "Иванов"))       # Ошибка

    print("\n--- Проверка массива ---")
    print(array_func([1, 2, 3]))  # Ошибка, но элемент добавляется

    print("\n--- Проверка массива с несколькими обработчиками ---")
    print(array_func_ecept([1, 2, 3]))  # Ошибка

    print("\n--- Проверка деления на 0 ---")
    print(func(7))  # Успешно
    print(func(0))  # Ошибка

    print("\n--- Проверка строки на тип ---")
    print(string_func("Hello"))  # Успешно
    print(string_func(42))      # Ошибка

    print("\n--- Проверка возраста ---")
    print(age_func(65))  # Успешно
    print(age_func(50))  # Ошибка

    print("\n--- Проверка кредитоспособности ---")
    check_credit_eligibility("Иван", 700)  # Успешно
    check_credit_eligibility("Иван", 600)  # Ошибка

    print("\n--- Проверка веса груза ---")
    check_cargo_weight(800)  # Успешно
    check_cargo_weight(1200)  # Ошибка

    print("\n--- Проверка возраста для регистрации ---")
    check_registration_age(20)  # Успешно
    check_registration_age(16)  # Ошибка

    print("\n--- Проверка пользователя с кастомными исключениями ---")
    person = person_func("Иван", 30, 5, False)  # Успешно
    if person:
        person.display_info()
    person_func("John", 30, 5, False)  # Ошибка

if __name__ == "__main__":
    run_all_functions()