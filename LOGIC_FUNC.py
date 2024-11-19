import re
#  1. Минимум 2 разные функции, которые 
#  принимают на вход один или несколько параметров.
def devision_func(num_1:float, num_2:float):
    """Исключение деления на 0"""
    return num_1/num_2

def string_4(st1: str):
    """Исключение индекс вне массива"""
    return st1[4]

# 2. Функция, которая принимает на вход один или несколько параметров.
# Функция ДОЛЖНА выбрасывать исключение при определённых значениях входных параметров.
# Функция ДОЛЖНА содержать ОДИН обработчик исключений общего типа (Exception). Внутри блока обработки исключения ДОЛЖНА быть какая-нибудь логика, связанная с обработкой исключения.
# Обработчик НЕ ДОЛЖЕН содержать блок finally.
def fio_func(firstname, midlename, lastname):
    """Исключение, если какой-то из параметров не строка"""
    try:
        full_name = firstname + " " + midlename + " " + lastname
        return full_name
    except Exception:
        print("ООООООООООО НЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕТ, КАЖЕТСЯ КАКИЕ-ТО ДАННЫЕ ВВЕДЕНЫ НЕ ВЕРНО!(")

# 3. Функция, которая принимает на вход один или несколько параметров.
# Функция ДОЛЖНА выбрасывать исключение при определённых значениях входных параметров.
# Функция ДОЛЖНА содержать ОДИН обработчик исключений общего типа (Exception). Внутри блока обработки исключения ДОЛЖНА быть какая-нибудь логика, связанная с обработкой исключения.
# Обработчик ДОЛЖЕН содержать блок finally. Логика внутри блока finally ДОЛЖНА способствовать нормальному завершению работы функции.
def array_func(array):
    try:
        array[4] += 6
    except Exception as e:
        print(f"Упс, кажется длина индекс находится вне массива!\n{e}")
    finally:
        array.append(2)
        return array
    
# #4. Минимум 3 разные функции, которые принимают на вход один или несколько параметров.
# Функции ДОЛЖНЫ выбрасывать исключения при определённых значениях входных параметров.
# Функции ДОЛЖНЫ содержать НЕСКОЛЬКО обработчиков РАЗНЫХ типов исключений (минимум 3 типа исключений). Внутри блоков обработки исключения ДОЛЖНА быть какая-нибудь логика, связанная с обработкой соответствующего типа исключения.
# Каждый обработчик МОЖЕТ содержать блок finally. Логика внутри блока finally ДОЛЖНА способствовать нормальному завершению работы функции.
def array_func_ecept(array):
    try:
        array[3] += "La"
    except IndexError:
        print("О НЕЕЕЕЕТ, ИНДЕКС ВНЕ МАССИВА(")
    except TypeError:
        print("УПС, КАЖЕТСЯ НЕ ТОТ ТИП")
    except Exception as e:
        print(f"Упс, кажется неизвестная ошибка \n{e}")
    finally:
        print(array)
        return array
    
def func(num):
    try:
        num = 7 * 7 / num
    except ZeroDivisionError:
        print("На ноль делить нельзя(")
    except TypeError:
        print("УПС, КАЖЕТСЯ НЕ ТОТ ТИП")
    except Exception as e:
        print(f"Упс, кажется неизвестная ошибка \n{e}")
    finally:
        print(num)
        return num
    
def string_func(n):
    try:
        n += "jojo"
    except ValueError:
        print("На то значение(")
    except TypeError:
        print("УПС, КАЖЕТСЯ НЕ ТОТ ТИП")
    except Exception as e:
        print(f"Упс, кажется неизвестная ошибка \n{e}")
    finally:
        print(n)
        return n

