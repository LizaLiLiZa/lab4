
#  Минимум 2 разные функции, которые 
#  принимают на вход один или несколько параметров.
def devision(num_1: int, num_2:int):
    return num_1/num_2

def string_4(st1: str):
    return st1[4]

# Функция, которая принимает на вход один
# или несколько параметров.
def array_6(array):
    try:
        el = array[6]
        return el
    except Exception as e:
        print(f"Упс, кажется длина индекс находится вне массива!\n{e}")

# Функция, которая принимает на вход один или несколько параметров.
def array_func(array):
    try:
        array[4] += 6
    except Exception as e:
        print(f"Упс, кажется длина индекс находится вне массива!\n{e}")
    finally:
        array.append(2)
        return array
    
#  Минимум 3 разные функции, которые принимают на вход один или несколько параметров.
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