# 5. Функция, которая принимает на вход один или несколько параметров.
# Функция ДОЛЖНА генерировать исключения при определённых условиях (в Python есть конструкция для генерации исключений).
# Функция ДОЛЖНА содержать обрабоnчики всех исключений, которые генерируются внутри этой функции. Внутри блоков обработки исключения ДОЛЖНА быть какая-нибудь логика, связанная с обработкой соответствующего типа исключения.
# Обработчик МОЖЕТ содержать блок finally. Логика внутри блока finally ДОЛЖНА способствовать нормальному завершению работы функции.
def age_func(age):
    try:
        if age <= 60:
            raise Exception("Вы еще не можете выйти на пенсию(")
        return "Ваша пенсия составит 600000000 рублей)"
    except Exception as e:
        print(e)
        return "УВЫ("

# 6. Минимум 3 разных пользовательских исключения и примеры их использования
class Person:
    def __init__(self, name, age, years_experiens, was_an_employee):
        pattern = r"[а-яА-Я]*"
        if re.match(pattern, name):
            self.__name = name
        else:
            raise NameValidationException(name)
        self.__age = age
        if years_experiens > 3:
            self.__years_experiens = years_experiens
        else:
            raise PersonExperienceException(years_experiens, 3)
        if not was_an_employee:
            self.__was_an_employee = was_an_employee
        else:
            raise EmployeException(was_an_employee)

    def display_info(self):
        print(f"Имя: {self.__name}")
        print(f"Возраст: {self.__age}")
        print(f"Опыт работы (лет): {self.__years_experiens}")
        print(f"Был(а) сотрудником ранее: {'Да' if self.__was_an_employee else 'Нет'}")


class PersonExperienceException(Exception):
    """Исключение, если недостаточно опыта работы"""
    def __intit__(self, years, minyears):
        self.years = years
        self.minyears = minyears

    def __str__(self):
        return f"Недостаточный опыт работы"

class NameValidationException(Exception):
    """Исключение если имя введено не правильно"""
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "Некорректно введено имя"

class EmployeException(Exception):
    """Исключение, для отсеивания уже подававших заявку"""
    def __init__(self, employee):
        self.employee = employee

    def __str__(self):
        return "Упс, вы уже подавали заявку!!!("

# 7. Функция, которая принимает на вход один или несколько параметров.
# Функция ДОЛЖНА выбрасывать пользовательское исключение, созданное на шаге 6. при определённых значениях входных параметров.
# Функция ДОЛЖНА содержать МИНИМУМ ОДИН обработчик исключений. Внутри блока обработки исключения ДОЛЖНА быть какая-нибудь логика, связанная с обработкой исключения.
# Обработчик МОЖЕТ содержать блок finally.
def person_func(name, age, years_experiens, was_an_employee):
    try:
        pattern = r"[а-яА-Я]*"
        if not re.match(pattern, name):
            raise NameValidationException(name)
        person = Person(name, age, years_experiens, was_an_employee)
        return person
    except Exception:
        print("УУУУУУУУУУУУУПС")

# 8. Минимум 3 функции, демонстрирующие работу исключений.
# Алгоритм функций необходимо придумать самостоятельно

def check_credit_eligibility(name, credit_score):
    try:
        min_credit_score = 650
        if credit_score < min_credit_score:
            raise ValueError("Мы не можем вам дать кредит((")
        print("Вы можете получить кредит, УРААААААААААА!")
    except ValueError as e:
        print(f"Ой: {e}")

def check_cargo_weight(weight):
    try:
        max_weight = 1000
        if weight > max_weight:
            raise ValueError("ОЙ, слишком тяжело")
        print("ГРУЗ ПОВЕЗУТ!!.")
    except ValueError as e:
        print(f"ОЙ: {e}")
    finally:
        print("Операция проверки веса завершена.")

def check_registration_age(age):
    try:
        min_age = 18
        if age < min_age:
            raise ValueError("ОЙ, вы слишком молоды)")
        print("ДОБРО ПОЖАЛОВАТЬ!")
    except ValueError as e:
        print(f"ОЙ: {e}")
    finally:
        print("Операция проверки возраста завершена.")
